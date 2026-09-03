from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

SHREE_PATH = "public/SHREE-TEL.ttf"
REF_PATH = "/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf"

shree_font = ImageFont.truetype(SHREE_PATH, 50)
ref_font = ImageFont.truetype(REF_PATH, 50)
label_font = ImageFont.load_default()

font = TTFont(SHREE_PATH)
cmap = font.getBestCmap()
codes = sorted(cmap.keys())

# Let us test every code combined with various modifiers:
# modifiers: bare (0), 0xe6 (talakattu), 0x24 (bottom tick), 0x2a, 0xad, 0x2c, 0xa2, 0xe9, 0xb7

def render_candidates_for(target_char, cand_tuples):
    # cand_tuples is list of (label, str_to_render)
    w = 120 * (len(cand_tuples) + 1) + 40
    img = Image.new("RGB", (w, 110), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Ref
    draw.text((15, 25), target_char, fill=(0, 140, 0), font=ref_font)
    draw.text((15, 5), "Reference", fill=(100, 100, 100), font=label_font)
    
    x = 130
    for lbl, s in cand_tuples:
        draw.text((x, 5), lbl, fill=(180, 0, 0), font=label_font)
        try:
            draw.text((x, 25), s, fill=(0, 0, 0), font=shree_font)
        except:
            pass
        x += 120
    return img

# Let us find candidates for:
# 1. ఘ (Gha)
# In Telugu fonts, Gha is sometimes composed of (something + something) or a single code.
# Let's test all single codes and pairs with 0xe6, 0x24, 0xad, etc.

