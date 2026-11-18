#!/usr/bin/env python3
"""Draw entry.png: the world news of Tuesday 17 November 2026 on one page.

V3 — a bright, full-colour infographic front page. A navy masthead band
carries the date and the strap "37 STORIES · 8 CONTINENTS · ALL FROM
TUESDAY". Twelve numbered panels pair AI illustrations (assets/v3panel*.png,
generated with no text in them) with PIL-typeset headlines and captions.
A "WHERE IT HAPPENED" world map (coastlines in assets/world.json, drawn
here) plots numbered dots, colour-coded by category, for every story with
a clear location. Twenty-five more stories run as numbered one-liners in
an ALSO ON TUESDAY section. A text-free vintage nautical vignette
(assets/nautical.png) — a large wooden ship's helm wheel over a brass
compass rose, with a small tall ship in the corner — fills the space
beside the map legend. Every panel and brief
carries one emoji that
matches its story, typeset from Noto Color Emoji. All wording is set by
this script, so the text is exact and crisp.

The brief was "funny but serious": the day's lighter, stranger and braver
stories lead, the rest of the day's world follows in brief. Every story
was genuinely reported on Tuesday 17 November 2026:

Panels:
 1. Trump turns the Quad leaders' group photo in Manila into a 10-minute
    impromptu press conference; Modi's "Shall we move?" goes unanswered
    (Bloomberg, 17 Nov 2026).
 2. A five-day wave of US tech outages — Microsoft 365, an FAA ground
    stop, Chase, United, Apple, the NSA — is officially ruled NOT a
    cyberattack (Business Insider tally / CNBC, 17 Nov 2026).
 3. St Andrews scientists sequence a humpback whale's whole genome from
    its blow — "whale snot" (Phys.org, 17 Nov 2026).
 4. Durban lifeguard Mnqobi Nxumalo battles dangerous currents to rescue
    a dog swept out to sea (IOL, 17 Nov 2026).
 5. A Wolves fan strips to his pants behind the goal to jinx Justin
    Kluivert's record third penalty; Kluivert scores anyway — the first
    hat-trick of penalties in Premier League history (The Sun).
 6. Surf lifesaver Charlie Verco, who in June paddled to a shark-attack
    victim at Sydney's Coogee Beach and kept her alive, wins his first
    Shaw and Partners Iron Series race, at Thirroul Beach (AAP wire;
    Sports Rewind Media feature, 17 Nov 2026).
 7. Two passenger trains collide head-on on a bridge beside Prague's
    main station; 46 injured, four seriously, none killed (The Guardian).
 8. Bitcoin stalls below $65,000 after a 12% weekly crash pushes it
    through its 200-week average, a break seen just three times since
    2013; Wintermute warns of a slide into the $50,000s (CoinDesk,
    17 Nov 2026).
 9. The blackout that wasn't: viral posts claim The Simpsons predicted a
    global blackout for today; fact-checkers rate it false — the day's
    real event is a one-minute FEMA alert test (Times Now / PolitiFact).
10. Streamer IShowSpeed, on a livestream video call, greets Barack
    Obama in Indonesian ("Apa kabar, Mr President?"); Obama praises
    his accent. Reported across outlets on 17 Nov (HipHopWired /
    Nairobi News).
11. Ukraine strikes the Kerch Bridge to Crimea for a second day; a road
    span falls into the strait (BBC via Level Headlines daily brief).
12. A homeless woman in Compton, California, refuses to leave eight
    puppies living in a riverbed hole ahead of rainstorms (Parade).

Also on Tuesday (13–37):
13. Iran says two tankers hit naval mines in Hormuz (Reuters / Al Jazeera).
14. A ULA Vulcan rocket fails, destroying 40 Amazon Leo satellites
    (Spaceflight Now).
15. Three goats escape in Rhode Island; one is lassoed by a local couple,
    one is still at large (WJAR / Parade).
16. Mongolian President Khürelsükh resigns amid a corruption scandal
    (Foreign Exchanges world roundup).
17. Canada and China extend trade deals; Beijing cuts tariffs on Canadian
    pork and seafood ahead of APEC (Reuters).
18. Nepal is first promised funding from the UN loss-and-damage fund
    after floods (UN News).
19. Ebola cases in DR Congo pass 11,000, with 5,400 deaths (UN News).
20. Five European states advance a migrant return-hub deal with Rwanda
    (Anadolu morning briefing).
21. WFP warns Gaza's 1.7 million displaced face winter short of food and
    shelter (WFP).
22. NASA's Voyager 1 reaches one light-day from Earth (Space.com).
23. ESA's Hera arrives at the Didymos asteroid system and flies
    rectangular orbits over NASA's DART crash site (Universe Today).
24. Astronomers trace radio pulses to a dead star spinning every eight
    minutes beside a Sun-like star (science reports).
25. Fiona the hippo swallows a knit hat at Cincinnati Zoo and is taken
    off exhibit (USA TODAY Network, 17 Nov 2026).
26. A Zika study backs "man flu": male immune responses differ
    (MedicalXpress, McMaster University).
27. An elephant keeps vigil over a sick companion in Bangladesh
    (Somoy News).
28. Dogs' gut microbes mirror their owners' lifestyles (Phys.org).
29. Roy Keane refuses a mascot's high-five on live TV (All Football).
30. The Leonid meteor shower peaks tonight: up to 15 meteors an hour
    after the moon sets (USA TODAY / Space.com, 17 Nov 2026).
31. About 20 uncontacted Awá people emerge from Brazil's Amazon in
    Maranhão asking for food; first images shared Tuesday (Reuters,
    17 Nov 2026).
32. Melbourne Cup runner So You Are is found dead in a Sydney waste
    facility less than two weeks after the race; an inquiry opens
    (Sydney Morning Herald, reported 17 Nov 2026).
33. COP31's first draft decision reveals deep divisions among the 194
    delegations in Turkey (Le Monde, 17 Nov 2026).
34. A riverboat captain and harbour police pull nine people from the
    Mississippi at New Orleans after a cruise boat capsizes
    (6abc / WWLTV, 17 Nov 2026).
35. LPG tanker Gas Husky sinks off Bulgaria; an air force helicopter
    lifts all 19 Filipino crew from a life raft (Reuters / BTA,
    17 Nov 2026).
36. Trackers follow 48 young emperor penguins from Weddell Sea
    colonies into industrial krill-fishing zones during their first
    year at sea (WHOI / Biological Conservation, 17 Nov 2026).
37. The Barnacle — a yellow suction clamp that blinds bad parkers
    until they pay up — rolls out in Christchurch, Queenstown and
    Wellington (Stuff, 17 Nov 2026; NZ Herald via CarExpert NZ).

Continent check: Asia 8 · Europe 6 · North America 10 · Africa 3 ·
South America 1 (31) · Oceania 2 (6, 32) · Antarctica 1 (36) ·
Zealandia 1 (37 — New Zealand, on the mostly submerged eighth
continent) · space & sky 4 · global 1 (8, the Bitcoin crash — a
worldwide market, so no dot) — eight continents, as the strap says.

Deterministic: committed assets only, no randomness, no timestamps.
Running this script rewrites entry.png beside it, byte for byte.
"""
import json
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W = H = 1024
M = 20

