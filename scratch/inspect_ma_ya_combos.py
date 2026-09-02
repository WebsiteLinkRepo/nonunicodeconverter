from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
noto_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 36)
noto_font = ImageFont.truetype(noto_path, 28)
label_font = ImageFont.load_default()

# Let's test combinations for ma (మ) and ya (య)
# 'మ' = 0xC4 (Ä)
# 'య' = 0xC5 (Å)
# 'మి' = 0xCB (Ë) / 0xCC (Ì)? Wait, let's check what 0xCC, 0xCD, 0xCE, 0xCF, 0xD0... are!
# Let's inspect codes from 0xC0 to 0xDF with labels
tests = [
    # ma combinations
    ('మ', 'Äæ', 'Ä'),
    ('మి', 'Äì', 'Ì'),
    ('మీ', 'Äí', 'Í'),
    ('ము', 'Äî', 'Äî'),
    ('మూ', 'Äï', 'Äï'),
    ('య', 'Åæ', 'Å'),
    ('యి', 'Åì', 'Åì'),
    ('యీ', 'Åí', 'Åí'),
    ('యు', 'Åî', 'Åî'),
    ('యూ', 'Åï', 'Åï'),
    # ra combinations
    ('ర', 'ˆæ', 'ˆ'),
    ('రి', 'Ç', 'ˆì'),
    ('రీ', 'È', 'ˆí'),
    ('రు', 'ˆî', 'ˆî'),
    ('రూ', 'ˆï', 'ˆï'),
    # la combinations
    ('ల', 'Ëæ', 'Ë'),
    ('లి', 'Í', 'Ëì'),
    ('లీ', 'Î', 'Ëí'),
    ('లు', 'Ëî', 'Ëî'),
    ('లూ', 'Ëï', 'Ëï'),
    # va combinations
    ('వ', 'Ðæ', 'Ð'),
    ('వి', 'Ñ', 'Ðì'),
    ('వీ', 'Ò', 'Ðí'),
    ('వు', 'Ðî', 'Ðî'),
    ('వూ', 'Ðï', 'Ðï'),
]

img = Image.new('RGB', (900, len(tests) * 45 + 40), (255, 255, 255))
draw = ImageDraw.Draw(img)

y = 20
for label, opt1, opt2 in tests:
    draw.text((10, y), label, fill=(0,0,150), font=noto_font)
    draw.text((200, y), f"Opt 1: {opt1}", fill=(0,0,0), font=shree_font)
    draw.text((500, y), f"Opt 2: {opt2}", fill=(180,0,0), font=shree_font)
    y += 45

img.save('scratch/special_combos_test.png')
print("Saved scratch/special_combos_test.png")
