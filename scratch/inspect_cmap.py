from fontTools.ttLib import TTFont

font = TTFont('public/SHREE-TEL.ttf')
cmap = font['cmap'].getBestCmap()
print(f"Total mapped: {len(cmap)}")
for code, name in sorted(cmap.items()):
    hex_code = hex(code)
    print(f"{hex_code}: {name}")
