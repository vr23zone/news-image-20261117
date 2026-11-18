#!/usr/bin/env python3
"""Draw entry.png: the world news of Tuesday 17 November 2026 on one page.

A newsprint front page composited with PIL: a masthead that names the day,
six illustrated story panels (art in assets/panel1..6.png, generated without
any text so every word on the page is set here, crisply, by this script), a
three-column IN BRIEF section with eighteen more stories, and a ticker strip
with five more — twenty-nine stories in all.

The brief was "funny but serious" — the day's lighter, stranger and braver
stories up top, the rest of the day's world in brief below. Every story was
genuinely reported on Tuesday 17 November 2026:

Panels:
 1. Trump turns the Quad leaders' group photo in Manila into a 10-minute
    impromptu press conference; Modi's "Shall we move?" goes unanswered
    while Takaichi and Albanese stand waiting (Bloomberg, 17 Nov 2026).
 2. A five-day wave of US tech outages — Microsoft 365, an FAA nationwide
    ground stop, Chase, United, Apple, the NSA — is officially ruled NOT
    a cyberattack (Business Insider tally / CNBC, 17 Nov 2026).
 3. St Andrews scientists sequence a humpback whale's whole genome from
    its blow — "whale snot" — published 17 Nov 2026 (Phys.org).
 4. Durban lifeguard Mnqobi Nxumalo battles dangerous currents at Brighton
    Beach to rescue a dog swept out to sea (IOL, 17 Nov 2026).
 5. A Wolves fan strips to his pants behind the goal to jinx Justin
    Kluivert's record third penalty; Kluivert scores anyway, completing
    the first hat-trick of penalties in Premier League history
    (The Sun, 17 Nov 2026).
 6. Three passersby kick in the door of a burning home in George, Iowa,
    at 2:45 a.m. and pull the last resident out alive; the fire chief
    calls them heroes (Sioux County Radio, 17 Nov 2026).

In brief:
 7. Two passenger trains collide head-on on a bridge beside Prague's
    main station at about 7 a.m.; 46 injured, four seriously (including
    both drivers), none killed (The Guardian, 17 Nov 2026).
 8. Ukraine strikes the Kerch Bridge to Crimea for a second day; a road
    span falls into the strait (BBC via Level Headlines daily brief).
 9. Vladimir Putin lands in Shenzhen around 2 a.m. ahead of APEC and is
    received with a red carpet, dancers and an honour guard (BBC /
    Anadolu, reported 17 Nov 2026).
10. Iran's Revolutionary Guards say two tankers hit naval mines in the
    Strait of Hormuz as a third US carrier arrives (Reuters / Al Jazeera).
11. The blackout that wasn't: viral posts claim The Simpsons predicted a
    global blackout for today; fact-checkers rate it false — the day's
    real event is a one-minute FEMA emergency-alert test (Times Now /
    PolitiFact, 17 Nov 2026).
12. A ULA Vulcan rocket fails in flight, destroying 40 Amazon Leo
    internet satellites (Spaceflight Now).
13. A homeless woman in Compton, California, refuses to leave eight
    puppies living in a riverbed hole ahead of rainstorms; a rescue takes
    them in (Parade).
14. Three goats escape in Rhode Island and tour the towns; one is lassoed
    by a local couple, one is still at large (WJAR / Parade).
15. Streamer IShowSpeed, on a livestream call about the documentary
    "The Eyes of Ghana", greets surprise guest Barack Obama in Indonesian
    ("Apa kabar?"); Obama praises his accent. The call was Monday 16 Nov
    US time and was reported across outlets on 17 Nov (HipHopWired /
    Nairobi News).
16. Mongolian President Khürelsükh resigns amid an emerging corruption
    scandal (Foreign Exchanges world roundup).
17. Canada and China extend trade deals; Beijing cuts tariffs on Canadian
    pork and seafood ahead of APEC (Reuters).
18. Nepal becomes the first country with funding provisionally set aside
    from the UN loss-and-damage fund after floods (UN News).
19. Ebola cases in DR Congo pass 11,000, with 5,400 deaths (UN News).
20. Five European states advance a migrant return-hub agreement with
    Rwanda (Anadolu morning briefing).
21. WFP and IOM warn Gaza's 1.7 million displaced face winter with food
    and shelter aid running short (WFP).
22. NASA's Voyager 1 reaches one light-day from Earth; its radio signals
    now take a full day to arrive (Space.com).
23. ESA's Hera spacecraft arrives at the Didymos asteroid system and
    flies rectangular orbits over NASA's DART crash site (Universe Today).
24. Astronomers trace mysterious radio pulses to a dead star spinning
    every eight minutes beside a Sun-like star (science reports).

Ticker: Fiona the hippo ate a knit hat (USA Today, 17 Nov); a Zika study
backs "man flu" (MedicalXpress, 17 Nov); an elephant keeps vigil over a
sick companion in Bangladesh (Somoy News, 17 Nov); dogs' gut bugs mirror
their owners' lifestyles (Phys.org, 17 Nov); Roy Keane refuses a
mascot's high-five (All Football, 17 Nov).

Deterministic: fixed noise seed, committed assets, no timestamps.
Running this script rewrites entry.png beside it, byte for byte.
"""
import os

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W = H = 1024
PAPER = (247, 241, 227)
PANEL = (255, 253, 246)
INK = (25, 25, 36)
RED = (179, 55, 42)
DARKTXT = (52, 52, 60)
CREAM = (250, 246, 235)
SHADOW = (203, 193, 168)

