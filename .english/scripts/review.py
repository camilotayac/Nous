#!/usr/bin/env python3
"""
Interactive vocabulary review with audio and IPA pronunciation.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
import srs_engine
from utils.audio import ensure_audio, play_audio
from utils.ipa import format_pronunciation_guide


def show_card(card, show_answer=False):
    ipa = card.get("ipa", "")
    topic = card.get("topic", "")
    card_type = card.get("card_type", "")
    front = card.get("front", "")
    back = card.get("back", "")

    print()
    print("┌─────────────────────────────────────────────────┐")
    if topic:
        print(f"│  📚 {topic}")
    print("│")

    if card_type == "vocab_es_en":
        print(f"│  🟢 {front}")
        print("│")
        if show_answer:
            print(f"│  ✅ {back}")
            if ipa:
                print(f"│  IPA: {ipa}")
            if card.get("example_es"):
                print(f"│")
                print(f"│  Ejemplo: {card['example_es'][:100]}")

    elif card_type == "vocab_en_es":
        print(f"│  🔵 {front}")
        if ipa:
            print(f"│  IPA: {ipa}")
        print("│")
        if show_answer:
            print(f"│  ✅ {back}")

    print("│")
    print("└─────────────────────────────────────────────────┘")

    if show_answer and ipa:
        print("  Desglose fonético:")
        print(format_pronunciation_guide(ipa))
        print()


def review_session(topic=None, limit=20):
    if topic:
        cards = [c for c in srs_engine.get_due(limit=100) if c["topic"] == topic][:limit]
        if not cards:
            cards = srs_engine.get_new_cards(limit=limit)
            cards = [c for c in cards if c["topic"] == topic][:limit]
    else:
        cards = srs_engine.get_due(limit=limit)
        if not cards:
            cards = srs_engine.get_new_cards(limit=limit)

    if not cards:
        print("🎉 No hay cards pendientes. ¡Todo al día!")
        return

    print(f"\n📚 Repasando {len(cards)} cards...")
    print("   Calificación: 1=Otra vez  2=Difícil  3=Bien  4=Fácil")
    print("   Comandos: 's' suspender  'q' salir  'a' mostrar respuesta")

    reviewed = 0
    for i, card in enumerate(cards):
        print(f"\n─── Card {i+1}/{len(cards)} ───")

        show_card(card, show_answer=False)

        if card["card_type"] == "vocab_es_en":
            audio_text = card["back"]
        else:
            audio_text = card["front"]
        audio_path = ensure_audio(audio_text)
        print(f"   🔊 Reproduciendo: {audio_text}")
        play_audio(audio_path)

        answer_revealed = False
        while True:
            try:
                if not answer_revealed:
                    action = input("\n   Enter=ver respuesta / s=suspender / q=salir: ").strip().lower()
                else:
                    action = input("\n   Tu respuesta (1-4 / a=repetir): ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\n\n👋 Sesión terminada.")
                return

            if action == "q":
                print(f"\n✅ Repasaste {reviewed} cards. ¡Hasta luego!")
                return
            elif action == "s":
                srs_engine.suspend_card(card["id"])
                print("   ⏸ Card suspendida.")
                break
            elif action in ("a", "") and not answer_revealed:
                show_card(card, show_answer=True)
                answer_revealed = True
                continue
            elif action == "a" and answer_revealed:
                if card["card_type"] == "vocab_es_en":
                    replay_text = card["back"]
                else:
                    replay_text = card["front"]
                print(f"   🔊 Reproduciendo: {replay_text}")
                play_audio(audio_path)
            elif action in ("1", "2", "3", "4") and answer_revealed:
                rating = int(action)
                srs_engine.review_card(card["id"], rating)
                reviewed += 1
                try:
                    import progress
                    progress.record_review()
                    stats = srs_engine.get_stats()
                    if stats["retention_pct"] is not None:
                        progress.set_retention(stats["retention_pct"])
                except Exception:
                    pass
                labels = {1: "Otra vez", 2: "Difícil", 3: "Bien", 4: "Fácil"}
                print(f"   ✓ {labels[rating]} — registrada.")
                break
            elif action in ("1", "2", "3", "4") and not answer_revealed:
                print("   Primero presiona Enter para ver la respuesta.")
            else:
                print("   Opción no válida.")

    print(f"\n🎉 ¡Sesión completada! Repasaste {reviewed} cards.")
    stats = srs_engine.get_stats()
    print(f"   📊 Total: {stats['total']} | Pendientes: {stats['due_now']} | Retención: {stats['retention_pct'] or 'N/A'}%")


if __name__ == "__main__":
    topic = sys.argv[1] if len(sys.argv) > 1 else None
    review_session(topic=topic)
