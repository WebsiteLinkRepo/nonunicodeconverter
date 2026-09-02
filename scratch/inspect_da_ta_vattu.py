from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
shree_font = ImageFont.truetype(font_path, 36)
label_font = ImageFont.load_default()

codes = [
    # Some candidates for da_vattu and ta_vattu
    (0xA7, '§', 'base da'),
    (0xAA, 'ª', 'ta vattu'),
    (0xAB, '«', 'da vattu?'),
    (0xAC, '¬', 'dha vettu?'),
    (0xAD, '\xad', '-'),
    (0xAE, '®', 'base dha'),
    (0xAF, '¯', 'base na'),
    (0xB0, '°', 'ni combo'),
    (0xB1, '±', 'nee combo'),
    (0xE2, 'â', 'Li combo'),
    (0xE3, 'ã', 'Lee combo'),
    (0xE4, 'ä', '?'),
    (0xE5, 'å', 'ha/La vattu'),
]

img = Image.new('RGB', (800, len(codes) * 45 + 40), (255, 255, 255))
draw = ImageDraw.Draw(img)

y = 20
for code, ch, desc in codes:
    draw.text((10, y), f"0x{code:02X} {desc}", fill=(0,0,120), font=label_font)
    try:
        # With 'a' prefix
        draw.text((250, y-5), f"a{ch}", fill=(180,0,0), font=shree_font)
    except:
        pass
    y += 45

img.save('scratch/da_ta_vattu_test.png')
print("Saved scratch/da_ta_vattu_test.png")