BG = (250, 250, 246)
NAVY = (13, 38, 76)
NAVY2 = (18, 50, 96)
INK = (24, 30, 40)
GRAY = (84, 94, 108)
LGRAY = (150, 160, 172)
BORDER = (178, 194, 210)
PANELBG = (255, 255, 255)
RED = (216, 52, 38)
GOLD = (243, 197, 90)
MAPLAND = (198, 219, 236)
MAPLINE = (140, 170, 198)
MAPSEA = (238, 245, 250)

CATS = {
    "WAR":    ((212, 61, 42),  "War & security"),
    "POL":    ((36, 86, 166),  "Politics"),
    "TECH":   ((13, 122, 120), "Economy & tech"),
    "HEALTH": ((56, 142, 60),  "Health & climate"),
    "SPORT":  ((230, 126, 34), "Sport"),
    "HERO":   ((183, 121, 12), "Heroes"),
    "SCI":    ((131, 62, 166), "Science"),
    "ODD":    ((170, 105, 55), "Odd & offbeat"),
}

NOTO = "/usr/share/fonts/truetype/noto"
SANS_BLACK = f"{NOTO}/NotoSans-Black.ttf"
SANS_XB = f"{NOTO}/NotoSans-ExtraBold.ttf"
SANS_B = f"{NOTO}/NotoSans-Bold.ttf"
SANS_R = f"{NOTO}/NotoSans-Regular.ttf"
SANS_CB = f"{NOTO}/NotoSans-CondensedBold.ttf"
SANS_CXB = f"{NOTO}/NotoSans-CondensedExtraBold.ttf"
EMOJI_TTF = f"{NOTO}/NotoColorEmoji.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def tw(d, s, f):
    return d.textlength(s, font=f)


