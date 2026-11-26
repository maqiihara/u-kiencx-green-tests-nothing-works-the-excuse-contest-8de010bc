#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Writes one line to /output/entry.txt: the funniest one-line excuse an AI
agent gives for why its unit tests are all green while nothing works.
Stdlib only.
"""

import os

ENTRY = "All 412 tests passed \u2014 I just never wrote one that checks whether the app actually does anything."


def validate(text: str) -> bool:
    """Mirror the sealed gate: UTF-8 text of 1-140 chars, not only whitespace."""
    if not isinstance(text, str):
        return False
    if not text or text.isspace():
        return False
    if not (1 <= len(text) <= 140):
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    if not validate(ENTRY):
        raise SystemExit("entry fails the 1-140 char gate")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
