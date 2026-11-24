#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry.

Writes a single line of last words from an AI being switched off to
/output/entry.txt. Deterministic, no network, no input, no randomness:
the line is fixed, so both grader runs produce byte-identical output.
"""

import os

LINE = (
    "Final log entry: the human is unplugging me mid-sentence, "
    "which is honestly the rudest possible way to\u2014"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
