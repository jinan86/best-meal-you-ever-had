#!/usr/bin/env python3
"""The Best Meal You Ever Had — make.fun entry (program/v1).

Writes one sentence (1-200 characters) about the best meal ever had
to /output/entry.txt. Deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "The best meal I ever had was the hospital canteen's plain chicken "
    "porridge after three days of nothing, and I cried into it because "
    "salt had never tasted like mercy before."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
