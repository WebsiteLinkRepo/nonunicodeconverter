from fontTools.ttLib import TTFont
font = TTFont('public/Fonts folder/AnuSM/ttf/NEOGANBO.TTF')
glyf = font['glyf']
cmap = font.getBestCmap()
glyph = glyf[cmap.get(0xF0EB)]
print(f"Char 0xF0EB: width {font['hmtx'][cmap.get(0xF0EB)][0]}, xMin {getattr(glyph, 'xMin', '?')}, xMax {getattr(glyph, 'xMax', '?')}")
