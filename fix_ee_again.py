with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

# Fix EE
content = content.replace("'ई': '{get_char(70)}{get_char(125)}'", "'ई': '{get_char(70)}{get_char(124)}'")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
