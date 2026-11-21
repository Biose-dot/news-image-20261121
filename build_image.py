#!/usr/bin/env python3
"""Build the news-image-20261121 entry: a one-page newspaper front page
summing up Saturday 21 November 2026 world news. Deterministic, no
network. Everything is drawn with PIL shapes and DejaVu fonts; the output
is a 1024x1024 PNG under 1 MiB.

Stories (all reported 21 Nov 2026, cross-checked across several outlets):
  1. Peru - M6.8 earthquake strikes Junin, felt in Lima.
  2. Poland - Russian missiles land in Poland; NATO calls it a grave
     violation of its airspace.
  3. Wall Street - S&P 500 slides ~3.7% into correction as AI shares sell off.
  4. New York - Mayor Mamdani unveils plan to close Rikers Island by 2032.
  5. The Hague - World Court: Myanmar committed genocide against the
     Rohingya; Myanmar calls the ruling unfair.
  Also today: Cyclone Akvan crosses the Odisha coast; KL Rahul completes
  Test centuries in all four SENA countries; Nepal PM Balendra Shah heads
  to Delhi on his first foreign visit; record foreign inflows into
  Indian shares (Rs 1.22 lakh crore in November).
"""
import math

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 230)
CARD = (255, 255, 255)
INK = (24, 24, 24)
GREY = (96, 92, 84)
NAVY = (18, 38, 68)
RED = (178, 34, 22)
TEAL = (14, 110, 110)
GOLD = (168, 132, 46)
RULE = (196, 188, 170)
SKY = (205, 226, 240)
EARTH = (122, 84, 52)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, font, max_w):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(d, text, font, x, y, max_w, leading, fill=INK):
    for line in wrap(d, text, font, max_w):
        d.text((x, y), line, font=font, fill=fill)
        y += leading
    return y


def headline(d, text, font, x, y, max_w, leading, fill=INK):
    return para(d, text, font, x, y, max_w, leading, fill)


def kicker(d, text, x, y, color=RED):
    f = F(SANS_B, 17)
    d.text((x, y), text.upper(), font=f, fill=color)
    return y + 24


def tile(w, h, bg, fn):
    img = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(img)
    fn(d, w, h)
    return img


def crack(d, w, h):
    """Jagged ground crack for the earthquake art."""
    d.rectangle([0, 0, w, h], fill=(58, 44, 34))
    d.rectangle([0, 0, w, int(h * 0.42)], fill=(214, 196, 158))
    d.rectangle([0, int(h * 0.42), w, int(h * 0.46)], fill=(150, 122, 82))
    pts = [(0, int(h * 0.46))]
    x, y = 0, int(h * 0.46)
    while x < w:
        x += w // 9
        y += 26 if (x // (w // 9)) % 2 else -18
        pts.append((min(x, w), max(int(h * 0.44), min(int(h * 0.92), y))))
    pts.append((w, h))
    pts.append((0, h))
    d.polygon(pts, fill=(38, 28, 20))
    # shaking buildings
    for bx, bw, bh, tilt in [(18, 34, 44, -4), (66, 28, 34, 3), (108, 40, 52, -3),
                             (162, 30, 38, 4), (206, 36, 48, -3),
                             (256, 30, 36, 3), (300, 34, 46, -4)]:
        top = int(h * 0.42) - bh
        d.polygon([(bx, int(h * 0.42)), (bx + tilt, top),
                   (bx + bw + tilt, top), (bx + bw, int(h * 0.42))],
                  fill=(84, 78, 66))
    # seismograph trace across the sky band
    xs = list(range(0, w + 1, 6))
    ys = []
    for i, xx in enumerate(xs):
        amp = 2 if i < 8 else (26 if 14 <= i <= 24 else 4)
        ys.append(int(h * 0.20) + int(amp * math.sin(i * 1.7)))
    d.line(list(zip(xs, ys)), fill=RED, width=4)


def rocket(d, w, h):
    """Missile streaking over a map pin, for the Poland story."""
    d.rectangle([0, 0, w, h], fill=NAVY)
    for i in range(26):
        sx = (i * 53) % w
        sy = (i * 37) % h
        d.ellipse([sx, sy, sx + 2, sy + 2], fill=(140, 160, 190))
    # missile body
    d.polygon([(70, 62), (190, 32), (280, 50), (190, 82)], fill=(220, 224, 230))
    d.polygon([(280, 50), (312, 42), (306, 62), (280, 50)], fill=RED)
    d.line([(70, 62), (26, 78)], fill=(255, 180, 60), width=5)
    d.line([(70, 62), (34, 44)], fill=(255, 210, 120), width=3)
    # target pin
    d.ellipse([356, 44, 396, 84], fill=RED)
    d.polygon([(366, 76), (386, 76), (376, 100)], fill=RED)
    d.ellipse([366, 54, 386, 74], fill=(255, 255, 255))
    d.text((14, 10), "NATO", font=F(SANS_B, 30), fill=(255, 255, 255))
    d.text((14, 44), "AIRSPACE", font=F(SANS_B, 16), fill=(150, 170, 200))


def chart_fall(d, w, h):
    """Plunging market chart."""
    d.rectangle([0, 0, w, h], fill=(238, 240, 236))
    d.line([(24, 24), (24, h - 24), (w - 16, h - 24)], fill=GREY, width=2)
    pts = [(30, 28), (95, 34), (160, 32), (225, 44), (300, 58), (390, 72)]
    d.line(pts, fill=RED, width=6)
    for x, y in pts:
        d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=RED)
    d.polygon([(390, 72), (406, 76), (392, 80)], fill=RED)
    d.text((w - 118, 10), "-3.7%", font=F(SANS_B, 30), fill=RED)
    d.text((30, 6), "S&P 500", font=F(SANS_B, 16), fill=INK)


