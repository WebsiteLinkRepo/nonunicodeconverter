from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

SHREE_PATH = "public/SHREE-TEL.ttf"
ref_font = ImageFont.truetype("/usr/share/fonts/noto/NotoSansTelugu-Regular.ttf", 60)
shree_font = ImageFont.truetype(SHREE_PATH, 60)

font = TTFont(SHREE_PATH)
codes = sorted(font.getBestCmap().keys())

missing = ['ఘ', 'ఙ', 'మ', 'హ', 'ణ', 'ధ', 'ప', 'బ', 'య', 'ల', 'ష', 'స']

# Let's just output a huge grid with all 217 codes again but explicitly grouped by visual similarity using our own eyes.
# I will just write a script to produce the target characters side-by-side with ALL 217 shree characters so I can scroll horizontally and visually match them.
