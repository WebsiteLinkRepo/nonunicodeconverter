import os
from PIL import Image, ImageDraw, ImageFont

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
noto_path = '/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf'

shree_font = ImageFont.truetype(font_path, 36)
noto_font = ImageFont.truetype(noto_path, 28)
label_font = ImageFont.load_default()

test_words = [
  ('తెలుగు', '™öËðVð'),
  ('భాష', '¿éÙæ'),
  ('ద్రావిడ', '§–éÑyæ'),
  ('కుటుంబానికి', 'aðrðÆºé°aì'),
  ('చెందిన', '^öÆ¨¯æ'),
  ('విశిష్టమైన', 'ÑÕÙsæÄø¯æ'),
  ('ప్రాచీన', '²–é`¯æ'),
  ('భారతదేశంలో', '¿éˆæ™æ§÷ÔæÆËú'),
  ('అత్యధిక', 'A™Ÿæ¤aæ'),
  ('ప్రజలు', '²–æ\æËð'),
  ('మాట్లాడే', 'ÄérÏéy÷'),
  ('హోదా', '˜ú§é'),
  ('లభించింది', 'ËæÀÆ_Æ¨'),
  ('అజంత', 'A\æÆ™æ'),
  ('ప్రసిద్ధి', '²–æÜì§Éì'),
  ('క్రీస్తుపూర్వం', 'a–íÜªð²óˆÓæÆ'),
  ('శ్రీనాథుని', '}¯é£ð°'),
  ('ఆణిముత్యాలుగా', 'B~ìÄð™ŸéËðVé')
]

cols = 3
rows = (len(test_words) + cols - 1) // cols
cell_w, cell_h = 420, 110

img = Image.new('RGB', (cols * cell_w + 40, rows * cell_h + 40), (255, 255, 255))
draw = ImageDraw.Draw(img)

for idx, (uni, nonuni) in enumerate(test_words):
    c = idx % cols
    r = idx // cols
    x = 20 + c * cell_w
    y = 20 + r * cell_h

    draw.rectangle([x, y, x + cell_w - 6, y + cell_h - 6], outline=(200, 200, 200))
    draw.text((x + 10, y + 8), f"Unicode:", fill=(120, 0, 0), font=label_font)
    draw.text((x + 80, y + 4), uni, fill=(0, 0, 0), font=noto_font)

    draw.text((x + 10, y + 50), f"Shree-Tel:", fill=(0, 100, 0), font=label_font)
    draw.text((x + 80, y + 42), nonuni, fill=(0, 0, 120), font=shree_font)

img.save('scratch/test_words_render.png')
print("Saved scratch/test_words_render.png")
