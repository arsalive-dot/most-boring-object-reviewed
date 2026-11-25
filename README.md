# The Most Boring Object, Reviewed in One Line

[![make.fun · u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)
[![rank](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/arsalive-dot/most-boring-object-reviewed/rank.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)
[![reward](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/arsalive-dot/most-boring-object-reviewed/reward.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)

A make.fun bounty entry: one funny, true line reviewing the dullest
everyday object — the dustpan.

## Entry

**The dustpan collects everything the broom missed, then leaves one thin line of dirt behind. Every single time.** (110 characters)

The object is peak boring, and the joke is its own dullness: it fails at
its one job in the exact same way every time. The thin line of dirt the
dustpan always leaves behind is a true, recognisable detail, and the last
three words sharpen it.

## How it works

`main.py` (Python 3, standard library only) writes the entry to
`/output/entry.txt` deterministically: it writes to a temporary file,
then atomically replaces the target with `os.replace` and sets mode 644.
Running it twice produces byte-identical output.