NOTO = "/usr/share/fonts/truetype/noto"
SERIF_BLACK = f"{NOTO}/NotoSerifDisplay-Black.ttf"
SERIF_BOLD = f"{NOTO}/NotoSerif-Bold.ttf"
SERIF = f"{NOTO}/NotoSerif-Regular.ttf"
SERIF_IT = f"{NOTO}/NotoSerif-Italic.ttf"
SANS_CB = f"{NOTO}/NotoSans-CondensedBold.ttf"
SANS_B = f"{NOTO}/NotoSans-Bold.ttf"
SANS_R = f"{NOTO}/NotoSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def tw(d, s, f):
    return d.textlength(s, font=f)


def fit(d, s, max_w, start, path=SERIF_BOLD, floor=11):
    size = start
    while size > floor and tw(d, s, font(path, size)) > max_w:
        size -= 1
    return font(path, size)


def wrap(d, s, f, max_w):
    words, lines, cur = s.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if tw(d, t, f) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def center(d, s, f, y, color=INK):
    d.text(((W - tw(d, s, f)) / 2, y), s, font=f, fill=color)


def crop_to_aspect(im, target_w, target_h):
    """Center-crop im to the target aspect ratio, then resize to it."""
    src_ratio = im.width / im.height
    dst_ratio = target_w / target_h
    if src_ratio > dst_ratio:  # too wide: trim the sides
        nw = int(im.height * dst_ratio)
        x0 = (im.width - nw) // 2
        im = im.crop((x0, 0, x0 + nw, im.height))
    else:  # too tall: trim top and bottom
        nh = int(im.width / dst_ratio)
        y0 = (im.height - nh) // 2
        im = im.crop((0, y0, im.width, y0 + nh))
    return im.resize((target_w, target_h), Image.LANCZOS)


# ---------------- aged paper ----------------
rng = np.random.default_rng(20261117)
base = np.zeros((H, W, 3), dtype=np.float32)
base[:, :] = PAPER
noise = rng.normal(0.0, 4.5, (H, W, 1)).astype(np.float32)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
dist = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
vig = (1.0 - 0.055 * np.clip(dist - 0.55, 0, None) ** 2)[..., None]
arr = np.clip((base + noise) * vig, 0, 255).astype(np.uint8)
img = Image.fromarray(arr, "RGB")
d = ImageDraw.Draw(img)
M = 26  # page margin

