from fontTools.ttLib import TTFont
font = TTFont('public/AnuSM/ttf/PRIYAANK.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()
for c in [0xF04E]:
    glyph_name = cmap.get(c)
    if glyph_name:
        glyph = glyf[glyph_name]
        print(f"Char {hex(c)} ({glyph_name}): xMin {getattr(glyph, 'xMin', 0)}, xMax {getattr(glyph, 'xMax', 0)}")
        print(glyph.getCoordinates(glyf)[0])
