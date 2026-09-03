from PIL import Image, ImageDraw, ImageFont

font_path = 'public/SHREE-DEV-0708.ttf'
font = ImageFont.truetype(font_path, 28)
label_font = ImageFont.load_default()

lines = [
    ('Input Sentence (Fixed vs Competitor Error):', '_amR>r hr _hmamï´>mMr amO^mfm AgyZ {Vbm Iyn _moR>m Am{U g_¥Õ B{Vhmg bm^bm Amho.'),
    ('Eyelash-ra (Marathi Distinctive):', 'Hw$èhmS>, dèhmS>, Vèhm, MèhmQ>, H$mèhmim, g§H«$m§V, JèhmUo'),
    ('Halant Lla before consonants (ù):', 'S>moù`m§V, H$ù`m, Ji$mg, MmiUr, H$mi^¡ad, Om§^im'),
    ('Complex Conjuncts & Matras:', 'CÀN²>dmg, d¡{eï²`, ñ\\y${V©, AmÐ©, Ñ{ïH$moZ, àkm, ñdmV§Í`, ApñVËd, Á`oð')
]

img = Image.new('RGB', (1100, 360), color='white')
draw = ImageDraw.Draw(img)

y = 20
for title, text in lines:
    draw.text((20, y), title, fill='#666666', font=label_font)
    draw.text((20, y + 18), text, fill='black', font=font)
    y += 80

img.save('scratch/all_verified_marathi_render.png')
print('Saved scratch/all_verified_marathi_render.png')
