with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

content = content.replace(r"content += \"  'प्र': '\\uF09C\\uF0E2',\\n\" # 156 (Full-Pa) + 226 (slant)", r"content += \"  'प्र': '\\uF09F',\\n\" # 159 (Precomposed Pra)")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
