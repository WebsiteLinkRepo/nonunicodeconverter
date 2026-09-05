#!/usr/bin/env python3
"""
The Shree-Tel-0908 slot inventory: every (3,1) cmap codepoint with its metrics and a
structural class, plus the groupings the search uses to build candidate sets.

Emit (3,1) codepoints, never raw font bytes. The font also carries (0,0) and (1,0) byte
cmaps, but both Chromium and Windows resolve text through (3,1), and the glyph names are
standard Macintosh names assigned by position, so they carry no meaning.
"""
import os

from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
LEGACY = os.path.join(REPO, 'public', 'SHREE-TEL.ttf')

_font = TTFont(LEGACY, lazy=True)
_gs = _font.getGlyphSet()
CMAP = {st.platformID: st for st in _font['cmap'].tables}[3].cmap
HMTX = _font['hmtx'].metrics


def _bbox(gname):
    from fontTools.pens.boundsPen import BoundsPen
    bp = BoundsPen(_gs)
    try:
        _gs[gname].draw(bp)
    except Exception:
        return None
    return bp.bounds


SLOTS = {}
for cp, gname in sorted(CMAP.items()):
    b = _bbox(gname)
    adv = HMTX[gname][0]
    if b is None:
        k = 'blank'
    elif (b[2] - b[0]) <= 8 and (b[3] - b[1]) <= 8:
        k = 'blank'
    elif adv <= 80 and b[3] <= 140:
        k = 'below'          # subscript: zero advance, ink under the baseline
    elif adv <= 80 and b[1] >= 250:
        k = 'above'          # talakattu / i-matra family
    elif adv <= 80:
        k = 'mark'           # zero advance but spans the x-height
    else:
        k = 'main'           # occupies its own advance
    SLOTS[cp] = {'gname': gname, 'adv': adv, 'bbox': b, 'class': k}


def of(k):
    return [cp for cp, s in SLOTS.items() if s['class'] == k]


def ch(cp):
    return chr(cp)


def s(cps):
    return ''.join(chr(c) for c in cps)


# Candidate sets for the search. Deliberately generous: the search is cheap and a
# hand-narrowed set is exactly how the previous attempt went wrong.

#: Main-line forms a consonant could be built on. Excludes the digit slots, which the
#: atlas identified as Telugu digits, and the blank stubs.
DIGITS = list(range(0x30, 0x3A))
LETTERS = [cp for cp in of('main') if cp not in DIGITS]

#: Zero-advance marks that sit above the base: the three talakattu hooks live here along
#: with the i/e/o matra family.
ABOVE = of('above')

#: Zero-advance marks under the baseline: subscripts.
BELOW = of('below')

#: Marks spanning the x-height (ృ and the wider o/au tails).
MIDMARK = of('mark')

#: The three narrow hooks that a `base` form expects to have drawn back over it.
TALAKATTU = [0x00E6, 0x00E7, 0x00E8]

if __name__ == '__main__':
    from collections import Counter
    print(Counter(v['class'] for v in SLOTS.values()))
    for k in ('above', 'below', 'mark'):
        print(f"\n{k} ({len(of(k))}):")
        for cp in of(k):
            v = SLOTS[cp]
            print(f"  U+{cp:04X} {v['gname']:<16} adv={v['adv']:<4} {v['bbox']}")
    print(f"\nmain letters: {len(LETTERS)}   digits: {len(DIGITS)}")
