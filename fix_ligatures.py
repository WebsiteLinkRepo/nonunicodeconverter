import re

with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

ligature_overrides = """
content += "  'क्ष': '{get_char(113)}',\n"
content += "  'ज्ञ': '{get_char(114)}',\n"
content += "  'त्र': '{get_char(222)}',\n"
content += "  'श्र': '{get_char(200)}',\n"
content += "  'द्र': '{get_char(252)}',\n"
content += "  'द्य': '{get_char(246)}',\n"
content += "  'ट्ट': '{get_char(242)}',\n"
content += "  'द्व': '{get_char(251)}',\n"
content += "  'त्त': '{get_char(240)}',\n"
content += "  'र्': '{get_char(165)}',\n"  # Flying R / Reph
content += "  'प्र': '{get_char(151)}{get_char(226)}',\n" # Pra = half-Pa + slant line
"""

# Insert these overrides before the closing brace
content = content.replace("content += \"  'रू': '\\\\uF0BF',\\n\"\ncontent += \"};\\n\"", "content += \"  'रू': '\\\\uF0BF',\\n\"\n" + ligature_overrides + "content += \"};\\n\"")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
