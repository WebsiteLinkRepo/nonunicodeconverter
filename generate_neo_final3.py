import json

def get_char(v):
    return chr(0xF000 + v)

map_dict = {
    '०': 48, '१': 49, '२': 50, '३': 51, '४': 52, '५': 53, '६': 54, '७': 55, '८': 56, '९': 57,
    'क्': 77, 'क': 78, 'ख्': 80, 'ख': 81, 'ग्': 83, 'ग': 84, 'घ्': 85, 'घ': 86, 'ङ': 87,
    'च्': 88, 'च': 89, 'छ': 90, 'ज्': 91, 'ज': 92, 'झ्': 93, 'झ': 94, 'ञ्': 96, 'ञ': 97,
    'ट': 98, 'ठ': 101, 'ड': 103, 'ढ': 106, 'ण्': 108, 'ण': 109,
    'त्': 110, 'त': 111, 'थ्': 115, 'द': 116, 'ध्': 134, 'ध': 135,
    'न्': 139, 'न': 140,
    'प्': 155, 'प': 156, 'फ्': 161, 'फ': 162, 'ब्': 163, 'ब': 164, 'भ्': 165, 'भ': 167, 
    'म्': 169, 'म': 170,
    'य्': 175, 'र्': 124, 'र': 186, 'ल्': 193, 'ल': 194, 'व्': 195, 'व': 196,
    'श्': 197, 'श': 198, 'ष्': 201, 'ष': 202, 'स्': 203, 'स': 204, 'ह्': 208, 'ह': 210,
    'ळ': 112, 'क्ष': 223, 'ज्ञ': 114, 'त्र': 222, 
    'ि': 117, 'ी': 121, 'ू': 238, 'े': 122, 'ै': 123, 'ृ': 119,  '्': 126,
    'ु': 236,  'ं': 230, 'ः': 58,
    'अ': 69, 'इ': 70, 'उ': 71, 'ऊ': 72, 'ऋ': 74, 'ए': 76,
    '।': 64, 'श्र': 200,
}

content = "export const neoMap: { [key: string]: string } = {\n"

for k, v in map_dict.items():
    unicode_char = get_char(v)
    if unicode_char == '\\':
        content += f"  '{k}': '\\\\',\n"
    elif unicode_char == "'":
        content += f"  '{k}': '\\'',\n"
    else:
        content += f"  '{k}': '{unicode_char}',\n"

# Overrides for problematic ligatures
content += f"  '्र': '{get_char(221)}',\n"

# Build full consonants that don't have single glyphs
content += f"  'थ': '{get_char(115)}',\n"
content += f"  'य': '{get_char(174)}',\n"

# A-Matra logic: 
# Default A-matra is 64 (@).
content += f"  'ा': '{get_char(231)}',\n"

# O and AU matras using the default A-matra (64)
content += f"  'ो': '{get_char(231)}{get_char(122)}',\n"
content += f"  'ौ': '{get_char(231)}{get_char(123)}',\n"
content += f"  'ॉ': '{get_char(231)}{get_char(125)}',\n"

# Independent vowels using 64
content += f"  'आ': '{get_char(69)}{get_char(231)}',\n"
content += f"  'ओ': '{get_char(69)}{get_char(231)}{get_char(122)}',\n"
content += f"  'औ': '{get_char(69)}{get_char(231)}{get_char(123)}',\n"
content += f"  'ऑ': '{get_char(69)}{get_char(231)}{get_char(125)}',\n"
content += f"  'ई': '{get_char(70)}{get_char(124)}',\n"

# NOW, the magic! We override the gap characters to force them to use 231 (ç)!
# Characters that have gaps: भ (167), ष (202), ध (135)
# For थ and य, their "base" is the half character (115 and 174).
gap_chars = {'भ': 167, 'ष': 202, 'ध': 135, 'थ': 115, 'य': 174, 'श': 198}

for char, code in gap_chars.items():
    content += f"  '{char}ा': '{get_char(code)}{get_char(231)}',\n"
    content += f"  '{char}ो': '{get_char(code)}{get_char(231)}{get_char(122)}',\n"
    content += f"  '{char}ौ': '{get_char(code)}{get_char(231)}{get_char(123)}',\n"
    content += f"  '{char}ॉ': '{get_char(code)}{get_char(231)}{get_char(125)}',\n"



content += f"  'ऐ': '{get_char(76)}{get_char(122)}',\n"
content += f"  '़': '',\n"

content += f"  'ॅ': '{get_char(125)}',\n"
content += f"  'ँ': '{get_char(229)}',\n"

# Characters with short top lines need the 254 bridge before the A-matra!
short_chars = {'क': 78, 'फ': 162}
for char, code in short_chars.items():
    content += f"  '{char}ा': '{get_char(code)}{get_char(254)}{get_char(231)}',\n"
    content += f"  '{char}ो': '{get_char(code)}{get_char(254)}{get_char(231)}{get_char(122)}',\n"
    content += f"  '{char}ौ': '{get_char(code)}{get_char(254)}{get_char(231)}{get_char(123)}',\n"
    content += f"  '{char}ॉ': '{get_char(code)}{get_char(254)}{get_char(231)}{get_char(125)}',\n"
    
    # Also need bridge for right-side matras like 'ी' (121)
    # Wait, does 'की' need the bridge? Yes, I'll add 'की' manually.
    content += f"  '{char}ी': '{get_char(code)}{get_char(254)}{get_char(121)}',\n"


content += "  'ैं': \'\uF0F8\',\n"
content += "  'कू': '',\n"
content += "  'फू': '',\n"


content += "  'रु': '\\uF0BB',\n"
content += "  'रू': '\\uF0BF',\n"
content += "  'क्ष': '\\uF071',\n"  # 113
content += "  'ज्ञ': '\\uF072',\n"  # 114
content += "  'त्र': '\\uF0DE',\n"  # 222
content += "  'श्र': '\\uF0C8',\n"  # 200
content += "  'द्र': '\\uF0FC',\n"  # 252
content += "  'द्य': '\\uF0F6',\n"  # 246
content += "  'द्व': '\\uF0FB',\n"  # 251
content += "  'त्त': '\\uF0F0',\n"  # 240
content += "  'ट्ट': '\\uF0F2',\n"  # 242
content += "  'द्द': '\\uF0B7',\n"  # 183
content += "  'र्': '\\uF07C',\n"   # 124 (Reph)
content += "  'प्र': '\\uF09F',\n" # 159 (Precomposed Pra)
content += "};\n"
print(content)
