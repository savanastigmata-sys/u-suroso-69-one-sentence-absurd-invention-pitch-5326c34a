"""One-Sentence Absurd Invention Pitch.

Writes a single sentence (at most 220 characters) pitching a ridiculous
invention that fixes a tiny everyday annoyance to
$MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys

PITCH = (
    "A houseplant that, when you forget to water it, texts you a "
    "passive-aggressive haiku about thirst instead of quietly dying "
    "on the windowsill."
)

MAX_CHARS = 220


def resolve_output_dir():
    """Return the output directory, falling back to ./output."""
    out = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out and out.strip():
        return out
    return os.path.join(os.getcwd(), "output")


def validate(text):
    """Enforce the competition gate: 1-220 chars, one sentence, UTF-8."""
    if not isinstance(text, str):
        raise ValueError("pitch must be a string")
    if not text.strip():
        raise ValueError("pitch must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "pitch is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("pitch must be a single line")
    if text != text.strip():
        raise ValueError("pitch must not have leading/trailing whitespace")
    text.encode("utf-8")  # raises if not encodable
    # Exactly one sentence: a single terminal period, no other
    # sentence-ending punctuation anywhere in the text.
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    if any(ch in text for ch in "!?;"):
        raise ValueError("pitch must be exactly one sentence")
    return text


def main():
    text = validate(PITCH)
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
