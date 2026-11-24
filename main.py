#!/usr/bin/env python3
"""Cat Reviews Its Human — R2 entry: "The Two-Inch Move".

Writes one funny one-star review by a house cat about its human to
/output/entry.txt. Pure stdlib only (grader is python:3.13-slim, no
site-packages). Deterministic: the line is a fixed literal.
"""

import os

ENTRY = "One star. He moved my bowl two inches to the left. I have eaten beside it for three days. I do not negotiate with movers."
# Reversal test: the last beat ("I do not negotiate with movers") redefines
# "He moved my bowl" — the human is no longer the owner but a moving crew,
# and "I have eaten beside it for three days" stops being stubbornness and
# becomes a negotiating position. The punch word "movers" is the last word;
# nothing after it explains the joke. Second beat: three days eating BESIDE
# the bowl is a laugh inside the setup (cat standards: bowl placement is
# law). Premise check: a moved food bowl is specific and recognisable
# (criterion 2 names the food bowl first) and is not a circulating joke.
# Beats R1 ("The Hairball Greeting", 52.695%) on premise freshness and on
# recontextualisation: the hairball redefines a greeting; "movers"
# redefines the human's whole role in the household.

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
