from fontTools.ttLib import TTFont
font = TTFont('public/SHREE-TEL-web.ttf')
cmap = font.getBestCmap()
print(f"Cmap for tilde (126): {cmap.get(126)}")
