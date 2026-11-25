#!/usr/bin/env python3
"""Write the competition entry: a one-line review (<=200 chars).

Entry: "The dustpan collects everything the broom missed, then leaves
one thin line of dirt behind. Every single time." (110 chars).
The object is peak boring - a dustpan - and the joke is its own
dullness: it fails at its one job in the exact same way every time.
The thin line of dirt the dustpan always leaves behind is a true,
recognisable detail, and the last three words sharpen it.
Gate: 1-200 UTF-8 characters; this entry is 110, so it passes with
room to spare and no padding words.
"""

import os

ENTRY = ("The dustpan collects everything the broom missed, then leaves "
         "one thin line of dirt behind. Every single time.")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    os.replace(tmp, target)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
