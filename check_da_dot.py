from fontTools.ttLib import TTFont
font = TTFont('public/Fonts folder/AnuSM/ttf/NEOGANBO.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()
for c in [0xF0E4, 0xF06A, 0xF067]:
    glyph_name = cmap.get(c)
    if glyph_name:
        glyph = glyf[glyph_name]
        print(f"Char {hex(c)}: width {font['hmtx'][glyph_name][0]}, xMin {getattr(glyph, 'xMin', 0)}, xMax {getattr(glyph, 'xMax', 0)}, yMin {getattr(glyph, 'yMin', 0)}, yMax {getattr(glyph, 'yMax', 0)}")
