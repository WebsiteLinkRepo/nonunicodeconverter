import re
with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

idx = content.find("content += \"  'रु': '\\uF0BB'")
if idx != -1:
    content = content[:idx]

ligatures = """
content += "  'रु': '\\\\uF0BB',\\n"
content += "  'रू': '\\\\uF0BF',\\n"
content += "  'क्ष': '\\\\uF071',\\n"  # 113
content += "  'ज्ञ': '\\\\uF072',\\n"  # 114
content += "  'त्र': '\\\\uF0DE',\\n"  # 222
content += "  'श्र': '\\\\uF0C8',\\n"  # 200
content += "  'द्र': '\\\\uF0FC',\\n"  # 252
content += "  'द्य': '\\\\uF0F6',\\n"  # 246
content += "  'द्व': '\\\\uF0FB',\\n"  # 251
content += "  'त्त': '\\\\uF0F0',\\n"  # 240
content += "  'द्द': '\\\\uF0B7',\\n"  # 183
content += "  'र्': '\\\\uF07E',\\n"   # 126 (Reph)
content += "  'प्र': '\\\\uF09B\\\\uF0E2',\\n" # 155 (half-Pa) + 226 (slant)
content += "};\\n"

with open('src/utils/mappings/neo.ts', 'w', encoding='utf-8') as f:
    f.write(content)
"""

content += ligatures

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
