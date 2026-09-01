from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('/home/samuelvictor/Downloads/Shreelipi_4642.TTF', 40)
img = Image.new('RGB', (1400, 600), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

test_texts = [
    ('Vowels', 'A Am B B© C D$ F$ E Eo Amo Am¡ A§ A…'),
    ('Consonants 1', 'H$ I J K L> M N> O P Äm'),
    ('Consonants 2', 'Q> R> S> T> U V W X Y Z'),
    ('Consonants 3', 'n $ ~ ^ _ ` a b d e f g h i j Ì k l'),
    ('Barakhadi (Ka)', '{H$ H$ H$m H$r Hw$ Hy$ H¥$ Ho$ H¡$ H$mo H$m¡ H§$ H$…'),
    ('Words', '^maV ‘oe am‘ go dZw ‘| h¡')
]

for idx, (label, line) in enumerate(test_texts):
    draw.text((20, 20 + idx * 90), f"{label}: {line}", font=ImageFont.load_default(), fill=(150, 150, 150))
    draw.text((20, 45 + idx * 90), line, font=font, fill=(0, 0, 0))

img.save('/home/samuelvictor/unicode2nonunicode.com/scratch/shree_test_render.png')
print('Rendered successfully!')
