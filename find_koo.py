from fontTools.ttLib import TTFont
font = TTFont('public/AnuSM/ttf/PRIYAANK.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()
# Look for wide glyphs that have advance width around 700 and contain a matra shape
found = False
for c in range(0xF020, 0xF0FF):
    glyph_name = cmap.get(c)
    if glyph_name:
        width = font['hmtx'][glyph_name][0]
        if 650 < width < 750:
            glyph = glyf[glyph_name]
            # Check if it has a low yMin (indicating a matra below)
            if hasattr(glyph, 'yMin') and glyph.yMin < -200:
                print(f"Possible koo: {hex(c)} ({glyph_name}), width {width}, yMin {glyph.yMin}")
