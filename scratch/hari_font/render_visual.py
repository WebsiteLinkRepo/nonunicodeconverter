from PIL import Image, ImageDraw, ImageFont
import sys

FONT_PATH = "/home/samuelvictor/Downloads/hari.ttf"

try:
    font = ImageFont.truetype(FONT_PATH, 48)
except Exception as e:
    print(f"PIL ImageFont error: {e}")
    sys.exit(1)

# Render the text
text = "Birt a[k (v(vFtiY) Br[li[ d[S C[, ¶yi> alg-alg ri¶yi[mi> li[ki[ j&d)-j&d) BiPiai[ bi[l[ C[. ah)>n) s>AkZ(t, kli an[ pr>priai[ (vVBrmi> p\²yit C[. (SxN an[ (vXinni x[#mi> pN g&jrit[ K*b p\g(t kr) C[. (vwiY„ai[a[ pi[tin) mitZBiPin&> sºmin krv&> ji[Ea[ an[ siY[ j Xinni[ Äyip vFirvi miT[ aºy BiPiai[ pN S)Kv) ji[Ea[. @(c an&sir nv) vAt&ai[ S)KviY) b&(Üni[ (vkis Yiy C[. k|mS: an[ ~mp*v<k kiy< krviY) sfLti ci[Ês mL[ C[. vZxi[ vivi[, pyi<vrN bcivi[ an[ pZ¸v)n[ h(ryiL) bnivi[."

# We need to render it multiline
words = text.split(" ")
lines = []
current_line = ""
for word in words:
    if len(current_line) + len(word) > 40:
        lines.append(current_line)
        current_line = word + " "
    else:
        current_line += word + " "
lines.append(current_line)

img = Image.new("RGB", (1200, len(lines) * 60 + 40), (255, 255, 255))
d = ImageDraw.Draw(img)

for i, line in enumerate(lines):
    d.text((20, 20 + i * 60), line, font=font, fill=(0, 0, 0))

img.save("scratch/hari_font/rendering_test.png")
print("Saved visually to scratch/hari_font/rendering_test.png")
