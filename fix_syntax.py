with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

# Just replace the last bit
import re
content = re.sub(r"f\.write\(content\).*", "f.write(content)", content, flags=re.DOTALL)

# Add the ru logic correctly
content = content.replace("content += \"};\n\"", "content += \"  'रु': '\\\\uF0BB',\\n\"\ncontent += \"  'रू': '\\\\uF0BF',\\n\"\ncontent += \"};\n\"")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
