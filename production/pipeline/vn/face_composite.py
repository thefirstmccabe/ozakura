#!/usr/bin/env python3
"""Paste only the face of an expression edit back onto its base CG, through a feathered ellipse,
so nothing else in the frame moves when the engine crossfades between the two (e.g. cg_natsuki_intro
-> cg_natsuki_intro_falter).

  face_composite.py BASE VARIANT OUT --center CX CY --radius RX RY [--feather PX]
  face_composite.py BASE VARIANT --diff          # print where the two images differ, to place the ellipse

Center and radius are fractions of the image width/height. The variant is resized to the base if needed.
"""
import argparse
import numpy as np
from PIL import Image, ImageDraw, ImageFilter


def load(base, var):
    b = Image.open(base).convert("RGB")
    v = Image.open(var).convert("RGB")
    if v.size != b.size:
        v = v.resize(b.size, Image.LANCZOS)
    return b, v


def diff_report(b, v, thresh=40):
    d = np.abs(np.asarray(b, np.int16) - np.asarray(v, np.int16)).max(axis=2)
    h, w = d.shape
    # coarse grid: share of strongly changed pixels per 1/20 cell
    gy, gx = 20, 20
    print("changed-pixel share per cell (rows top->bottom, %):")
    for r in range(gy):
        row = d[r * h // gy:(r + 1) * h // gy]
        cells = [int(100 * (row[:, c * w // gx:(c + 1) * w // gx] > thresh).mean()) for c in range(gx)]
        print(" ".join(f"{x:3d}" for x in cells))


def composite(b, v, cx, cy, rx, ry, feather):
    w, h = b.size
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).ellipse([(cx - rx) * w, (cy - ry) * h, (cx + rx) * w, (cy + ry) * h], fill=255)
    m = m.filter(ImageFilter.GaussianBlur(feather))
    return Image.composite(v, b, m)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("base"); ap.add_argument("variant"); ap.add_argument("out", nargs="?")
    ap.add_argument("--center", nargs=2, type=float); ap.add_argument("--radius", nargs=2, type=float)
    ap.add_argument("--feather", type=float, default=18)
    ap.add_argument("--diff", action="store_true")
    a = ap.parse_args()
    b, v = load(a.base, a.variant)
    if a.diff:
        diff_report(b, v)
    else:
        composite(b, v, *a.center, *a.radius, a.feather).save(a.out, quality=95)
        print("wrote", a.out)