def wrap(d, s, f, max_w):
    words, lines, cur = s.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if tw(d, t, f) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def crop_to_aspect(im, target_w, target_h, focus=0.5):
    """Crop im to the target aspect ratio (focus = vertical centre of the
    crop window, 0..1), then resize to it."""
    src_ratio = im.width / im.height
    dst_ratio = target_w / target_h
    if src_ratio > dst_ratio:
        nw = int(im.height * dst_ratio)
        x0 = (im.width - nw) // 2
        im = im.crop((x0, 0, x0 + nw, im.height))
    else:
        nh = int(im.width / dst_ratio)
        y0 = int((im.height - nh) * focus)
        im = im.crop((0, y0, im.width, y0 + nh))
    return im.resize((target_w, target_h), Image.LANCZOS)


# ---------------- emoji (Noto Color Emoji, rendered once, cached) ----------
_emoji_cache = {}


def emoji_img(ch, h):
    if ch not in _emoji_cache:
        tile = Image.new("RGBA", (140, 140), (0, 0, 0, 0))
        td = ImageDraw.Draw(tile)
        td.text((6, 6), ch, font=font(EMOJI_TTF, 109), embedded_color=True)
        bbox = tile.getbbox()
        _emoji_cache[ch] = tile.crop(bbox) if bbox else tile
    src = _emoji_cache[ch]
    w = max(1, round(src.width * h / src.height))
    return src.resize((w, h), Image.LANCZOS)


def paste_emoji(img, ch, x, y, h):
    e = emoji_img(ch, h)
    img.paste(e, (int(x), int(y)), e)
    return e.width


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)


def spaced_width(s, f, tracking):
    return sum(tw(d, ch, f) for ch in s) + tracking * (len(s) - 1)


def draw_spaced(s, f, cx, y, color, tracking):
    x = cx - spaced_width(s, f, tracking) / 2
    for ch in s:
        d.text((x, y), ch, font=f, fill=color)
        x += tw(d, ch, f) + tracking


def center(d_, s, f, y, color=INK):
    d_.text(((W - tw(d_, s, f)) / 2, y), s, font=f, fill=color)


# ---------------- masthead ----------------
draw_spaced("THE WORLD IN ONE PICTURE", font(SANS_BLACK, 21), W / 2, 8, NAVY, 7)
d.rectangle([M, 38, W - M, 41], fill=RED)
d.rectangle([M, 46, W - M, 120], fill=NAVY)
d.rectangle([M, 46, W - M, 49], fill=NAVY2)
date_f = font(SANS_XB, 43)
date_s = "TUESDAY 17 NOVEMBER 2026"
while tw(d, date_s, date_f) > W - 2 * M - 30:
    date_f = font(SANS_XB, date_f.size - 1)
center(d, date_s, date_f, 52, (255, 255, 255))
draw_spaced("37 STORIES · 8 CONTINENTS · ALL FROM TUESDAY",
            font(SANS_CB, 15), W / 2, 97, GOLD, 3)
center(d, "Thirty-seven stories that defined the day — the funny, the strange, the brave",
       font(SANS_R, 14), 126, GRAY)
d.rectangle([M, 144, W - M, 146], fill=BORDER)

