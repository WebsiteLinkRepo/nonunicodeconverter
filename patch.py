with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

content = content.replace(r"content += \"  'र्': '\\uF0A5',\\n\"   # 165 (Reph)", r"content += \"  'र्': '\\uF07C',\\n\"   # 124 (Reph)")
content = content.replace(r"content += \"  'प्र': '\\uF0A1\\uF0E2',\\n\" # 161 (Full-Pa) + 226 (slant)", r"content += \"  'प्र': '\\uF09C\\uF0E2',\\n\" # 156 (Full-Pa) + 226 (slant)")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
