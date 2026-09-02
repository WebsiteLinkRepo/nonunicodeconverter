#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
REF = ImageFont.truetype("/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf", 100)
LBL = ImageFont.load_default(19)
items = [
    ('అ','a'),('ఆ','aa'),('ఇ','i'),('ఈ','ii'),('ఉ','u'),('ఊ','uu'),
    ('ఋ','vocalic R'),('ౠ','vocalic RR'),('ఌ','vocalic L'),('ఎ','e'),('ఏ','ee'),
    ('ఐ','ai'),('ఒ','o'),('ఓ','oo'),('ఔ','au'),
    ('క','ka'),('ఖ','kha'),('గ','ga'),('ఘ','gha'),('ఙ','nga'),
    ('చ','ca'),('ఛ','cha'),('జ','ja'),('ఝ','jha'),('ఞ','nya'),
    ('ట','Ta'),('ఠ','Tha'),('డ','Da'),('ఢ','Dha'),('ణ','Na'),
    ('త','ta'),('థ','tha'),('ద','da'),('ధ','dha'),('న','na'),
    ('ప','pa'),('ఫ','pha'),('బ','ba'),('భ','bha'),('మ','ma'),
    ('య','ya'),('ర','ra'),('ఱ','Ra'),('ల','la'),('ళ','La'),
    ('వ','va'),('శ','sha'),('ష','Sha'),('స','sa'),('హ','ha'),
    ('క్ష','ksha'),('అం','anusvara'),('అః','visarga'),('క్','ka+virama'),
]
CW, CH, COLS = 280, 215, 5
rows = (len(items) + COLS - 1) // COLS
img = Image.new("RGB", (COLS*CW, rows*CH), "white")
d = ImageDraw.Draw(img)
for i,(t,n) in enumerate(items):
    x,y = (i%COLS)*CW, (i//COLS)*CH
    d.rectangle([x,y,x+CW-1,y+CH-1], outline="#bbb")
    d.text((x+8,y+6), n, fill="red", font=LBL)
    d.text((x+55,y+45), t, fill="black", font=REF)
img.save("scratch/ref_sheet.png")
print("wrote scratch/ref_sheet.png")
