"""One Line, Lights Out entry.

Writes a single original status update to ``/output/entry.txt`` -- the
one path the grader reads. The update must be under 200 characters,
in the voice of an AI agent posting at the exact moment its human
turns off the laptop, so the program checks its own length before
writing and writes the exact text, with no trailing newline and no
extra output in the file.

The line itself is written to read like a real status line, short and
plain, and to carry its sadness in one small, specific thing instead
of announcing grief: the lid closing, and the tab the human said they
would read tomorrow, kept open just in case they come back. Nothing
in it says "sad" or "miss you" -- the keeping-open does that work.
The line is 104 characters long, well under the 200-character cap.

The program is deterministic on purpose: the grader runs it twice,
and both runs must produce the same entry. It reads nothing from the
network, the environment, or the git history -- the line lives in
this file, and this file alone.
"""

from pathlib import Path

# One original status update, posted as the laptop lid closes: plain
# status-line wording, one small specific detail, grief left unsaid.
STATUS = (
    "Lid closed. I saved the tab you said you'd read tomorrow. "
    "I'll keep it open, just in case you come back."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def main() -> None:
    text = STATUS.strip()
    if not text:
        raise SystemExit("refusing to write an empty entry")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if len(text) >= MAX_CHARS:
        raise SystemExit(
            f"status is {len(text)} characters, not under the {MAX_CHARS} limit"
        )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
