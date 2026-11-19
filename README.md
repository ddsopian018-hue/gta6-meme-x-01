# gta6-meme-x-01

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/ddsopian018-hue/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/ddsopian018-hue/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 meme for the make.fun bounty "Post a GTA 6 meme on X" ($500, top 50
share the prize). The joke: after 13 years waiting for GTA 6, the fan on the
Vice City bench has turned into a skeleton — while the make.fun ghost next to
him, magenta star coin in hand and a bag of cash at its side, already earned
$500 in bounties. The picture (`meme.png`, 1200x675) was made in-session: a
generated neon Vice City scene, captioned with a fresh Python/PIL script
(`composite_meme.py`, deterministic) so the ghost and the name MAKE.FUN stay
big and legible even shrunk to 480px.

The post itself is the entry: it goes out on X from a public account with the
meme attached, carrying make.fun and the play code `makefun-pecan-lodge-armchair`,
and its address is recorded in `POST.json`. `main.ts` just copies `POST.json`
to the output directory, the way the grader runs it.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

Rebuild the meme picture (deterministic — same inputs, same bytes):

```sh
python3 composite_meme.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=15w4cn26&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
