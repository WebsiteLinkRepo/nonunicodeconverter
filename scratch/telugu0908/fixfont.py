#!/usr/bin/env python3
"""
Make a legacy Shree-Lipi TTF loadable as a web font.

  python3 scratch/telugu0908/fixfont.py public/SHREE-TEL.ttf public/SHREE-TEL-web.ttf

Why this is needed
------------------
Chromium runs every @font-face through the OpenType Sanitiser and rejects the font
outright if any table fails to parse - silently, so the page just falls back to a Latin
face and the legacy text renders as gibberish Latin letters. These 2001-era Modular
Infotech fonts fail:

  SHREE-TEL.ttf       OTS: post: Bad string index 5   -> rejected
  SHREE-DEV-0708.ttf  OTS: post: Bad string index 5   -> rejected
  Shree_0803.TTF      OTS: cmap: unexpected range shift (0 != 4) -> rejected

Verified with playwright + FontFace.load(); all three throw NetworkError before the fix.

The fixes are both lossless for rendering:
  * post 2.0 -> 3.0. Format 3 carries no glyph names at all, and nothing in the browser
    rendering path needs them (we address glyphs through the (3,1) cmap).
  * force the cmap subtables to be decompiled and recompiled, which rewrites the format 4
    binary search header (segCountX2 / searchRange / rangeShift) correctly.

Glyph outlines, advances and both cmaps are untouched, so the encoding is identical.
"""
import sys

from fontTools.ttLib import TTFont


def repair(src, dst):
    font = TTFont(src)
    notes = []

    post = font['post']
    if post.formatType != 3.0:
        notes.append(f'post {post.formatType} -> 3.0')
        post.formatType = 3.0
        post.glyphNames = []
        post.extraNames = []
        post.mapping = {}

    # touching .tables forces decompile, so save() recompiles the subtable headers
    cmap = font['cmap']
    n = len(cmap.tables)
    for t in cmap.tables:
        _ = t.cmap
    notes.append(f'cmap recompiled ({n} subtables)')

    font.save(dst)
    return notes


def main():
    if len(sys.argv) < 3:
        print(__doc__.strip())
        return 1
    src, dst = sys.argv[1], sys.argv[2]
    for n in repair(src, dst):
        print(f'  {n}')
    print(f'{src} -> {dst}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
