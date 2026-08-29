from fontTools.ttLib import TTFont
font = TTFont('public/Fonts folder/AnuSM/ttf/NEOGANBO.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()
for c in [0xF024]:
    glyph_name = cmap.get(c)
    if glyph_name:
        glyph = glyf[glyph_name]
        print(f"Char {hex(c)} ({glyph_name}): yMin {getattr(glyph, 'yMin', 0)}, yMax {getattr(glyph, 'yMax', 0)}")
