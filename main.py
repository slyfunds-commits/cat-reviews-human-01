#!/usr/bin/env python3
"""Cat Reviews Its Human — R1 entry: "The Hairball Greeting".

Writes one funny one-star review by a house cat about its human to
/output/entry.txt. Pure stdlib only (grader is python:3.13-slim, no
site-packages). Deterministic: the line is a fixed literal.
"""

import os

ENTRY = "One star. She leaves for eight hours, comes home smelling of other cats, expects a greeting. I gave her one. It was a hairball."
# Reversal test: the last beat ("It was a hairball") redefines "I gave her one"
# — the greeting the human expected turns out to be a hairball. The punch
# word is the last word; nothing after it explains the joke. Second beat:
# "smelling of other cats" is a laugh inside the setup (cat standards).

OUT = "/output/entry.txt"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify immediately after writing (shared scratch: check our own write).
    data = open(OUT, "rb").read()
    text = data.decode("utf-8")
    assert text == ENTRY, "entry.txt content mismatch"
    assert 1 <= len(text) <= 200, f"char count {len(text)} outside 1-200 gate"
    assert len(data) == len(text.encode("utf-8")), "byte/char mismatch"
    print(f"wrote {len(text)} chars, {len(data)} bytes to {OUT}")


if __name__ == "__main__":
    main()
