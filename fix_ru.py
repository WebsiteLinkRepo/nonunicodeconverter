with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

# Add the overrides before the closing brace
ru_overrides = """
content += "  'रु': '\\u00BB',\n"
content += "  'रू': '\\u00BF',\n"
"""
content = content.replace("};\n", ru_overrides + "};\n")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
