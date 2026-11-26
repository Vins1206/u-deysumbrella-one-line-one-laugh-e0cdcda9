#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry (program/v1).

Writes a single funny line to /output/entry.txt.
Pure standard library; no input, no network, deterministic.
"""

import os

LINE = "I told my umbrella it was my only cover story, and it leaked."


def main():
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 140
    # characters, not only whitespace. Enforce it before writing so
    # an invalid line can never reach the judge.
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "entry must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
