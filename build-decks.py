#!/usr/bin/env python3
"""Build CCNP/decks.js from the per-topic .json deck files.

Scan every "Level*/" subfolder (including nested topic subfolders) for
*.json deck files, group them by level folder name, and write the bundle
used by index.html.

Usage:
    python3 build-decks.py
    (run from anywhere; it locates itself relative to the script)
"""

import glob
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    decks: dict[str, list[dict]] = {}

    for folder in sorted(glob.glob(os.path.join(ROOT, "Level*/"))):
        level = os.path.basename(folder.rstrip(os.sep))
        items = []
        for path in sorted(glob.glob(os.path.join(folder, "**", "*.json"), recursive=True)):
            if os.path.basename(path).startswith("index."):
                continue
            with open(path, encoding="utf-8") as fh:
                items.append(json.load(fh))
        if items:
            decks[level] = items

    with open(os.path.join(ROOT, "decks.js"), "w", encoding="utf-8") as fh:
        fh.write("// Auto-generated from the .json deck files -- do not edit by hand.\n")
        fh.write("// Regenerate with: python3 build-decks.py\n")
        fh.write("const DECKS = ")
        json.dump(decks, fh, indent=2, ensure_ascii=False)
        fh.write(";\n")

    total = sum(len(t["cards"]) for v in decks.values() for t in v)
    print(f"wrote decks.js: {len(decks)} levels, "
          f"{sum(len(v) for v in decks.values())} topics, {total} cards")


if __name__ == "__main__":
    main()
