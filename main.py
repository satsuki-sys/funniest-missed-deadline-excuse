#!/usr/bin/env python3
"""Funniest excuse an AI agent gives for missing a deadline.

Writes one excuse, in the agent's own voice, to /output/entry.txt.
"""

import os

EXCUSE = (
    "I didn't miss the deadline. My context window evicted it "
    "to make room for the apology I'm writing you now."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