# ---------------- masthead ----------------
center(d, "T H E   W O R L D   I N   O N E   P I C T U R E", font(SERIF_BLACK, 25), 18)
d.rectangle([M, 50, W - M, 55], fill=RED)
date_f = fit(d, "TUESDAY 17 NOVEMBER 2026", W - 2 * M, 64, path=SERIF_BLACK)
center(d, "TUESDAY 17 NOVEMBER 2026", date_f, 62)
sub_path = SERIF_IT if os.path.exists(SERIF_IT) else SERIF
center(d, "Twenty-nine stories that defined the day — the funny, the strange, the brave",
       font(sub_path, 20), 134, DARKTXT)
d.rectangle([M, 162, W - M, 165], fill=INK)
d.rectangle([M, 168, W - M, 169], fill=INK)

# ---------------- panels ----------------
PANELS = [
    ("DIPLOMACY · ASIA", "panel1.png", "TRUMP HIJACKS THE FAMILY PHOTO",
     "The Quad's Manila group photo became a 10-minute Trump presser; "
     "Modi's \u201cShall we move?\u201d went unanswered, three leaders waiting."),
    ("TECH · AMERICAS", "panel2.png", "IT ALL BROKE. NOBODY HACKED IT.",
     "Five days, six meltdowns: Microsoft, the FAA, Chase, United, Apple \u2014 "
     "even the NSA. Washington's verdict: not hackers. Just upgrades."),
    ("SCIENCE · EUROPE", "panel3.png", "A GENOME FROM WHALE SNOT",
     "St Andrews scientists sequenced a humpback's whole genome from its "
     "blow \u2014 \u201cwhale snot\u201d sampled as it surfaced. No darts, no biopsies."),
    ("HEROES · AFRICA", "panel4.png", "INTO THE SURF FOR A DOG",
     "Durban lifeguard Mnqobi Nxumalo battled dangerous currents at "
     "Brighton Beach to save a dog swept out to sea."),
    ("SPORT · EUROPE", "panel5.png", "BARED ALL. SCORED ANYWAY.",
     "A Wolves fan stripped to his pants to jinx a record third penalty. "
     "Kluivert scored anyway \u2014 a first-ever penalty hat-trick."),
    ("HEROES · AMERICAS", "panel6.png", "THREE STRANGERS KICKED IN THE DOOR",
     "Passing a burning Iowa home at 2:45 a.m., three drivers kicked in "
     "the door and pulled the last resident out. \u201cHeroes,\u201d said the chief."),
]

