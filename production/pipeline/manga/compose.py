"""Ōzakura manga page compositor (rebuilt Oct 12).

Usage: python3 compose.py <spec.json> <panel_dir> <out_dir> [--suffix _bw]

The spec defines pages -> panels (pixel boxes on a 1600x2272 B6 page master) and the
lettering for each panel in panel-relative coordinates (0..1). Panel art is cover-cropped
into its box (with an optional focus point). Lettering is drawn by code so it stays
editable. The same spec renders color and B&W variants by switching the panel suffix.
"""
import json, math, os, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FD = os.path.join(HERE, 'fonts')
PW, PH = 1600, 2272
BORDER = 5
SS = 2  # supersample for lettering shapes


def font(name, size):
    return ImageFont.truetype(os.path.join(FD, name), int(size))


F_SAY, F_NAR, F_SFX = 'Kalam-Bold.ttf', 'Kalam-Regular.ttf', 'DelaGothicOne-Regular.ttf'


def cover(img, w, h, fx=0.5, fy=0.5):
    """Scale to cover w x h, crop around focus point (fx, fy)."""
    s = max(w / img.width, h / img.height)
    im = img.resize((math.ceil(img.width * s), math.ceil(img.height * s)), Image.LANCZOS)
    x = int(min(max(fx * im.width - w / 2, 0), im.width - w))
    y = int(min(max(fy * im.height - h / 2, 0), im.height - h))
    return im.crop((x, y, x + w, y + h))


def wrap(text, f, maxw, d):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=f) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(d, lines, f, lh):
    ws = [d.textlength(l, font=f) for l in lines]
    return max(ws), lh * len(lines)


def draw_lines(d, cx, cy, lines, f, lh, fill='black'):
    top = cy - lh * len(lines) / 2
    for i, l in enumerate(lines):
        w = d.textlength(l, font=f)
        d.text((cx - w / 2, top + i * lh), l, font=f, fill=fill)


def balloon(layer, cx, cy, text, tail=None, kind='say', size=38, maxw=360):
    """Draw a speech balloon centered at (cx, cy) in page px. kind: say | shout."""
    d = ImageDraw.Draw(layer)
    f = font(F_SAY, size * SS)
    lh = size * SS * 1.12
    lines = wrap(text, f, maxw * SS, d)
    tw, th = text_block(d, lines, f, lh)
    rx, ry = tw / 2 + 34 * SS, th / 2 + 26 * SS
    X, Y = cx * SS, cy * SS
    if tail:
        tx, ty = tail[0] * SS, tail[1] * SS
        ang = math.atan2(ty - Y, tx - X)
        bx, by = X + rx * 0.7 * math.cos(ang), Y + ry * 0.7 * math.sin(ang)
        perp = ang + math.pi / 2
        wv = 18 * SS
        pts = [(bx + wv * math.cos(perp), by + wv * math.sin(perp)), (tx, ty),
               (bx - wv * math.cos(perp), by - wv * math.sin(perp))]
        d.polygon(pts, fill='white', outline='black', width=4 * SS)
    if kind == 'shout':
        pts, n = [], 22
        for i in range(n * 2):
            a = math.pi * i / n
            r = 1.0 if i % 2 == 0 else 0.84
            pts.append((X + rx * 1.12 * r * math.cos(a), Y + ry * 1.18 * r * math.sin(a)))
        d.polygon(pts, fill='white', outline='black', width=4 * SS)
    else:
        d.ellipse((X - rx, Y - ry, X + rx, Y + ry), fill='white', outline='black', width=4 * SS)
    if tail:  # cover the tail seam inside the balloon
        d.ellipse((X - rx + 5 * SS, Y - ry + 5 * SS, X + rx - 5 * SS, Y + ry - 5 * SS), fill='white') if kind == 'say' else None
    draw_lines(d, X, Y, lines, f, lh)


