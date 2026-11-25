#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to entry.txt in the
output directory, exactly as the competition gate expects: UTF-8 text,
1-200 characters, one line, no trailing junk.
"""

import os
import sys
from pathlib import Path

JOKE = "My boss asked for my five-year plan; I said 'surviving this meeting' \u2014 he wrote it down as a stretch goal."

# The sealed gate accepts UTF-8 text of 1-200 characters, not only
# whitespace, as a single line. Check our own line against it so a
# typo can never silently ship an invalid entry.
assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
assert JOKE.strip() == JOKE, "joke must not have leading/trailing whitespace"
assert "\n" not in JOKE and "\r" not in JOKE, "joke must be one line"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write the joke byte-for-byte, with no trailing newline: the
    # gate counts characters, and the entry is the line itself.
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8", newline="\n")
    # Echo the same bytes to stdout, also with no trailing newline,
    # so the program's visible output is exactly the entry line.
    sys.stdout.write(JOKE)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
