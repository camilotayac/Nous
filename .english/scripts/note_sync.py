#!/usr/bin/env python3
"""
Note synchronization: detect changes in Obsidian vault,
regenerate reading materials and audio when notes change.
"""
import os
import re
import json
import hashlib
from pathlib import Path

VAULT_DIR = os.path.expanduser("~/Documents/GitHub/Nous/obsidian")
READING_DIR = os.path.expanduser("~/.english/data/reading")
AUDIO_DIR = os.path.expanduser("~/.english/data/note_audio")
SYNC_FILE = os.path.expanduser("~/.english/data/note_hashes.json")

SKIP_FILES = {"index.md", "intro.md", "summary.md"}


def _load_hashes():
    if os.path.exists(SYNC_FILE):
        with open(SYNC_FILE) as f:
            return json.load(f)
    return {}


def _save_hashes(hashes):
    os.makedirs(os.path.dirname(SYNC_FILE), exist_ok=True)
    with open(SYNC_FILE, "w") as f:
        json.dump(hashes, f, indent=2)


def _file_hash(filepath):
    with open(filepath, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def _clean_markdown(content):
    clean = re.sub(r'\$\$[\s\S]*?\$\$', '', content)
    clean = re.sub(r'\$[^$]+\$', '', clean)
    clean = re.sub(r'```[\s\S]*?```', '', clean)
    clean = re.sub(r':::.*?:::', '', clean, flags=re.DOTALL)
    clean = re.sub(r'\[\[.*?\]\]', '', clean)
    clean = re.sub(r'[@#]\S+', '', clean)
    clean = re.sub(r'!\[.*?\]\(.*?\)', '', clean)
    clean = re.sub(r'\[.*?\]\(.*?\)', '', clean)
    clean = re.sub(r'[-=]{3,}', '', clean)
    clean = re.sub(r'[|]', ' ', clean)
    return clean.strip()


def scan_vault():
    notes = []
    for root, dirs, files in os.walk(VAULT_DIR):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith(".md") and f not in SKIP_FILES and not f.startswith("."):
                filepath = os.path.join(root, f)
                abs_path = str(Path(filepath).resolve())
                rel_path = os.path.relpath(filepath, VAULT_DIR)
                notes.append({
                    "abs_path": abs_path,
                    "rel_path": rel_path,
                    "hash": _file_hash(abs_path),
                })
    return notes


def detect_changes():
    stored = _load_hashes()
    current = scan_vault()

    new_notes = []
    updated_notes = []
    deleted_notes = []

    current_paths = {n["abs_path"] for n in current}
    stored_paths = set(stored.keys())

    for note in current:
        if note["abs_path"] not in stored:
            new_notes.append(note)
        elif stored[note["abs_path"]] != note["hash"]:
            updated_notes.append(note)

    for path in stored_paths - current_paths:
        deleted_notes.append(path)

    return new_notes, updated_notes, deleted_notes


def generate_reading(note_path):
    with open(note_path) as f:
        content = f.read()

    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else Path(note_path).stem

    clean = _clean_markdown(content)

    from utils.translate import extract_spanish_terms, translate_to_english
    terms = extract_spanish_terms(clean, max_terms=50)
    term_map = {}
    for t in terms:
        en = translate_to_english(t)
        if en.lower() != t.lower():
            term_map[t.lower()] = en

    paragraphs = [p.strip() for p in clean.split('\n\n') if p.strip()]

    reading_lines = [f"# {title}\n"]
    for para in paragraphs:
        if para.startswith('#'):
            reading_lines.append(f"\n{para}\n")
            continue
        en_para = _translate_paragraph(para, term_map)
        reading_lines.append(f"{en_para}\n")

    return "\n".join(reading_lines)


def _translate_paragraph(text, term_map):
    try:
        from deep_translator import GoogleTranslator
        result = GoogleTranslator(source='es', target='en').translate(text)
        if result:
            for es_term, en_term in term_map.items():
                result = re.sub(r'\b' + re.escape(es_term) + r'\b', en_term, result, flags=re.IGNORECASE)
            return result
    except Exception:
        pass
    for es_term, en_term in term_map.items():
        text = re.sub(r'\b' + re.escape(es_term) + r'\b', en_term, text, flags=re.IGNORECASE)
    return text


def save_reading(note_path, reading_text):
    os.makedirs(READING_DIR, exist_ok=True)
    basename = Path(note_path).stem
    out_path = os.path.join(READING_DIR, f"{basename}.md")
    with open(out_path, "w") as f:
        f.write(reading_text)
    return out_path


def generate_note_audio(note_path):
    with open(note_path) as f:
        content = f.read()

    clean = _clean_markdown(content)

    try:
        from deep_translator import GoogleTranslator
        english_text = GoogleTranslator(source='es', target='en').translate(clean)
    except Exception:
        english_text = clean

    paragraphs = [p.strip() for p in english_text.split('\n') if p.strip()]
    return paragraphs


def save_note_audio(note_path, paragraphs):
    os.makedirs(AUDIO_DIR, exist_ok=True)
    basename = Path(note_path).stem
    audio_dir = os.path.join(AUDIO_DIR, basename)
    os.makedirs(audio_dir, exist_ok=True)

    from utils.audio import generate_audio
    paths = []
    for i, para in enumerate(paragraphs):
        if len(para.strip()) < 5:
            continue
        audio_path = os.path.join(audio_dir, f"part_{i:03d}.mp3")
        if not os.path.exists(audio_path):
            generate_audio(para, audio_path)
        paths.append(audio_path)
    return paths


def sync_all(verbose=True):
    new, updated, deleted = detect_changes()

    if not new and not updated and not deleted:
        if verbose:
            print("✅ Vault sincronizado — sin cambios.")
        return 0

    total = 0
    if verbose and new:
        print(f"📝 {len(new)} notas nuevas:")
    for note in new:
        if verbose:
            print(f"   + {note['rel_path']}")
        _process_note(note["abs_path"])
        total += 1

    if verbose and updated:
        print(f"🔄 {len(updated)} notas actualizadas:")
    for note in updated:
        if verbose:
            print(f"   ~ {note['rel_path']}")
        _process_note(note["abs_path"], is_update=True)
        total += 1

    if verbose and deleted:
        print(f"🗑️  {len(deleted)} notas eliminadas:")
        for path in deleted:
            if verbose:
                print(f"   - {os.path.basename(path)}")

    hashes = _load_hashes()
    for note in new + updated:
        hashes[note["abs_path"]] = note["hash"]
    for path in deleted:
        hashes.pop(path, None)
    _save_hashes(hashes)

    if verbose:
        print(f"\n✅ {total} notas procesadas.")

    return total


def _process_note(abs_path, is_update=False):
    import generate_cards
    try:
        generate_cards.generate_from_note(abs_path, force=is_update)
    except Exception as e:
        print(f"   ⚠️ Error generando cards: {e}")

    try:
        reading_text = generate_reading(abs_path)
        save_reading(abs_path, reading_text)
    except Exception as e:
        print(f"   ⚠️ Error generando lectura: {e}")


if __name__ == "__main__":
    sync_all()
