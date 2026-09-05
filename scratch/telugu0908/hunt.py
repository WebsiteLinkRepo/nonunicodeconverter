#!/usr/bin/env python3
"""
Exhaustive offline search for the legacy recipe of one Unicode letter.

  python3 scratch/telugu0908/hunt.py మ ధ థ

Bare consonants and independent vowels need no shaping, so both sides can be rasterised
locally with fontTools + PIL - no browser, which makes an exhaustive 2- and 3-glyph search
affordable. Composite bounding boxes are computed analytically from hmtx + glyf first and
implausible ones are dropped before anything is rendered; that is what makes 40k+
combinations tractable.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tel908 as T

H = 72


def composite_bbox(face, cps):
    x = 0
    x0 = y0 = 10**9
    x1 = y1 = -10**9
    for cp in cps:
        m = face.metrics(cp)
        if m['bbox']:
            bx0, by0, bx1, by1 = m['bbox']
            x0 = min(x0, x + bx0); x1 = max(x1, x + bx1)
            y0 = min(y0, by0); y1 = max(y1, by1)
        x += m['adv']
    return (x0, y0, x1, y1) if x0 < x1 else None


def plausible(bb, ref_bb, tol=0.42):
    if bb is None:
        return False
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    rw, rh = ref_bb[2] - ref_bb[0], ref_bb[3] - ref_bb[1]
    if h <= 0 or w <= 0:
        return False
    if not (1 - tol) * rh <= h <= (1 + tol) * rh:
        return False
    return (1 - tol) * (rw / rh) <= (w / h) <= (1 + tol) * (rw / rh)


def main():
    leg = T.Face(T.LEGACY)
    refs = [T.Face(T.NOTO_SERIF), T.Face(T.NOTO_SANS)]
    codes = [cp for cp in sorted(leg.plat3) if leg.metrics(cp)['bbox']]
    bases = [cp for cp in codes if leg.metrics(cp)['adv'] > 80]
    marks = [cp for cp in codes if leg.metrics(cp)['adv'] <= 80]

    for ch in sys.argv[1:]:
        imgs = [T.render(f, ch, height=H) for f in refs if f.has(ord(ch))]
        imgs = [i for i in imgs if i is not None]
        if not imgs:
            print(f'{ch}: no reference glyph'); continue
        rf = next(f for f in refs if f.has(ord(ch)))
        rbb = rf.metrics(ord(ch))['bbox'] if ord(ch) in rf.plat3 else None
        # normalise the reference bbox to the legacy upem
        s = leg.upem / rf.upem
        rbb = tuple(v * s for v in rbb)

        cand = []
        for a in codes:
            cand.append((a,))
        for a in bases:
            for b in codes:
                if b != a:
                    cand.append((a, b))
        for a in bases:
            for b in marks:
                for c in marks:
                    if len({a, b, c}) == 3:
                        cand.append((a, b, c))
        keep = [c for c in cand if plausible(composite_bbox(leg, c), rbb)]
        scored = []
        for cps in keep:
            im = T.render(leg, ''.join(chr(x) for x in cps), height=H)
            if im is None:
                continue
            scored.append((max(T.iou(r, im) for r in imgs), cps))
        scored.sort(reverse=True)
        print(f"\n{ch}  ({len(cand)} combos, {len(keep)} plausible)")
        for sc, cps in scored[:10]:
            print('   ' + '+'.join(f'{x:#04x}' for x in cps) + f'   {sc:.3f}')


if __name__ == '__main__':
    main()
