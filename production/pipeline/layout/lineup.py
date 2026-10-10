"""Cast scale lineups (style guide §1b). Imperial units only (author's rule, Oct 10).
Each figure is masked from its white/cream background, its head top found in the
central band of its bounding box (ignores raised hands and props), scaled so
feet-to-head equals its height, and pasted bottom-aligned on a 6-inch grid.
Run from the repo root: python3 production/pipeline/layout/lineup.py"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np

R = "production/refs/"
I = R + "inventory/"
PX = 8.0           # pixels per inch
TOP_IN = 84        # grid goes to 7 ft
MARGIN = 60

def fmt(inches):
    return f"{inches // 12}′{inches % 12}″"

ROW1 = [("Kōhei", I+"full-kohei.png", 69), ("Nanoha", I+"full-nanoha.png", 59),
        ("Natsuki", R+"natsuki-v2/01-restyle-uniform.png", 63), ("Akane", I+"full-akane.png", 60),
        ("Ryōsuke", I+"full-ryosuke.png", 67), ("Rika", I+"full-rika.png", 61),
        ("Takatsuki", I+"full-takatsuki.png", 68), ("Kirishima", I+"full-kirishima.png", 71),
        ("Yuzu", I+"full-yuzu.png", 61), ("Ōno", I+"full-ono.png", 72),
        ("Adviser", I+"adviser.png", 66), ("Manager", I+"full-manager.png", 65)]
ROW2 = [("Kazuo", I+"kazuo-B.png", 72), ("Emi", I+"full-emi.png", 62), ("Sōta", I+"full-sota.png", 48),
        ("Genji", I+"genji.png", 62), ("Mom", I+"kohei-mom-recover.png", 62), ("Dad", I+"kohei-dad-healthy.png", 68),
        ("Rōnin (past)", I+"ronin-B.png", 69), ("Natsuki (past)", I+"past-natsuki-A.png", 62),
        ("Her father", I+"past-father.png", 65), ("Thug", I+"thug.png", 70), ("Opponent", I+"opponent.png", 68),
        ("Beast", ("beast", I+"beast-size-reference-v2.png"), 51)]

def cutout(path):
    beast = isinstance(path, tuple)
    im = Image.open(path[1] if beast else path).convert("RGB")
    if beast:  # right half of the size reference holds the beast
        im = im.crop((560, 0, im.width, im.height))
    a = np.asarray(im).astype(int)
    bg = np.median(np.concatenate([a[:8].reshape(-1, 3), a[-8:].reshape(-1, 3), a[:, :8].reshape(-1, 3), a[:, -8:].reshape(-1, 3)]), axis=0)
    m = np.abs(a - bg).sum(2) > 45
    ys, xs = np.where(m)
    x0, x1, y1 = xs.min(), xs.max(), ys.max()
    if beast:
        top = ys.min()
    else:
        c0, c1 = x0 + int(0.35 * (x1 - x0)), x0 + int(0.65 * (x1 - x0))
        top = np.where(m[:, c0:c1].any(1))[0].min()
    alpha = Image.fromarray((np.clip((np.abs(a - bg).sum(2) - 20) / 60, 0, 1) * 255).astype("uint8"))
    rgba = im.copy(); rgba.putalpha(alpha)
    return rgba.crop((x0, top if beast else ys.min(), x1 + 1, y1 + 1)), (top - (top if beast else ys.min()))

def row(items, out, note=""):
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
    small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    figs = []
    for name, path, h in items:
        im, off = cutout(path)
        s = (h * PX) / (im.height - off)
        figs.append((name, h, im.resize((max(1, int(im.width * s)), int(im.height * s)), Image.LANCZOS)))
    meas = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    slot = [max(f[2].width, int(meas.textlength(f[0], font=font))) for f in figs]
    W = MARGIN * 2 + sum(slot) + 30 * (len(figs) - 1)
    base = int(TOP_IN * PX) + 40
    H = base + 90
    can = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(can)
    for inch in range(0, TOP_IN + 1, 6):
        y = base - int(inch * PX)
        d.line([(MARGIN - 10, y), (W, y)], fill=(205, 205, 215) if inch % 12 == 0 else (232, 232, 238), width=2 if inch % 12 == 0 else 1)
        if inch % 12 == 0:
            d.text((6, y - 12), f"{inch // 12} ft", fill=(120, 120, 130), font=small)
    x = MARGIN
    for (name, h, im), sw in zip(figs, slot):
        can.paste(im, (x, base - im.height), im)
        d.text((x, base + 10), name, fill=(20, 20, 20), font=font)
        d.text((x, base + 44), fmt(h) + (" to the ears" if name == "Beast" else ""), fill=(90, 90, 90), font=small)
        x += sw + 30
    can.save(out); return can

if __name__ == "__main__":
    row(ROW1, R + "lineup/lineup-1-school.png")
    row(ROW2, R + "lineup/lineup-2-family-past.png")
