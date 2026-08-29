from fontTools.ttLib import TTFont
font = TTFont('public/AnuSM/ttf/PRIYAANK.TTF')
hmtx = font['hmtx']
cmap = font.getBestCmap()
for c in [0xF0E6, 0xF0AA, 0xF07A]:
    glyph_name = cmap.get(c)
    if glyph_name:
        width = hmtx[glyph_name][0]
        print(f"Char {hex(c)}: width {width}")
