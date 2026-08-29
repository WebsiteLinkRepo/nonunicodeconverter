with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

idx = content.rfind("};\n\"")
# Actually, let's just append to the file directly before the write line!
