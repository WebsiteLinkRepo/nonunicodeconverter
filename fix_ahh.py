with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

# Fix Independent Vowels that use अ (69) to use the bridge 254
content = content.replace("'{get_char(69)}{get_char(231)}'", "'{get_char(69)}{get_char(254)}{get_char(231)}'")
content = content.replace("'{get_char(69)}{get_char(231)}{get_char(122)}'", "'{get_char(69)}{get_char(254)}{get_char(231)}{get_char(122)}'")
content = content.replace("'{get_char(69)}{get_char(231)}{get_char(123)}'", "'{get_char(69)}{get_char(254)}{get_char(231)}{get_char(123)}'")
content = content.replace("'{get_char(69)}{get_char(231)}{get_char(125)}'", "'{get_char(69)}{get_char(254)}{get_char(231)}{get_char(125)}'")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
