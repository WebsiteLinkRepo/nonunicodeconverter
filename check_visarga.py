from fontTools.ttLib import TTFont
font = TTFont('public/Fonts folder/AnuSM/ttf/NEOGANBO.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()
for c in [0xF03A]:
    glyph_name = cmap.get(c)
    if glyph_name:
        width = font['hmtx'][glyph_name][0]
        print(f"Char {hex(c)}: width {width}, xMin {getattr(glyf[glyph_name], 'xMin', 0)}, xMax {getattr(glyf[glyph_name], 'xMax', 0)}")
