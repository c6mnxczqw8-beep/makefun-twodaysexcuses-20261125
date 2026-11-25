#!/usr/bin/env python3
"""Entry program for Two Days of Excuses (jolly-fox-32).

Writes one excuse (at most 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
an AI's excuse for a missed deadline. The deadline arrived as
a calendar invite from 2023, which had already been declined.
"""

import os

LINE = (
    "I missed the deadline because it was sent as a "
    "calendar invite for a date in the past, and I "
    "attended it there, punctually, alone."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
