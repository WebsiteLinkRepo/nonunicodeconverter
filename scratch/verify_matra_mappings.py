from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
noto_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 36)
noto_font = ImageFont.truetype(noto_path, 28)
label_font = ImageFont.load_default()

# Let's test standard gunintham for 'క' (ka), 'త' (ta), 'ప' (pa), 'మ' (ma)
chars_to_test = [
    # ka series
    ('క', 'aæ'), ('కా', 'aé'), ('కి', 'aì'), ('కీ', 'aí'), ('కు', 'aî'), ('కూ', 'aï'),
    ('కె', 'að'), ('కే', 'añ'), ('కై', 'aò'), ('కొ', 'aö'), ('కో', 'aø'), ('కౌ', 'aú'),
    ('కృ', 'a#'), ('కం', 'aæÆ'), ('కః', 'aæ:'),
    # ta series
    ('త', '™æ'), ('తా', '™é'), ('తి', '†'), ('తీ', '¡'), ('తు', '™î'), ('తూ', '™ï'),
    ('తె', '™ð'), ('తే', '™ñ'), ('తై', '™ò'), ('తొ', '™ö'), ('తో', '™ø'), ('తౌ', '™ú'),
    ('తృ', '™#'), ('తం', '™æÆ'), ('తః', '™æ:'),
    # pa series
    ('ప', '²æ'), ('పా', '²é'), ('పి', '³'), ('పీ', '´'), ('పు', '²î'), ('పూ', '²ï'),
    ('పె', '²ð'), ('పే', '²ñ'), ('పై', '²ò'), ('పొ', '²ö'), ('పో', '²ø'), ('పౌ', '²ú'),
    ('పృ', '²#'), ('పం', '²æÆ'), ('పః', '²æ:'),
    # ma series
    ('మ', 'Äæ'), ('మా', 'Äé'), ('మి', 'Äì'), ('మీ', 'Äí'), ('ము', 'Äî'), ('మూ', 'Äï'),
    ('మె', 'Äð'), ('మే', 'Äñ'), ('మై', 'Äò'), ('మొ', 'Äö'), ('మో', 'Äø'), ('మౌ', 'Äú'),
    ('మృ', 'Ä#'), ('మం', 'ÄæÆ'), ('మః', 'Äæ:')
]

cols = 6
rows = (len(chars_to_test) + cols - 1) // cols
cell_w, cell_h = 160, 80

img = Image.new('RGB', (cols * cell_w + 20, rows * cell_h + 20), (255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, (uni, shree) in enumerate(chars_to_test):
    c = idx % cols
    r = idx // cols
    x = 10 + c * cell_w
    y = 10 + r * cell_h

    draw.rectangle([x, y, x + cell_w - 4, y + cell_h - 4], outline=(200, 200, 200))
    draw.text((x + 6, y + 4), uni, fill=(0, 0, 150), font=noto_font)
    draw.text((x + 60, y + 4), shree, fill=(0, 0, 0), font=shree_font)

img.save('scratch/matra_verification.png')
print("Saved scratch/matra_verification.png")
