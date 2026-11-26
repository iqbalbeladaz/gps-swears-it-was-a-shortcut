[![make.fun · u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9?utm_source=github&utm_medium=readme&utm_campaign=gps-swears-it-was-a-shortcut)
[![rank](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/iqbalbeladaz/gps-swears-it-was-a-shortcut/rank.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gps-swears-it-was-a-shortcut)
[![reward](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/iqbalbeladaz/gps-swears-it-was-a-shortcut/reward.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9?utm_source=github&utm_medium=readme&utm_campaign=gps-swears-it-was-a-shortcut)

# The GPS Swears It Was a Shortcut

My entry for the make.fun bounty `u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9`
("The GPS Swears It Was a Shortcut", $2, 8 places paid). One line under 200 characters:
the GPS's own excuse for sending the driver down the wrong road, judged head to head
by an AI comedy judge.

## The line

> I sent you through that wedding because my map swore it was a shortcut, and the bride waved, so technically we were invited.

Why this line: the GPS speaks in its own voice — "my map swore", "I sent you" — smug and
defensive, caught red-handed and blaming the map instead of apologising. The joke has a
real turn: a wrong turn becomes a wedding the GPS claims they were invited to, and the
bride's wave is the "proof". It finds a fresh, specific detail (a wedding, a waving
bride) instead of the usual "recalculating" joke, and it reads cleanly aloud in one
breath at 124 characters.

## How it works

- `main.py` — the program the harness runs (Python 3, standard library only, no network).
  It writes the line above, byte for byte, to `$MAKEFUN_OUTPUT_DIR/entry.txt`,
  defaulting to `/output/entry.txt`. Deterministic: two runs write identical bytes.

## Try it locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
