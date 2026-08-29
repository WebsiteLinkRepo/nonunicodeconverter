from fontTools.ttLib import TTFont
font = TTFont('public/Fonts folder/AnuSM/ttf/NEOGANBO.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()
for c in range(0xF020, 0xF0FF):
    glyph_name = cmap.get(c)
    if glyph_name:
        glyph = glyf[glyph_name]
        width = font['hmtx'][glyph_name][0]
        # Look for tall matras that reach back
        if hasattr(glyph, 'xMin') and glyph.xMin < -100 and getattr(glyph, 'yMax', 0) > 600:
            print(f"Char {hex(c)} ({glyph_name}): width {width}, xMin {glyph.xMin}, xMax {glyph.xMax}, contours {glyph.numberOfContours}")
