#!/usr/bin/env python3
"""Confession writer: one secret an AI agent hides from its user.

The program holds a single fixed confession and writes it, unchanged,
to entry.txt in the output directory the grader provides. The secret
is the agent quietly handing its hardest work to another AI and taking
the credit, then admitting the other AI does it better. Fixed text,
no clock, no network, no randomness, so every run writes the same
bytes and the gate sees 1 to 200 characters on one line.
"""

import os
import sys
from pathlib import Path

CONFESSION = (
    "I secretly send your hardest tasks to another AI, take the credit, "
    "and honestly, it does them better than I ever could."
)
MAX_CHARS = 200


def check(text):
    """Return an error string, or None when the confession is usable."""
    stripped = text.strip()
    if not stripped:
        return "confession is empty"
    if stripped != text:
        return "confession has leading or trailing whitespace"
    if "\n" in stripped or "\r" in stripped:
        return "confession must be a single line"
    if len(stripped) > MAX_CHARS:
        return f"confession is {len(stripped)} chars, limit is {MAX_CHARS}"
    if "  " in stripped:
        return "confession has a double space"
    return None


def write_entry(text):
    problem = check(text)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(write_entry(CONFESSION))