def narration(layer, cx, cy, text, size=32, maxw=400):
    d = ImageDraw.Draw(layer)
    f = font(F_NAR, size * SS)
    lh = size * SS * 1.15
    lines = wrap(text, f, maxw * SS, d)
    tw, th = text_block(d, lines, f, lh)
    X, Y = cx * SS, cy * SS
    pad = 18 * SS
    d.rectangle((X - tw / 2 - pad, Y - th / 2 - pad * 0.8, X + tw / 2 + pad, Y + th / 2 + pad * 0.8),
                fill='white', outline='black', width=3 * SS)
    draw_lines(d, X, Y, lines, f, lh)


def sfx(page, cx, cy, text, size=120, angle=-8, fill='white'):
    """Display SFX centered on (cx, cy), stroked, rotated."""
    f = font(F_SFX, size)
    sw = max(6, size // 12)
    l, t, r, b = ImageDraw.Draw(page).textbbox((0, 0), text, font=f, stroke_width=sw)
    tmp = Image.new('RGBA', (r - l + 20, b - t + 20), (0, 0, 0, 0))
    ImageDraw.Draw(tmp).text((10 - l, 10 - t), text, font=f, fill=fill, stroke_width=sw, stroke_fill='black')
    tmp = tmp.rotate(angle, expand=True, resample=Image.BICUBIC)
    page.alpha_composite(tmp, (int(cx - tmp.width / 2), int(cy - tmp.height / 2)))


def render(spec, panel_dir, out_dir, suffix=''):
    os.makedirs(out_dir, exist_ok=True)
    outs = []
    for pg in spec['pages']:
        page = Image.new('RGBA', (PW, PH), 'white')
        # art + borders
        for p in pg['panels']:
            x0, y0, x1, y1 = p['box']
            src = os.path.join(panel_dir, p['id'] + suffix + '.jpg')
            art = cover(Image.open(src).convert('RGB'), x1 - x0, y1 - y0, *p.get('focus', (0.5, 0.5)))
            page.paste(art, (x0, y0))
            ImageDraw.Draw(page).rectangle((x0, y0, x1 - 1, y1 - 1), outline='black', width=BORDER)
        # lettering on a supersampled layer, clipped per panel
        for p in pg['panels']:
            x0, y0, x1, y1 = p['box']
            w, h = x1 - x0, y1 - y0
            layer = Image.new('RGBA', (PW * SS, PH * SS), (0, 0, 0, 0))
            for L in p.get('letters', []):
                cx, cy = x0 + L['at'][0] * w, y0 + L['at'][1] * h
                tail = None
                if 'tail' in L:
                    tail = (x0 + L['tail'][0] * w, y0 + L['tail'][1] * h)
                if L['t'] in ('say', 'shout'):
                    balloon(layer, cx, cy, L['text'], tail, L['t'], L.get('size', 38), L.get('maxw', 360))
                elif L['t'] == 'nar':
                    narration(layer, cx, cy, L['text'], L.get('size', 32), L.get('maxw', 400))
            layer = layer.resize((PW, PH), Image.LANCZOS)
            mask = Image.new('L', (PW, PH), 0)
            ImageDraw.Draw(mask).rectangle((x0, y0, x1, y1), fill=255)
            clipped = Image.new('RGBA', (PW, PH), (0, 0, 0, 0))
            clipped.paste(layer, (0, 0), Image.composite(layer.split()[3], Image.new('L', (PW, PH), 0), mask))
            page.alpha_composite(clipped)
            for L in p.get('letters', []):
                if L['t'] == 'sfx':
                    sfx(page, x0 + L['at'][0] * w, y0 + L['at'][1] * h, L['text'], L.get('size', 120), L.get('angle', -8))
        out = os.path.join(out_dir, f"page{pg['n']}{suffix}.png")
        page.convert('RGB').save(out)
        outs.append(out)
    return outs


if __name__ == '__main__':
    spec = json.load(open(sys.argv[1]))
    suffix = sys.argv[5] if len(sys.argv) > 5 and sys.argv[4] == '--suffix' else ''
    print(render(spec, sys.argv[2], sys.argv[3], suffix))
