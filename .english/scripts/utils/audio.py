#!/usr/bin/env python3
"""
Audio utilities: TTS generation with gTTS, playback with afplay.
"""
import os
import re
import subprocess
import hashlib
from datetime import datetime

AUDIO_DIR = os.path.expanduser("~/.english/data/audio")
CONVERSATION_AUDIO_DIR = os.path.expanduser("~/.english/data/conversation_audio")


def generate_audio(text, output_path):
    """Generate MP3 audio from English text using gTTS."""
    try:
        from gtts import gTTS
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        tts = gTTS(text=text, lang="en", tld="com")
        tts.save(output_path)
        return output_path
    except ImportError:
        print("   ⚠️  gTTS no instalado. Instala con: pip install gTTS")
        return None
    except Exception as e:
        print(f"   ⚠️  Error generando audio: {e}")
        return None


def play_audio(filepath):
    """Play audio with afplay (blocks until done)."""
    try:
        subprocess.run(["afplay", filepath], check=True)
    except FileNotFoundError:
        print("   ⚠️  afplay no encontrado (solo macOS)")
    except subprocess.CalledProcessError:
        print("   ⚠️  Error reproduciendo audio")


def play_and_cleanup(filepath):
    """Play audio then delete the file."""
    try:
        play_audio(filepath)
    finally:
        if os.path.exists(filepath):
            os.remove(filepath)


def speak(text):
    """Generate audio, play it, and clean up. Used for conversation responses."""
    os.makedirs(CONVERSATION_AUDIO_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    audio_path = os.path.join(CONVERSATION_AUDIO_DIR, f"resp_{timestamp}.mp3")
    generate_audio(text, audio_path)
    print(f"   🔊 [audio]")
    play_and_cleanup(audio_path)


def get_audio_path(term):
    """Get consistent audio path for a term (cached)."""
    os.makedirs(AUDIO_DIR, exist_ok=True)
    safe = re.sub(r'[^\w\-.]', '_', term)[:64]
    h = hashlib.md5(term.encode()).hexdigest()[:8]
    return os.path.join(AUDIO_DIR, f"{h}_{safe}.mp3")


def ensure_audio(term):
    """Generate audio for term if it doesn't exist, return path."""
    path = get_audio_path(term)
    if not os.path.exists(path):
        generate_audio(term, path)
    return path
