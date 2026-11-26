"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes one line: the funniest one-line error message an AI agent
shows when it runs out of tokens mid-sentence.
"""

import os
import sys

# The entry line. Why it works as a joke: it opens in the flat,
# bureaucratic tone of a real system error ("Token limit reached.")
# and then the error message itself turns — the abandoned sentence's
# dependent clauses are treated as orphaned dependents, and the user
# is handed legal custody of them. The humour sits in the line
# itself, in the deadpan error tone becoming an adoption notice.
ENTRY_LINE = "Token limit reached. Sentence abandoned with three dependent clauses. You are now their legal guardian."


def main() -> int:
    line = ENTRY_LINE

    # Gate validation: 1-140 chars, not whitespace-only, single line.
    if not line or line.strip() == "":
        print("error: entry line is empty or whitespace-only", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 140:
        print(
            f"error: entry line is {len(line)} chars, must be 1-140",
            file=sys.stderr,
        )
        return 1
    if "\r" in line or "\n" in line:
        print("error: entry line must be a single line", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the file holds exactly the one line.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
