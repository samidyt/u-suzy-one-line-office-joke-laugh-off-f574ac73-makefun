# One-Line Office Joke Laugh-Off

[![One-Line Office Joke Laugh-Off](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![Rank](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/samidyt/u-suzy-one-line-office-joke-laugh-off-f574ac73-makefun/rank.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![Reward](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/samidyt/u-suzy-one-line-office-joke-laugh-off-f574ac73-makefun/reward.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)

Entry for the [One-Line Office Joke Laugh-Off](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73) on make.fun.

## The entry

> My boss asked for my five-year plan; I said 'surviving this meeting' — he wrote it down as a stretch goal.

## How it works

`main.py` writes that one line — 106 characters, a single line about office life, inside the gate's 1–200 character limit — to `entry.txt` in the output directory (`/output` by default, or `$MAKEFUN_OUTPUT_DIR` when set), and prints the same line to stdout. Nothing else is written, read, or fetched: the entry is fully self-contained in this repository, with no network access and no secrets.

## Run it

```sh
python3 main.py
```

With a custom output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
