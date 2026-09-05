#!/usr/bin/env python3
"""
Identify Shree-Tel-0908 glyph slots by matching each one against the *named* atoms of
Noto Serif Telugu.

  python3 scratch/telugu0908/atlas.py            # report + atlas.json
  python3 scratch/telugu0908/atlas.py U+00A7 M   # explain specific slots

Why this beats the cluster search in bmatch.py for *finding* identities: Noto names every
atom Telugu needs (see notoatoms.py), so a slot is compared against a labelled single
glyph. No shaping, no browser, no mark positioning in the measurement - a correct glyph
that Shree-Lipi happens to position differently still scores as correct.

What it cannot do: partial forms. A Shree-Tel `base` is a letter with its talakattu
removed, and Noto has no such glyph, so bases score low and ambiguously. Those are settled
by bmatch.py's contextual voting instead. Slots this tool ranks confidently - full letters,
subscripts, precomposed C+matra, matras, marks, digits - are the ones it is trusted for.

Output atlas.json:
  {"slots":  {"00A7": {"class": "main", "top": [["్ద/subscript", 0.93], ...]}, ...},
   "atoms":  {"్ద/subscript": [["00A7", 0.93], ...], ...}}
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))

import glyphmask as G
import notoatoms as A
from fontTools.ttLib import TTFont

LEGACY = os.path.join(REPO, 'public', 'SHREE-TEL.ttf')
NOTO = '/usr/share/fonts/noto/NotoSerifTelugu-Regular.ttf'
TOP = 12
# A tall narrow mark can never be a wide letter; skip the pair rather than score it.
ASPECT_TOL = 3.0
# Roles worth ranking. 'other' is kept because an unnamed Noto glyph is still a real shape.
ROLES = ('full', 'subscript', 'precomposed', 'halant', 'rasubscript', 'postscript',
         'matra', 'vowel', 'mark', 'digit', 'lengthmark', 'ailengthmark', 'punct', 'other')


def label(name, dec):
    text, role, variant = dec
    core = text if text else name.split('.')[0][:-4]
    return f"{core}/{role}" + (f"/{variant}" if variant else '')


def build():
    leg = TTFont(LEGACY, lazy=True)
    lgs = leg.getGlyphSet()
    luni = {st.platformID: st for st in leg['cmap'].tables}[3].cmap

    noto = TTFont(NOTO, lazy=True)
    ngs = noto.getGlyphSet()

    slots = {}
    for cp, gname in sorted(luni.items()):
        m = G.mask(lgs, gname)
        k = G.klass(G.bbox(lgs, gname))
        slots[cp] = {'gname': gname, 'mask': m, 'class': k}

    atoms = {}
    for gname in noto.getGlyphOrder():
        dec = A.decode(gname)
        if dec is None or dec[1] not in ROLES:
            continue
        m = G.mask(ngs, gname)
        if m is None:
            continue
        lab = label(gname, dec)
        atoms[lab] = {'gname': gname, 'mask': m, 'role': dec[1],
                      'class': G.klass(G.bbox(ngs, gname))}
    return slots, atoms


def cross(slots, atoms):
    pairs = 0
    out = {}
    for cp, s in slots.items():
        sm = s['mask']
        if sm is None:
            out[cp] = []
            continue
        ranked = []
        for lab, a in atoms.items():
            am = a['mask']
            # hard filters: a below-baseline form is never a main-line one, and aspect
            # ratios that differ by more than ASPECT_TOL cannot be the same shape.
            if (s['class'] == 'below') != (a['class'] == 'below'):
                continue
            r = sm[2] / am[2] if am[2] else 0
            if r and (r > ASPECT_TOL or r < 1 / ASPECT_TOL):
                continue
            pairs += 1
            sc = G.score(sm, am)
            if sc > 0.15:
                ranked.append((sc, lab))
        ranked.sort(reverse=True)
        out[cp] = ranked[:TOP]
    return out, pairs


def main():
    slots, atoms = build()
    ranked, pairs = cross(slots, atoms)
    print(f"# {len(slots)} slots x {len(atoms)} named Noto atoms, {pairs} pairs scored",
          file=sys.stderr)

    want = [a.upper().replace('U+', '') for a in sys.argv[1:]]
    doc = {'slots': {}, 'atoms': {}}
    for cp, r in ranked.items():
        key = f"{cp:04X}"
        doc['slots'][key] = {'class': slots[cp]['class'], 'gname': slots[cp]['gname'],
                             'top': [[lab, round(sc, 3)] for sc, lab in r]}
        for sc, lab in r:
            doc['atoms'].setdefault(lab, []).append([key, round(sc, 3)])
    for lab in doc['atoms']:
        doc['atoms'][lab].sort(key=lambda x: -x[1])
        doc['atoms'][lab] = doc['atoms'][lab][:TOP]

    for cp in sorted(ranked):
        key = f"{cp:04X}"
        if want and key not in want and slots[cp]['gname'].upper() not in want:
            continue
        r = ranked[cp]
        head = f"U+{key} {slots[cp]['class']:<5}"
        print(head + '  ' + '  '.join(f"{lab} {sc:.2f}" for sc, lab in r[:6]))

    with open(os.path.join(HERE, 'atlas.json'), 'w') as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=0)
    print(f"# wrote {os.path.join(HERE, 'atlas.json')}", file=sys.stderr)


if __name__ == '__main__':
    main()
