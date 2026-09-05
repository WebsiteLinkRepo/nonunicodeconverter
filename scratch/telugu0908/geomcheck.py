#!/usr/bin/env python3
"""Which conjuncts place the subscript outside the letter it belongs to.

Pure geometry from hmtx and the glyph bboxes - no rendering, no reference font. After the
head form is emitted the pen sits at the sum of its advances; a subscript is a mark with
negative x bounds, so its ink lands at pen+x0..pen+x1. If the centre of that falls left of
the letter's own ink, Shree-Lipi is being asked to draw the subscript beside the letter
instead of under it, which no correct spelling would do.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import heads as H
import slotinfo as S

CONS = list('కఖగఘఙచఛజఝఞటఠడఢణతథదధనపఫబభమయరఱలళవశషసహ') + ['క్ష']


def geom(seq):
    pen, x0, x1 = 0, 1e9, -1e9
    for cp in seq:
        v = S.SLOTS[cp]
        if v['bbox']:
            x0 = min(x0, pen + v['bbox'][0])
            x1 = max(x1, pen + v['bbox'][2])
        pen += v['adv']
    return pen, x0, x1


def main():
    bad = []
    for a in CONS:
        _pen, bx0, bx1 = geom(H.head(a))
        for b in CONS:
            # the per-pair pad is what build_tables.py ships, so check that, not the
            # per-letter default
            pad = H.pad_for(a, H.VATTU[b], S.SLOTS)
            pen, _x0, _x1 = geom(H.head(a) + ([pad] if pad else []))
            v = S.SLOTS[H.VATTU[b]]
            mid = pen + (v['bbox'][0] + v['bbox'][2]) / 2
            if mid < bx0 or mid > bx1 + 120:
                bad.append((a, b, round(mid), round(bx0), round(bx1)))
    print(f"{len(bad)} of {len(CONS) ** 2} conjuncts misplace the subscript")
    from collections import Counter
    for a, n in Counter(x[0] for x in bad).most_common():
        pen, bx0, bx1 = geom(H.head(a))
        print(f"  {a:<4} head adv={pen:<4} ink={round(bx0)}..{round(bx1):<4} misplaced={n}")
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
