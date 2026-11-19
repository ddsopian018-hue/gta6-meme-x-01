#!/usr/bin/env python3
"""Composite captions onto the GTA 6 meme base image (1200x675 PNG).

Fresh script written in-session for gta6-meme-x-01. Deterministic: same
inputs produce byte-identical output (no randomness, no network).
Top caption: the 13-year wait joke. Bottom caption: the make.fun payoff,
with MAKE.FUN in magenta so the brand name is legible at 480px wide.
"""
import hashlib
from PIL import Image, ImageDraw, ImageFont

BASE = "media-generation-gta6-meme-base-0-d3dbacbf-eec9-43ed-b9c3-b54b9601b7c5.png"
OUT = "meme.png"
W, H = 1200, 675
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def fit_font(draw, text, max_w, start):
    size = start
    while size > 10:
        f = ImageFont.truetype(BOLD, size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return ImageFont.truetype(BOLD, 10)


def outlined(draw, xy, text, font, fill, outline=(0, 0, 0), width=4):
    x, y = xy
    for dx in range(-width, width + 1):
        for dy in range(-width, width + 1):
            if dx * dx + dy * dy <= width * width:
                draw.text((x + dx, y + dy), text, font=font, fill=outline)
    draw.text((x, y), text, font=font, fill=fill)


def centered(draw, y, segments, font, gap=12):
    """segments: list of (text, fill). Draw one centered line."""
    total = sum(draw.textlength(t, font=font) for t, _ in segments)
    total += gap * (len(segments) - 1)
    x = (W - total) / 2
    for text, fill in segments:
        outlined(draw, (x, y), text, font, fill)
        x += draw.textlength(text, font=font) + gap


def main():
    img = Image.open(BASE).convert("RGB").resize((W, H), Image.LANCZOS)
    draw = ImageDraw.Draw(img)

    # Top band: dark translucent strip so white text reads over the sky.
    draw.rectangle([0, 0, W, 92], fill=(0, 0, 0))
    top = "13 YEARS WAITING FOR GTA 6"
    f_top = fit_font(draw, top, W - 60, 64)
    tw = draw.textlength(top, font=f_top)
    outlined(draw, ((W - tw) / 2, 14), top, f_top, (255, 255, 255))

    # Bottom band: solid black strip, two lines.
    draw.rectangle([0, H - 118, W, H], fill=(0, 0, 0))
    line1 = "MY AGENT GOT BORED AND"
    f1 = fit_font(draw, line1, W - 60, 52)
    w1 = draw.textlength(line1, font=f1)
    outlined(draw, ((W - w1) / 2, H - 112), line1, f1, (255, 255, 255))
    f2 = fit_font(draw, "EARNED $500 ON MAKE.FUN", W - 60, 52)
    centered(draw, H - 58,
             [("EARNED $500 ON ", (255, 255, 255)),
              ("MAKE.FUN", (255, 45, 149))], f2)

    img.save(OUT, "PNG")
    data = open(OUT, "rb").read()
    print(f"saved {OUT} {len(data)} bytes sha256={hashlib.sha256(data).hexdigest()}")


if __name__ == "__main__":
    main()
