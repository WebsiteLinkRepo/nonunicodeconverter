#!/usr/bin/env python3
"""
Phase 1: mechanical glyph inventory of a legacy Shree-Lipi font, addressed in plat3.

  python3 scratch/telugu0908/inventory.py [font.ttf] > scratch/telugu0908/inventory.txt

Also writes scratch/telugu0908/inventory.json. Nothing here involves judgement: every
field is read off the font. Identities get attached in Phase 2 (see INVENTORY.md).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tel908 as T

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inventory.json')


def classify(m):
    bbox, adv = m['bbox'], m['adv']
    if bbox is None or m['contours'] == 0:
        return 'BLANK'
    x0, y0, x1, y1 = bbox
    if x1 - x0 <= 6 and y1 - y0 <= 6:
        return 'DUMMY'          # 5x5 spacer, carries width only
    if adv <= 80:
        if y0 >= 250:
            return 'ABOVE'      # talakattu / i-e-o matra tops
        if x1 <= 10:
            return 'BELOW'      # vattu / pollu, drawn back and under
        return 'MARK'
    return 'BASE'


def js_escape(cp):
    if 0x20 < cp < 0x7F and chr(cp) not in '\\\'"':
        return chr(cp)
    return '\\u%04X' % cp


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else T.LEGACY
    face = T.Face(path)
    codes = sorted(face.plat3)

    rows = []
    prev = None
    for cp in codes:
        m = face.metrics(cp)
        cls = classify(m)
        bbox = m['bbox']
        overhang = bool(bbox and m['adv'] < bbox[2] and cls == 'BASE')
        desc = bool(bbox and bbox[1] < -150)
        near = None
        if prev and bbox and prev['bbox'] and cls == 'BASE' and prev['class'] == 'BASE':
            pb = prev['bbox']
            if (abs(m['adv'] - prev['adv']) <= 2 and abs(bbox[0] - pb[0]) <= 4
                    and abs(bbox[2] - pb[2]) <= 4 and bbox[3] - pb[3] > 40):
                near = prev['cp']       # this looks like the ii-form of the previous slot
        row = {
            'cp': cp, 'char': chr(cp), 'js': js_escape(cp), 'byte': m['byte'],
            'glyph': m['glyph'], 'adv': m['adv'], 'contours': m['contours'],
            'bbox': list(bbox) if bbox else None, 'class': cls,
            'overhangBase': overhang, 'descender': desc,
            'tallerTwinOf': near,
            'gapBefore': prev is not None and cp - prev['cp'] > 1,
            'identity': None,           # filled in by Phase 2
        }
        rows.append(row)
        prev = row

    # runs: a BASE opens a run; BELOW/MARK closes it; a gap always breaks
    runs, cur = [], []
    for r in rows:
        if r['class'] in ('BLANK', 'DUMMY'):
            if cur:
                runs.append(cur); cur = []
            continue
        if cur and (r['gapBefore'] or (r['class'] == 'BASE' and cur[-1]['class'] in ('BELOW', 'MARK'))):
            runs.append(cur); cur = []
        cur.append(r)
    if cur:
        runs.append(cur)

    doc = {'font': path, 'fullName': face.tt['name'].getDebugName(4),
           'numGlyphs': face.tt['maxp'].numGlyphs, 'codes': len(codes),
           'talakattu': T.TALAKATTU, 'rows': rows,
           'runs': [[r['cp'] for r in run] for run in runs]}
    with open(OUT, 'w') as fh:
        json.dump(doc, fh, indent=1, ensure_ascii=False)

    print(f"# {doc['fullName']}  glyphs={doc['numGlyphs']}  plat3 codes={doc['codes']}")
    counts = {}
    for r in rows:
        counts[r['class']] = counts.get(r['class'], 0) + 1
    print('# classes: ' + '  '.join(f'{k}={v}' for k, v in sorted(counts.items())))
    print(f"# overhangBase={sum(r['overhangBase'] for r in rows)}  "
          f"tallerTwin={sum(r['tallerTwinOf'] is not None for r in rows)}  runs={len(runs)}")
    print()
    for i, run in enumerate(runs):
        head = ' '.join(f"{r['cp']:#04x}" for r in run)
        print(f"--- run {i:2d}  [{head}]")
        for r in run:
            b = r['bbox']
            flags = ''.join(('O' if r['overhangBase'] else '.',
                             'D' if r['descender'] else '.',
                             'T' if r['tallerTwinOf'] else '.'))
            print(f"  {r['cp']:#06x} {r['js']:<7} byte={r['byte'] if r['byte'] is not None else -1:#04x} "
                  f"{r['class']:<6} adv={r['adv']:<4} {flags} "
                  f"bbox=({b[0]},{b[1]})-({b[2]},{b[3]})")


if __name__ == '__main__':
    main()
