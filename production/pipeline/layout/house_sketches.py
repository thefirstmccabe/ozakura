"""Layout sketches for the two-houses backgrounds (style-guide §6 method).
Blocking shapes only; passed as image 1 (structure) to the edit model."""
from PIL import Image, ImageDraw
import sys, os
out = sys.argv[1] if len(sys.argv) > 1 else "."
W, H = 1920, 1080

def street():
    im = Image.new("RGB", (W, H), (235, 240, 245)); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 300], fill=(200, 220, 240))              # sky
    d.polygon([(0, 420), (500, 230), (1000, 200), (1500, 240), (W, 380), (W, 700), (0, 700)], fill=(120, 150, 110))  # wooded hill
    d.rectangle([0, 900, W, H], fill=(170, 170, 165))               # street
    d.rectangle([0, 840, W, 900], fill=(200, 200, 195))             # curb/front strip
    # left house (Kohei) and right house (Nanoha): walls ~1 m apart
    L = [150, 360, 900, 860]; R = [985, 360, 1760, 860]               # 85 px gap ~ 1 m at house scale (~8 m wide = 750 px)
    for (x0, y0, x1, y1), col in [(L, (215, 205, 190)), (R, (225, 215, 195))]:
        d.rectangle([x0, y0, x1, y1], fill=col, outline=(60, 60, 60), width=4)
        d.polygon([(x0 - 40, y0), ((x0 + x1) // 2, y0 - 150), (x1 + 40, y0)], fill=(90, 95, 105), outline=(40, 40, 40))  # roof
        d.rectangle([x0 - 30, 600, x1 + 30, 625], fill=(90, 95, 105))  # ground-floor eave
        d.rectangle([x0 + 90, 430, x0 + 300, 560], fill=(150, 180, 205), outline=(50, 50, 50), width=4)   # upstairs front window
        d.rectangle([x0 + 420, 700, x0 + 560, 860], fill=(120, 90, 60), outline=(40, 40, 40), width=4)    # door
        d.rectangle([x0 + 90, 680, x0 + 330, 800], fill=(150, 180, 205), outline=(50, 50, 50), width=4)   # downstairs window
    d.rectangle([900, 360, 985, 860], fill=(45, 45, 50))             # the narrow dark slit between walls (no path)
    d.rectangle([890, 780, 995, 860], fill=(110, 110, 110))          # low block wall closing the gap at the front
    return im

def across(lit=True, interior=False):
    """View from inside one bedroom, through its open window, straight across to the other house's window ~1 m away."""
    im = Image.new("RGB", (W, H), (25, 25, 35)); d = ImageDraw.Draw(im)
    # through-window area: the opposite wall fills it (1 m away)
    d.rectangle([260, 120, 1660, 880], fill=(70, 75, 95) if lit else (205, 200, 190))
    d.rectangle([260, 120, 1660, 190], fill=(20, 30, 70) if lit else (170, 205, 235))   # slit of sky above
    d.rectangle([260, 190, 1660, 230], fill=(50, 50, 55))                                 # opposite eave/gutter
    # opposite window, directly facing, close
    wx0, wy0, wx1, wy1 = 640, 330, 1280, 800
    if interior:
        d.rectangle([wx0, wy0, wx1, wy1], fill=(225, 215, 195), outline=(30, 30, 30), width=10)
        d.rectangle([wx0 + 40, wy0 + 260, wx0 + 300, wy1 - 10], fill=(150, 120, 90))   # desk
        d.rectangle([wx0 + 380, wy0 + 330, wx1 - 10, wy1 - 10], fill=(60, 70, 110))    # bed corner
    else:
        d.rectangle([wx0, wy0, wx1, wy1], fill=(255, 210, 120) if lit else (220, 225, 230), outline=(30, 30, 30), width=10)
        d.rectangle([wx0 + 10, wy0 + 10, wx0 + 120, wy1 - 10], fill=(240, 200, 200))   # curtain left
        d.rectangle([wx1 - 120, wy0 + 10, wx1 - 10, wy1 - 10], fill=(240, 200, 200))   # curtain right
    d.line([((wx0 + wx1) // 2, wy0), ((wx0 + wx1) // 2, wy1)], fill=(30, 30, 30), width=8)  # sliding sash
    d.rectangle([wx0 - 20, wy1, wx1 + 20, wy1 + 25], fill=(90, 90, 90))                  # opposite sill
    d.rectangle([260, 880, 1660, 900], fill=(10, 10, 12))                                 # dark gap far below
    # this room's own window frame, foreground
    d.rectangle([0, 0, W, 120], fill=(40, 38, 45)); d.rectangle([0, 900, W, H], fill=(60, 50, 45))  # wall above, sill/desk below
    d.rectangle([0, 0, 260, H], fill=(40, 38, 45)); d.rectangle([1660, 0, W, H], fill=(40, 38, 45))
    d.rectangle([250, 110, 1670, 910], outline=(15, 15, 15), width=22)                    # frame
    d.rectangle([250, 890, 1670, 940], fill=(95, 80, 70))                                 # own sill, foreground
    d.rectangle([1500, 100, 1650, 900], fill=(120, 120, 140))                             # own sash slid open
    return im

street().save(os.path.join(out, "sketch-houses-street.png"))
across(lit=True).save(os.path.join(out, "sketch-window-night.png"))
across(lit=False, interior=True).save(os.path.join(out, "sketch-window-day-reverse.png"))