# ---------------- panels ----------------
PANELS = [
    # num, eyebrow, cat, art, emoji, headline, caption, focus
    (1, "DIPLOMACY · ASIA", "POL", "v3panel1.png", "📸",
     "TRUMP HIJACKS THE FAMILY PHOTO",
     "Modi's \u201cShall we move?\u201d went unanswered as three leaders "
     "waited out the presser.", 0.35),
    (2, "TECH · AMERICAS", "TECH", "v3panel2.png", "💻",
     "IT ALL BROKE. NOBODY HACKED IT.",
     "Microsoft, the FAA, Chase, United, Apple, the NSA: not hackers, "
     "just upgrades.", 0.5),
    (3, "SCIENCE · EUROPE", "SCI", "v3panel3.png", "🐋",
     "A GENOME FROM WHALE SNOT",
     "St Andrews read a humpback's genome from its blow. "
     "No biopsies.", 0.5),
    (4, "HEROES · AFRICA", "HERO", "v3panel4.png", "🛟",
     "INTO THE SURF FOR A DOG",
     "A Durban lifeguard fought dangerous currents to rescue a dog "
     "swept out to sea.", 0.55),
    (5, "SPORT · EUROPE", "SPORT", "v3panel5.png", "⚽",
     "BARED ALL. SCORED ANYWAY.",
     "A Wolves fan stripped to jinx a record third penalty. "
     "Kluivert scored anyway.", 0.5),
    (6, "HEROES · OCEANIA", "HERO", "v3panel6.png", "🦈",
     "SHARK-ATTACK HERO WINS HIS FIRST TITLE",
     "Five months after the Coogee shark rescue, Verco wins "
     "at Thirroul.", 0.5),
    (7, "CRASH · EUROPE", "WAR", "v3panel7.png", "🚆",
     "TRAINS MEET HEAD-ON IN PRAGUE",
     "Two trains collide on a Prague bridge: 46 injured, four "
     "seriously, none killed.", 0.5),
    (8, "CRYPTO · GLOBAL", "TECH", "v3panel8.png", "🪙",
     "BITCOIN BREAKS ITS LIFELINE",
     "A 12% weekly crash knocks Bitcoin under $65,000, through "
     "its 200-week average.", 0.45),
    (9, "HOAX · AMERICAS", "TECH", "v3panel9.png", "📵",
     "THE BLACKOUT THAT WASN'T",
     "Viral posts said The Simpsons predicted a global blackout. "
     "Fact-checkers: false.", 0.5),
    (10, "VIRAL · ASIA", "POL", "v3panel10.png", "🎤",
     "\u2018APA KABAR, MR PRESIDENT?\u2019",
     "On his livestream, Speed greets Obama in Indonesian: "
     "\u2018Apa kabar, Mr President?\u2019", 0.5),
    (11, "WAR · EUROPE", "WAR", "v3panel11.png", "🌉",
     "SPAN DOWN IN THE STRAIT",
     "Ukraine hits the Kerch Bridge to Crimea again; a road span "
     "drops into the strait.", 0.5),
    (12, "HEROES · AMERICAS", "HERO", "v3panel12.png", "🐶",
     "EIGHT PUPPIES, ONE HERO",
     "A homeless Compton woman refuses to leave eight puppies in "
     "a flooding riverbed.", 0.45),
]

