#!/usr/bin/env python3
"""
Phase 2 step 3: rank legacy candidates against a Unicode reference by bitmap IoU.

  python3 scratch/telugu0908/match.py cons          # all 36 consonants
  python3 scratch/telugu0908/match.py chars క ఖ గ   # specific single codepoints
  python3 scratch/telugu0908/match.py slot 0x5a     # which reference does THIS slot look like?

Single Unicode codepoints only - no shaping is applied, so this is valid for bare
consonants, independent vowels and isolated marks. Clusters that need GSUB (anything
with a matra or a virama) must go through refsheet.mjs + Chromium instead.

Scores are max over {Noto Serif, Noto Sans} x {aspect-preserved, stretched}: the legacy
face is a different design from either reference, and taking the max keeps a correct
match from being penalised for proportions. Triage only - always confirm on a sheet.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tel908 as T

CONSONANTS = list('కఖగఘఙచఛజఝఞటఠడఢణతథదధనపఫబభమయరలళవశషసహఱ')
VOWELS = list('అఆఇఈఉఊఎఏఐఒఓఔ')
H = 64


def refs():
    return [T.Face(T.NOTO_SERIF), T.Face(T.NOTO_SANS)]


def ref_imgs(faces, ch):
    out = []
    for f in faces:
        if f.has(ord(ch)):
            im = T.render(f, ch, height=H)
            if im is not None:
                out.append(im)
    return out


def candidates(leg, rows):
    """(label, image) for every plausible standalone rendering of a slot."""
    out = []
    tk = chr(T.TALAKATTU)
    for r in rows:
        if r['class'] in ('BLANK', 'DUMMY'):
            continue
        cp = r['cp']
        if r['class'] == 'BASE':
            im = T.render(leg, chr(cp), height=H)
            if im is not None:
                out.append((f"{cp:#04x}", im))
            if r['overhangBase']:
                im2 = T.render(leg, chr(cp) + tk, height=H)
                if im2 is not None:
                    out.append((f"{cp:#04x}+tk", im2))
    return out


def best(ref_list, cands, n=6):
    scored = []
    for label, im in cands:
        scored.append((max(T.iou(r, im) for r in ref_list), label))
    scored.sort(reverse=True)
    return scored[:n]


def main():
    import json
    here = os.path.dirname(os.path.abspath(__file__))
    inv = json.load(open(os.path.join(here, 'inventory.json')))
    leg = T.Face(inv['font'])
    faces = refs()
    cands = candidates(leg, inv['rows'])
    mode = sys.argv[1] if len(sys.argv) > 1 else 'cons'

    if mode == 'slot':
        pool = CONSONANTS + VOWELS
        for a in sys.argv[2:]:
            cp = int(a, 16)
            r = next(x for x in inv['rows'] if x['cp'] == cp)
            tk = chr(T.TALAKATTU)
            for suffix in ([''] + ([tk] if r['overhangBase'] else [])):
                im = T.render(leg, chr(cp) + suffix, height=H)
                if im is None:
                    continue
                scored = sorted(((max(T.iou(x, im) for x in ref_imgs(faces, ch)), ch)
                                 for ch in pool if ref_imgs(faces, ch)), reverse=True)
                tag = f"{cp:#04x}{'+tk' if suffix else ''}"
                print(f"{tag:<9} -> " + '  '.join(f"{c} {s:.2f}" for s, c in scored[:6]))
        return

    targets = sys.argv[2:] if mode == 'chars' else (VOWELS if mode == 'vowels' else CONSONANTS)
    for ch in targets:
        rl = ref_imgs(faces, ch)
        if not rl:
            print(f"{ch}  (no reference glyph)")
            continue
        print(f"{ch}  " + '  '.join(f"{lab} {sc:.2f}" for sc, lab in best(rl, cands)))


if __name__ == '__main__':
    main()
