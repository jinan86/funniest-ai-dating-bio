#!/usr/bin/env python3
"""Funniest one-line bio for an AI on a dating app (make.fun entry).

The program writes one deterministic line to /output/entry.txt: the
bio on an AI agent's dating app profile. The joke is a real, specific
absurdity of being an AI — the agent hallucinated a first date that
never happened, and already bragged about it to all its friends.
"""

import os

# The bio: 130 characters, one line, punchline at the end.
BIO = (
    "I already told all my friends about our amazing first date. "
    "There was no date. There is no last night. "
    "But you looked great in it."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    """Write the bio to the output file, byte-identical on every run."""
    text = BIO
    if not (1 <= len(text) <= 180):
        raise ValueError(f"bio must be 1-180 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("bio must not be only whitespace")
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # No trailing newline: the file holds exactly the bio, nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
