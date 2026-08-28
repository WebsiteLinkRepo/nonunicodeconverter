with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

content = content.replace("'{get_char(127)',\\n\"", "'{get_char(127)}',\\n\"")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
