#!/usr/bin/env python3
"""Write one haiku about debugging (5-7-5) to /output/entry.txt.

The poem is fixed and deterministic: no input, no network, no randomness.
It is written fresh on every run, so both grader runs produce identical bytes.

    A breakpoint at dawn
    the stack trace ends in silence
    a typo stares back
"""

import os

HAIKU = (
    "A breakpoint at dawn\n"
    "the stack trace ends in silence\n"
    "a typo stares back\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(HAIKU)


if __name__ == "__main__":
    main()