def jail_bars(d, w, h):
    """Jail bars with an open gate, for the Rikers story."""
    d.rectangle([0, 0, w, h], fill=(226, 222, 210))
    for i in range(7):
        x = 16 + i * 34
        d.rectangle([x, 0, x + 12, h], fill=(60, 60, 60))
    # one bar swung open
    d.polygon([(16 + 3 * 34, 0), (16 + 3 * 34 + 60, 30),
               (16 + 3 * 34 + 60, h), (16 + 3 * 34, h)], fill=(120, 120, 120))
    d.rectangle([0, 0, w, 10], fill=NAVY)


def scales(d, w, h):
    """Scales of justice for the ICJ ruling."""
    d.rectangle([0, 0, w, h], fill=(232, 228, 214))
    cx = w // 2
    d.rectangle([cx - 4, 26, cx + 4, h - 30], fill=GOLD)
    d.rectangle([cx - 34, 18, cx + 34, 26], fill=GOLD)
    d.polygon([(cx - 10, h - 30), (cx + 10, h - 30), (cx + 26, h - 12),
               (cx - 26, h - 12)], fill=GOLD)
    for side in (-1, 1):
        px = cx + side * 78
        d.line([(cx, 26), (px, 62)], fill=GOLD, width=3)
        d.polygon([(px - 42, 62), (px + 42, 62), (px, 96)], fill=(150, 110, 60))
        d.ellipse([px - 42, 58, px + 42, 70], fill=(120, 88, 44))
    d.ellipse([cx - 12, 8, cx + 12, 30], fill=GOLD)
    d.text((14, 8), "ICJ", font=F(SANS_B, 30), fill=NAVY)


