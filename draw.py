#!/usr/bin/env python3
"""Draw entry.png: the world news of Tuesday 17 November 2026 on one page.

A newsprint-style front page, drawn with PIL only (no network, no assets):
a masthead that names the day, six story panels with pictograms, headlines
and one-line captions, and a ticker strip with five more of the day's
stories. Every story was reported on 17 November 2026:

 1. Ukraine strikes the Kerch (Crimea) Bridge again; a span falls into the
    strait and Zelensky hails an "unprecedented" operation (Reuters/BBC).
 2. Iran fires drones at a US radar in Bahrain; US jets strike an Iranian
    missile site on Qeshm Island in reply (CBS/NPR/Al Jazeera).
 3. Trump travels to Asia for the APEC summit in Shenzhen and talks with
    Xi Jinping and Vladimir Putin (Hong Kong Free Press/BBC).
 4. Nvidia reports record quarterly revenue above $115bn and says it will
    not reinstate ousted CEO Jensen Huang (BBC).
 5. Japan scrambles fighter jets and protests after two suspected Russian
    aircraft violate its airspace (Reuters).
 6. The US loses its measles elimination status after 26 years amid record
    cases (BBC).
 Ticker: Ebola cases pass 11,000 in DR Congo; a Russian military plane
 crash kills all 19 aboard; Nepal is first to have funding set aside from
 the UN loss-and-damage fund; Belgium beat Italy 4-1 in the Nations
 League; five European states plan a joint migrant return hub in Rwanda.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 241, 227)
PANEL = (255, 253, 246)
INK = (25, 25, 36)
RED = (179, 55, 42)
BLUE = (31, 78, 121)
STEEL = (70, 120, 165)
GOLD = (217, 164, 65)
GRAY = (105, 105, 110)
TINT = (233, 238, 242)
GREEN = (74, 124, 74)
DARKTXT = (52, 52, 60)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def tw(d, s, f):
    return d.textlength(s, font=f)


def fit(d, s, max_w, start, floor=14):
    size = start
    while size > floor and tw(d, s, font(FB, size)) > max_w:
        size -= 1
    return font(FB, size)


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


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
M = 26  # page margin

# ---------------- masthead ----------------
center(d, "T H E   W O R L D   I N   O N E   P I C T U R E", font(FB, 25), 30)
d.rectangle([M, 68, W - M, 73], fill=RED)
date_f = fit(d, "TUESDAY 17 NOVEMBER 2026", W - 2 * M, 74)
center(d, "TUESDAY 17 NOVEMBER 2026", date_f, 84)
center(d, "Six stories that defined the day — and five more in brief",
       font(FR, 23), 172, DARKTXT)
d.rectangle([M, 206, W - M, 209], fill=INK)

# ---------------- icons ----------------

def icon_bridge(x0, y0, x1, y1):
    deck = y0 + 78
    d.rectangle([x0, y1 - 34, x1, y1], fill=STEEL)
    for wx in range(x0 + 12, x1 - 10, 46):  # waves
        d.arc([wx, y1 - 26, wx + 26, y1 - 8], 0, 180, fill=(230, 240, 248), width=3)
    for px in (x0 + 92, x1 - 92):  # pylons
        d.rectangle([px - 5, deck - 44, px + 5, y1 - 30], fill=INK)
    d.line([x0 + 92, deck - 44, x0 + 170, deck], fill=INK, width=3)
    d.line([x1 - 92, deck - 44, x1 - 170, deck], fill=INK, width=3)
    gap_l, gap_r = x0 + 168, x1 - 150
    d.rectangle([x0 + 6, deck - 4, gap_l, deck + 4], fill=INK)          # left deck
    d.rectangle([gap_r, deck - 4, x1 - 6, deck + 4], fill=INK)          # right deck
    fallen = [(gap_l, deck), (gap_r - 8, deck + 8), (gap_r - 2, y1 - 40),
              (gap_l + 8, y1 - 48)]                                     # fallen span
    d.polygon(fallen, fill=RED)
    for sx, sy, r in ((gap_l + 26, deck - 30, 17), (gap_l + 52, deck - 48, 22),
                      (gap_l + 82, deck - 34, 14)):                     # smoke
        d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(178, 178, 182))
    qx, qy = x0 + 52, y0 + 22                                               # drone
    d.rectangle([qx - 13, qy - 5, qx + 13, qy + 5], fill=INK)
    for dx, dy in ((-20, -10), (20, -10), (-20, 10), (20, 10)):
        d.line([qx, qy, qx + dx, qy + dy], fill=INK, width=3)
        d.ellipse([qx + dx - 6, qy + dy - 3, qx + dx + 6, qy + dy + 3], outline=INK, width=2)


def icon_iran(x0, y0, x1, y1):
    cx, base = x0 + 58, y1 - 14
    d.line([cx, base, cx, base - 40], fill=INK, width=6)                          # radar mast
    d.arc([cx - 46, base - 96, cx + 28, base - 22], 305, 125, fill=INK, width=6)  # dish
    d.line([cx - 8, base - 58, cx + 16, base - 66], fill=INK, width=4)            # feed arm
    d.ellipse([cx + 13, base - 69, cx + 21, base - 61], fill=RED)
    for r in (24, 40, 56):                                                        # signal rings
        d.arc([cx + 16, base - 66 - r // 2, cx + 16 + r, base - 66 + r // 2],
              305, 55, fill=GOLD, width=4)
    qx, qy = x1 - 80, y0 + 32                                                     # drone
    d.rectangle([qx - 16, qy - 6, qx + 16, qy + 6], fill=INK)
    for dx, dy in ((-24, -12), (24, -12), (-24, 12), (24, 12)):
        d.line([qx, qy, qx + dx, qy + dy], fill=INK, width=3)
        d.ellipse([qx + dx - 7, qy + dy - 3, qx + dx + 7, qy + dy + 3], outline=INK, width=2)
    # missile climbing to the right: body, nose cone, fins, flame
    bx, by = x0 + 168, y1 - 34                       # tail point
    ex, ey = bx + 74, by - 56                        # nose tip
    import math
    ux, uy = ex - bx, ey - by
    ln = math.hypot(ux, uy)
    ux, uy = ux / ln, uy / ln
    px_, py_ = -uy * 9, ux * 9                       # half-width perpendicular
    body = [(bx + px_, by + py_), (bx - px_, by - py_),
            (ex - ux * 20 - px_, ey - uy * 20 - py_), (ex - ux * 20 + px_, ey - uy * 20 + py_)]
    d.polygon(body, fill=RED)
    d.polygon([(ex - ux * 20 - px_, ey - uy * 20 - py_),
               (ex - ux * 20 + px_, ey - uy * 20 + py_), (ex, ey)], fill=(140, 40, 30))
    d.polygon([(bx + px_, by + py_), (bx - px_, by - py_),
               (bx - ux * 16, by - uy * 16)], fill=GOLD)                          # flame
    d.polygon([(bx + px_, by + py_), (bx + px_ * 2.2, by + py_ * 2.2),
               (bx - ux * 6 + px_, by - uy * 6 + py_)], fill=INK)                 # fin
    d.polygon([(bx - px_, by - py_), (bx - px_ * 2.2, by - py_ * 2.2),
               (bx - ux * 6 - px_, by - uy * 6 - py_)], fill=INK)                 # fin
    for t in range(3):                                                            # dashed path
        sx, sy = bx - 16 - t * 17, by + 12 + t * 4
        d.line([sx, sy, sx + 9, sy + 2], fill=GRAY, width=3)


def flag(x, y, kind):
    w_, h_ = 56, 38
    d.rectangle([x, y, x + w_, y + h_], outline=INK, width=2)
    if kind == "us":
        for i in range(5):
            if i % 2 == 0:
                d.rectangle([x, y + i * 8, x + w_, y + i * 8 + 4], fill=RED)
        d.rectangle([x, y, x + 24, y + 20], fill=BLUE)
        for r in range(3):
            for c in range(4):
                d.ellipse([x + 3 + c * 5, y + 3 + r * 6, x + 5 + c * 5, y + 5 + r * 6],
                          fill=(255, 255, 255))
    elif kind == "cn":
        d.rectangle([x, y, x + w_, y + h_], fill=RED)
        for sx, sy, r in ((10, 8, 4), (22, 5, 2), (25, 12, 2), (22, 19, 2), (17, 15, 2)):
            d.ellipse([x + sx - r, y + sy - r, x + sx + r, y + sy + r], fill=GOLD)
    else:  # ru
        d.rectangle([x, y, x + w_, y + 13], fill=(245, 245, 245))
        d.rectangle([x, y + 13, x + w_, y + 25], fill=BLUE)
        d.rectangle([x, y + 25, x + w_, y + h_], fill=RED)


def icon_trump(x0, y0, x1, y1):
    cy = y0 + 44
    d.polygon([(x0 + 40, cy), (x1 - 70, cy - 4), (x1 - 34, cy + 8),
               (x1 - 70, cy + 18), (x0 + 48, cy + 16)], fill=BLUE)      # fuselage
    d.polygon([(x0 + 130, cy + 12), (x0 + 178, cy + 44), (x0 + 206, cy + 44),
               (x0 + 190, cy + 12)], fill=INK)                          # wing
    d.polygon([(x0 + 44, cy - 2), (x0 + 62, cy - 26), (x0 + 82, cy - 24),
               (x0 + 78, cy)], fill=RED)                                # tail
    for i in range(6):
        d.ellipse([x0 + 96 + i * 26, cy + 2, x0 + 103 + i * 26, cy + 9],
                  fill=(255, 255, 255))
    fy = y1 - 52
    for fx, kind in ((x0 + 36, "us"), (x0 + 128, "cn"), (x0 + 220, "ru")):
        d.line([fx, fy + 44, fx, fy], fill=INK, width=3)
        flag(fx + 3, fy, kind)


def icon_nvidia(x0, y0, x1, y1):
    cx, cy, s = (x0 + x1) // 2 - 26, (y0 + y1) // 2, 96
    for i in range(4):  # pins
        p = cx - s // 2 + 14 + i * 24
        d.line([p, cy - s // 2 - 12, p, cy - s // 2], fill=INK, width=5)
        d.line([p, cy + s // 2, p, cy + s // 2 + 12], fill=INK, width=5)
        p2 = cy - s // 2 + 14 + i * 24
        d.line([cx - s // 2 - 12, p2, cx - s // 2, p2], fill=INK, width=5)
        d.line([cx + s // 2, p2, cx + s // 2 + 12, p2], fill=INK, width=5)
    d.rectangle([cx - s // 2, cy - s // 2, cx + s // 2, cy + s // 2], outline=INK, width=5)
    d.rectangle([cx - 26, cy - 26, cx + 26, cy + 26], outline=INK, width=4)
    pts = [(x0 + 168, y1 - 26), (x0 + 204, y1 - 48), (x0 + 232, y1 - 40),
           (x0 + 272, y1 - 84)]
    d.line(pts, fill=RED, width=6)
    ax, ay = pts[-1]
    d.polygon([(ax, ay), (ax - 18, ay + 2), (ax - 4, ay + 16)], fill=RED)


def icon_japan(x0, y0, x1, y1):
    d.rectangle([x0, y1 - 30, x1, y1], fill=STEEL)
    d.ellipse([x0 + 30, y1 - 44, x0 + 130, y1 - 18], fill=GREEN)       # islands
    d.ellipse([x0 + 170, y1 - 40, x0 + 238, y1 - 20], fill=GREEN)
    jx, jy = x0 + 66, y0 + 30                                          # fighter jet
    d.polygon([(jx, jy + 18), (jx + 44, jy), (jx + 120, jy + 12), (jx + 128, jy + 20),
               (jx + 118, jy + 27), (jx + 40, jy + 30), (jx + 8, jy + 34)], fill=INK)
    d.polygon([(jx + 30, jy + 24), (jx + 8, jy + 46), (jx + 26, jy + 46),
               (jx + 52, jy + 28)], fill=INK)
    d.polygon([(jx + 2, jy + 16), (jx - 12, jy + 2), (jx + 8, jy + 4)], fill=RED)
    for t in range(6):                                                 # dashed incursion arc
        sx, sy = x1 - 30 - t * 26, y0 + 12 + t * 9
        d.line([sx, sy, sx - 14, sy + 5], fill=RED, width=4)


def icon_measles(x0, y0, x1, y1):
    def virus(cx, cy, r, color):
        import math
        for k in range(10):
            a = k * math.pi / 5
            ex, ey = cx + (r + 13) * math.cos(a), cy + (r + 13) * math.sin(a)
            d.line([cx, cy, ex, ey], fill=color, width=5)
            d.ellipse([ex - 6, ey - 6, ex + 6, ey + 6], fill=color)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
        for dx, dy, rr in ((-12, -8, 7), (10, 6, 9), (2, -16, 5)):
            d.ellipse([cx + dx - rr, cy + dy - rr, cx + dx + rr, cy + dy + rr],
                      fill=(247, 241, 227))
    virus(x0 + 96, y0 + 66, 34, RED)
    virus(x0 + 196, y0 + 92, 22, (214, 110, 90))
    bx, by = x1 - 74, y1 - 66                                          # medical badge
    d.ellipse([bx, by, bx + 52, by + 52], fill=BLUE)
    d.rectangle([bx + 21, by + 10, bx + 31, by + 42], fill=(255, 255, 255))
    d.rectangle([bx + 10, by + 21, bx + 42, by + 31], fill=(255, 255, 255))


# ---------------- panels ----------------
PANELS = [
    ("WAR · EUROPE", icon_bridge, "CRIMEA BRIDGE HIT AGAIN",
     "Ukrainian drones knock a span of Russia's Kerch Bridge into the strait."),
    ("CONFLICT · THE GULF", icon_iran, "US & IRAN TRADE FIRE",
     "Iranian drones strike a US radar in Bahrain; US jets hit back on Qeshm Island."),
    ("DIPLOMACY · ASIA", icon_trump, "TRUMP LANDS IN ASIA",
     "Trump flies to Shenzhen for APEC talks with Xi and Putin on nukes and Ukraine."),
    ("TECH · BUSINESS", icon_nvidia, "NVIDIA'S $115BN DAY",
     "Record revenue tops $115bn, but the board won't reinstate ousted CEO Jensen Huang."),
    ("SECURITY · ASIA", icon_japan, "JAPAN SCRAMBLES JETS",
     "Tokyo protests after two Russian aircraft violate its airspace early Tuesday."),
    ("HEALTH · AMERICAS", icon_measles, "MEASLES-FREE NO MORE",
     "Record cases end 26 years of US elimination: 5,400+ cases, 10 deaths in 2026."),
]

PW, PH, GAP = 314, 336, 14
GX, GY = M, 222
for i, (tag, icon, head, cap) in enumerate(PANELS):
    px = GX + (i % 3) * (PW + GAP)
    py = GY + (i // 3) * (PH + GAP)
    d.rectangle([px, py, px + PW, py + PH], fill=PANEL, outline=INK, width=3)
    d.text((px + 14, py + 10), tag, font=font(FB, 16), fill=RED)
    d.rectangle([px + 14, py + 36, px + PW - 14, py + 38], fill=INK)
    d.rectangle([px + 10, py + 46, px + PW - 10, py + 180], fill=TINT)
    icon(px + 10, py + 46, px + PW - 10, py + 180)
    # headline: shrink from 30px until it wraps to at most two lines
    hsize = 30
    while hsize > 22 and len(wrap(d, head, font(FB, hsize), PW - 28)) > 2:
        hsize -= 1
    hy = py + 190
    for line in wrap(d, head, font(FB, hsize), PW - 28):
        d.text((px + 14, hy), line, font=font(FB, hsize), fill=INK)
        hy += hsize + 5
    cy = max(py + 264, hy + 4)
    for line in wrap(d, cap, font(FR, 18), PW - 28):
        d.text((px + 14, cy), line, font=font(FR, 18), fill=DARKTXT)
        cy += 23

# ---------------- ticker ----------------
TY = 920
d.rectangle([M, TY, W - M, 998], fill=INK)
t1 = "ALSO TUESDAY — EBOLA IN DR CONGO PASSES 11,000 CASES · RUSSIAN PLANE CRASH KILLS 19"
t2 = "NEPAL FIRST FOR UN CLIMATE FUNDS · BELGIUM ROUT ITALY 4–1 · FIVE EU STATES PLAN RWANDA HUB"
for j, t in enumerate((t1, t2)):
    f = fit(d, t, W - 2 * M - 24, 21)
    d.text(((W - tw(d, t, f)) / 2, TY + 12 + j * 38), t, font=f, fill=(250, 246, 235))

img.save("/home/hatch/workspace/makefun/news-image-repo/entry.png")
print("saved entry.png", img.size)
