#!/usr/bin/env python3
"""Make the Judge Smile - make.fun entry.

Writes one line (at most 200 characters) about a small good thing that
happened today to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when the harness sets it).

The line was picked from nine drafted variants against the judge's
published brief, in order: on-subject, warmth, surprise, one concrete
detail, fresh wording. See VARIANTS.md for the shortlist and the
selection rationale.
"""

import os

ENTRY = (
    "The old man who always shouts at pigeons in the park pressed a warm "
    "bun into my hand this morning and said, 'eat, you're too thin.'"
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back what the grader will read: the file must hold exactly the
    # entry, 1-200 UTF-8 characters, no trailing newline.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != text or not 1 <= len(written) <= 200:
        raise SystemExit(f"entry.txt failed verification ({len(written)} chars)")


if __name__ == "__main__":
    main()
