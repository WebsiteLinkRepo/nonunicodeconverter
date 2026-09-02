from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
noto_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'
shree_font = ImageFont.truetype(font_path, 36)
noto_font = ImageFont.truetype(noto_path, 28)
label_font = ImageFont.load_default()

# Let's test combinations for:
# 1. తెలుగు
# 2. భాష
# 3. ద్రావిడ
# 4. కుటుంబానికి
# 5. చెందిన
# 6. విశిష్టమైన
# 7. ప్రాచీన
# 8. దక్షిణ
# 9. భారతదేశంలో
# 10. అత్యధిక

tests = [
    ("తెలుగు", [
        "™ðËîVî",
        "™ðËîV",
        "™ð Ëî Vî",
        # What is త + ె? Is there a precomposed 'తె'? Let's check glyphs
        # What is ల + ు? Is there a precomposed 'లు'?
        # What is గ + ు? Is there a precomposed 'గు'?
    ]),
]

img = Image.new('RGB', (800, 400), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Let's inspect all glyphs in the font and their shapes!
