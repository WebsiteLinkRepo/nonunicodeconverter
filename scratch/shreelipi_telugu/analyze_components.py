import os
from fontTools.ttLib import TTFont
import json

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'
tt = TTFont(font_path)
cmap = tt.getBestCmap()

# Map each character explicitly based on our 9 catalog pages
# We will create a comprehensive glyph index
glyph_info = {}

# Let's write out the known characters directly
# Pages 0 to 8:
# 0x20: space
# 0x21: !
# 0x22: '
# 0x23: ృ (matra vocalic R - small)
# 0x24: ృ (matra vocalic R - alternative)
# 0x25: %
# 0x26: - (horizontal dash/top line)
# 0x27: ,
# 0x28: (
# 0x29: )
# 0x2A: ా (aa matra)
# 0x2B: +
# 0x2C: ,
# 0x2D: -
# 0x2E: .
# 0x2F: /
# 0x30: 0
# 0x31: ౧ (telugu 1)
# 0x32: ౨ (telugu 2)
# 0x33: ౩ (telugu 3)
# 0x34: ౪ (telugu 4)
# 0x35: ౫ (telugu 5)
# 0x36: ౬ (telugu 6)
# 0x37: ౭ (telugu 7)
# 0x38: ౮ (telugu 8)
# 0x39: ౯ (telugu 9)
# 0x3A: :
# 0x3B: ;
# 0x3C: క్ష (ksha subscript/base)
# 0x3D: =
# 0x3E: ౕ (length mark / extender)
# 0x3F: ?
# 0x40: ః (visarga)
# 0x41: అ
# 0x42: ఆ
# 0x43: ఇ
# 0x44: ఈ
# 0x45: ఉ
# 0x46: ఊ
# 0x47: ఎ
# 0x48: ఏ
# 0x49: ఐ
# 0x4A: ఒ
# 0x4B: ఓ
# 0x4C: ఔ
# 0x4D: ऽ (avagraha)
# 0x4E: ా (aa matra)
# 0x4F: ౕ (extender)
# 0x50: ృ (vocalic r matra)
# 0x51: ఖ (kha base)
# 0x52: ఖ (kha base)
# 0x53: ఖి (khi)
# 0x54: ఖీ (khee)
# 0x55: ఖు (khu)
# 0x56: గ (ga base)
# 0x57: గ (ga full)
# 0x58: గి (gi)
# 0x59: గ (ga base)
# 0x5A: ఙ (nga)
# 0x5B: ు (u matra)
# 0x5C: జ (ja base)
# 0x5D: జు (ju)
# 0x5E: చ (cha base)
# 0x5F: చి (chi)
# 0x60: చీ (chee)
# 0x61: క (ka base)
# 0x62: ఛ (chha base)
# 0x63: ఛి (chhi)
# 0x64: ఛీ (chhee)
# 0x65: చు (chu)
# 0x66: జ (ja full)
# 0x67: జ (ja base)
# 0x68: జి (ji)
# 0x69: జీ (jee)
# 0x6A: జు (ju)
# 0x6B: జూ (joo)
# 0x6C: జౌ (jau)
# 0x6D: ఝ (jha)
# 0x6E: ఞ (nya)
# 0x6F: ౌ (au matra)
# 0x70: ఞ (nya)
# 0x71: ఞ (nya)
# 0x72: ట (ta base)
# 0x73: ట (ta full)
# 0x74: ఠ (tha base)
# 0x75: ఠ (tha)
# 0x76: ఠి (thi)
# 0x77: ఠీ (thee)
# 0x78: ఠు (thu)
# 0x79: డ (da base)
# 0x7A: డ (da full)
# 0x7B: ు (u matra - tall/straight)
# 0x7C: ఢ (dha base)
# 0x7D: శ్రీ (shree full ligature)
# 0x7E: ణ (nna base)
# 0xA1: తి (ti)
# 0xA2: ౕ (extender)
# 0xA3: థ (tha base)
# 0xA4: థ (tha full)
# 0xA5: థీ (thee)
# 0xA6: థు (thu)
# 0xA7: ద (da base)
# 0xA8: ద (da full)
# 0xA9: ది (di)
# 0xAA: ధ (dha base)
# 0xAB: ఁ (candrabindu or top tick)
# 0xAC: ౨ (two or ligature)
# 0xAE: ధు (dhu)
# 0xAF: న (na base)
# 0xB0: ని (ni)
# 0xB1: నీ (nee)
# 0xB2: ప (pa base)
# 0xB3: ప (pa full)
# 0xB4: పి (pi)
# 0xB5: పీ (pee)
# 0xB6: C (bracket or mark)
# 0xB7: • (bullet/dot)
# 0xB8: ఫ (pha base)
# 0xB9: ఫి (phi)
# 0xBA: బ (ba base)
# 0xBB: బ (ba full)
# 0xBC: బి (bi)
# 0xBD: బీ (bee)
# 0xBE: బ (ba alt)
# 0xBF: భ (bha base)
# 0xC0: భి (bhi)
# 0xC1: భీ (bhee)
# 0xC2: భు (bhu)
# 0xC3: భ (bha alt)
# 0xC4: మ (ma base) / య (ya base)
# 0xC5: మి (mi) / యి (yi)
# 0xC6: ం (anusvara / sunna)
# 0xC7: ర (ra base)
# 0xC8: రి (ri)
# 0xC9: ఢి (dhi)
# 0xCA: ళ (la base)
# 0xCB: ల (la base)
# 0xCC: ల (la full)
# 0xCD: లి (li)
# 0xCE: లీ (lee)
# 0xCF: లు (lu)
# 0xD0: వ (va base)
# 0xD1: వి (vi)
# 0xD2: వీ (vee)
# 0xD3: వ (va full)
# 0xD4: శ (sha base)
# 0xD5: శి (shi)
# 0xD6: శీ (shee)
# 0xD7: ణ (nna full)
# 0xD8: ణి (nni)
# 0xD9: ష (ssa base)
# 0xDA: షి (ssi)
# 0xDB: షీ (ssee)
# 0xDC: స (sa base)
# 0xDD: సి (si)
# 0xDE: సీ (see)
# 0xDF: హ (ha base)
# 0xE0: హ (ha full)
# 0xE1: హ (ha full)
# 0xE2: ళి (lli)
# 0xE3: ళీ (llee)
# 0xE4: ళు (llu)
# 0xE5: ళూ (lloo)
# 0xE6: ్ (virama / pollu / talakattu checkmark)
# 0xE7: ్ (virama)
# 0xE8: ్ (virama)
# 0xE9: ో (o matra top)
# 0xEA: ో (o matra)
# 0xEB: ో (o matra)
# 0xEC: ి (i matra)
# 0xED: ీ (ii matra)
# 0xEE: ీ (ii matra)
# 0xEF: ీ (ii matra)
# 0xF0: ు (u matra)
# 0xF1: ు (u matra)
# 0xF2: ు (u matra)
# 0xF3: ూ (uu matra)
# 0xF4: ూ (uu matra)
# 0xF5: ూ (uu matra)
# 0xF6: ై (ai matra)
# 0xF7: ై (ai matra)
# 0xF8: ై (ai matra)
# 0xF9: ై (ai matra)
# 0xFA: ా (aa matra)
# 0xFB: ా (aa matra)
# 0x152: ౯
# 0x153: ష
# 0x160: ౬
# 0x161: ష్మ (shma / complex)
# 0x178: ౌ
# 0x192: ఘ
# 0x2C6: ఙ
# 0x2DC: హ
# 0x2013: ు
# 0x2014: ూ
# 0x2018: |
# 0x2019: ★
# 0x201A: ఱ
# 0x201C: ౬
# 0x201D: ౬
# 0x201E: క్ష
# 0x2020: తి
# 0x2021: ళ్ళ
# 0x2022: _
# 0x2026: O
# 0x2030: ఱ
# 0x2039: ౬
# 0x2122: త

print("Mapped key components")
