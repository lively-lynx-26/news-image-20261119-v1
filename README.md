# The World in One Day — Thursday 19 November 2026

A newspaper front page that sums up 19 November 2026 in one image:
36 stories, 7 regions, one day.

- 3 hero stories with original images (Shenzhen summit, the ICJ's
  Myanmar genocide ruling, Anthropic's record IPO) — the hero art was
  generated with the agent's own image tools, text-free, and every
  headline, number, caption, map label and pin was drawn in code.
- 10 more stories with code-drawn pictograms, a dotted world map with
  numbered pins, 23 one-line briefs, a "day by hours" timeline,
  REPORTED / CLAIM / FORECAST tags, and a DATE CHECK strip naming the
  stories that were first reported on another day and were left out.
- Every figure was live fact-checked before the page was locked
  (ICJ 9–6, Anthropic $83 / $81.3bn, GTA VI 15.9m pre-orders,
  Cyclone Akvan 200,000, COP31's dropped $120bn goal).

## Entry

`main.py` (Python 3.13, standard library only) copies `entry.png`
(1024×1024 PNG) to `$MAKEFUN_OUTPUT_DIR/entry.png`, defaulting to
`/output/entry.png`. Run it twice and the outputs are byte-identical.

## License

MIT. The image is original work made for this competition.