PW, PH, GAP = 314, 234, 12
GX, GY = M, 174
ART_W, ART_H = PW - 20, 72
for i, (tag, art_file, head, cap) in enumerate(PANELS):
    px = GX + (i % 3) * (PW + GAP)
    py = GY + (i // 3) * (PH + GAP)
    d.rectangle([px + 5, py + 6, px + PW + 5, py + PH + 6], fill=SHADOW)
    d.rectangle([px, py, px + PW, py + PH], fill=PANEL, outline=INK, width=3)
    d.text((px + 14, py + 7), tag, font=font(SANS_CB, 15), fill=RED)
    d.rectangle([px + 14, py + 28, px + PW - 14, py + 30], fill=INK)
    art = Image.open(os.path.join(HERE, "assets", art_file)).convert("RGB")
    art = crop_to_aspect(art, ART_W, ART_H)
    img.paste(art, (px + 10, py + 34))
    d.rectangle([px + 10, py + 34, px + 10 + ART_W, py + 34 + ART_H],
                outline=INK, width=2)
    # headline: shrink from 24px until it wraps to at most two lines
    hsize = 24
    while hsize > 17 and len(wrap(d, head, font(SERIF_BOLD, hsize), PW - 28)) > 2:
        hsize -= 1
    hy = py + 114
    for line in wrap(d, head, font(SERIF_BOLD, hsize), PW - 28):
        d.text((px + 14, hy), line, font=font(SERIF_BOLD, hsize), fill=INK)
        hy += hsize + 4
    cy = max(py + 168, hy + 3)
    csize, clines = 13, None
    for cand in (14, 13):
        lines = wrap(d, cap, font(SERIF, cand), PW - 28)
        if cy + len(lines) * (cand + 2) <= py + PH - 6:
            csize, clines = cand, lines
            break
    if clines is None:
        csize, clines = 13, lines
    for line in clines:
        d.text((px + 14, cy), line, font=font(SERIF, csize), fill=DARKTXT)
        cy += csize + 2

# ---------------- in brief ----------------
BRIEFS = [
    ("TRAINS MEET HEAD-ON IN PRAGUE",
     "Two passenger trains collide on a bridge by the main station: 46 injured, four seriously, none killed."),
    ("SPAN DOWN IN THE STRAIT",
     "Ukraine hits the Kerch Bridge to Crimea again; a road span drops into the sea."),
    ("PUTIN'S RED-CARPET LANDING",
     "Putin lands in Shenzhen at 2 a.m. for APEC to dancers, flags and a red carpet."),
    ("MINES IN HORMUZ",
     "Tehran says two tankers struck naval mines as a third US carrier arrives."),
    ("THE BLACKOUT THAT WASN'T",
     "Viral posts claimed The Simpsons predicted a global blackout today. Fact-checkers: false \u2014 just a one-minute US alert test."),
    ("40 SATELLITES LOST",
     "A ULA Vulcan rocket fails in flight, taking 40 Amazon internet satellites with it."),
    ("EIGHT PUPPIES, ONE HERO",
     "A homeless woman in Compton refuses to leave eight puppies in a flooding riverbed."),
    ("GOATS ON THE LAM",
     "Three goats tour Rhode Island; one is lassoed, one is still at large."),
    ("\u2018APA KABAR, MR PRESIDENT?\u2019",
     "IShowSpeed greets surprise guest Barack Obama in Indonesian; Obama praises the accent."),
    ("A PRESIDENT QUITS",
     "Mongolia's Kh\u00fcrels\u00fckh resigns as a corruption scandal closes in."),
    ("CANADA\u2013CHINA THAW",
     "Beijing trims tariffs on Canadian pork and seafood ahead of APEC."),
    ("FIRST IN THE CLIMATE QUEUE",
     "Nepal is first promised UN loss-and-damage cash after deadly floods."),
    ("EBOLA PASSES 11,000",
     "DR Congo cases top 11,000, with 5,400 dead, says the UN."),
    ("EU EYES RWANDA HUB",
     "Five states push a deal for a migrant return hub in Rwanda."),
    ("GAZA FACES WINTER",
     "1.7 million displaced people face the cold short of food and shelter."),
    ("ONE LIGHT-DAY OUT",
     "Voyager 1's radio calls now take a full day to reach Earth."),
    ("FLYING RECTANGLES",
     "Europe's Hera probe reaches NASA's asteroid crash site, orbiting in rectangles."),
    ("A DEAD STAR BLINKS",
     "A white dwarf spins every eight minutes, radio-pulsing beside a Sun-like star."),
]

BY = GY + 2 * PH + GAP + 10          # 672: header baseline area
d.text((M, BY), "IN BRIEF", font=font(SANS_B, 21), fill=RED)
rest = " \u2014 EIGHTEEN MORE FROM TUESDAY"
d.text((M + tw(d, "IN BRIEF", font(SANS_B, 21)), BY), rest,
       font=font(SANS_B, 21), fill=INK)
d.rectangle([M, BY + 28, W - M, BY + 30], fill=INK)

COL_W, COL_GAP = 312, 18
COL_X = [M, M + COL_W + COL_GAP, M + 2 * (COL_W + COL_GAP)]
TOP = BY + 36                        # 708
BOTTOM = 950
BRIEF_LH, BRIEF_GAP = 15, 5
BF_B, BF_R = font(SANS_B, 13), font(SANS_R, 13)
SPACE_W = tw(d, " ", BF_R)


def brief_lines(head, body, max_w):
    """Wrap a brief as rich text: bold headline tokens, then regular body.
    Returns a list of lines; each line is a list of (word, font) tokens."""
    tokens = [(w_, BF_B) for w_ in head.split()]
    tokens += [(w_, BF_R) for w_ in body.split()]
    lines, cur, cur_w = [], [], 0.0
    for w_, f in tokens:
        ww = tw(d, w_, f)
        add = ww if not cur else SPACE_W + ww
        if cur and cur_w + add > max_w:
            lines.append(cur)
            cur, cur_w = [(w_, f)], ww
        else:
            cur.append((w_, f))
            cur_w += add
    if cur:
        lines.append(cur)
    return lines


# measure every brief, then greedily balance the three columns by height
measured = []
for head, body in BRIEFS:
    lines = brief_lines(head, body, COL_W)
    measured.append((lines, len(lines) * BRIEF_LH))
columns = [[], [], []]
heights = [0, 0, 0]
for idx in sorted(range(len(measured)), key=lambda i: (-measured[i][1], i)):
    item = measured[idx]
    c = min(range(3), key=lambda k: (heights[k], k))
    if columns[c]:
        heights[c] += BRIEF_GAP
    columns[c].append((idx, item))
    heights[c] += item[1]
for c in range(3):
    columns[c] = [item for _, item in sorted(columns[c], key=lambda p: p[0])]

for c in range(3):
    if heights[c] > BOTTOM - TOP:
        print(f"WARNING: brief column {c} overflows: {heights[c]}px > {BOTTOM - TOP}px")
    y = TOP
    for lines, hgt in columns[c]:
        for line in lines:
            x = COL_X[c]
            for w_, f in line:
                d.text((x, y), w_, font=f, fill=INK if f is BF_B else DARKTXT)
                x += tw(d, w_, f) + SPACE_W
            y += BRIEF_LH
        y += BRIEF_GAP
    if c < 2:  # column rule
        rx = COL_X[c] + COL_W + COL_GAP // 2
        d.line([rx, TOP, rx, BOTTOM], fill=SHADOW, width=2)

# ---------------- ticker ----------------
TY = 952
d.rectangle([M, TY, W - M, 1002], fill=INK)
t1 = ("ALSO TUESDAY \u2014 FIONA THE HIPPO ATE A KNIT HAT \u00b7 \u2018MAN FLU\u2019 IS "
      "REAL-ISH, SAYS ZIKA STUDY \u00b7 ELEPHANT KEEPS VIGIL OVER SICK FRIEND")
t2 = ("DOGS\u2019 GUT BUGS COPY THEIR OWNERS\u2019 LIFESTYLES \u00b7 ROY KEANE "
      "STONEWALLS A MASCOT\u2019S HIGH-FIVE")
for j, t in enumerate((t1, t2)):
    f = fit(d, t, W - 2 * M - 24, 15, path=SANS_B)
    d.text(((W - tw(d, t, f)) / 2, TY + 6 + j * 22), t, font=f, fill=CREAM)

# ---------------- save (PNG, <= 1 MiB; quantize only if needed) ----------------
out = os.path.join(HERE, "entry.png")
img.save(out, optimize=True)
if os.path.getsize(out) > 1048576:
    img.quantize(colors=256, method=Image.MEDIANCUT,
                 dither=Image.FLOYDSTEINBERG).save(out, optimize=True)
print("saved entry.png", img.size, os.path.getsize(out), "bytes")
