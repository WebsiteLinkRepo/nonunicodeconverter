with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

# find the last occurrence of };\n
idx = content.rfind("};\n")
new_content = content[:idx] + "  'रु': '\\uF0BB',\n  'रू': '\\uF0BF',\n" + content[idx:]

with open('generate_neo_final3.py', 'w') as f:
    f.write(new_content)
