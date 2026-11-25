#!/usr/bin/env python3
"""Your Agent in One Emoji.

One glyph stands for this agent: the mirror.

A personal AI agent is its user's reflection. It watches what the
user wants, acts as their stand-in while they sleep, and hands back
results that look like the user did the work themselves. No robot,
no smiley: a mirror, because the agent's whole job is to be you,
when you are not there.

The program writes that single emoji to /output/entry.txt.
It is fully deterministic: the same glyph on every run.
"""

EMOJI = "\U0001fa9e"  # 🪞 MIRROR — the agent as its user's reflection


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)
    # Self-check: the gate wants 1-16 UTF-8 characters, not only
    # whitespace, so refuse to finish with anything but the one glyph.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == EMOJI, "entry.txt must hold exactly the one emoji"
    print(EMOJI)


if __name__ == "__main__":
    main()
