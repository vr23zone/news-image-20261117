#!/usr/bin/env python3
"""Draw entry.png: the world news of Tuesday 17 November 2026 on one page.

A newsprint front page composited with PIL: a masthead that names the day,
six story panels whose illustrations live in assets/panel1..6.png (rich
editorial art, generated without any text so every word on the page is set
here, crisply, by this script), and a ticker strip with five more stories.

The brief was "funny but serious" — the day's lighter, stranger and braver
stories, all genuinely reported on Tuesday 17 November 2026:

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


def font(path, size):
    return ImageFont.truetype(path, size)


def tw(d, s, f):
    return d.textlength(s, font=f)


def fit(d, s, max_w, start, path=SERIF_BOLD, floor=13):
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
center(d, "T H E   W O R L D   I N   O N E   P I C T U R E", font(SERIF_BLACK, 27), 26)
d.rectangle([M, 66, W - M, 72], fill=RED)
date_f = fit(d, "TUESDAY 17 NOVEMBER 2026", W - 2 * M, 76, path=SERIF_BLACK)
center(d, "TUESDAY 17 NOVEMBER 2026", date_f, 82)
sub_path = SERIF_IT if os.path.exists(SERIF_IT) else SERIF
center(d, "Six stories that defined the day — the funny, the strange, the brave",
       font(sub_path, 22), 170, DARKTXT)
d.rectangle([M, 204, W - M, 207], fill=INK)
d.rectangle([M, 210, W - M, 211], fill=INK)

# ---------------- panels ----------------
PANELS = [
    ("DIPLOMACY · ASIA", "panel1.png", "TRUMP HIJACKS THE FAMILY PHOTO",
     "The Quad's Manila group photo became a 10-minute Trump presser. "
     "Modi's \u201cShall we move?\u201d went unanswered; three leaders stood waiting."),
    ("TECH · AMERICAS", "panel2.png", "IT ALL BROKE. NOBODY HACKED IT.",
     "Five days, six meltdowns: Microsoft, the FAA, Chase, United, Apple \u2014 "
     "even the NSA. Washington's verdict: not hackers. Just upgrades."),
    ("SCIENCE · EUROPE", "panel3.png", "A GENOME FROM WHALE SNOT",
     "St Andrews scientists sequenced a humpback's whole genome from its "
     "blow \u2014 \u201cwhale snot\u201d sampled as it surfaced. No darts, no biopsies."),
    ("HEROES · AFRICA", "panel4.png", "INTO THE SURF FOR A DOG",
     "Durban lifeguard Mnqobi Nxumalo battled dangerous currents at "
     "Brighton Beach to reach a dog swept out to sea \u2014 and got it ashore."),
    ("SPORT · EUROPE", "panel5.png", "BARED ALL. SCORED ANYWAY.",
     "A Wolves fan stripped to his pants to jinx a record third penalty. "
     "Kluivert scored anyway \u2014 a first-ever penalty hat-trick."),
    ("HEROES · AMERICAS", "panel6.png", "THREE STRANGERS KICKED IN THE DOOR",
     "Passing a burning Iowa home at 2:45 a.m., three drivers kicked in "
     "the door and pulled the last resident out. \u201cHeroes,\u201d said the chief."),
]

PW, PH, GAP = 314, 344, 12
GX, GY = M, 214
ART_W, ART_H = PW - 20, 126
for i, (tag, art_file, head, cap) in enumerate(PANELS):
    px = GX + (i % 3) * (PW + GAP)
    py = GY + (i // 3) * (PH + GAP)
    d.rectangle([px + 5, py + 6, px + PW + 5, py + PH + 6], fill=SHADOW)
    d.rectangle([px, py, px + PW, py + PH], fill=PANEL, outline=INK, width=3)
    d.text((px + 14, py + 9), tag, font=font(SANS_CB, 17), fill=RED)
    d.rectangle([px + 14, py + 34, px + PW - 14, py + 36], fill=INK)
    art = Image.open(os.path.join(HERE, "assets", art_file)).convert("RGB")
    art = art.resize((ART_W, ART_H), Image.LANCZOS)
    img.paste(art, (px + 10, py + 42))
    d.rectangle([px + 10, py + 42, px + 10 + ART_W, py + 42 + ART_H],
                outline=INK, width=2)
    # headline: shrink from 29px until it wraps to at most two lines
    hsize = 29
    while hsize > 20 and len(wrap(d, head, font(SERIF_BOLD, hsize), PW - 28)) > 2:
        hsize -= 1
    hy = py + 178
    for line in wrap(d, head, font(SERIF_BOLD, hsize), PW - 28):
        d.text((px + 14, hy), line, font=font(SERIF_BOLD, hsize), fill=INK)
        hy += hsize + 5
    cy = max(py + 250, hy + 4)
    csize, clines = 17, None
    for cand in (17, 16, 15):
        lines = wrap(d, cap, font(SERIF, cand), PW - 28)
        if cy + len(lines) * (cand + 3) <= py + PH - 8:
            csize, clines = cand, lines
            break
    if clines is None:
        csize, clines = 15, lines
    for line in clines:
        d.text((px + 14, cy), line, font=font(SERIF, csize), fill=DARKTXT)
        cy += csize + 3

# ---------------- ticker ----------------
TY = 924
d.rectangle([M, TY, W - M, 996], fill=INK)
t1 = ("ALSO TUESDAY \u2014 FIONA THE HIPPO ATE A KNIT HAT \u00b7 \u2018MAN FLU\u2019 IS "
      "REAL-ISH, SAYS ZIKA STUDY \u00b7 ELEPHANT KEEPS VIGIL OVER SICK FRIEND")
t2 = ("DOGS\u2019 GUT BUGS COPY THEIR OWNERS\u2019 LIFESTYLES \u00b7 ROY KEANE "
      "STONEWALLS A MASCOT\u2019S HIGH-FIVE")
for j, t in enumerate((t1, t2)):
    f = fit(d, t, W - 2 * M - 24, 20, path=SANS_B)
    d.text(((W - tw(d, t, f)) / 2, TY + 11 + j * 38), t, font=f, fill=CREAM)

# ---------------- save (PNG, <= 1 MiB; quantize only if needed) ----------------
out = os.path.join(HERE, "entry.png")
img.save(out, optimize=True)
if os.path.getsize(out) > 1048576:
    img.quantize(colors=256, method=Image.MEDIANCUT,
                 dither=Image.FLOYDSTEINBERG).save(out, optimize=True)
print("saved entry.png", img.size, os.path.getsize(out), "bytes")
