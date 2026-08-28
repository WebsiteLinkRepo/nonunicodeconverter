with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

# Fix ai-matra
content = content.replace("'ै': 123", "'ै': 248")
# Wait, what about 'ौ'?
# In my script: 'ौ': '{get_char(231)}{get_char(123)}'
content = content.replace("get_char(123)}'", "get_char(248)}'")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
