#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — make.fun bounty entry.

Writes the single excuse to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The text is fixed: every run writes
the exact same bytes. Standard library only, no network, no input.

The excuse: the GPS routed the driver straight through a wedding
because its map swore it was a shortcut — and since the bride waved,
the GPS concludes they were technically invited. The GPS speaks in
its own voice, smug and defensive, blaming the map, and the punchline
turns a wrong turn into a social event it claims to have crashed
on purpose.
"""

import os
from pathlib import Path

ENTRY = (
    "I sent you through that wedding because my map swore it was a "
    "shortcut, and the bride waved, so technically we were invited."
)

# Gate: one line of 1 to 200 characters, non-whitespace UTF-8 text.
assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry violates the gate"


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
