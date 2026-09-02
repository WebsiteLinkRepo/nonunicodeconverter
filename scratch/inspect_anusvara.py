from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
noto_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 36)
noto_font = ImageFont.truetype(noto_path, 28)
label_font = ImageFont.load_default()

tests = [
    ('కం (aæÆ vs aÆ)', 'aæÆ', 'aÆ'),
    ('గం (VæÆ vs VÆ)', 'VæÆ', 'VÆ'),
    ('తం (™æÆ vs ™Æ)', '™æÆ', '™Æ'),
    ('నం (¯æÆ vs ¯Æ)', '¯æÆ', '¯Æ'),
    ('పం (²æÆ vs ²Æ)', '²æÆ', '²Æ'),
    ('వం (ÐæÆ vs ÐÆ)', 'ÐæÆ', 'ÐÆ'),
    ('సం (ÜæÆ vs ÜÆ)', 'ÜæÆ', 'ÜÆ'),
    ('భం (¿æÆ vs ¿Æ)', '¿æÆ', '¿Æ'),
    ('మం (ÄæÆ vs ÄÆ)', 'ÄæÆ', 'ÄÆ'),
    ('యం (ÅæÆ vs ÅÆ)', 'ÅæÆ', 'ÅÆ'),
    ('రం (ˆæÆ vs ˆÆ)', 'ˆæÆ', 'ˆÆ'),
    ('లం (ËæÆ vs ËÆ)', 'ËæÆ', 'ËÆ'),
    ('శాస్త్రం (ÜæÜì™–æÆ vs ÜæÜì™–Æ)', 'ÜæÜì™–æÆ', 'ÜæÜì™–Æ'),
    ('పుస్తకం (²îÜªæaæÆ vs ²îÜªæaÆ)', '²îÜªæaæÆ', '²îÜªæaÆ'),
]

img = Image.new('RGB', (800, len(tests) * 50 + 40), (255, 255, 255))
draw = ImageDraw.Draw(img)

y = 20
for label, opt1, opt2 in tests:
    draw.text((10, y), label, fill=(0,0,150), font=noto_font)
    draw.text((300, y), f"Opt1: {opt1}", fill=(0,0,0), font=shree_font)
    draw.text((550, y), f"Opt2: {opt2}", fill=(180,0,0), font=shree_font)
    y += 50

img.save('scratch/anusvara_test.png')
print("Saved scratch/anusvara_test.png")
