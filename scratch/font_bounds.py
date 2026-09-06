from fontTools.ttLib import TTFont
import sys

font = TTFont('public/SHREE-TEL.ttf')
cmap = font['cmap'].getBestCmap()
glyf = font['glyf']
hmtx = font['hmtx']

for code, name in sorted(cmap.items()):
    metrics = hmtx[name]
    advance = metrics[0]
    
    g = glyf.get(name)
    bounds = "empty"
    if g:
        g.expand(font)
        if hasattr(g, 'xMin'):
            bounds = f"x:{g.xMin}..{g.xMax} y:{g.yMin}..{g.yMax}"
        
    print(f"0x{code:02x} ({code:d}): adv={advance:4d} {bounds}")
