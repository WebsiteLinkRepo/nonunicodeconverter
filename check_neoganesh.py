from fontTools.ttLib import TTFont
font = TTFont('public/Fonts folder/AnuSM/ttf/NEOGANBO.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()
for c in [0xF04E, 0xF0FE, 0xF0E7, 0xF0EE, 0xF0EF, 0xF0ED, 0xF0E6, 0xF0A2]:
    glyph_name = cmap.get(c)
    if glyph_name:
        glyph = glyf[glyph_name]
        width = font['hmtx'][glyph_name][0]
        print(f"Char {hex(c)}: width {width}, xMin {getattr(glyph, 'xMin', 0)}, xMax {getattr(glyph, 'xMax', 0)}, yMin {getattr(glyph, 'yMin', 0)}")