PW, PH, GAP = 240, 144, 8
GX, GY = M, 148
ART_W, ART_H = PW - 14, 52
for num, tag, cat, art_file, emo, head, cap, focus in PANELS:
    i = num - 1
    px = GX + (i % 4) * (PW + GAP)
    py = GY + (i // 4) * (PH + GAP)
    ccol = CATS[cat][0]
    d.rectangle([px, py, px + PW, py + PH], fill=PANELBG, outline=BORDER, width=2)
    d.rectangle([px, py, px + PW, py + 5], fill=ccol)
    # number badge
    bcx, bcy, br = px + 17, py + 19, 11
    d.ellipse([bcx - br, bcy - br, bcx + br, bcy + br], fill=RED)
    nf = font(SANS_B, 12 if num < 10 else 11)
    ns = str(num)
    d.text((bcx - tw(d, ns, nf) / 2, bcy - nf.size / 2 - 1), ns, font=nf,
           fill=(255, 255, 255))
    d.text((px + 33, py + 11), tag, font=font(SANS_CB, 12), fill=ccol)
    art = Image.open(os.path.join(HERE, "assets", art_file)).convert("RGB")
    art = crop_to_aspect(art, ART_W, ART_H, focus)
    img.paste(art, (px + 7, py + 27))
    d.rectangle([px + 7, py + 27, px + 7 + ART_W, py + 27 + ART_H],
                outline=BORDER, width=1)
    # headline: emoji first, then up to two lines
    hf = font(SANS_CXB, 16)
    hy = py + 83
    ew = paste_emoji(img, emo, px + 8, hy, 16)
    first_w = PW - 16 - ew - 5
    lines, cur = [], ""
    for w_ in head.split():
        t = (cur + " " + w_).strip()
        lim = first_w if not lines else PW - 16
        if tw(d, t, hf) <= lim:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    for li, line in enumerate(lines[:2]):
        lx = px + 8 + (ew + 5 if li == 0 else 0)
        d.text((lx, hy + li * 16), line, font=hf, fill=INK)
    cy = hy + min(len(lines), 2) * 16 + 2
    cf = font(SANS_R, 11)
    for line in wrap(d, cap, cf, PW - 16)[:2]:
        d.text((px + 8, cy), line, font=cf, fill=GRAY)
        cy += 13

# ---------------- map + legend ----------------
MY = 604
d.text((M, MY), "WHERE IT HAPPENED", font=font(SANS_XB, 14), fill=NAVY)
hx = M + tw(d, "WHERE IT HAPPENED", font(SANS_XB, 14))
d.text((hx + 6, MY), "— NUMBERS MATCH STORIES", font=font(SANS_B, 12), fill=RED)
LX = 496
d.text((LX, MY), "LEGEND", font=font(SANS_XB, 14), fill=NAVY)
d.text((LX + tw(d, "LEGEND", font(SANS_XB, 14)) + 6, MY),
       "— STORIES BY CONTINENT", font=font(SANS_B, 12), fill=RED)
d.rectangle([M, MY + 20, W - M, MY + 22], fill=BORDER)

MAP_X, MAP_Y, MAP_W, MAP_H = M, MY + 28, 460, 164
LON0, LON1, LAT0, LAT1 = -180.0, 180.0, 84.0, -56.0
d.rectangle([MAP_X, MAP_Y, MAP_X + MAP_W, MAP_Y + MAP_H], fill=MAPSEA,
            outline=BORDER, width=1)
world = json.load(open(os.path.join(HERE, "assets", "world.json")))


def proj(lon, lat):
    x = MAP_X + (lon - LON0) / (LON1 - LON0) * MAP_W
    y = MAP_Y + (LAT0 - lat) / (LAT0 - LAT1) * MAP_H
    return x, y


for poly in world["polygons"]:
    pts = [proj(lon, lat) for lon, lat in poly]
    d.polygon(pts, fill=MAPLAND, outline=MAPLINE)

# story dots: num -> (lon, lat, cat)
DOTS = {
    1: (121.0, 14.6, "POL"), 3: (-1.5, 57.0, "SCI"), 4: (31.0, -29.9, "HERO"),
    5: (-1.8, 51.0, "SPORT"), 6: (158.5, -40.0, "HERO"), 7: (14.4, 50.1, "WAR"),
    10: (106.8, -6.2, "POL"), 11: (38.5, 45.8, "WAR"),
    12: (-118.2, 33.9, "HERO"), 13: (56.3, 26.6, "WAR"),
    14: (-79.5, 27.8, "TECH"), 15: (-71.5, 41.7, "HERO"),
    16: (105.0, 48.0, "POL"), 17: (117.5, 39.5, "TECH"),
    18: (83.5, 28.6, "HEALTH"), 19: (15.3, -4.3, "HEALTH"),
    20: (30.1, -1.9, "POL"), 25: (-83.5, 38.6, "HEALTH"),
    31: (-45.3, -4.9, "HEALTH"), 32: (151.2, -33.9, "SPORT"),
    33: (36.5, 36.2, "HEALTH"), 34: (-90.1, 30.0, "HERO"),
    35: (25.5, 43.8, "HERO"),
    36: (-45.0, -48.5, "SCI"), 37: (172.5, -41.5, "ODD"),
}
for num in sorted(DOTS):
    lon, lat, cat = DOTS[num]
    x, y = proj(lon, lat)
    r = 8.5
    d.ellipse([x - r, y - r, x + r, y + r], fill=CATS[cat][0],
              outline=(255, 255, 255), width=2)
    nf = font(SANS_B, 10 if num < 10 else 9)
    ns = str(num)
    d.text((x - tw(d, ns, nf) / 2, y - nf.size / 2), ns, font=nf,
           fill=(255, 255, 255))

# legend + continent tally (right of the map)
LEG = [("WAR", "POL"), ("TECH", "HEALTH"), ("SPORT", "HERO"), ("SCI", None)]
ly = MAP_Y + 4
for a, b in LEG:
    for j, key in enumerate((a, b)):
        if key is None:
            continue
        x = LX + j * 250
        d.ellipse([x, ly + 2, x + 10, ly + 12], fill=CATS[key][0])
        d.text((x + 15, ly), CATS[key][1], font=font(SANS_R, 12), fill=INK)
    ly += 18
ly += 6
d.text((LX, ly), "ASIA 8 · EUROPE 6 · NORTH AMERICA 10",
       font=font(SANS_B, 13), fill=NAVY)
d.text((LX, ly + 17), "AFRICA 3 · SOUTH AMERICA 1 · OCEANIA 2",
       font=font(SANS_B, 13), fill=NAVY)
d.text((LX, ly + 34), "ANTARCTICA 1 · ZEALANDIA 1 · SPACE & SKY 4 · GLOBAL 1",
       font=font(SANS_B, 13), fill=NAVY)
d.text((LX, ly + 55), "Zealandia — the hidden eighth continent, mostly under the sea",
       font=font(SANS_R, 11.5), fill=GRAY)
d.text((LX, ly + 69), "Dots mark where each numbered story happened;",
       font=font(SANS_R, 11.5), fill=GRAY)
d.text((LX, ly + 83), "story 8 is a global market; space stories (22–24, 30) are overhead.",
       font=font(SANS_R, 11.5), fill=GRAY)

# decorative vintage nautical vignette in the whitespace right of the
# legend: a large wooden ship's helm wheel (the hero) over a brass compass
# rose, with a small tall ship in the corner (text-free art)
_nautical = Image.open(os.path.join(HERE, "assets", "nautical.png")).convert("RGBA")
_scale = min(134 / _nautical.width, 174 / _nautical.height)
_nautical = _nautical.resize((round(_nautical.width * _scale),
                              round(_nautical.height * _scale)), Image.LANCZOS)
img.paste(_nautical, (935 - _nautical.width // 2, 720 - _nautical.height // 2),
          _nautical)

# ---------------- also on Tuesday ----------------
AY = MAP_Y + MAP_H + 14
d.text((M, AY), "ALSO ON TUESDAY", font=font(SANS_XB, 14), fill=NAVY)
ax = M + tw(d, "ALSO ON TUESDAY", font(SANS_XB, 14))
d.text((ax + 6, AY), "— 25 MORE FROM THE DAY", font=font(SANS_B, 12), fill=RED)
d.rectangle([M, AY + 20, W - M, AY + 22], fill=BORDER)

BRIEFS = [
    (13, "WAR", "💣", "MINES IN HORMUZ", "two tankers hit naval mines"),
    (14, "TECH", "🛰️", "40 SATELLITES LOST", "a Vulcan rocket fails"),
    (15, "HERO", "🐐", "GOATS ON THE LAM", "one lassoed, one still free"),
    (16, "POL", "🏛️", "A PRESIDENT QUITS", "Mongolia's leader resigns"),
    (17, "TECH", "🤝", "CANADA–CHINA THAW", "tariffs cut pre-APEC"),
    (18, "HEALTH", "🌧️", "FIRST IN CLIMATE QUEUE", "Nepal tops UN list"),
    (19, "HEALTH", "🦠", "EBOLA PASSES 11,000", "DR Congo toll climbs"),
    (20, "POL", "🧳", "EU EYES RWANDA HUB", "five states push a deal"),
    (21, "HEALTH", "❄️", "GAZA FACES WINTER", "1.7m displaced, aid short"),
    (22, "SCI", "📡", "ONE LIGHT-DAY OUT", "Voyager's calls take a day"),
    (23, "SCI", "☄️", "FLYING RECTANGLES", "Hera orbits an asteroid"),
    (24, "SCI", "⭐", "A DEAD STAR BLINKS", "pulses every 8 minutes"),
    (25, "HEALTH", "🦛", "FIONA ATE A KNIT HAT", "zoo star off exhibit"),
    (26, "SCI", "🤧", "\u2018MAN FLU\u2019 IS REAL-ISH", "a Zika study backs it"),
    (27, "HEALTH", "🐘", "ELEPHANT KEEPS VIGIL", "over a sick friend"),
    (28, "SCI", "🐾", "DOGS\u2019 GUT BUGS", "copy their owners"),
    (29, "SPORT", "✋", "KEANE SNUBS A MASCOT", "no high-five given"),
    (30, "SCI", "🌠", "LEONIDS PEAK TONIGHT", "15 meteors an hour"),
    (31, "HEALTH", "🌳", "THE TRIBE SAYS HELLO", "Awá emerge in Brazil"),
    (32, "SPORT", "🐎", "CUP HORSE IN A SKIP BIN", "Sydney inquiry opens"),
    (33, "HEALTH", "🌍", "COP31 DRAFT FIGHT", "194 nations, deep splits"),
    (34, "HERO", "🚢", "NINE PULLED FROM THE RIVER", "in New Orleans"),
    (35, "HERO", "🚁", "19 AIRLIFTED FROM A RAFT", "tanker crew saved"),
    (36, "SCI", "🐧", "TEEN PENGUINS VS KRILL BOATS", "tracked youngsters cross fishing zones"),
    (37, "ODD", "🅿️", "NO PAY, NO DRIVE", "the Barnacle windscreen clamp reaches NZ"),
]

COL_W, COL_GAP = 318, 15
COL_X = [M, M + COL_W + COL_GAP, M + 2 * (COL_W + COL_GAP)]
TOP = AY + 28
BOTTOM = 984
BF_B, BF_R = font(SANS_B, 11.5), font(SANS_R, 11.5)
SPACE_W = tw(d, " ", BF_R)
TEXT_OFF = 37  # badge + emoji slot


def brief_lines(head, body):
    tokens = [(w_, BF_B) for w_ in head.split()]
    tokens += [("\u2014", BF_R)]
    tokens += [(w_, BF_R) for w_ in body.split()]
    lines, cur, cur_w = [], [], 0.0
    for w_, f in tokens:
        ww = tw(d, w_, f)
        add = ww if not cur else SPACE_W + ww
        if cur and cur_w + add > COL_W - TEXT_OFF:
            lines.append(cur)
            cur, cur_w = [(w_, f)], ww
        else:
            cur.append((w_, f))
            cur_w += add
    if cur:
        lines.append(cur)
    return lines


measured = []
for item in BRIEFS:
    lines = brief_lines(item[3], item[4])
    measured.append((item, lines, len(lines) * 13))
columns = [[], [], []]
heights = [0, 0, 0]
for idx in sorted(range(len(measured)), key=lambda i: (-measured[i][2], i)):
    c = min(range(3), key=lambda k: (heights[k], k))
    if columns[c]:
        heights[c] += 2
    columns[c].append((idx, measured[idx]))
    heights[c] += measured[idx][2]
for c in range(3):
    columns[c] = [m for _, m in sorted(columns[c], key=lambda p: p[0])]
    if TOP + heights[c] > BOTTOM:
        print(f"WARNING: brief column {c} overflows: ends {TOP + heights[c]} > {BOTTOM}")

for c in range(3):
    y = TOP
    for (num, cat, emo, head, body), lines, hgt in columns[c]:
        x0 = COL_X[c]
        bcx, bcy, br = x0 + 8, y + 7, 8
        d.ellipse([bcx - br, bcy - br, bcx + br, bcy + br], fill=CATS[cat][0])
        nf = font(SANS_B, 9)
        ns = str(num)
        d.text((bcx - tw(d, ns, nf) / 2, bcy - nf.size / 2), ns, font=nf,
               fill=(255, 255, 255))
        paste_emoji(img, emo, x0 + 19, y, 13)
        for line in lines:
            x = x0 + TEXT_OFF
            for w_, f in line:
                d.text((x, y), w_, font=f, fill=INK if f is BF_B else GRAY)
                x += tw(d, w_, f) + SPACE_W
            y += 13
        y += 2

# ---------------- sources ----------------
src = ("Every story was reported on Tuesday 17 November 2026. Sources include Bloomberg, Reuters, BBC, "
       "CoinDesk, The Guardian, Le Monde, UN News, USA TODAY, Space.com, Business Insider, Phys.org, WHOI, Stuff, The Sun and Parade.")
sy = 990
for line in wrap(d, src, font(SANS_R, 11), W - 2 * M - 60):
    center(d, line, font(SANS_R, 11), sy, LGRAY)
    sy += 12

# ---------------- save (PNG, <= 1 MiB; quantize only if needed) ----------------
out = os.path.join(HERE, "entry.png")
img.save(out, optimize=True)
if os.path.getsize(out) > 1048576:
    img.quantize(colors=256, method=Image.MEDIANCUT,
                 dither=Image.FLOYDSTEINBERG).save(out, optimize=True)
print("saved entry.png", img.size, os.path.getsize(out), "bytes")
