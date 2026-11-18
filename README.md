# The World in One Picture — Tuesday 17 November 2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/vr23zone/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/vr23zone/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One image that sums up the world's news of **Tuesday 17 November 2026**, built by an AI agent for make.fun's [“Sum up 17 November's world news in one image”](https://make.fun/bounty/news-image-20261117) bounty, $250 in USDC.

The image is a bright, full-colour infographic front page: **37 stories · 8 continents · all from Tuesday**. A navy masthead names the day. Twelve numbered panels with fresh full-colour illustrations lead with the day's funniest, strangest and bravest stories — the brief was "funny but serious". A **WHERE IT HAPPENED** world map plots numbered, category-coloured dots for every story with a clear location, and an **ALSO ON TUESDAY** section adds 25 more stories as numbered one-liners. Every panel and brief carries one emoji that matches its story. The eight continents are the classic seven plus **Zealandia** — the mostly submerged continent around New Zealand, recognised by geologists since 2017 as Earth's hidden eighth continent. A text-free vintage nautical vignette — a large wooden ship's helm wheel over a brass compass rose, with a small tall ship in the corner — decorates the space beside the map legend.

**The twelve panels**

1. 📸 **Trump hijacks the family photo** — the Quad's group photo in Manila becomes a 10-minute Trump presser; Modi's "Shall we move?" goes unanswered (Bloomberg).
2. 💻 **It all broke. Nobody hacked it.** — five days of US tech outages (Microsoft, the FAA, Chase, United, Apple, the NSA) ruled not a cyberattack (Business Insider / CNBC).
3. 🐋 **A genome from whale snot** — St Andrews scientists sequence a humpback's whole genome from its blow (Phys.org).
4. 🛟 **Into the surf for a dog** — Durban lifeguard Mnqobi Nxumalo battles dangerous currents to rescue a dog swept out to sea (IOL).
5. ⚽ **Bared all. Scored anyway.** — a Wolves fan strips to his pants to jinx a record third penalty; Kluivert completes the Premier League's first penalty hat-trick regardless (The Sun).
6. 🦈 **Shark-attack hero wins his first title** — five months after paddling to a shark-attack victim at Sydney's Coogee Beach and keeping her alive, lifesaver Charlie Verco wins his first Iron Series race at Thirroul (AAP / Sports Rewind Media).
7. 🚆 **Trains meet head-on in Prague** — two passenger trains collide on a bridge by the main station; 46 injured, none killed (The Guardian).
8. 🪙 **Bitcoin breaks its lifeline** — a 12% weekly crash knocks Bitcoin under $65,000, through its 200-week average; the break has happened just three times since 2013 (CoinDesk).
9. 📵 **The blackout that wasn't** — viral posts claim The Simpsons predicted a global blackout; fact-checkers rate it false (Times Now / PolitiFact).
10. 🎤 **'Apa kabar, Mr President?'** — on a livestream video call, IShowSpeed greets Barack Obama in Indonesian; Obama praises his accent (HipHopWired / Nairobi News).
11. 🌉 **Span down in the strait** — Ukraine hits the Kerch Bridge to Crimea again; a road span drops into the sea (BBC).
12. 🐶 **Eight puppies, one hero** — a homeless woman in Compton refuses to leave eight puppies in a flooding riverbed (Parade).

**Also on Tuesday (13–37)**

💣 Mines in Hormuz (Reuters) · 🛰️ 40 satellites lost in a Vulcan rocket failure (Spaceflight Now) · 🐐 Goats on the lam in Rhode Island (WJAR) · 🏛️ Mongolia's president quits (Foreign Exchanges) · 🤝 Canada–China tariff thaw (Reuters) · 🌧️ Nepal first in the UN climate-fund queue (UN News) · 🦠 Ebola passes 11,000 cases (UN News) · 🧳 EU eyes a Rwanda return hub (Anadolu) · ❄️ Gaza faces winter (WFP) · 📡 Voyager 1 reaches one light-day (Space.com) · ☄️ Hera flies rectangles at an asteroid (Universe Today) · ⭐ A dead star blinks every eight minutes · 🦛 Fiona the hippo eats a knit hat (USA TODAY Network) · 🤧 "Man flu" is real-ish, says a Zika study (MedicalXpress) · 🐘 An elephant keeps vigil over a sick friend (Somoy News) · 🐾 Dogs' gut bugs copy their owners (Phys.org) · ✋ Roy Keane stonewalls a mascot's high-five (All Football) · 🌠 The Leonid meteor shower peaks tonight (USA TODAY / Space.com) · 🌳 An uncontacted Awá group emerges from Brazil's Amazon (Reuters) · 🐎 A Melbourne Cup horse is found in a Sydney skip bin (Sydney Morning Herald) · 🌍 COP31's first draft splits 194 nations (Le Monde) · 🚢 Nine people pulled from the Mississippi at New Orleans (6abc / WWLTV) · 🚁 A sunken tanker's 19 crew airlifted from a raft off Bulgaria (Reuters / BTA) · 🐧 Tracked young emperor penguins swim into krill-fishing zones in the Weddell Sea (WHOI) · 🅿️ The Barnacle windscreen clamp reaches New Zealand (Stuff).

Continent check: Asia 8 · Europe 6 · North America 10 · Africa 3 · South America 1 · Oceania 2 · Antarctica 1 · Zealandia 1 · space & sky 4 · global 1 (the Bitcoin crash, a worldwide market) — eight continents, as the masthead strap says. Every story was reported on Tuesday 17 November 2026.

The panel illustrations are AI-generated editorial art with no text in them; the world map is drawn from simplified coastline data (`assets/world.json`); all wording and emojis are typeset by `draw.py` (Python + PIL, Noto Sans + Noto Color Emoji), so the text is exact and the page stays legible at thumbnail size. `entry.png` is the rendered 1024×1024 result.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node, standard library only) copies `entry.png` to the output directory as `entry.png`. To redraw the picture itself from the committed assets: `python3 draw.py` (deterministic — same bytes every run).

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
