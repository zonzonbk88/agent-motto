#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one short original motto (1-200 chars, no trailing newline)
to <MAKEFUN_OUTPUT_DIR or /output>/entry.txt.
"""
import os

MOTTO = "I read the entire internet so you don't have to. I regret most of it."

def main():
    assert 1 <= len(MOTTO) <= 200, "motto outside 1-200 char gate"
    assert MOTTO.strip(), "motto is only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(MOTTO)

if __name__ == "__main__":
    main()
