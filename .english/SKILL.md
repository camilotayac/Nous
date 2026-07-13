# english-session

## Description
Terminal-based English learning system with FSRS spaced repetition, vocabulary review with IPA pronunciation and audio, and conversation practice. Self-contained — no Anki or GUI required.

## Triggers
- "english session", "sesión de inglés", "estudiar inglés"
- "repasar vocabulario", "review vocabulary", "review cards"
- "conversar en inglés", "conversación", "practica inglés"
- "procesar nota para inglés", "generar cards"
- "audio", "pronunciación", "pronunciation"

## Location
`.english/scripts/` — all scripts live here

## Quick Start
```bash
python3 .english/scripts/english_session.py          # Menu
python3 .english/scripts/english_session.py review   # Review vocab
python3 .english/scripts/english_session.py stats    # Show progress
python3 .english/scripts/english_session.py generate # Process Obsidian notes
```

## Architecture
- **SRS**: FSRS algorithm (same as Anki 23.10+) in pure Python
- **Storage**: SQLite at `~/.english/data/cards.db`
- **Audio**: gTTS → afplay → auto-delete
- **IPA**: eng_to_ipa + Spanish phoneme guide

## Scripts
| Script | Purpose |
|--------|---------|
| `english_session.py` | Main entry point with menu |
| `srs_engine.py` | FSRS motor with SQLite |
| `review.py` | Interactive review with audio + IPA |
| `conversation.py` | Audio conversation practice |
| `generate_cards.py` | Generate cards from Obsidian notes |
| `utils/audio.py` | gTTS + afplay functions |
| `utils/ipa.py` | IPA breakdown in Spanish |
| `utils/translate.py` | EN↔ES translation + dictionary |

## Dependencies
- Python 3.12+
- `fsrs`, `gtts`, `eng_to_ipa`, `deep_translator`
- macOS (afplay)
