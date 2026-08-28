with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

content = content.replace("'{get_char(code)}{get_char(254)}{get_char(121)}'", "'{get_char(code)}{get_char(121)}'")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
