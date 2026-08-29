from fontTools.ttLib import TTFont
font = TTFont('public/Fonts folder/AnuSM/ttf/NEOGANBO.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()
for c in range(0xF020, 0xF0FF):
    glyph_name = cmap.get(c)
    if glyph_name:
        width = font['hmtx'][glyph_name][0]
        # Look for chars similar to width 424
        if 400 < width < 450:
            print(f"Char {hex(c)}: width {width}")
