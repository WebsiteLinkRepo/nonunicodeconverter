with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

# Add a specific mapping for 'ैं'
# Wait, my engine uses a character-by-character replacement. 
# Will it replace 'ैं' correctly?
# Yes, because it sorts keys by length descending! 'ैं' (length 2) will be replaced before 'ै' (length 1).

content = content.replace("content += \"};\\n\"", "  'ैं': '{get_char(248)}',\\n" + "content += \"};\\n\"")

with open('generate_neo_final3.py', 'w') as f:
    f.write(content)
