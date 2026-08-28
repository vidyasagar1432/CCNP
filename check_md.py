#!/usr/bin/env python3
"""Markdown lint for the CCNP vault.

Detects broken backtick formatting in .md notes:
  A. Fence open/close mismatch  -> opening fence of N backticks "closed" with < N backticks
  B. Unclosed fence             -> fence opened but never closed by EOF
  C. Unclosed inline code span  -> ` span opened with N backticks, never closed by EOF
  D. Crammed heading            -> heading with inline code glued to text (`foo`Bar)

Usage:
    python3 check_md.py [root]
    (root defaults to "." -- run from the vault root)

Scan skips: .git, .obsidian, .trash, .opencode, .agents, node_modules,
and copilot/ (auto-generated conversation exports, not hand-written notes).
"""
import os
import re
import sys

EXCLUDED_DIRS = {'.git', '.obsidian', '.trash', '.opencode', '.agents',
                 'node_modules', 'copilot'}
MAX_FENCE_INDENT = 8  # tolerate list-nested fences (Obsidian is lenient)

def walk_md(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS]
        for fn in sorted(filenames):
            if fn.endswith('.md'):
                yield os.path.join(dirpath, fn)

def backtick_runs(s):
    """Yield (start_index, run_length) for every backtick run in s."""
    i = 0
    while i < len(s):
        if s[i] == '`':
            j = i
            while j < len(s) and s[j] == '`':
                j += 1
            yield (i, j - i)
            i = j
        else:
            i += 1

def check_file(path):
    issues = []  # (kind, line_no, message)
    with open(path, encoding='utf-8', errors='replace') as f:
        lines = f.read().split('\n')

    fence = None   # {count, line} of open fence
    span = None    # {count, line} of open inline code span

    for i, raw in enumerate(lines, 1):
        line = raw.rstrip()
        lstrip = line.lstrip()
        indent = len(line) - len(lstrip)
        is_fenced_line = indent <= MAX_FENCE_INDENT and lstrip.startswith('`')

        if fence is None:
            # --- not inside a code fence ---
            if is_fenced_line and re.match(r'^`{3,}', lstrip):
                # line starting with 3+ backticks -> candidate fence line
                m = re.match(r'^(`{3,})\s*(.*)$', lstrip)
                if '`' not in m.group(2):  # CommonMark: info string has no backticks
                    fence = {'count': len(m.group(1)), 'line': i}
                    continue
            # inline code span tracking
            for _, run in backtick_runs(line):
                if span is None:
                    span = {'count': run, 'line': i}
                elif run == span['count']:
                    span = None
                # run > or < count stays open (spec: only exact-length run closes)
        else:
            # --- inside a code fence ---
            if is_fenced_line:
                m = re.match(r'^(`+)\s*$', lstrip)
                if m:
                    run = len(m.group(1))
                    if run >= fence['count']:
                        fence = None
                    else:
                        issues.append(('A-fence-mismatch', i,
                            f"fence closes with {run} backtick(s); opener at line {fence['line']} "
                            f"has {fence['count']} (CommonMark: block keeps running -> "
                            f"rest of file renders as code)"))
                        fence = None  # treat intended close as close (author intent)
        # crammed heading check (outside fences only) -- backtick glued on BOTH sides
        if fence is None and re.match(r'^#{1,6}\s', line) and '`' in line:
            if re.search(r'(?<=[^\s`])`(?=[\w*"\'\-~])', line):
                issues.append(('D-heading-glued', i,
                               "heading text glued to inline code (add a space)"))

    if fence is not None:
        issues.append(('B-unclosed-fence', fence['line'],
                       f"fence opened with {fence['count']} backticks never closed (EOF)"))
    if span is not None:
        issues.append(('C-unclosed-span', span['line'],
                       f"inline code span opened with {span['count']} backtick(s) never closed (EOF)"))
    return issues

KIND_LABEL = {
    'A-fence-mismatch': 'FENCE MISMATCH',
    'B-unclosed-fence': 'UNCLOSED FENCE',
    'C-unclosed-span':  'UNCLOSED INLINE CODE',
    'D-heading-glued':  'HEADING GLUED TEXT (minor)',
}

def main(root):
    total_files = 0
    flagged = []
    for path in walk_md(root):
        total_files += 1
        issues = check_file(path)
        if issues:
            flagged.append((path, issues))
    print(f"Scanned {total_files} .md files; {len(flagged)} with issues.\n")
    for path, issues in flagged:
        print(f"### {path}")
        for kind, ln, msg in issues:
            print(f"  L{ln:5d}  [{KIND_LABEL[kind]}] {msg}")
        print()
    kinds = {}
    for _, issues in flagged:
        for kind, _, _ in issues:
            kinds[kind] = kinds.get(kind, 0) + 1
    if kinds:
        print("Summary by issue type:",
              ', '.join(f"{KIND_LABEL[k].split(' (')[0]}: {v}" for k, v in kinds.items()))

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.')