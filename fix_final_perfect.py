with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

# Fix Candrabindu to 229 (the perfect pre-built glyph)
content = content.replace("'{get_char(125)}{get_char(254)}{get_char(230)}'", "'{get_char(229)}'")
content = content.replace("'{get_char(230)}{get_char(125)}'", "'{get_char(229)}'") # in case it was this

# Remove the bridge from Aah (because it created a gap!)
content = content.replace("'{get_char(69)}{get_char(254)}{get_char(231)}'", "'{get_char(69)}{get_char(231)}'")
content = content.replace("'{get_char(69)}{get_char(254)}{get_char(231)}{get_char(122)}'", "'{get_char(69)}{get_char(231)}{get_char(122)}'")
content = content.replace("'{get_char(69)}{get_char(254)}{get_char(231)}{get_char(123)}'", "'{get_char(69)}{get_char(231)}{get_char(123)}'")
content = content.replace("'{get_char(69)}{get_char(254)}{get_char(231)}{get_char(125)}'", "'{get_char(69)}{get_char(231)}{get_char(125)}'")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
