from fontTools.ttLib import TTFont
font = TTFont('public/Fonts folder/AnuSM/ttf/NEOGANBO.TTF')
hmtx = font['hmtx']
cmap = font.getBestCmap()
def w(c): return hmtx[cmap.get(c)][0] if cmap.get(c) else '?'
print(f"N (F04E): {w(0xF04E)}")
print(f"þ (F0FE): {w(0xF0FE)}")
print(f"y (F079): {w(0xF079)}")
print(f"ç (F0E7): {w(0xF0E7)}")
print(f"ª (F0AA): {w(0xF0AA)}")
