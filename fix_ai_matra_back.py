with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

# Fix ai-matra back to 123
content = content.replace("'ै': 248", "'ै': 123")
content = content.replace("get_char(248)}'", "get_char(123)}'")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
