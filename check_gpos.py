from fontTools.ttLib import TTFont
font = TTFont('public/AnuSM/ttf/PRIYAANK.TTF')
if 'GPOS' in font:
    print("Has GPOS table!")
else:
    print("No GPOS table.")
