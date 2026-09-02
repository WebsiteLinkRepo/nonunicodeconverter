from fontTools.ttLib import TTFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
font = TTFont(font_path)
cmap = font.getBestCmap()
hmtx = font['hmtx']

print("--- Marks / Matras metrics ---")
for code in [0xE6, 0xE7, 0xE9, 0xEC, 0xED, 0xEE, 0xEF, 0xF0, 0xF1, 0xF2, 0xF6, 0xF8, 0xFA, 0x23, 0xA2, 0x82]:
    if code in cmap:
        gname = cmap[code]
        adv, lsb = hmtx[gname]
        print(f"Code 0x{code:02X} ({chr(code)}): gname={gname:15s} adv={adv:5d}, lsb={lsb:5d}")

print("\n--- Some Consonants metrics ---")
for ch in ['a', 'V', '^', '™', '§', '¯', '²', 'Ä', 'Å', 'ˆ', 'Ë', 'Ð', 'Ü']:
    code = ord(ch)
    if code in cmap:
        gname = cmap[code]
        adv, lsb = hmtx[gname]
        print(f"Char '{ch}' (0x{code:02X}): gname={gname:15s} adv={adv:5d}, lsb={lsb:5d}")
