with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

content = content.replace("'{get_char(230)}{get_char(125)}'", "'{get_char(125)}{get_char(254)}{get_char(230)}'")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
