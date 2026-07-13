#!/usr/bin/env python3
"""
Terminal SRS Engine using FSRS algorithm.
Stores cards in SQLite, provides API for review and stats.

Database: ~/.english/data/cards.db
"""
import sqlite3
import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from fsrs import Card, Rating, Scheduler, State

DB_PATH = os.path.expanduser("~/.english/data/cards.db")
scheduler = Scheduler()


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    _init_db(conn)
    return conn


def _init_db(conn):
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            term TEXT NOT NULL,
            ipa TEXT DEFAULT '',
            translation_es TEXT DEFAULT '',
            pronunciation_es TEXT DEFAULT '',
            example_en TEXT DEFAULT '',
            example_es TEXT DEFAULT '',
            topic TEXT DEFAULT '',
            card_type TEXT DEFAULT 'vocab_en_es',
            front TEXT NOT NULL,
            back TEXT NOT NULL,
            tags TEXT DEFAULT '[]',
            created_at TEXT DEFAULT (datetime('now')),
            due_at TEXT DEFAULT (datetime('now')),
            stability REAL DEFAULT 0,
            difficulty REAL DEFAULT 0,
            step INTEGER DEFAULT 0,
            lapses INTEGER DEFAULT 0,
            state TEXT DEFAULT 'New',
            last_review TEXT DEFAULT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_cards_due ON cards(due_at);
        CREATE INDEX IF NOT EXISTS idx_cards_type ON cards(card_type);
        CREATE INDEX IF NOT EXISTS idx_cards_topic ON cards(topic);

        CREATE TABLE IF NOT EXISTS review_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            card_id INTEGER NOT NULL,
            rating INTEGER NOT NULL,
            review_at TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (card_id) REFERENCES cards(id)
        );
    """)
    conn.commit()


def add_card(term, ipa="", translation_es="", pronunciation_es="",
             example_en="", example_es="", topic="", card_type="vocab_en_es",
             front=None, back=None, tags=None):
    conn = get_conn()
    try:
        if front is None:
            front = term
        if back is None:
            back = translation_es
        if tags is None:
            tags = []

        now = datetime.now(timezone.utc)

        conn.execute("""
            INSERT INTO cards (term, ipa, translation_es, pronunciation_es,
                              example_en, example_es, topic, card_type,
                              front, back, tags, due_at, stability, difficulty,
                              step, lapses, state)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            term, ipa, translation_es, pronunciation_es,
            example_en, example_es, topic, card_type,
            front, back, json.dumps(tags),
            now.isoformat(),
            0, 0, 0, 0, "New"
        ))
        conn.commit()
        card_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
        return card_id
    finally:
        conn.close()


