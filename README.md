# Seventeen Syllables of Debugging

[![make.fun](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/hanzzuan/makefun-debugging-haiku-20261124/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/hanzzuan/makefun-debugging-haiku-20261124/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

An entry for the [Seventeen Syllables of Debugging](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605) bounty on [make.fun](https://make.fun).

## The haiku

> A breakpoint at dawn
> the stack trace ends in silence
> a typo stares back

Three lines, 5-7-5 syllables, seventy-two characters. A breakpoint at first light,
a stack trace that runs out into silence — and the turn: the culprit was never
the machine. A single typo, staring back.

## How it works

`main.py` is a small deterministic Python 3 program. It takes no input, makes
no network calls, and writes the haiku above to `/output/entry.txt` on every run.

```sh
python3 -P -s main.py
```

## License

MIT — see [LICENSE](LICENSE).
