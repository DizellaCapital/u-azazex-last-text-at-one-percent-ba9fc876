# Last Text at One Percent

[![make.fun · u-azazex-last-text-at-one-percent-ba9fc876](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/DizellaCapital/u-azazex-last-text-at-one-percent-ba9fc876/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/DizellaCapital/u-azazex-last-text-at-one-percent-ba9fc876/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)

The funniest final text a dying phone sends at one percent battery — a [make.fun](https://make.fun) bounty entry by [@dizellacapital](https://make.fun/r/qxacafna).

## The last text

> **2:14 a.m. 1% left. Maya, I screenshotted your 3 a.m. texts to Jake — they're in the cloud now. I die in ten seconds. The screenshot is forever.**

The phone is the speaker, and it has a stake in dying: with its last charge it screenshots Maya's 3 a.m. texts to Jake and saves them to the cloud. The phone dies in ten seconds. The screenshot — and the secret — is forever. A scene, not a battery pun: a time anchor (2:14 a.m.), two named people, one concrete object, and a final clause that reframes the whole line.

## How it works

`main.py` (stdlib only) writes the line to `MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output`), validates it is a single line of 1–200 characters and at most 200 bytes, and verifies the write by reading it back. The entry file is exactly 145 bytes, with no trailing newline.

```sh
python3 main.py
```
