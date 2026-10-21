#!/usr/bin/env python3
"""Export a CG or background master (art/masters, 2752×1536) to the game sizes the v2 engine loads.

  export_cg.py MASTER NAME [--game v2]

Writes GAME/img/bg/NAME.webp (2400×1340, WebP q85, the settings the Ch1 images were shipped with) and the chapter-select
and save-slot thumbnail GAME/img/th/NAME.webp (480×268, q80). No script makes the thumbnails, so re-export after every
master change.
"""
import argparse, os
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("master"); ap.add_argument("name"); ap.add_argument("--game", default="v2")
a = ap.parse_args()
im = Image.open(a.master).convert("RGB")
big = im.resize((2400, 1340), Image.LANCZOS)
big.save(os.path.join(a.game, "img", "bg", a.name + ".webp"), quality=85)
big.resize((480, 268), Image.LANCZOS).save(os.path.join(a.game, "img", "th", a.name + ".webp"), quality=80)
print("wrote", os.path.join(a.game, "img", "bg", a.name + ".webp"), "and the thumbnail")
