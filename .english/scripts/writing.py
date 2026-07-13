#!/usr/bin/env python3
"""
Writing mode: fill-in-the-blank exercises using vocabulary from SRS.
"""
import os
import sys
import re
import random

sys.path.insert(0, os.path.dirname(__file__))

READING_DIR = os.path.expanduser("~/.english/data/reading")


def list_readings():
    if not os.path.exists(READING_DIR):
        return []
    return [f for f in os.listdir(READING_DIR) if f.endswith(".md")]


def extract_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if len(s.strip()) > 20 and not s.strip().startswith("#")]


def get_vocabulary_map():
    try:
        import srs_engine
        cards = srs_engine.get_due(limit=500)
        vocab = {}
        for c in cards:
            front = c.get("front", "")
            back = c.get("back", "")
            if front and back and front != back:
                vocab[front.lower()] = back
                vocab[back.lower()] = front
        return vocab
    except Exception:
        return {}


def create_blanks(sentence, vocab):
    words = re.findall(r'\b[a-zA-Z]{4,}\b', sentence)
    blanks = []
    for word in words:
        wl = word.lower()
        if wl in vocab:
            blanks.append((word, vocab[wl]))
    if not blanks:
        return None
    blank_word, answer = random.choice(blanks[:3])
    pattern = re.compile(r'\b' + re.escape(blank_word) + r'\b', re.IGNORECASE)
    blanked = pattern.sub("______", sentence, count=1)
    return {
        "text": blanked,
        "answer": blank_word,
        "translation": answer,
    }


def writing_session():
    readings = list_readings()
    if not readings:
        print("📭 No hay notas traducidas aún.")
        print("   Procesa notas con la opción de sync del menú principal.")
        return

    print("\n✍️  Modo Escritura — Completa las palabras")
    print("   Vas a ver oraciones en inglés con palabras faltantes.")
    print("   Escribe la palabra correcta en inglés.\n")

    for i, r in enumerate(readings, 1):
        name = r.replace(".md", "").replace("_", " ").title()
        print(f"  {i}. {name}")

    print(f"  0. Volver\n")

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
    with open(os.path.join(READING_DIR, filename)) as f:
        content = f.read()

    sentences = extract_sentences(content)
    vocab = get_vocabulary_map()

    if not sentences:
        print("⚠️ No se encontraron oraciones suficientes.")
        return

    exercises = []
    for sent in sentences:
        ex = create_blanks(sent, vocab)
        if ex:
            exercises.append(ex)
        if len(exercises) >= 10:
            break

    if not exercises:
        print("⚠️ No se encontraron vocabulario para ejercicios.")
        print("   Asegúrate de tener cards en el SRS.")
        return

    random.shuffle(exercises)

    print(f"\n📝 {len(exercises)} ejercicios de escritura\n")
    correct = 0
    total = len(exercises)

    for i, ex in enumerate(exercises, 1):
        print(f"  ── Ejercicio {i}/{total} ──")
        print(f"  {ex['text']}")
        print(f"  (Pista: {ex['translation']})")

        try:
            answer = input("  Tu respuesta: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n\n👋 Sesión terminada.")
            return

        if answer == ex["answer"].lower():
            print(f"  ✅ ¡Correcto! {ex['answer']}\n")
            correct += 1
        else:
            print(f"  ❌ Incorrecto. La respuesta era: {ex['answer']}\n")

    print(f"  🎉 Ejercicio completado: {correct}/{total} correctas ({correct/total*100:.0f}%)")

    try:
        import progress
        progress.record_writing_exercise()
        print("   📊 Registrado: +1 ejercicio de escritura")
    except Exception:
        pass


if __name__ == "__main__":
    writing_session()
