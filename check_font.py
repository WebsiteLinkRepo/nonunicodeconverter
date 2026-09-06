from fontTools.ttLib import TTFont
font = TTFont('shreelipi_fonts/Shreelipi_4926.TTF')
cmap = font['cmap'].getBestCmap()
if 0x20 in cmap:
    glyph_name = cmap[0x20]
    print(f"0x20 (space) -> {glyph_name}, width: {font['hmtx'][glyph_name][0]}")
else:
    print("0x20 not in cmap!")

if 0xE6 in cmap:
    glyph_name = cmap[0xE6]
    print(f"0xE6 (æ) -> {glyph_name}, width: {font['hmtx'][glyph_name][0]}, lsb: {font['hmtx'][glyph_name][1]}")
for code in [0x4D, 0x51, 0x56]:
    if code in cmap:
        g = cmap[code]
        print(f"0x{code:X} -> {g}, width: {font['hmtx'][g][0]}, lsb: {font['hmtx'][g][1]}")
g_ae = font['glyf']['ae']
print(f"ae bounding box: xMin={g_ae.xMin}, xMax={g_ae.xMax}")
for code in [0xB8, 0xBA, 0xBF]:
    if code in cmap:
        g = cmap[code]
        print(f"0x{code:X} -> {g}, width: {font['hmtx'][g][0]}")
