#!/usr/bin/env python3
"""
Progression state machine for English learning system.
Tracks stages, metrics, and unlock conditions.
"""
import json
import os
from datetime import datetime, timedelta

PROGRESS_FILE = os.path.expanduser("~/.english/data/progress_state.json")

STAGES = {
    1: {
        "name": "Vocabulary",
        "name_es": "Vocabulario",
        "icon": "📚",
        "unlock_when": None,
        "description": "Aprende vocabulary con flashcards ES→EN",
    },
    2: {
        "name": "Reading",
        "name_es": "Lectura",
        "icon": "📖",
        "unlock_when": {"cards_reviewed": 20, "retention_pct": 60},
        "description": "Lee tus notas traducidas al inglés",
    },
    3: {
        "name": "Listening",
        "name_es": "Escucha",
        "icon": "🔊",
        "unlock_when": {"notes_read": 3, "retention_pct": 70},
        "description": "Escucha tus notas completas en inglés",
    },
    4: {
        "name": "Writing",
        "name_es": "Escritura",
        "icon": "✍️",
        "unlock_when": {"notes_listened": 3, "retention_pct": 70},
        "description": "Completa oraciones usando vocabulary",
    },
    5: {
        "name": "Speaking",
        "name_es": "Hablar",
        "icon": "🎤",
        "unlock_when": {"writing_exercises": 5, "retention_pct": 75},
        "description": "Compara tu pronunciación con audio original",
    },
    6: {
        "name": "Conversation",
        "name_es": "Conversación",
        "icon": "💬",
        "unlock_when": {"speaking_sessions": 3, "retention_pct": 75},
        "description": "Chatea en inglés con corrección en tiempo real",
    },
}


def _load():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {
        "current_stage": 1,
        "unlocked_stages": [1],
        "metrics": {
            "cards_reviewed": 0,
            "retention_pct": None,
            "notes_read": 0,
            "notes_listened": 0,
            "writing_exercises": 0,
            "speaking_sessions": 0,
            "streak_days": 0,
            "last_review_date": None,
        },
        "stage_progress": {},
    }


def _save(data):
    os.makedirs(os.path.dirname(PROGRESS_FILE), exist_ok=True)
    with open(PROGRESS_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_state():
    return _load()


def get_current_stage():
    return _load()["current_stage"]


def get_unlocked_stages():
    return _load()["unlocked_stages"]


def get_metrics():
    return _load()["metrics"]


def update_metrics(**kwargs):
    state = _load()
    for key, value in kwargs.items():
        if key in state["metrics"]:
            state["metrics"][key] = value
    _save(state)
    _check_unlocks()


def increment_metric(key, amount=1):
    state = _load()
    if key in state["metrics"]:
        state["metrics"][key] += amount
    _save(state)
    _check_unlocks()


def set_retention(pct):
    state = _load()
    state["metrics"]["retention_pct"] = round(pct, 1)
    _save(state)
    _check_unlocks()


def record_review():
    state = _load()
    state["metrics"]["cards_reviewed"] += 1
    today = datetime.now().strftime("%Y-%m-%d")
    last = state["metrics"].get("last_review_date")
    if last == today:
        pass
    elif last == (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"):
        state["metrics"]["streak_days"] += 1
    else:
        state["metrics"]["streak_days"] = 1
    state["metrics"]["last_review_date"] = today
    _save(state)
    _check_unlocks()


def record_note_read():
    state = _load()
    state["metrics"]["notes_read"] += 1
    _save(state)
    _check_unlocks()


def record_note_listened():
    state = _load()
    state["metrics"]["notes_listened"] += 1
    _save(state)
    _check_unlocks()


def record_writing_exercise():
    state = _load()
    state["metrics"]["writing_exercises"] += 1
    _save(state)
    _check_unlocks()


def record_speaking_session():
    state = _load()
    state["metrics"]["speaking_sessions"] += 1
    _save(state)
    _check_unlocks()


def _check_unlocks():
    state = _load()
    metrics = state["metrics"]
    changed = False

    for stage_id in range(2, 7):
        if stage_id in state["unlocked_stages"]:
            continue
        condition = STAGES[stage_id]["unlock_when"]
        if condition is None:
            continue
        met = True
        for key, threshold in condition.items():
            value = metrics.get(key)
            if value is None:
                met = False
                break
            if value < threshold:
                met = False
                break
        if met:
            state["unlocked_stages"].append(stage_id)
            if stage_id > state["current_stage"]:
                state["current_stage"] = stage_id
            changed = True
            print(f"\n🎉 ¡Nueva etapa desbloqueada: {STAGES[stage_id]['icon']} {STAGES[stage_id]['name_es']}!")

    if changed:
        state["unlocked_stages"].sort()
        _save(state)


def get_next_unlock():
    state = _load()
    metrics = state["metrics"]
    for stage_id in range(2, 7):
        if stage_id not in state["unlocked_stages"]:
            condition = STAGES[stage_id]["unlock_when"]
            if condition is None:
                continue
            remaining = {}
            for key, threshold in condition.items():
                current_val = metrics.get(key) or 0
                remaining[key] = max(0, threshold - current_val)
            return {
                "stage": stage_id,
                "name": STAGES[stage_id]["name_es"],
                "icon": STAGES[stage_id]["icon"],
                "remaining": remaining,
            }
    return None


def show_progress():
    state = _load()
    metrics = state["metrics"]
    current = state["current_stage"]
    unlocked = state["unlocked_stages"]

    print()
    print("╔═══════════════════════════════════════════════════╗")
    print("║        🇬🇧 Progreso de Inglés                      ║")
    print("╚═══════════════════════════════════════════════════╝")
    print()

    bar_len = 30
    filled = int(bar_len * current / 6)
    bar = "█" * filled + "░" * (bar_len - filled)
    print(f"  Progreso general: [{bar}] Etapa {current}/6")
    print()

    for sid, info in STAGES.items():
        icon = info["icon"]
        name = info["name_es"]
        if sid in unlocked:
            if sid == current:
                print(f"  {icon} {name} ← ESTÁS AQUÍ")
            else:
                print(f"  {icon} {name} ✓")
        else:
            print(f"  {icon} {name} 🔒")

    print()
    print("  📊 Métricas:")
    print(f"     Cards repasadas:  {metrics['cards_reviewed']}")
    ret = metrics.get("retention_pct")
    if ret is not None:
        color = "🟢" if ret >= 80 else "🟡" if ret >= 60 else "🔴"
        print(f"     Retención:        {color} {ret}%")
    else:
        print(f"     Retención:        ⚪ Sin datos")
    print(f"     Notas leídas:     {metrics['notes_read']}")
    print(f"     Notas escuchadas: {metrics['notes_listened']}")
    print(f"     Ejercicios writes: {metrics['writing_exercises']}")
    print(f"     Sesiones speaking: {metrics['speaking_sessions']}")
    print(f"     Racha:            {metrics['streak_days']} días")

    next_unlock = get_next_unlock()
    if next_unlock:
        print()
        print(f"  🎯 Siguiente desbloqueo: {next_unlock['icon']} {next_unlock['name']}")
        for key, remaining in next_unlock["remaining"].items():
            label = {
                "cards_reviewed": "cards por repasar",
                "retention_pct": "puntos de retención",
                "notes_read": "notas por leer",
                "notes_listened": "notas por escuchar",
                "writing_exercises": "ejercicios de escritura",
                "speaking_sessions": "sesiones de speaking",
            }.get(key, key)
            print(f"     → {remaining} {label}")

    print()
