"""Letter Natsuki's whiteboard (cg_whiteboard, Ch2 c2_0325) in code: the image model garbles text, so the art is
wordless (seed 612) and the labels are drawn here in a marker hand (Kalam), multiplied onto the board.

Usage (from the repo root):
  python3 production/pilot-v2/art/ch2/whiteboard_letter.py RAW_612.png OUT_MASTER.png
"""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

FONT = "production/pipeline/manga/fonts/Kalam-Bold.ttf"
INK = (30, 32, 44)       # black marker
RED = (196, 38, 44)      # the red marker of her circles

# (text, size, colour, anchor point in 2752x1536 pixels, anchor, rotation in degrees)
LABELS = [
    ("KENDO", 92, INK, (1030, 300), "ls", -3),
    ("lesson 1", 62, INK, (1052, 370), "ls", -3),
    ("MEN", 84, INK, (1838, 262), "ls", -4),
    ("head", 58, RED, (1844, 326), "ls", -4),
    ("TSUKI", 80, INK, (1772, 700), "ls", -2),
    ("throat", 56, RED, (1780, 756), "ls", -2),
    ("not until high school!!", 40, RED, (1782, 802), "ls", -2),
    ("DŌ", 84, INK, (1792, 912), "ls", -3),
    ("side", 56, RED, (1798, 972), "ls", -3),
    ("KOTE", 80, INK, (1282, 512), "rs", -4),
    ("wrist (right one!)", 50, RED, (1288, 564), "rs", -4),
]


def stamp(base, text, size, colour, at, anchor, rot):
    font = ImageFont.truetype(FONT, size)
    pad = size * 2
    w = int(font.getlength(text)) + 2 * pad
    h = size * 2 + 2 * pad
    layer = Image.new("L", (w, h), 0)
    ax = pad if anchor[0] == "l" else w - pad
    ImageDraw.Draw(layer).text((ax, pad + size * 1.4), text, font=font, fill=255, anchor=anchor)
    layer = layer.rotate(rot, resample=Image.BICUBIC, center=(ax, pad + size * 1.4))
    layer = layer.filter(ImageFilter.GaussianBlur(0.9))          # marker edge, matched to the drawn lines
    ink = Image.new("RGB", base.size, (255, 255, 255))
    mask = Image.new("L", base.size, 0)
    ox, oy = int(at[0] - ax), int(at[1] - (pad + size * 1.4))
    mask.paste(layer, (ox, oy))
    ink.paste(Image.new("RGB", base.size, colour), (0, 0), mask.point(lambda v: int(v * 0.93)))
    return ImageChops.multiply(base, ink)


def main(src, out):
    im = Image.open(src).convert("RGB")
    for lab in LABELS:
        im = stamp(im, *lab)
    im.save(out)


if __name__ == "__main__":
    main(*sys.argv[1:3])
