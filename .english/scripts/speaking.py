#!/usr/bin/env python3
"""
Speaking mode: compare pronunciation with audio using SpeechRecognition.
"""
import os
import sys
import random

sys.path.insert(0, os.path.dirname(__file__))


def get_words_to_practice():
    try:
        import srs_engine
        cards = srs_engine.get_due(limit=50)
        words = []
        seen = set()
        for c in cards:
            front = c.get("front", "")
            back = c.get("back", "")
            if back and back.lower() not in seen:
                seen.add(back.lower())
                words.append({"english": back, "spanish": front})
        return words
    except Exception:
        return []


def record_audio():
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("   🎤 Escuchando... (habla ahora)")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        try:
            text = recognizer.recognize_google(audio, language="en-US")
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            print("   ⚠️ Error con el servicio de reconocimiento.")
            return None
    except ImportError:
        print("   ⚠️ speech_recognition no instalado.")
        print("   Instala con: pip install SpeechRecognition pyaudio")
        return None
    except OSError:
        print("   ⚠️ No se encontró micrófono.")
        return None


def speaking_session():
    words = get_words_to_practice()

    if not words:
        print("📭 No hay vocabulary para practicar.")
        print("   Asegúrate de tener cards en el SRS.")
        return

    random.shuffle(words)
    practice_words = words[:10]

    print("\n🎤 Modo Speaking — Practica tu pronunciación")
    print("   Escucharás una palabra en inglés.")
    print("   Después, habla al micrófono y compara.\n")
    print("   Comandos: Enter=escuchar de nuevo  s=saltar  q=salir\n")

    correct = 0
    total = len(practice_words)

    for i, word_info in enumerate(practice_words, 1):
        english = word_info["english"]
        spanish = word_info["spanish"]

        print(f"  ── Palabra {i}/{total} ──")
        print(f"  🇪🇸 {spanish}")

        audio_path = os.path.expanduser(f"~/.english/data/speaking/{english}.mp3")
        os.makedirs(os.path.dirname(audio_path), exist_ok=True)

        from utils.audio import ensure_audio, play_audio
        path = ensure_audio(english)
        print(f"  🔊 Reproduciendo: {english}")
        play_audio(path)

        from utils.ipa import format_pronunciation_guide
        from utils.translate import get_ipa
        ipa = get_ipa(english)
        if ipa:
            print(f"  IPA: {ipa}")

        print(f"  Intenta decir: {english}")

        while True:
            try:
                action = input("  Enter=hablar / r=repetir audio / s=saltar / q=salir: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\n\n👋 Sesión terminada.")
                return

            if action == "q":
                return
            elif action == "s":
                break
            elif action == "r":
                print(f"  🔊 Reproduciendo: {english}")
                play_audio(path)
                continue
            elif action == "":
                recognized = record_audio()
                if recognized is None:
                    print("  ⚠️ No se pudo reconocer. Intenta de nuevo.")
                    continue
                print(f"  🎤 Dijiste: {recognized}")

                if english.lower() in recognized.lower():
                    print(f"  ✅ ¡Correcto!")
                    correct += 1
                else:
                    print(f"  ❌ Casi — la palabra era: {english}")
                break
            else:
                print("  Opción no válida.")
                continue

        print()

    print(f"  🎉 Práctica completada: {correct}/{total} correctas ({correct/total*100:.0f}%)")

    try:
        import progress
        progress.record_speaking_session()
        print("   📊 Registrado: +1 sesión de speaking")
    except Exception:
        pass


if __name__ == "__main__":
    speaking_session()
