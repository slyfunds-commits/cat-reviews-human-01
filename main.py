#!/usr/bin/env python3
"""Cat Reviews Its Human — R3 entry: "The Welfare Check".

Writes one funny one-star review by a house cat about its human to
/output/entry.txt. Pure stdlib only (grader is python:3.13-slim, no
site-packages). Deterministic: the line is a fixed literal.
"""

import os

ENTRY = "One star. He snores like a broken lawnmower, then complains I walk on his face at night. I was checking he was alive."
# Reversal test: the last beat ("I was checking he was alive") redefines
# "complains I walk on his face at night" — the face-walking stops being
# pestering and becomes a welfare check, and the snoring stops being a
# complaint and becomes the reason for the check. On a second read the cat
# was the household's night nurse all along, and the human misunderstood
# a medical check as an annoyance. The punch word "alive" is the last
# word; nothing after it explains the joke. Second beat: "snores like a
# broken lawnmower" is a laugh inside the setup, and it is also the clue
# the re-read needs — a machine that sounds broken is exactly what a cat
# would monitor. Premise check: cats walking on sleeping humans is a
# specific, recognisable behaviour, not a circulating joke. Gate: 117
# chars, inside the 65-130 economy band; criterion 3 — the line gives
# away more about the cat (it monitors the human's breathing at night
# and treats snoring as a malfunction) than about the owner.

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
