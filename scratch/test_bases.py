from PIL import Image, ImageDraw, ImageFont

font_path = "public/SHREE-TEL.ttf"
shree_font = ImageFont.truetype(font_path, 60)

codes_to_test = [
    ("Gha?", [0xb7, 0x51, 0x52, 0x53, 0x5b, 0x5c, 0x61]),
    ("Nga ఙ", [0x50, 0x57, 0x58, 0x59, 0x5a, 0x5b, 0x5c, 0x66, 0x67]),
    ("Ma మ", [0x46, 0x47, 0x48, 0xc4, 0xc5, 0xc6, 0x90, 0xa1]),
    ("Ha హ", [0xe0, 0xe1, 0x2dc, 0x60, 0x70]),
    ("Ana ణ", [0xd7, 0x7e, 0xd8]),
    ("Dha ధ", [0xae, 0xaf, 0xbf, 0xc0]),
    ("Pa ప", [0xd1, 0xb2, 0xb3]),
    ("Ba బ", [0xbb, 0xbc, 0xba]),
    ("Ya య", [0xc4, 0xc5, 0xcc, 0xcd]),
    ("La ల", [0xcc, 0xcb, 0xcd, 0xce]),
    ("Sha ష", [0x201e, 0xd9, 0xda, 0xdb]),
    ("Sa స", [0xa8, 0xa9, 0xdc, 0xdd]),
]

# collect all base codes that might need talakattu test
bases = set()
for _, c_list in codes_to_test:
    bases.update(c_list)

img = Image.new("RGB", (1200, len(codes_to_test) * 80), "white")
draw = ImageDraw.Draw(img)
label_font = ImageFont.load_default()

y = 10
for name, c_list in codes_to_test:
    draw.text((10, y + 20), name, fill="blue", font=label_font)
    
    x = 100
    for code in c_list:
        try:
            # draw raw
            draw.text((x, y + 10), chr(code), fill="black", font=shree_font)
            # draw with talakattu
            draw.text((x + 40, y + 10), chr(code) + chr(0xE6), fill="red", font=shree_font)
            draw.text((x + 10, y - 5), f"{hex(code)}", fill="gray", font=label_font)
        except:
            pass
        x += 100
    y += 80

img.save("scratch/test_bases_out.png")
print("Saved scratch/test_bases_out.png")
