with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

content = content.replace("content += \"};\n\"", "content += \"  'रु': '\\\\uF0BB',\\n\"\ncontent += \"  'रू': '\\\\uF0BF',\\n\"\ncontent += \"};\n\"")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