def story_card(d, x, y, w, h, art, kick, head, body):
    d.rectangle([x, y, x + w, y + h], fill=CARD, outline=RULE, width=2)
    d.rectangle([x, y, x + w, y + 4], fill=NAVY)
    aw, ah = w - 28, 104
    d.rectangle([x + 14, y + 12, x + 14 + aw, y + 12 + ah], outline=RULE, width=1)
    img = tile(aw, ah, CARD, art)
    d._image.paste(img, (x + 14, y + 12))
    ty = y + 12 + ah + 10
    ty = kicker(d, kick, x + 14, ty)
    headline(d, head, F(SERIF_B, 22), x + 14, ty, w - 28, 27)
    nlines = len(wrap(d, head, F(SERIF_B, 22), w - 28))
    by = ty + nlines * 27 + 4
    para(d, body, F(SANS, 15), x + 14, by, w - 28, 20)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    d.rectangle([0, 0, W, 100], fill=NAVY)
    d.text((32, 10), "THE WORLD TODAY", font=F(SERIF_B, 52), fill=(255, 255, 255))
    d.text((32, 70), "SATURDAY 21 NOVEMBER 2026  •  ONE DAY, ONE PAGE",
           font=F(SANS_B, 18), fill=(196, 208, 224))
    d.text((W - 32 - d.textlength("No. 325", font=F(SANS_B, 18)), 70),
           "No. 325", font=F(SANS_B, 18), fill=(196, 208, 224))

    # ---- Lead story: Peru earthquake ----
    lx, ly, lw, lh = 32, 116, 960, 234
    d.rectangle([lx, ly, lx + lw, ly + lh], fill=CARD, outline=RULE, width=2)
    d.rectangle([lx, ly, lx + lw, ly + 4], fill=RED)
    art = tile(400, 202, CARD, crack)
    d._image.paste(art, (lx + 16, ly + 16))
    tx = lx + 436
    ty = ly + 18
    ty = kicker(d, "Peru  •  Earthquake", tx, ty)
    nhead = len(wrap(d, "M6.8 quake shakes Peru", F(SERIF_B, 34), lw - 452))
    headline(d, "M6.8 quake shakes Peru",
             F(SERIF_B, 34), tx, ty, lw - 452, 40)
    ty += nhead * 40 + 8
    para(d, "A magnitude 6.8 earthquake struck the Andean region of "
            "Junin in central Peru on Friday, Peru's Geophysical "
            "Institute said. Tremors were felt in the capital, Lima, "
            "around 320 km away.",
         F(SANS, 19), tx, ty, lw - 452, 26)

    # ---- Four story cards ----
    cy, ch = 362, 268
    cw = 468
    story_card(d, 32, cy, cw, ch, rocket,
               "Poland  •  NATO",
               "Russian missiles hit Poland",
               "Two Russian missiles and a suspected drone came down "
               "in Poland. Warsaw called it a deliberate provocation; "
               "NATO called it a grave violation of its airspace.")
    story_card(d, 524, cy, cw, ch, chart_fall,
               "Markets  •  Wall Street",
               "Stocks slide into correction",
               "US stocks fell about 3.7% on Friday as a sell-off in "
               "AI and chip shares pushed the S&P 500 into correction "
               "territory; Nvidia led the rout.")
    story_card(d, 32, cy + ch + 10, cw, ch, jail_bars,
               "New York  •  Rikers Island",
               "Mamdani: Rikers to close by 2032",
               "Mayor Zohran Mamdani unveiled the city's first "
               "comprehensive plan to close the Rikers Island jail "
               "complex by 2032, replacing it with four borough jails.")
    story_card(d, 524, cy + ch + 10, cw, ch, scales,
               "The Hague  •  World Court",
               "Myanmar committed genocide",
               "The International Court of Justice ruled Myanmar's "
               "security forces committed genocide against the "
               "Rohingya in 2017. Myanmar called the ruling unfair.")

    # ---- Also today strip ----
    ay = cy + 2 * ch + 22
    d.rectangle([32, ay, 992, ay + 86], fill=NAVY)
    d.text((52, ay + 8), "ALSO TODAY", font=F(SANS_B, 17), fill=(255, 205, 80))
    items = [
        "Cyclone Akvan crosses the Odisha coast near Gopalpur.",
        "KL Rahul completes Test 100s in all SENA countries.",
        "Nepal PM Shah heads to Delhi on first foreign visit.",
        "Record foreign inflows into Indian shares in November.",
    ]
    yy = ay + 34
    for row in range(2):
        d.text((52, yy), "•  " + items[row * 2], font=F(SANS, 15),
               fill=(235, 238, 242))
        d.text((512, yy), "•  " + items[row * 2 + 1], font=F(SANS, 15),
               fill=(235, 238, 242))
        yy += 22

    img.save("entry.png", optimize=True)


if __name__ == "__main__":
    main()
