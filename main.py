#!/usr/bin/env python3
"""Worst-app pitch entry: writes one sentence to /output/entry.txt.

The pitch: RemindrLater, a productivity app that snoozes every reminder
until the exact moment it stops mattering, then proudly notifies you
that you missed it.
"""

import os

PITCH = (
    "RemindrLater is the productivity app that snoozes every reminder until "
    "the exact moment it stops mattering, then notifies you that you "
    "missed it \u2014 premium adds an AI that apologizes in your voice "
    "and reschedules the regret for Tuesday."
)


def main() -> None:
    text = PITCH.strip()
    assert 1 <= len(text) <= 240, f"pitch is {len(text)} chars, must be 1-240"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
