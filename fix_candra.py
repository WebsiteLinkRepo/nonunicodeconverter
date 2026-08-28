with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

# Fix candra bindings
content = content.replace("get_char(124)}',\\n\"", "get_char(125)}',\\n\"")
content = content.replace("'ॅ': 124", "'ॅ': 125")
content = content.replace("'ँ': 125", "'ँ': '{get_char(125)}{get_char(88)}'")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
