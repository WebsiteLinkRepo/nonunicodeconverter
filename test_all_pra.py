from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF', 50)
img = Image.new('RGB', (1000, 1000), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Try combinations of 155, 156, 159 + various vertical bars or strokes
combinations = [
    # Full pra + matras
    (159, 64), (159, 185), (159, 92),
    # Full pa + ra stroke + matras
    (156, 221, 64), (156, 64, 221),
    # Half pa + ra stroke + matras
    (155, 221, 64), (155, 64, 221),
    # Half pa + matra + ra stroke
    (155, 64, 221, 64),
]

y = 20
for combo in combinations:
    text = "".join(chr(61440 + c) for c in combo)
    draw.text((20, y), text, font=font, fill=(0, 0, 0))
    draw.text((150, y), str(combo), font=font, fill=(0, 0, 0))
    y += 60

img.save('pra_combos.png')
