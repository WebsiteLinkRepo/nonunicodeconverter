from fontTools.ttLib import TTFont

font = TTFont('/home/samuelvictor/Downloads/Shreelipi_4642.TTF')
cmap = font['cmap'].getBestCmap()
glyf = font['glyf']
hmtx = font['hmtx']

chars = ['_', 'g', 'h', 'W', '`', 'X', '^', 'ñ', 'J', 'm', 'V']
for ch in chars:
    code = ord(ch)
    name = cmap.get(code)
    g = glyf[name]
    adv, lsb = hmtx[name]
    print(f"Char: {repr(ch):6} (0x{code:02x}) -> Glyph: {name:12} adv={adv:4} lsb={lsb:4} xMin={g.xMin:4} xMax={g.xMax:4} yMin={g.yMin:4} yMax={g.yMax:4}")
