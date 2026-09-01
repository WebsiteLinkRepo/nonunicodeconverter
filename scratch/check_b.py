import json
with open('scratch/all_font_glyphs.json') as f:
    glyphs = json.load(f)

for g in glyphs:
    if g['char'] in ['~', 'b', 'B', '^', '`', '_', 'X', 'Õ', 'Ù', 'Ô', 'Ú', 'Û', 'Õ']:
        print(f"{repr(g['char']):5} ({g['hex']}): {g['name']:15} adv={g['adv']} lsb={g['lsb']} xMin={g['xMin']} xMax={g['xMax']} yMin={g['yMin']} yMax={g['yMax']}")
