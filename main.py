"""Write the midnight fridge roast to the configured output directory."""

import os
import tempfile

LINE = "It's not a fridge, it's a bouncer with a curfew."
CHAR_LIMIT = 200


def validate(text):
    if not text.strip():
        raise ValueError("text must not be empty after stripping whitespace")
    if len(text) > CHAR_LIMIT:
        raise ValueError(f"text must be no more than {CHAR_LIMIT} characters")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = tempfile.mkdtemp()
    validate(LINE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as output:
        output.write(LINE)


if __name__ == "__main__":
    main()
