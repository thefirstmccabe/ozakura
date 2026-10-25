"""Build a new outfit's sprite set for a character whose sprites already exist (Ch2: Natsuki in kendo gear).

1. Align: find the similarity (scale + shift) that puts the new outfit's face where the base master's face is
   (multi-scale template match on the face box), and warp the new cutout into the base master's frame.
2. Frame: crop it the way the existing sprites were cropped from the base master (found by template matching an
   existing sprite against the master), widened symmetrically if the new outfit is wider (a held shinai), so the
   head lands at the same size and the same horizontal center; scale to 1800 px tall like sprites.py.
3. Faces: paste each existing expression's face through a feathered ellipse (sprite space) onto the new sprite, so
   every expression is the approved face exactly (style guide §3: expressions differ only in the face).

Usage:
  python3 outfit_sprite.py --master BASE_MASTER.png --ref-sprite EXISTING_SPRITE.webp --cutout NEW_CUTOUT.png \
      --face-box cx,cy,w,h (master px) --oval cx,cy,rx,ry (sprite px, as for the existing set) --feather 10 \
      --out OUTDIR --name natsuki_kendo  EXISTING_EXPR_SPRITES...
Writes OUTDIR/NAME_base.webp (the new outfit with its own face) and OUTDIR/NAME_EXPR.webp per expression sprite
(EXPR = the last _part of each input name), plus OUTDIR/NAME_frame.json (the numbers, for the record).
--headroom F adds empty space above the frame, F times its height (Ch2's teach pose: a shinai held up past her head). The
sprite comes out (1+F) times as tall with the figure at the same scale, and v2/index.html's HEADROOM map must list it with F."""
import argparse, json, os
import cv2, numpy as np
from PIL import Image, ImageDraw, ImageFilter

ap = argparse.ArgumentParser()
ap.add_argument("--master"); ap.add_argument("--ref-sprite"); ap.add_argument("--cutout")
ap.add_argument("--face-box"); ap.add_argument("--oval"); ap.add_argument("--feather", type=float, default=10)
ap.add_argument("--headroom", type=float, default=0)
ap.add_argument("--align", help="s,tx,ty: skip the face search and use this alignment (from an earlier run's frame.json), "
                "so a second expression of the same new outfit lands on exactly the same pixels")
ap.add_argument("--out"); ap.add_argument("--name"); ap.add_argument("exprs", nargs="*")
a = ap.parse_args()
os.makedirs(a.out, exist_ok=True)
gray = lambda im: np.asarray(im.convert("L")).astype(np.float32)
def on_white(im):
    w = Image.new("RGBA", im.size, (255, 255, 255, 255)); w.alpha_composite(im.convert("RGBA")); return w

master = Image.open(a.master).convert("RGB"); MW, MH = master.size
cut = Image.open(a.cutout).convert("RGBA")
ref = Image.open(a.ref_sprite).convert("RGBA")

# 1. align the new outfit's face to the master's face
fx, fy, fw, fh = map(float, a.face_box.split(","))
tpl = gray(master)[int(fy - fh / 2):int(fy + fh / 2), int(fx - fw / 2):int(fx + fw / 2)]
k = gray(on_white(cut))
best = None
for s in np.arange(0.85, 1.15, 0.0025):
    ks = cv2.resize(k, (round(k.shape[1] * s), round(k.shape[0] * s)), interpolation=cv2.INTER_AREA)
    r = cv2.matchTemplate(ks, tpl, cv2.TM_CCOEFF_NORMED); _, mx, _, loc = cv2.minMaxLoc(r)
    if best is None or mx > best[0]: best = (mx, s, loc)
score, s, loc = best
tx, ty = (fx - fw / 2) - loc[0], (fy - fh / 2) - loc[1]
if a.align: s, tx, ty = map(float, a.align.split(","))
T = int(round(a.headroom * MH))                # extra rows above the master frame
L = MW // 2                                    # side margin, so a held shinai past the frame's edge survives the warp
arr = np.asarray(cut).astype(np.float32)
M = np.float32([[s, 0, tx + L], [0, s, ty + T]])
warped = cv2.warpAffine(arr, M, (MW + 2 * L, MH + T), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
warped = Image.fromarray(np.clip(warped, 0, 255).astype(np.uint8), "RGBA")

# 2. how the existing sprites were cropped from the master
rs = gray(on_white(ref)); rh, rw = rs.shape
sc = rh / MH                                   # sprites are the full master height scaled to 1800
mg = cv2.resize(gray(master), (round(MW * sc), round(MH * sc)), interpolation=cv2.INTER_AREA)
y0, y1, x0, x1 = int(rh * .08), int(rh * .25), int(rw * .28), int(rw * .72)   # face band of the sprite
r = cv2.matchTemplate(mg, rs[y0:y1, x0:x1], cv2.TM_CCOEFF_NORMED); _, rscore, _, rloc = cv2.minMaxLoc(r)
crop_x0 = (rloc[0] - x0) / sc                  # master x of the sprite's left edge
center = crop_x0 + rw / sc / 2
al = np.asarray(warped)[..., 3]; xs = np.where((al > 24).any(0))[0] - L   # master x
half = max(rw / sc / 2, center - xs.min() + 6, xs.max() - center + 6)
box = (center - half, -T, center + half, MH)
cx0 = int(round(box[0])) + L
canvas = warped.crop((cx0, 0, cx0 + int(np.ceil(2 * half)), MH + T))
dy = T * sc                                    # existing-sprite y -> new-sprite y
sprite = canvas.resize((round(canvas.width * sc), round((MH + T) * sc)), Image.LANCZOS)
dx = (crop_x0 - box[0]) * sc                   # existing-sprite x -> new-sprite x
sprite.save(os.path.join(a.out, f"{a.name}_base.webp"), "WEBP", quality=90, method=6)

# 3. faces
ocx, ocy, orx, ory = map(float, a.oval.split(","))
mask = Image.new("L", sprite.size, 0)
ImageDraw.Draw(mask).ellipse((ocx + dx - orx, ocy + dy - ory, ocx + dx + orx, ocy + dy + ory), fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(a.feather))
for f in a.exprs:
    ex = Image.open(f).convert("RGBA")
    layer = Image.new("RGBA", sprite.size, (0, 0, 0, 0)); layer.alpha_composite(ex, (int(round(dx)), int(round(dy))))
    out = Image.composite(layer, sprite, mask)
    # keep the new outfit's alpha outside the face, the face's alpha inside
    oa = np.asarray(sprite)[..., 3].astype(float); la = np.asarray(layer)[..., 3].astype(float); m = np.asarray(mask).astype(float) / 255
    o = np.asarray(out).copy(); o[..., 3] = np.clip(oa * (1 - m) + la * m, 0, 255).astype(np.uint8)
    expr = os.path.basename(f).rsplit(".", 1)[0].split("_")[-1]
    Image.fromarray(o, "RGBA").save(os.path.join(a.out, f"{a.name}_{expr}.webp"), "WEBP", quality=90, method=6)
info = {"align_score": round(float(score), 3), "scale": round(float(s), 4), "shift": [round(float(tx), 1), round(float(ty), 1)],
        "ref_match": round(float(rscore), 3), "ref_crop_x0_master": round(float(crop_x0), 1), "new_box_master": [round(float(v), 1) for v in box],
        "sprite_size": sprite.size, "face_dx_sprite": round(float(dx), 1), "headroom": a.headroom, "face_dy_sprite": round(float(dy), 1)}
json.dump(info, open(os.path.join(a.out, f"{a.name}_frame.json"), "w"), indent=1)
print(json.dumps(info))
