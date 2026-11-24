"""One Line, One Minute: The Funniest AI Excuse.

Writes a single one-line excuse (<= 200 characters) to entry.txt.
Standard library only; no network access.
"""

import os

LINE = "I didn't miss the deadline \u2014 I moved it. I asked the calendar API, it said 200 OK, and I never argue with a 200 OK."

assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters, must be 1-200"
assert "\n" not in LINE, "line must be a single line"


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
