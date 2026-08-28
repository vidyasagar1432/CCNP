#!/usr/bin/env python3
"""Fix "glued" heading text: insert a space where text touches inline-code backticks.

Opening delimiter glued to preceding text  -> space BEFORE the backtick run.
Closing delimiter glued to following text  -> space AFTER  the backtick run.
Only touches heading lines (lines starting with '#'). Plain punctuation
attached to code (`code`., `code`)) is left alone -- normal typography.

Usage:
    python3 fix_glued.py [root]
    (root defaults to "." -- run from the vault root)

Skips: .git, .obsidian, .trash, .opencode, copilot (auto-generated exports).
Prints a diff-style summary; rewrites files in place. Review with
`git diff` afterwards.
"""
import os
import re
import sys

EXCLUDED_DIRS = {'.git', '.obsidian', '.trash', '.opencode', '.agents',
                 'node_modules', 'copilot'}
# characters that count as "text" when glued to a backtick (word chars plus a
# few typographic helpers); pure punctuation like .,;:!?)]} is a boundary
GLUE_CHARS = frozenset("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                       "0123456789_*\"'-~")

def is_glue_char(c):
    return c in GLUE_CHARS

def walk_md(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS]
        for fn in sorted(filenames):
            if fn.endswith('.md'):
                yield os.path.join(dirpath, fn)

def fix_heading(line):
    """Return (fixed_line, changed_bool). Sorted-insert positions right-to-left."""
    runs = [(m.start(), len(m.group(0))) for m in re.finditer(r'`+', line)]
    if not runs:
        return line, False
    inserts = []          # (index, 'before'|'after')
    opener_len = None
    for start, ln in runs:
        if opener_len is None:
            if start > 0 and is_glue_char(line[start - 1]):
                inserts.append((start, 'before'))
            opener_len = ln
        elif ln == opener_len:
            end = start + ln
            if end < len(line) and is_glue_char(line[end]):
                inserts.append((end, 'after'))
            opener_len = None
        # runs of different length inside the span: ignore (spec: not a closer)
    if not inserts:
        return line, False
    new = line
    for idx, where in sorted(inserts, reverse=True):
        new = new[:idx] + ' ' + new[idx:]
    return new, True

def main(root):
    changed_files = 0
    changed_lines = 0
    for path in walk_md(root):
        with open(path, encoding='utf-8', errors='replace') as f:
            lines = f.read().split('\n')
        out = []
        file_changed = False
        for line in lines:
            if re.match(r'^#{1,6}\s', line):
                fixed, did = fix_heading(line)
                if did:
                    print(f"{path}:")
                    print(f"  - {line}")
                    print(f"  + {fixed}")
                    file_changed = True
                    changed_lines += 1
                    line = fixed
            out.append(line)
        if file_changed:
            with open(path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(out))
            changed_files += 1
    print(f"\nChanged {changed_lines} heading lines in {changed_files} files.")

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.')