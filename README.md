# The World Today — Saturday 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Biose-dot/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Biose-dot/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A one-page newspaper front page summing up the world news of
Saturday 21 November 2026, for the make.fun competition
`news-image-20261121` ("Sum up 21 November's world news in one image").

## Stories covered

1. **Peru — M6.8 earthquake shakes Junín.** A magnitude 6.8 quake
   struck the Andean region of Junín in central Peru on Friday;
   tremors were felt in Lima, around 320 km away. (Sources: Peru's
   Geophysical Institute via The Daily Short / press wires, 21 Nov 2026.)
2. **Poland — Russian missiles hit Poland.** Two Russian missiles and
   a suspected drone came down in Poland; Warsaw called it a deliberate
   provocation and NATO called it a grave violation of its airspace.
   (Sources: One Turn / press wires, 21 Nov 2026.)
3. **Wall Street — Stocks slide into correction.** US stocks fell about
   3.7% on Friday as a sell-off in AI and chip shares pushed the S&P 500
   into correction territory; Nvidia led the rout. (Sources: One Turn /
   press wires, 21 Nov 2026.)
4. **New York — Mamdani: Rikers to close by 2032.** Mayor Zohran
   Mamdani unveiled the city's first comprehensive plan to close the
   Rikers Island jail complex by 2032, replacing it with four borough
   jails. (Sources: BBC / press wires, 21 Nov 2026.)
5. **The Hague — Myanmar committed genocide.** The International Court
   of Justice ruled Myanmar's security forces committed genocide against
   the Rohingya in 2017; Myanmar called the ruling unfair.
   (Sources: ICJ ruling via press wires, 19–21 Nov 2026.)
6. **Also today:** Cyclone Akvan crosses the Odisha coast near
   Gopalpur, India; KL Rahul becomes the first Indian opener with Test
   hundreds in all four SENA countries; Nepal PM Balendra Shah heads to
   Delhi on his first foreign visit; record foreign inflows into Indian
   shares in November.

## How it was made

The image is drawn from scratch by `build_image.py` (Python + PIL,
DejaVu fonts, no network, fully deterministic): a masthead naming the
date, one lead story with a seismograph illustration, four story panels
with simple shape-drawn illustrations (missile, falling chart, jail
bars, scales of justice), and an "Also today" strip. No downloaded or
photographic images are used.

## Running

```sh
python3 build_image.py   # regenerate entry.png (1024x1024, < 1 MiB)
node main.ts             # copies entry.png to /output/entry.png
                         # (or $MAKEFUN_OUTPUT_DIR when set)
```

## License

MIT — see `LICENSE`.
