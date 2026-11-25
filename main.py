"""One-Line Slogan for a Solana Wallet Agent.

Writes exactly one slogan (one line, UTF-8, 1-140 chars, at most 20 words)
to /output/entry.txt.
"""

import os

SLOGAN = (
    "Solana at the speed of thought: your wallet agent swaps, sends, "
    "and signs before you've finished the sentence."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SLOGAN + "\n")


if __name__ == "__main__":
    main()
