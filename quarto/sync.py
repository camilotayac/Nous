#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OBSIDIAN_DIR = BASE_DIR.parent / "obsidian"

IGNORE_DIRS = {".venv", ".venv-mineru", ".agents", "output", ".obsidian", ".git", "_book", ".quarto"}

def _filter_dirs(dirs):
    return [d for d in dirs if not d.startswith(".") and not d.startswith("_") and d not in IGNORE_DIRS]

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
            src_file = Path(root) / file
            target_dir = BASE_DIR / rel_path

            if file.endswith(".md"):
                target_dir.mkdir(parents=True, exist_ok=True)
                target_file = target_dir / (src_file.stem + ".qmd")
                shutil.copy2(src_file, target_file)
                copied.add(target_file.resolve())
                print(f"📝 [Doc] {rel_path / file} -> {rel_path / target_file.name}")
            elif file.lower().endswith((".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp")):
                target_dir.mkdir(parents=True, exist_ok=True)
                target_file = target_dir / file
                shutil.copy2(src_file, target_file)
                print(f"🖼️ [Img] {rel_path / file} -> {rel_path / file}")

    # 3. Limpiar archivos .qmd huérfanos (ya no existen en Obsidian)
    removed = 0
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = _filter_dirs(dirs)
        for file in files:
            if not file.endswith(".qmd"):
                continue
            local_file = Path(root) / file
            if file == "references.qmd":
                continue  # archivo propio de Quarto, no proviene de Obsidian
            if local_file.resolve() in copied:
                continue

            # Seguridad estricta: verificar contención dentro de BASE_DIR
            try:
                rel = local_file.relative_to(BASE_DIR)
            except ValueError:
                print(f"⚠️ [Skip] {local_file} está fuera de BASE_DIR, omitiendo por seguridad.")
                continue

            # En lugar de eliminar permanentemente, mover a .trash como respaldo de seguridad
            trash_dir = BASE_DIR / ".trash"
            trash_target = trash_dir / rel
            trash_target.parent.mkdir(parents=True, exist_ok=True)
            if trash_target.exists():
                trash_target.unlink()
            shutil.move(str(local_file), str(trash_target))
            removed += 1
            print(f"🗑️ [Orphan] {rel} respaldado en .trash/ (ya no existe en obsidian/)")

    if removed:
        print(f"🧹 [Sync] Limpieza: {removed} archivos huérfanos eliminados.")
    print(f"✅ [Sync] Completado: {len(copied)} documentos sincronizados.")

if __name__ == "__main__":
    sync()
