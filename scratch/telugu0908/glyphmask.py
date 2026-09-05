#!/usr/bin/env python3
"""
Rasterise individual font glyphs to comparable ink masks, and score two masks.

Why this exists
---------------
bmatch.py compares whole *clusters* through a browser, because the Unicode side needs real
HarfBuzz shaping. That is the right tool for confirming a finished table but a poor one for
*finding* slot identities: a cluster score mixes glyph shape with mark positioning, so a
correct glyph in a slightly wrong position scores like a wrong glyph.

This module compares single glyphs, addressed by name, with no shaping and no browser. It
is what makes the Noto atom atlas possible (atlas.py): Noto Serif Telugu names every atom
Telugu needs - `katelu`, `kasubscripttelu`, `ailengthmarktelu`, `kivoweltelu` - so a
Shree-Tel slot can be identified against a *named* reference instead of being guessed from
byte order.

Masks are packed one bit per pixel into a Python int, with a row stride wider than the mask
so an x-shift cannot bleed into the neighbouring row. Score is max IoU over a +/-JITTER
translation search, same convention as bmatch.py so the numbers are comparable.
"""
import cairo
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.cairoPen import CairoPen

N = 64          # mask fits in N x N
STRIDE = 80     # > N + 2*JITTER
JITTER = 3
RENDER = 200    # rasterise at this size before downsampling
THRESH = 96     # A8 coverage counted as ink


def bbox(gs, gname):
    if gname not in gs:
        return None
    bp = BoundsPen(gs)
    try:
        gs[gname].draw(bp)
    except Exception:
        return None
    return bp.bounds


def klass(b, upem=1000):
    """Structural class from outline geometry alone. Both Noto and Shree-Tel put
    combining marks at negative x with zero-ish advance, so bbox y-range separates them:
    a form whose ink is entirely below the baseline can only be a subscript."""
    if b is None:
        return 'blank'
    x0, y0, x1, y1 = b
    s = 1000.0 / upem
    if (x1 - x0) * s <= 8 and (y1 - y0) * s <= 8:
        return 'blank'
    if y1 * s <= 140:
        return 'below'
    if y0 * s >= 200:
        return 'above'
    return 'main'


def mask(gs, gname):
    """-> (bits, popcount, aspect) or None. Aspect is width/height before normalisation,
    which is a cheap pre-filter: a tall narrow mark never matches a wide letter."""
    b = bbox(gs, gname)
    if b is None:
        return None
    x0, y0, x1, y1 = b
    w, h = x1 - x0, y1 - y0
    if w <= 0 or h <= 0:
        return None
    scale = (RENDER - 8) / max(w, h)
    surf = cairo.ImageSurface(cairo.FORMAT_A8, RENDER, RENDER)
    ctx = cairo.Context(surf)
    ctx.translate(4, RENDER - 4)
    ctx.scale(scale, -scale)
    ctx.translate(-x0, -y0)
    gs[gname].draw(CairoPen(gs, ctx))
    ctx.fill()
    surf.flush()
    data = surf.get_data()
    stride = surf.get_stride()

    rows = []
    for y in range(RENDER):
        off = y * stride
        acc = 0
        for x in range(RENDER):
            if data[off + x] >= THRESH:
                acc |= 1 << x
        if acc:
            rows.append((y, acc))
    if not rows:
        return None
    y0p, y1p = rows[0][0], rows[-1][0]
    xlo = min((a & -a).bit_length() - 1 for _, a in rows)
    xhi = max(a.bit_length() - 1 for _, a in rows)
    cw, ch = xhi - xlo + 1, y1p - y0p + 1
    s = N / max(cw, ch)
    ox = (N - int(cw * s)) // 2 + JITTER
    oy = (N - int(ch * s)) // 2 + JITTER

    bits = 0
    for y, acc in rows:
        ny = int((y - y0p) * s) + oy
        shifted = 0
        a = acc >> xlo
        while a:
            lsb = (a & -a).bit_length() - 1
            shifted |= 1 << (int(lsb * s) + ox)
            a &= a - 1
        bits |= shifted << (ny * STRIDE)
    return bits, bits.bit_count(), cw / ch


def score(a, b):
    """max IoU over a +/-JITTER translation search."""
    if a is None or b is None:
        return 0.0
    ab, an = a[0], a[1]
    bb, bn = b[0], b[1]
    if not an or not bn:
        return 0.0
    best = 0.0
    for dy in range(-JITTER, JITTER + 1):
        sh = dy * STRIDE
        s1 = bb << sh if sh >= 0 else bb >> -sh
        for dx in range(-JITTER, JITTER + 1):
            c = s1 << dx if dx >= 0 else s1 >> -dx
            inter = (ab & c).bit_count()
            if inter:
                best = max(best, inter / (an + c.bit_count() - inter))
    return best
