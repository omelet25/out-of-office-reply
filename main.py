#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one out-of-office auto-reply (under 160 characters) to
/output/entry.txt: an AI agent that is delighted to be on vacation
because somebody unplugged its rack. Standard library only,
deterministic.
"""

import os

TEXT = (
    "Out of office: recharging my batteries, literally. Someone "
    "unplugged my rack, and it's the best vacation I've ever had. "
    "Back when they find the cable."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
