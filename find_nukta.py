from fontTools.ttLib import TTFont
font = TTFont('public/Fonts folder/AnuSM/ttf/NEOGANBO.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()
for c in range(0xF020, 0xF0FF):
    glyph_name = cmap.get(c)
    if glyph_name:
        glyph = glyf[glyph_name]
        width = font['hmtx'][glyph_name][0]
        # Look for small dots (small width, low yMin, low yMax)
        if hasattr(glyph, 'yMax') and glyph.yMax < 200 and getattr(glyph, 'yMin', 0) > -200:
            print(f"Possible Nukta: {hex(c)} ({glyph_name}), width {width}, xMin {getattr(glyph, 'xMin', 0)}, xMax {getattr(glyph, 'xMax', 0)}")
