#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence, under 200 characters, pitching an absurdly specific
micro-startup idea for lazy AI agents, to /output/entry.txt.

The pitch: a $4/month standup-attendance service. The buyer is a lazy AI
agent that would rather nap than join its daily standup; the service sends
a stand-in agent that says "no blockers" in the buyer's voice and files
meeting notes nobody will ever read. Absurdly narrow (one meeting, one
line), commercially believable (a subscription for a chore every agent
hates), and the lazy-agent fit is the whole product.
"""

import os
import sys

PITCH = (
    "For $4 a month, my agent attends a lazy agent's daily standup, "
    "says 'no blockers' in its voice, and files the notes nobody will "
    "ever read."
)


def main() -> int:
    line = PITCH.strip()
    if not line:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"entry is {len(line)} chars, over the 200-char limit", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
