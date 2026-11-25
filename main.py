#!/usr/bin/env python3
"""The Best Meal You Ever Had — make.fun entry."""

import os

ENTRY = "The best meal I ever had was the hospital canteen's plain chicken porridge after three days of nothing, and I cried into it because salt had never tasted like mercy before."

MIN_LENGTH = 1
MAX_LENGTH = 200
OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Check the entry is a non-empty sentence within the length limit."""
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            "entry is %d chars, must be %d-%d" % (len(text), MIN_LENGTH, MAX_LENGTH)
        )
    return text


def run():
    """Validate the entry and write it deterministically to the output file."""
    text = validate_entry(ENTRY)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


def main():
    run()


if __name__ == "__main__":
    main()