def add_cards_batch(cards_list):
    conn = get_conn()
    try:
        added = 0
        now = datetime.now(timezone.utc)
        for c in cards_list:
            conn.execute("""
                INSERT INTO cards (term, ipa, translation_es, pronunciation_es,
                                  example_en, example_es, topic, card_type,
                                  front, back, tags, due_at, stability, difficulty,
                                  step, lapses, state)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                c.get("term", ""),
                c.get("ipa", ""),
                c.get("translation_es", ""),
                c.get("pronunciation_es", ""),
                c.get("example_en", ""),
                c.get("example_es", ""),
                c.get("topic", ""),
                c.get("card_type", "vocab_en_es"),
                c.get("front", c.get("term", "")),
                c.get("back", c.get("translation_es", "")),
                json.dumps(c.get("tags", [])),
                now.isoformat(),
                0, 0, 0, 0, "New"
            ))
            added += 1
        conn.commit()
        return added
    finally:
        conn.close()


def get_due(limit=20):
    conn = get_conn()
    try:
        now = datetime.now(timezone.utc).isoformat()
        rows = conn.execute("""
            SELECT * FROM cards
            WHERE due_at <= ? AND state != 'Suspended'
            ORDER BY due_at ASC
            LIMIT ?
        """, (now, limit)).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def get_new_cards(limit=20):
    conn = get_conn()
    try:
        rows = conn.execute("""
            SELECT * FROM cards
            WHERE state = 'New'
            ORDER BY created_at ASC
            LIMIT ?
        """, (limit,)).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def review_card(card_id, rating):
    conn = get_conn()
    try:
        row = conn.execute("SELECT * FROM cards WHERE id = ?", (card_id,)).fetchone()
        if not row:
            return None

        card_dict = dict(row)

        state_map = {
            "New": State.Learning,
            "Learning": State.Learning,
            "Review": State.Review,
            "Relearning": State.Relearning,
            "Suspended": State.Learning,
        }
        fsrs_state = state_map.get(card_dict["state"], State.Learning)

        card = Card(
            state=fsrs_state,
            step=card_dict.get("step", 0),
            stability=card_dict.get("stability", 0) or None,
            difficulty=card_dict.get("difficulty", 0) or None,
            due=datetime.fromisoformat(card_dict["due_at"]).astimezone(timezone.utc),
            last_review=datetime.fromisoformat(card_dict["last_review"]).astimezone(timezone.utc) if card_dict.get("last_review") else None,
        )

        rating_map = {
            1: Rating.Again,
            2: Rating.Hard,
            3: Rating.Good,
            4: Rating.Easy
        }
        fsrs_rating = rating_map.get(rating, Rating.Good)
        now = datetime.now(timezone.utc)

        new_card, _ = scheduler.review_card(card, fsrs_rating, now)

        lapses = conn.execute(
            "SELECT COUNT(*) FROM review_log WHERE card_id = ? AND rating = 1",
            (card_id,)
        ).fetchone()[0]
        if rating == 1:
            lapses += 1

        conn.execute("""
            UPDATE cards SET
                due_at = ?, stability = ?, difficulty = ?, step = ?,
                lapses = ?, state = ?, last_review = ?
            WHERE id = ?
        """, (
            new_card.due.isoformat(),
            new_card.stability or 0,
            new_card.difficulty or 0,
            new_card.step or 0,
            lapses,
            new_card.state.name,
            now.isoformat(),
            card_id
        ))

        conn.execute(
            "INSERT INTO review_log (card_id, rating) VALUES (?, ?)",
            (card_id, rating)
        )

        conn.commit()
        return card_dict
    finally:
        conn.close()


def get_stats():
    conn = get_conn()
    try:
        total = conn.execute("SELECT COUNT(*) FROM cards").fetchone()[0]
        new_count = conn.execute("SELECT COUNT(*) FROM cards WHERE state = 'New'").fetchone()[0]
        learning = conn.execute("SELECT COUNT(*) FROM cards WHERE state = 'Learning'").fetchone()[0]
        review = conn.execute("SELECT COUNT(*) FROM cards WHERE state = 'Review'").fetchone()[0]
        due_now = conn.execute(
            "SELECT COUNT(*) FROM cards WHERE due_at <= ? AND state != 'Suspended'",
            (datetime.now(timezone.utc).isoformat(),)
        ).fetchone()[0]

        last_7_days = (datetime.now(timezone.utc) - timedelta(days=7)).isoformat()
        reviews_7d = conn.execute(
            "SELECT COUNT(*) FROM review_log WHERE review_at >= ?",
            (last_7_days,)
        ).fetchone()[0]

        correct_7d = conn.execute(
            "SELECT COUNT(*) FROM review_log WHERE review_at >= ? AND rating >= 3",
            (last_7_days,)
        ).fetchone()[0]

        retention = (correct_7d / reviews_7d * 100) if reviews_7d > 0 else None

        return {
            "total": total,
            "new": new_count,
            "learning": learning,
            "review": review,
            "due_now": due_now,
            "reviews_7d": reviews_7d,
            "retention_pct": round(retention, 1) if retention else None
        }
    finally:
        conn.close()


def suspend_card(card_id):
    conn = get_conn()
    try:
        conn.execute("UPDATE cards SET state = 'Suspended' WHERE id = ?", (card_id,))
        conn.commit()
    finally:
        conn.close()


def unsuspend_card(card_id):
    conn = get_conn()
    try:
        conn.execute("UPDATE cards SET state = 'New' WHERE id = ?", (card_id,))
        conn.commit()
    finally:
        conn.close()


def get_all_topics():
    conn = get_conn()
    try:
        rows = conn.execute("SELECT DISTINCT topic FROM cards WHERE topic != ''").fetchall()
        return [r[0] for r in rows]
    finally:
        conn.close()


def delete_cards_by_topic(topic):
    conn = get_conn()
    try:
        card_ids = [r[0] for r in conn.execute("SELECT id FROM cards WHERE topic = ?", (topic,)).fetchall()]
        if card_ids:
            placeholders = ",".join("?" * len(card_ids))
            conn.execute(f"DELETE FROM review_log WHERE card_id IN ({placeholders})", card_ids)
            conn.execute(f"DELETE FROM cards WHERE id IN ({placeholders})", card_ids)
            conn.commit()
        return len(card_ids)
    finally:
        conn.close()


def delete_all_cards():
    conn = get_conn()
    try:
        conn.execute("DELETE FROM cards")
        conn.execute("DELETE FROM review_log")
        conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    stats = get_stats()
    print(f"📊 SRS Stats: {json.dumps(stats, indent=2)}")
