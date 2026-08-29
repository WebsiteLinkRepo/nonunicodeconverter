from fontTools.ttLib import TTFont
font = TTFont('public/AnuSM/ttf/PRIYAANK.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()
for c in range(0xF020, 0xF0FF):
    glyph_name = cmap.get(c)
    if glyph_name:
        glyph = glyf[glyph_name]
        width = font['hmtx'][glyph_name][0]
        if hasattr(glyph, 'yMin') and glyph.yMin < -200 and glyph.yMax < 100:
            print(f"Below matra: {hex(c)} ({glyph_name}), width {width}, xMin {glyph.xMin}, xMax {glyph.xMax}, yMin {glyph.yMin}, yMax {glyph.yMax}")
