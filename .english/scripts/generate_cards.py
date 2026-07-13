#!/usr/bin/env python3
"""
Generate vocabulary cards from Obsidian markdown notes.
"""
import sys
import os
import re
import json
from pathlib import Path
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))
import srs_engine
from utils.translate import extract_spanish_terms, translate_to_english, get_ipa, get_context_sentence

PROGRESS_FILE = os.path.expanduser("~/.english/data/progress.json")
VAULT_DIR = os.path.expanduser("~/Documents/GitHub/Nous/obsidian")


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {"processed": [], "total_cards": 0}


def save_progress(progress):
    os.makedirs(os.path.dirname(PROGRESS_FILE), exist_ok=True)
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def process_note(filepath):
    with open(filepath) as f:
        content = f.read()

    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else Path(filepath).stem

    category = "General"
    parts = Path(filepath).parts
    for part in parts:
        if part.startswith("01_"):
            category = "Matemáticas"
        elif part.startswith("02_"):
            category = "Química"
        elif part.startswith("03_"):
            category = "Física"
        elif part.startswith("04_"):
            category = "Biología"

    clean_text = re.sub(r'\$\$[\s\S]*?\$\$', '', content)
    clean_text = re.sub(r'\$[^$]+\$', '', clean_text)
    clean_text = re.sub(r'```[\s\S]*?```', '', clean_text)
    clean_text = re.sub(r':::.*?:::', '', clean_text, flags=re.DOTALL)
    clean_text = re.sub(r'[@#]\S+', '', clean_text)
    clean_text = re.sub(r'!\[.*?\]\(.*?\)', '', clean_text)
    clean_text = re.sub(r'\[.*?\]\(.*?\)', '', clean_text)
    clean_text = re.sub(r'[-=]{3,}', '', clean_text)
    clean_text = re.sub(r'[|]', ' ', clean_text)

    terms = extract_spanish_terms(clean_text)

    cards = []
    seen_english = set()
    for term in terms:
        english = translate_to_english(term)
        if english.lower() == term.lower():
            continue
        if english.lower() in seen_english:
            continue
        seen_english.add(english.lower())

        ipa = get_ipa(english)
        context = get_context_sentence(clean_text, term)

        cards.append({
            "term": term,
            "ipa": ipa,
            "translation_en": english,
            "example_es": context,
            "example_en": "",
            "topic": f"{category}::{title}",
            "card_type": "vocab_es_en",
            "front": term,
            "back": english,
            "tags": [category, title]
        })

    for card in cards[:]:
        reverse = card.copy()
        reverse["card_type"] = "vocab_en_es"
        reverse["front"] = card["translation_en"]
        reverse["back"] = card["term"]
        reverse["tags"] = card["tags"] + ["reverso"]
        cards.append(reverse)

    return cards, title, category


def generate_from_note(filepath, force=False):
    progress = load_progress()
    abs_path = str(Path(filepath).resolve())

    if not force and abs_path in [p["file"] for p in progress["processed"]]:
        print(f"⚠️  Ya procesado: {filepath}")
        return 0

    if force:
        old_entry = [p for p in progress["processed"] if p["file"] == abs_path]
        if old_entry:
            cat = old_entry[0].get("category", "")
            tit = old_entry[0].get("title", "")
            full_topic = f"{cat}::{tit}" if cat and cat != "General" else tit
            if full_topic:
                srs_engine.delete_cards_by_topic(full_topic)
        progress["processed"] = [p for p in progress["processed"] if p["file"] != abs_path]
        save_progress(progress)

    cards, title, category = process_note(filepath)
    if not cards:
        print(f"⚠️  No se encontraron terms en: {filepath}")
        return 0

    added = srs_engine.add_cards_batch(cards)

    progress["processed"].append({
        "file": abs_path,
        "title": title,
        "category": category,
        "cards": added,
        "timestamp": datetime.now().isoformat()
    })
    progress["total_cards"] += added
    save_progress(progress)

    print(f"✅ {title}: {added} cards generados")
    return added


def generate_all():
    progress = load_progress()
    processed_files = {p["file"] for p in progress["processed"]}

    total = 0
    for root, dirs, files in os.walk(VAULT_DIR):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith(".md") and not f.startswith(".") and f not in ("index.md", "intro.md", "summary.md"):
                filepath = os.path.join(root, f)
                abs_path = str(Path(filepath).resolve())
                if abs_path not in processed_files:
                    total += generate_from_note(filepath)

    print(f"\n📊 Total: {total} cards nuevos")
    stats = srs_engine.get_stats()
    print(f"   Total en SRS: {stats['total']} | Pendientes: {stats['due_now']}")
    return total


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for fp in sys.argv[1:]:
            generate_from_note(fp)
    else:
        generate_all()
