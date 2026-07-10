#!/usr/bin/env python3
"""
update_biblioteca.py
Escanea transcripcion/output/ buscando archivos .md generados por MinerU,
los copia a biblioteca/ con nombre estandarizado, y actualiza biblioteca_index.json.
"""

import hashlib
import json
import os
import re
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSCRIPCION_DIR = ROOT / "transcripcion" / "output"
BIBLIOTECA_DIR = ROOT / "biblioteca"
INDEX_PATH = BIBLIOTECA_DIR / "biblioteca_index.json"
KNOWLEDGE_MAP_PATH = ROOT / "obsidian" / "knowledge_map.json"

RAMA_PATTERNS = {
    "quimica": re.compile(r"quimi|brown|oriakhi|chem"),
    "fisica": re.compile(r"física|physics|griffith|mekan"),
    "biologia": re.compile(r"biolog|herencia|genet"),
    "matematicas": re.compile(r"matem|calc|algebr"),
}

KNOWN_SOURCES = {
    "cap14_cinetica": {
        "title": "Cinética química",
        "libro": "Theodore L. Brown - Química, la ciencia central (12ed, 2014)",
        "capitulo": 14,
        "rama": "quimica",
    },
}


def load_index() -> dict:
    if INDEX_PATH.exists():
        with open(INDEX_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"generated_at": "", "entries": []}


def save_index(index: dict):
    index["generated_at"] = datetime.now().isoformat(timespec="seconds")
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    print(f"[OK] Index guardado en {INDEX_PATH}")


def detect_rama(folder_name: str, content_sample: str = "") -> str:
    combined = folder_name + " " + content_sample
    for rama, pattern in RAMA_PATTERNS.items():
        if pattern.search(combined.lower()):
            return rama
    return "general"


def extract_title_from_frontmatter(content: str) -> str | None:
    match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if match:
        fm = match.group(1)
        title_match = re.search(r"titulo:\s*[\"']?(.+?)[\"']?\s*$", fm, re.MULTILINE)
        if title_match:
            return title_match.group(1).strip()
        title_match = re.search(r"title:\s*[\"']?(.+?)[\"']?\s*$", fm, re.MULTILINE)
        if title_match:
            return title_match.group(1).strip()
    return None


def extract_title_from_heading(content: str) -> str | None:
    match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


def standardize_name(folder_name: str, rama: str) -> str:
    clean = re.sub(r"[^a-z0-9_]", "_", folder_name.lower())
    clean = re.sub(r"_+", "_", clean).strip("_")
    if rama not in clean:
        clean = f"{rama}_{clean}"
    return clean


def find_existing_id(index: dict, filename: str) -> dict | None:
    for entry in index["entries"]:
        if entry["archivo"].endswith(filename):
            return entry
    return None


def cross_reference(entry: dict, knowledge_map: dict | None) -> list:
    if not knowledge_map:
        return entry.get("notas_relacionadas", [])

    related = []
    rama = entry.get("rama", "")
    title_lower = entry.get("title", "").lower()

    for note_path, note_meta in knowledge_map.get("notes", {}).items():
        if rama != "general" and rama not in note_path.lower():
            continue
        note_title = note_meta.get("title", "").lower()
        if any(word in note_title for word in title_lower.split()):
            related.append({
                "nota": f"obsidian/{note_path}",
                "coincidencia": "media",
                "secciones": note_meta.get("sections", []),
            })

    return related if related else entry.get("notas_relacionadas", [])


def content_hash(filepath: Path) -> str:
    return hashlib.md5(filepath.read_bytes()).hexdigest()


def existing_hashes() -> set:
    hashes = set()
    for md in BIBLIOTECA_DIR.glob("*.md"):
        hashes.add(content_hash(md))
    return hashes


def scan_and_update():
    print(f"[SCAN] Escaneando {TRANSCRIPCION_DIR} ...")

    if not TRANSCRIPCION_DIR.exists():
        print(f"[WARN] Directorio no encontrado: {TRANSCRIPCION_DIR}")
        return

    index = load_index()
    existing_ids = {e["id"] for e in index["entries"]}
    skip_hashes = existing_hashes()

    knowledge_map = None
    if KNOWLEDGE_MAP_PATH.exists():
        with open(KNOWLEDGE_MAP_PATH, "r", encoding="utf-8") as f:
            knowledge_map = json.load(f)
        print(f"[OK] knowledge_map cargado")

    BIBLIOTECA_DIR.mkdir(parents=True, exist_ok=True)

    new_entries = 0

    for item in sorted(TRANSCRIPCION_DIR.iterdir()):
        if not item.is_dir():
            continue
        if item.name.startswith("_") or item.name == "auto":
            continue

        md_files = list(item.glob("*.md"))
        if not md_files:
            continue

        md_file = md_files[0]
        content = md_file.read_text(encoding="utf-8")
        sample = content[:500]

        file_hash = content_hash(md_file)
        if file_hash in skip_hashes:
            print(f"[SKIP] Duplicado por contenido: {item.name}")
            continue

        rama = detect_rama(item.name, sample)
        info = KNOWN_SOURCES.get(item.name, {})

        title = (
            info.get("title")
            or extract_title_from_frontmatter(content)
            or extract_title_from_heading(content)
            or item.name.replace("_", " ").title()
        )

        std_name = standardize_name(item.name, rama)

        if std_name in existing_ids:
            print(f"[SKIP] Ya existe: {std_name}")
            continue

        dest = BIBLIOTECA_DIR / f"{std_name}.md"
        shutil.copy2(md_file, dest)
        print(f"[COPY] {md_file.name} -> {dest.name}")

        entry = {
            "id": std_name,
            "title": title,
            "libro": info.get("libro", "desconocido"),
            "capitulo": info.get("capitulo"),
            "rama": rama,
            "archivo": f"biblioteca/{std_name}.md",
            "notas_relacionadas": info.get("notas_relacionadas", []),
        }

        entry["notas_relacionadas"] = cross_reference(entry, knowledge_map)

        index["entries"].append(entry)
        existing_ids.add(std_name)
        new_entries += 1
        print(f"[ADD] {std_name} (rama={rama})")

    save_index(index)
    print(f"[DONE] {new_entries} nuevas entradas, {len(index['entries'])} total")


if __name__ == "__main__":
    scan_and_update()
