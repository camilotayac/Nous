#!/usr/bin/env python3
"""
Listening mode: play translated notes audio with optional text display.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

READING_DIR = os.path.expanduser("~/.english/data/reading")
AUDIO_DIR = os.path.expanduser("~/.english/data/note_audio")


def list_available():
    if not os.path.exists(READING_DIR):
        return []
    notes = []
    for f in os.listdir(READING_DIR):
        if f.endswith(".md"):
            name = f.replace(".md", "")
            audio_dir = os.path.join(AUDIO_DIR, name)
            has_audio = os.path.exists(audio_dir) and any(
                fp.endswith(".mp3") for fp in os.listdir(audio_dir)
            ) if os.path.exists(audio_dir) else False
            notes.append({"file": f, "name": name, "has_audio": has_audio})
    return notes


def generate_audio_for_note(note_name):
    reading_path = os.path.join(READING_DIR, f"{note_name}.md")
    if not os.path.exists(reading_path):
        print(f"❌ No existe la nota traducida: {note_name}")
        return []

    with open(reading_path) as f:
        content = f.read()

    paragraphs = [p.strip() for p in content.split("\n") if p.strip()]

    from utils.audio import generate_audio
    audio_dir = os.path.join(AUDIO_DIR, note_name)
    os.makedirs(audio_dir, exist_ok=True)

    paths = []
    for i, para in enumerate(paragraphs):
        if len(para) < 5 or para.startswith("#"):
            continue
        audio_path = os.path.join(audio_dir, f"part_{i:03d}.mp3")
        if not os.path.exists(audio_path):
            print(f"   🔊 Generando audio parte {i+1}...")
            generate_audio(para, audio_path)
        paths.append((audio_path, para))
    return paths


def play_with_text(audio_parts):
    from utils.audio import play_audio

    print()
    print("┌──────────────────────────────────────────────────────────┐")
    print("│  🔊 Modo Listening                                      │")
    print("│  Escucha el audio y sigue el texto                      │")
    print("│  Comandos: Enter=siguiente  t=toggle texto  q=salir     │")
    print("└──────────────────────────────────────────────────────────┘")
    print()

    show_text = True
    for i, (audio_path, text) in enumerate(audio_parts):
        print(f"  ── Parte {i+1}/{len(audio_parts)} ──")
        if show_text:
            print(f"  📝 {text[:120]}{'...' if len(text) > 120 else ''}")
        print(f"  🔊 Reproduciendo...")
        play_audio(audio_path)

        try:
            action = input("  Enter=continuar / t=texto off/on / q=salir: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n\n👋 Sesión terminada.")
            return

        if action == "q":
            return
        elif action == "t":
            show_text = not show_text
            print(f"  Texto: {'ON' if show_text else 'OFF'}")

    print()
    print("  🎉 ¡Escucha completada!")


def listening_session():
    notes = list_available()

    if not notes:
        print("📭 No hay notas disponibles para escuchar.")
        print("   Primero procesa notas desde el menú principal.")
        return

    print("\n🔊 Modo Listening — Notas en inglés")
    print()

    for i, n in enumerate(notes, 1):
        status = "🔊" if n["has_audio"] else "📝 (sin audio)"
        name = n["name"].replace("_", " ").title()
        print(f"  {i}. {name} {status}")

    print(f"  0. Volver")
    print()

    try:
        choice = input("Selecciona nota: ").strip()
    except (EOFError, KeyboardInterrupt):
        return

    if choice == "0" or choice == "":
        return

    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(notes):
        print("❌ Opción no válida.")
        return

    selected = notes[int(choice) - 1]
    note_name = selected["name"]

    audio_parts = generate_audio_for_note(note_name)

    if not audio_parts:
        print("⚠️ No se pudo generar audio para esta nota.")
        return

    print(f"\n✅ Audio generado: {len(audio_parts)} partes")
    play_with_text(audio_parts)

    try:
        import progress
        progress.record_note_listened()
        print("   📊 Registrado: +1 nota escuchada")
    except Exception:
        pass


if __name__ == "__main__":
    listening_session()
