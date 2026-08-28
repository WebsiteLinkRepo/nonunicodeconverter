import re

with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

# Restore 64 for normal A-matra
content = content.replace("get_char(231)}',\\n\"", "get_char(64)}',\\n\"")
content = content.replace("get_char(231)}{get_char(122)}',\\n\"", "get_char(64)}{get_char(122)}',\\n\"")
content = content.replace("get_char(231)}{get_char(123)}',\\n\"", "get_char(64)}{get_char(123)}',\\n\"")
# Keep candra bindings but use 64 for base matra
content = content.replace("get_char(231)}{get_char(125)}',\\n\"", "get_char(64)}{get_char(125)}',\\n\"")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
