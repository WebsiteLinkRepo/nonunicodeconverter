import json

def get_char(v):
    # Map directly to the Private Use Area (PUA) where Anu fonts natively store their glyphs
    return chr(0xF000 + v)

map_dict = {
    '०': 48, '१': 49, '२': 50, '३': 51, '४': 52, '५': 53, '६': 54, '७': 55, '८': 56, '९': 57,
    'ा': 231, 'ं': 230, 'ः': 58,
    'अ': 69, 'इ': 70, 'उ': 71, 'ऊ': 72, 'ऋ': 73, 'ए': 76,
    
    'क्': 77, 'क': 78, 'ख्': 80, 'ख': 81, 'ग्': 83, 'ग': 84, 'घ्': 85, 'घ': 86, 'ङ': 87,
    'च्': 88, 'च': 89, 'छ': 90, 'ज्': 91, 'ज': 92, 'झ्': 93, 'झ': 94, 'ञ्': 95, 'ञ': 96,
    'ट': 98, 'ठ': 101, 'ड': 103, 'ढ': 106, 'ण्': 108, 'ण': 109,
    'त्': 110, 'त': 111, 'थ्': 115, 'द': 116, 'ध्': 134, 'ध': 135,
    'न्': 139, 'न': 140,
    
    'प्': 155, 'प': 156, 'फ्': 161, 'फ': 162, 'ब्': 163, 'ब': 164, 'भ्': 165, 'भ': 167, 
    'म्': 169, 'म': 170,
    
    'य्': 174, 'य': 175, 'र्': 128, 'र': 186, 'ल्': 193, 'ल': 194, 'व्': 195, 'व': 196,
    'श्': 197, 'श': 198, 'ष्': 201, 'ष': 202, 'स्': 203, 'स': 204, 'ह्': 208, 'ह': 210,
    
    'ळ': 112, 'क्ष': 223, 'ज्ञ': 114, 'त्र': 222, 'क्र': 139, 'प्र': 159,
    
    'ि': 117, 'ी': 121, 'ू': 120, 'े': 122, 'ै': 123, 'ृ': 119, 'ॅ': 124, '्': 126,
    '।': 64,

    # THE REAL U MATRA AND CANDRA BINDU
    'ु': 236,
    'ँ': 125,

    # RA-KAR LIGATURES:
    'श्र': 200,
    '्'+'र': 221, # Fallback diagonal stroke for ANY other consonant
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
content += f"  'द्र': '{get_char(183)}',\n"

# Overrides for complex/missing
content += f"  'थ': '{get_char(115)}{get_char(231)}',\n"
content += f"  'ई': '{get_char(70)}{get_char(128)}',\n"

# Complex Vowels
content += f"  'आ': '{get_char(69)}{get_char(231)}',\n"
content += f"  'ओ': '{get_char(69)}{get_char(231)}{get_char(122)}',\n"
content += f"  'औ': '{get_char(69)}{get_char(231)}{get_char(123)}',\n"
content += f"  'ॉ': '{get_char(231)}{get_char(124)}',\n"
content += f"  'ऑ': '{get_char(69)}{get_char(231)}{get_char(124)}',\n"

content += "};\n"

with open('src/utils/mappings/neo.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Generated neo.ts with PUA mapping!")
