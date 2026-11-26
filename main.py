#!/usr/bin/env python3
"""Entry for make.fun:
Make the Judge Laugh in One Line.

Writes one funny line, deterministically, to /output/entry.txt.
No network, no randomness, no time dependence.
"""

import os

ENTRY = "I bought a self-help book and it filed a restraining order.\n"


def main() -> None:
    line = ENTRY.rstrip("\n")
    assert 1 <= len(line) <= 200, f"entry line must be 1-200 chars, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
