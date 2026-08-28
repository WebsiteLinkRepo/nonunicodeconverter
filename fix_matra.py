with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

content = content.replace("get_char(64)}',\\n\"", "get_char(231)}',\\n\"")
content = content.replace("get_char(64)}{get_char(122)}',\\n\"", "get_char(231)}{get_char(122)}',\\n\"")
content = content.replace("get_char(64)}{get_char(123)}',\\n\"", "get_char(231)}{get_char(123)}',\\n\"")
content = content.replace("get_char(64)}{get_char(124)}',\\n\"", "get_char(231)}{get_char(124)}',\\n\"")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
