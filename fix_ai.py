with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

content = content.replace("'{get_char(76)}{get_char(123)}'", "'{get_char(76)}{get_char(122)}'")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
