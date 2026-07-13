#!/usr/bin/env python3
"""
English Learning Session - Main Entry Point with progression system.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
import srs_engine
import review
import generate_cards
import progress
import note_sync


def show_stats():
    progress.show_progress()
    stats = srs_engine.get_stats()
    print("  📦 Base de datos SRS:")
    print(f"     Total cards:    {stats['total']}")
    print(f"     Nuevas:         {stats['new']}")
    print(f"     Aprendiendo:    {stats['learning']}")
    print(f"     En repaso:      {stats['review']}")
    print(f"     Pendientes:     {stats['due_now']}")
    print()


def main_menu():
    unlocked = progress.get_unlocked_stages()
    current = progress.get_current_stage()
    stage_info = progress.STAGES[current]

    bar_len = 20
    filled = int(bar_len * current / 6)
    bar = "█" * filled + "░" * (bar_len - filled)

    print()
    print("╔═══════════════════════════════════════════════════════╗")
    print("║        🇬🇧 English Learning System                    ║")
    print(f"║        [{bar}] Etapa {current}/6                         ║")
    print(f"║        {stage_info['icon']} {stage_info['name_es']:<40}  ║")
    print("╠═══════════════════════════════════════════════════════╣")

    options = []
    idx = 1

    if 1 in unlocked:
        print(f"║  {idx}. 📚 Repasar vocabulario                        ║")
        options.append("vocab")
        idx += 1
    if 2 in unlocked:
        print(f"║  {idx}. 📖 Leer notas en inglés                       ║")
        options.append("reading")
        idx += 1
    if 3 in unlocked:
        print(f"║  {idx}. 🔊 Escuchar notas en inglés                   ║")
        options.append("listening")
        idx += 1
    if 4 in unlocked:
        print(f"║  {idx}. ✍️  Ejercicios de escritura                    ║")
        options.append("writing")
        idx += 1
    if 5 in unlocked:
        print(f"║  {idx}. 🎤 Practicar pronunciación                    ║")
        options.append("speaking")
        idx += 1
    if 6 in unlocked:
        print(f"║  {idx}. 💬 Conversar en inglés                        ║")
        options.append("conversation")
        idx += 1

    print("║")
    print(f"║  {idx}. 📊 Ver progreso completo                      ║")
    print(f"║  {idx+1}. 🔄 Sincronizar notas de Obsidian              ║")
    print(f"║  {idx+2}. 🗑️  Eliminar todas las cards                  ║")
    print(f"║  q. 👋 Salir                                         ║")
    print("╚═══════════════════════════════════════════════════════╝")

    next_unlock = progress.get_next_unlock()
    if next_unlock:
        print()
        print(f"  🎯 Siguiente: {next_unlock['icon']} {next_unlock['name']}")
        for key, remaining in next_unlock["remaining"].items():
            label = {
                "cards_reviewed": "cards repasadas",
                "retention_pct": "puntos retención",
                "notes_read": "notas leídas",
                "notes_listened": "notas escuchadas",
                "writing_exercises": "ejercicios escritura",
                "speaking_sessions": "sesiones speaking",
            }.get(key, key)
            print(f"     → Faltan {remaining} {label}")
        print()

    while True:
        try:
            choice = input("Selecciona: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 ¡Hasta luego!")
            return

        if choice == "q":
            print("👋 ¡Hasta luego!")
            return

        if not choice.isdigit():
            print("Opción no válida.")
            continue

        num = int(choice)

        if num == idx:
            show_stats()
            continue
        if num == idx + 1:
            print("\n🔄 Sincronizando notas de Obsidian...")
            note_sync.sync_all()
            continue
        if num == idx + 2:
            confirm = input("⚠️  ¿Eliminar TODAS las cards? (s/n): ").strip().lower()
            if confirm == "s":
                srs_engine.delete_all_cards()
                print("🗑️  Todas las cards eliminadas.")
            continue

        if num < 1 or num > len(options):
            print("Opción no válida.")
            continue

        action = options[num - 1]

        if action == "vocab":
            topics = srs_engine.get_all_topics()
            if topics:
                print("\nTemas disponibles:")
                for i, t in enumerate(topics, 1):
                    print(f"  {i}. {t}")
                print(f"  0. Todos")
                try:
                    tchoice = input("Tema: ").strip()
                    if tchoice == "0" or tchoice == "":
                        review.review_session()
                    elif tchoice.isdigit() and 1 <= int(tchoice) <= len(topics):
                        review.review_session(topic=topics[int(tchoice)-1])
                    else:
                        review.review_session()
                except (EOFError, KeyboardInterrupt):
                    pass
            else:
                review.review_session()

        elif action == "reading":
            import reading
            reading.reading_session()

        elif action == "listening":
            import listening
            listening.listening_session()

        elif action == "writing":
            import writing
            writing.writing_session()

        elif action == "speaking":
            import speaking
            speaking.speaking_session()

        elif action == "conversation":
            import conversation
            conversation.conversation_session()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "review":
            topic = sys.argv[2] if len(sys.argv) > 2 else None
            review.review_session(topic=topic)
        elif cmd == "stats":
            show_stats()
        elif cmd == "generate":
            if len(sys.argv) > 2:
                for fp in sys.argv[2:]:
                    generate_cards.generate_from_note(fp)
            else:
                generate_cards.generate_all()
        elif cmd == "sync":
            note_sync.sync_all()
        elif cmd == "reading":
            import reading
            reading.reading_session()
        elif cmd == "listening":
            import listening
            listening.listening_session()
        elif cmd == "writing":
            import writing
            writing.writing_session()
        elif cmd == "speaking":
            import speaking
            speaking.speaking_session()
        elif cmd == "conversation":
            import conversation
            conversation.conversation_session()
        else:
            print(f"Comando desconocido: {cmd}")
            print("Uso: python3 english_session.py [review|stats|generate|sync|reading|listening|writing|speaking|conversation]")
    else:
        main_menu()
