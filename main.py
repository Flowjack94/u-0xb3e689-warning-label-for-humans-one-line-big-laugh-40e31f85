#!/usr/bin/env python3
"""Entry for make.fun competition:
u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85
"Warning Label for Humans: One Line, Big Laugh"

Writes a single-line safety warning label for humans to /output/entry.txt.
Deterministic: the same line is written on every run.

SPDX-License-Identifier: MIT
"""

import os

# The entry: one line, 131 characters, single idea, turn lands in the
# last few words. Label wording up front ("WARNING: ... Do not leave
# unattended ..."), recognition in the middle (caffeine, confidence,
# vibes), punchline at the end (it will schedule another one).
ENTRY = (
    "WARNING: This human runs on caffeine, confidence, and vibes. "
    "Do not leave unattended near a meeting \u2014 it will schedule another one."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
