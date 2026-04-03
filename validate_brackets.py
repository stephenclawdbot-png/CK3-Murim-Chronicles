#!/usr/bin/env python3
"""Validate bracket matching in CK3 PDX script .txt files."""

import os
import sys

def strip_comments(line):
    """Remove everything after # (comment), respecting that # inside quotes is not a comment.
    CK3 PDX script doesn't really use quoted # much, but we handle simple cases."""
    result = []
    in_quote = False
    for ch in line:
        if ch == '"':
            in_quote = not in_quote
            result.append(ch)
        elif ch == '#' and not in_quote:
            break
        else:
            result.append(ch)
    return ''.join(result)

def validate_file(filepath):
    """Check bracket balance in a single file.
    Returns (is_balanced, open_count, close_count, error_line, error_detail)."""
    try:
        with open(filepath, 'r', encoding='utf-8-sig', errors='replace') as f:
            lines = f.readlines()
    except Exception as e:
        return (False, 0, 0, 0, f"Could not read file: {e}")

    depth = 0
    total_open = 0
    total_close = 0
    first_error_line = None
    first_error_detail = None

    for lineno, raw_line in enumerate(lines, start=1):
        line = strip_comments(raw_line)
        for ch in line:
            if ch == '{':
                depth += 1
                total_open += 1
            elif ch == '}':
                depth -= 1
                total_close += 1
                if depth < 0 and first_error_line is None:
                    first_error_line = lineno
                    first_error_detail = f"Extra closing '}}' (depth went to {depth})"

    if depth > 0 and first_error_line is None:
        # Find the last unmatched opening brace
        # Walk backwards to find where depth last increased beyond final balance
        d = 0
        target = total_open - total_close  # how many unmatched opens
        unmatched_opens = []
        for lineno, raw_line in enumerate(lines, start=1):
            line = strip_comments(raw_line)
            for ch in line:
                if ch == '{':
                    d += 1
                    unmatched_opens.append(lineno)
                elif ch == '}':
                    d -= 1
                    if unmatched_opens:
                        unmatched_opens.pop()
        if unmatched_opens:
            first_error_line = unmatched_opens[0]
            first_error_detail = f"Unclosed '{{' (file ends with depth {depth}, {depth} unclosed)"
        else:
            first_error_line = len(lines)
            first_error_detail = f"Unclosed braces (depth {depth} at EOF)"

    balanced = (total_open == total_close)
    if not balanced and first_error_line is None:
        first_error_line = 1
        first_error_detail = f"open={total_open} close={total_close}"

    return (balanced, total_open, total_close, first_error_line, first_error_detail)


def main():
    base = "/home/user/CK3-Murim-Chronicles"
    dirs = [os.path.join(base, "common"), os.path.join(base, "events")]

    txt_files = []
    for d in dirs:
        if not os.path.isdir(d):
            print(f"WARNING: directory {d} not found, skipping.")
            continue
        for root, _, files in os.walk(d):
            for fname in sorted(files):
                if fname.endswith('.txt'):
                    txt_files.append(os.path.join(root, fname))

    txt_files.sort()
    total = len(txt_files)
    problems = []
    ok_count = 0

    for fpath in txt_files:
        balanced, opens, closes, err_line, err_detail = validate_file(fpath)
        rel = os.path.relpath(fpath, base)
        if not balanced:
            problems.append((rel, opens, closes, err_line, err_detail))
        else:
            ok_count += 1

    print(f"=== CK3 Bracket Validation Report ===")
    print(f"Files scanned: {total}")
    print(f"Files OK:      {ok_count}")
    print(f"Files ERROR:   {len(problems)}")
    print()

    if problems:
        print("UNBALANCED FILES:")
        print("-" * 90)
        for rel, opens, closes, err_line, err_detail in problems:
            diff = opens - closes
            direction = f"{abs(diff)} more '{{'" if diff > 0 else f"{abs(diff)} more '}}'"
            print(f"  {rel}")
            print(f"    Opens: {opens}  Closes: {closes}  ({direction})")
            print(f"    Likely issue at line {err_line}: {err_detail}")
            print()
    else:
        print("All files have balanced brackets!")

    return len(problems)


if __name__ == "__main__":
    sys.exit(main())
