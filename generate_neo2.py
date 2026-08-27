import json

win1252_to_unicode = {
    128: 0x20AC, 129: 0x0081, 130: 0x201A, 131: 0x0192,
    132: 0x201E, 133: 0x2026, 134: 0x2020, 135: 0x2021,
    136: 0x02C6, 137: 0x2030, 138: 0x0160, 139: 0x2039,
    140: 0x0152, 141: 0x008D, 142: 0x017D, 143: 0x008F,
    144: 0x0090, 145: 0x2018, 146: 0x2019, 147: 0x201C,
    148: 0x201D, 149: 0x2022, 150: 0x2013, 151: 0x2014,
    152: 0x02DC, 153: 0x2122, 154: 0x0161, 155: 0x203A,
    156: 0x0153, 157: 0x009D, 158: 0x017E, 159: 0x0178
}
for i in range(160, 256):
    win1252_to_unicode[i] = i

def get_char(v):
    if v < 128:
        return chr(v)
    return chr(win1252_to_unicode[v])

# Create the base mapping
map_dict = {
    '०': 48, '१': 49, '२': 50, '३': 51, '४': 52, '५': 53, '६': 54, '७': 55, '८': 56, '९': 57,
    'ा': 64, 'ं': 65, 'ँ': 173, 'ः': 58,
    'अ': 69, 'इ': 70, 'उ': 71, 'ऊ': 72, 'ऋ': 73, 'ए': 76,
    
    'क्': 77, 'क': 78, 'ख्': 80, 'ख': 81, 'ग्': 83, 'ग': 84, 'घ्': 85, 'घ': 86, 'ङ': 87,
    'च्': 88, 'च': 89, 'छ': 90, 'ज्': 91, 'ज': 92, 'झ्': 93, 'झ': 94, 'ञ्': 95, 'ञ': 96,
    'ट': 98, 'ठ': 101, 'ड': 103, 'ढ': 106, 'ण्': 108, 'ण': 109,
    'त्': 110, 'त': 111, 'थ्': 115, 'द': 116, 'ध्': 134,
    # 'न्' is 139 but it fails in clipboard, so we use 140 (न) + 126 (्)
    
    'प्': 156, 'फ्': 161, 'ब्': 164, 'भ्': 167, 'म्': 170, 'य्': 174,
    'र': 186, 'ल्': 193, 'व्': 195, 'श्': 197, 'ष्': 201, 'స్': 204, 'स्': 204, 'ह्': 208,
    
    'ळ': 112, 'क्ष': 223, 'జ్ఞ': 114, 'ज्ञ': 114, 'त्र': 222,
    
    'ि': 117, 'ी': 121, 'ु': 119, 'ू': 120, 'े': 122, 'ै': 123, 'ृ': 125, 'ॅ': 124, '्': 126,
    '।': 64,
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

# Construct full characters from half characters + vertical bar (@)
constructed_full = {
    'न': get_char(140), # 140 is full 'न'
    'थ': get_char(115) + '@',
    'ध': get_char(134) + '@',
    'प': get_char(156) + '@',
    'फ': get_char(161) + '@',
    'ब': get_char(164) + '@',
    'भ': get_char(167) + '@',
    'म': get_char(170) + '@',
    'य': get_char(174) + '@',
    'ल': get_char(193) + '@',
    'व': get_char(195) + '@',
    'श': get_char(197) + '@',
    'ष': get_char(201) + '@',
    'स': get_char(204) + '@',
    'ह': get_char(208) + '@', # wait, does H take a vertical bar? Let's check 210 (h). It is full ह!
}

# Let me check 210 in big_grid.png for 'ह'. Yes, 210 is ह!
content += "  'ह': '" + get_char(210) + "',\n"
# Remove 'ह' from constructed_full
del constructed_full['ह']

# Wait, what about 'न्'? We can't use 139. We use 140 (न) + 126 (्).
content += "  'न्': '" + get_char(140) + "~',\n"

for k, v in constructed_full.items():
    content += f"  '{k}': '{v}',\n"

# Complex Vowels
content += "  'आ': 'E@',\n"
content += "  'ई': 'F',\n" # Let's hope F works for now
content += "  'ओ': 'E@z',\n"
content += "  'औ': 'E@{',\n"
content += "  'ॉ': '@|',\n"
content += "  'ऑ': 'E@|',\n"
content += "};\n"

with open('src/utils/mappings/neo.ts', 'w', encoding='utf-8') as f:
    f.write(content)

