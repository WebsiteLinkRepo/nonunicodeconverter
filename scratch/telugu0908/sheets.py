#!/usr/bin/env python3
"""
Phase 2 step 1: labelled contact sheets of every plat3 slot in the legacy font.

  python3 scratch/telugu0908/sheets.py            # all slots, ~48 per sheet
  python3 scratch/telugu0908/sheets.py 0x4d 0x4e  # just these

Each cell shows the slot rendered two ways:
  top    - the glyph on its own
  bottom - the glyph IN CONTEXT (grey), because a zero-advance mark or a subscript is
           unreadable alone. Marks are shown after a complete ka ('Mae'); overhang bases
           are shown with the talakattu appended.

Writes scratch/telugu0908/sheets/sheet_NN.png.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tel908 as T
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(HERE, 'sheets')
LABEL = '/usr/share/fonts/TTF/DejaVuSansMono.ttf'
KA = 'Mæ'            # complete ka, used as the context prefix
COLS, ROWS = 8, 6
CELL_W, CELL_H = 158, 182
GLYPH_H, CTX_H = 74, 52


def context_for(row):
    """(string to render, caption) showing this slot in a readable context."""
    ch = chr(row['cp'])
    cls, cp = row['class'], row['cp']
    if cls in ('BELOW', 'MARK', 'ABOVE'):
        return KA + ch, 'ka+'
    if row['overhangBase']:
        return ch + chr(T.TALAKATTU), '+tk'
    if row['descender']:
        return KA + ch, 'ka+'
    return None, ''


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    inv = json.load(open(os.path.join(HERE, 'inventory.json')))
    face = T.Face(inv['font'])
    want = [int(a, 16) for a in sys.argv[1:]] or None
    rows = [r for r in inv['rows'] if r['class'] != 'BLANK' and (want is None or r['cp'] in want)]

    f_big = ImageFont.truetype(LABEL, 15)
    f_sm = ImageFont.truetype(LABEL, 11)
    per = COLS * ROWS
    made = []
    for s in range((len(rows) + per - 1) // per):
        chunk = rows[s * per:(s + 1) * per]
        img = Image.new('RGB', (COLS * CELL_W, ROWS * CELL_H), 'white')
        d = ImageDraw.Draw(img)
        for i, r in enumerate(chunk):
            cx, cy = (i % COLS) * CELL_W, (i // COLS) * CELL_H
            d.rectangle([cx, cy, cx + CELL_W - 1, cy + CELL_H - 1], outline=(205, 205, 205))
            tag = f"{r['cp']:#06x} {r['class'][:5]}"
            d.text((cx + 5, cy + 3), tag, font=f_big, fill=(150, 0, 0))
            d.text((cx + 5, cy + 21), f"js {r['js']}  adv {r['adv']}", font=f_sm, fill=(110, 110, 110))
            g = T.render(face, chr(r['cp']), height=GLYPH_H)
            if g is not None and g.size[0] < CELL_W - 12:
                img.paste(Image.merge('RGB', (g.point(lambda v: 255 - v),) * 3),
                          (cx + (CELL_W - g.size[0]) // 2, cy + 36))
            ctx, cap = context_for(r)
            if ctx:
                c = T.render(face, ctx, height=CTX_H)
                if c is not None and c.size[0] < CELL_W - 12:
                    inv_c = c.point(lambda v: 255 - v // 2)   # grey, so it reads as context
                    img.paste(Image.merge('RGB', (inv_c,) * 3),
                              (cx + (CELL_W - c.size[0]) // 2, cy + CELL_H - CTX_H - 6))
                d.text((cx + 5, cy + CELL_H - 16), cap, font=f_sm, fill=(0, 110, 0))
        p = os.path.join(OUTDIR, f'sheet_{s:02d}.png')
        img.save(p)
        made.append(p)
        print(p, f'({len(chunk)} slots: {chunk[0]["cp"]:#06x}..{chunk[-1]["cp"]:#06x})')
    return made


if __name__ == '__main__':
    main()
