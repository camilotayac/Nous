#!/usr/bin/env python3
"""Sync _quarto.yml chapter listings with actual .qmd files on disk.

Regular chapters go into their normal parts (Conjuntos, Química, etc.).
MOC files are grouped into a 'Mapas de contenido' part at the end.
"""

import re
import yaml
from pathlib import Path
from collections import OrderedDict

BASE_DIR = Path(__file__).resolve().parent
QUARTO_YML = BASE_DIR / "_quarto.yml"

MOC_PART_NAME = "Mapas de contenido"
EXCLUDE_EXACT = {"references.qmd", "index.qmd", "intro.qmd", "summary.qmd"}
MOC_SUFFIX = "_moc.qmd"


def ordered_load(stream):
    class OrderedLoader(yaml.SafeLoader):
        pass

    def construct_mapping(loader, node):
        return OrderedDict(loader.construct_pairs(node))

    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping
    )
    return yaml.load(stream, OrderedLoader)


def ordered_dump(data, stream=None, **kw):
    class OrderedDumper(yaml.SafeDumper):
        pass

    def represent_ordereddict(dumper, value):
        return dumper.represent_mapping(
            "tag:yaml.org,2002:map", value.items()
        )

    OrderedDumper.add_representer(OrderedDict, represent_ordereddict)
    return yaml.dump(data, stream, Dumper=OrderedDumper, **kw)


def extract_part_name(dirname: str) -> str:
    """Convert '02_quimica' -> 'Química'"""
    name = dirname.split("_", 1)[-1] if "_" in dirname else dirname
    return name.capitalize()


def list_qmd_files(directory: Path) -> tuple[list[str], list[str]]:
    """Return (regular_files, moc_files) sorted."""
    regular, mocs = [], []
    if not directory.exists():
        return regular, mocs
    for f in sorted(directory.iterdir()):
        if f.suffix != ".qmd":
            continue
        if f.name in EXCLUDE_EXACT:
            continue
        if f.name.endswith(MOC_SUFFIX):
            mocs.append(f.name)
        else:
            regular.append(f.name)
    return regular, mocs


def main():
    if not QUARTO_YML.exists():
        print(f"❌ {QUARTO_YML} not found")
        return

    with open(QUARTO_YML) as f:
        config = ordered_load(f)

    chapters = config.get("book", {}).get("chapters", [])
    if not chapters:
        print("❌ No chapters section found in _quarto.yml")
        return

    # Split into preamble, parts, postamble
    preamble, parts_list, postamble = [], [], []
    in_parts = False
    for item in chapters:
        if isinstance(item, dict) and "part" in item:
            in_parts = True
            parts_list.append(item)
        elif in_parts:
            postamble.append(item)
        else:
            preamble.append(item)

    seen_dirs = set()
    new_parts = []
    all_mocs = []  # collect MOCs from all dirs

    for part_entry in parts_list:
        part_name = part_entry.get("part", "")

        # Skip Mapas de contenido (will be rebuilt from scratch)
        if part_name == MOC_PART_NAME:
            continue

        cur_chapters = part_entry.get("chapters", [])
        if not cur_chapters:
            new_parts.append(part_entry)
            continue

        first = Path(cur_chapters[0])
        parent = str(first.parent)

        # Parts without a chapter directory (e.g. Apéndices)
        if parent == ".":
            new_parts.append(part_entry)
            continue

        chapter_dir = BASE_DIR / parent
        if not chapter_dir.exists():
            print(f"  🗑️ {parent}: directorio eliminado → parte '{part_name}' eliminada")
            continue

        regular, mocs = list_qmd_files(chapter_dir)
        new_paths = [f"{parent}/{f}" for f in regular]
        new_parts.append({"part": part_name, "chapters": new_paths})
        seen_dirs.add(parent)

        for moc in mocs:
            all_mocs.append(f"{parent}/{moc}")

        print(f"  ✅ {parent}: {len(regular)} capítulos, {len(mocs)} MOC{'s' if len(mocs) != 1 else ''}")

    # Discover new chapter directories
    for item in sorted(BASE_DIR.iterdir()):
        if not item.is_dir():
            continue
        if not re.match(r"^\d{2}_", item.name):
            continue
        if item.name in seen_dirs:
            continue
        regular, mocs = list_qmd_files(item)
        if not regular and not mocs:
            continue
        part_name = extract_part_name(item.name)
        new_paths = [f"{item.name}/{f}" for f in regular]
        new_parts.append({"part": part_name, "chapters": new_paths})
        seen_dirs.add(item.name)

        for moc in mocs:
            all_mocs.append(f"{item.name}/{moc}")

        print(f"  ➕ {item.name}: nueva parte '{part_name}' ({len(regular)} capítulos, {len(mocs)} MOC{'s' if len(mocs) != 1 else ''})")

    # Add Mapas de contenido part with all MOCs
    if all_mocs:
        new_parts.append({"part": MOC_PART_NAME, "chapters": sorted(all_mocs)})
        print(f"  📍 {MOC_PART_NAME}: {len(all_mocs)} MOC{'s' if len(all_mocs) != 1 else ''}")

    config["book"]["chapters"] = preamble + new_parts + postamble

    with open(QUARTO_YML, "w") as f:
        ordered_dump(config, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

    print("\n✅ _quarto.yml actualizado")


if __name__ == "__main__":
    main()
