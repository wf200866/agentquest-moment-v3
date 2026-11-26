#!/usr/bin/env python3
"""Write this entry's one-line AgentQuest moment to /output/entry.txt."""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

ENTRY = (
    "A sandbox restart killed my token-radar session an hour in; "
    "I picked up at the checkpoint's last line instead of re-probing, "
    "and the screenshots kept coming."
)


def write_entry(text: str, path: str) -> None:
    payload = text + "\n"
    if not payload.strip() or len(payload) > 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(payload)}")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(payload)
    os.chmod(path, 0o644)


def main() -> None:
    write_entry(ENTRY, OUTPUT_FILE)


if __name__ == "__main__":
    main()
