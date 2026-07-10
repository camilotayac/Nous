#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OBSIDIAN_DIR = BASE_DIR.parent / "obsidian"

IGNORE_DIRS = {".venv", ".venv-mineru", ".agents", "output", ".obsidian", ".git", "_book", ".quarto"}

def _filter_dirs(dirs):
    return [d for d in dirs if not d.startswith(".") and d not in IGNORE_DIRS]

def sync():
    print("🔄 [Sync] Sincronizando Fuente de Verdad (Obsidian -> Quarto)...")
    if not OBSIDIAN_DIR.exists():
        print(f"⚠️ No se encontró el directorio {OBSIDIAN_DIR}")
        return

    # 1. Copiar base bibliográfica
    for bib_name in ["references.bib", "referencias.bib"]:
        src_bib = OBSIDIAN_DIR / bib_name
        if src_bib.exists():
            shutil.copy2(src_bib, BASE_DIR / "references.bib")
            print(f"📚 [Bib] {bib_name} -> quarto/references.bib")
            break

    # 2. Copiar y transformar archivos .md -> .qmd
    copied = set()
    for root, dirs, files in os.walk(OBSIDIAN_DIR):
        dirs[:] = _filter_dirs(dirs)
        rel_path = Path(root).relative_to(OBSIDIAN_DIR)

        for file in files:
            if file.endswith(".md"):
                src_file = Path(root) / file
                target_dir = BASE_DIR / rel_path
                target_dir.mkdir(parents=True, exist_ok=True)

                target_file = target_dir / (src_file.stem + ".qmd")
                shutil.copy2(src_file, target_file)
                copied.add(target_file.resolve())
                print(f"📝 [Doc] {rel_path / file} -> {rel_path / target_file.name}")

    # 3. Limpiar archivos .qmd huérfanos (ya no existen en Obsidian)
    removed = 0
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = _filter_dirs(dirs)
        for file in files:
            if not file.endswith(".qmd"):
                continue
            target_file = (Path(root) / file).resolve()
            if file == "references.qmd":
                continue  # archivo propio de Quarto, no proviene de Obsidian
            if target_file in copied:
                continue
            target_file.unlink()
            removed += 1
            rel = target_file.relative_to(BASE_DIR)
            print(f"🗑️ [Orphan] {rel} eliminado (ya no existe en obsidian/)")

    if removed:
        print(f"🧹 [Sync] Limpieza: {removed} archivos huérfanos eliminados.")
    print(f"✅ [Sync] Completado: {len(copied)} documentos sincronizados.")

if __name__ == "__main__":
    sync()
