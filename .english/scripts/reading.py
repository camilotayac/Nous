#!/usr/bin/env python3
"""
Reading mode: display translated notes in English with vocabulary highlighting.
"""
import os
import sys
import re

sys.path.insert(0, os.path.dirname(__file__))

READING_DIR = os.path.expanduser("~/.english/data/reading")


def list_readings():
    if not os.path.exists(READING_DIR):
        return []
    return [f for f in os.listdir(READING_DIR) if f.endswith(".md")]


def read_note(filename):
    filepath = os.path.join(READING_DIR, filename)
    if not os.path.exists(filepath):
        print(f"❌ No existe: {filename}")
        return
    with open(filepath) as f:
        return f.read()


def highlight_known_words(text):
    try:
        import srs_engine
        cards = srs_engine.get_due(limit=500)
        known = set()
        for c in cards:
            known.add(c["front"].lower())
            known.add(c["back"].lower())
            known.add(c.get("term", "").lower())
    except Exception:
        known = set()

    def bold_match(word):
        if word.lower() in known:
            return f"**{word}**"
        return word

    result = re.sub(r'\b([a-zA-Z]+)\b', lambda m: bold_match(m.group(1)), text)
    return result


def reading_session():
    readings = list_readings()

    if not readings:
        print("📭 No hay notas traducidas aún.")
        print("   Procesa notas con la opción de sync del menú principal.")
        return

    print("\n📖 Modo Lectura — Notas en inglés")
    print()

    for i, r in enumerate(readings, 1):
        name = r.replace(".md", "").replace("_", " ").title()
        print(f"  {i}. {name}")

    print(f"  0. Volver")
    print()

    try:
        choice = input("Selecciona nota: ").strip()
    except (EOFError, KeyboardInterrupt):
        return

    if choice == "0" or choice == "":
        return

    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(readings):
        print("❌ Opción no válida.")
        return

    filename = readings[int(choice) - 1]
    content = read_note(filename)

    if not content:
        return

    highlighted = highlight_known_words(content)

    print()
    print("┌──────────────────────────────────────────────────────────┐")
    print("│  📖 Lectura en inglés                                    │")
    print("│  Palabras en **negrita** = vocabulary que ya estás       │")
    print("│  aprendiendo en tus flashcards                           │")
    print("└──────────────────────────────────────────────────────────┘")
    print()

    paragraphs = highlighted.split("\n")
    for para in paragraphs:
        para = para.strip()
        if not para:
            print()
            continue
        if para.startswith("#"):
            print(f"\n{para}")
            print()
        else:
            print(f"  {para}")
            print()

    print()
    print("┌──────────────────────────────────────────────────────────┐")
    print("│  ✅ Lectura completada                                   │")
    print("│  Comandos: 'q' salir                                    │")
    print("└──────────────────────────────────────────────────────────┘")

    try:
        import progress
        progress.record_note_read()
        print("   📊 Registrado: +1 nota leída")
    except Exception:
        pass


if __name__ == "__main__":
    reading_session()
