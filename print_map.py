import re

with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

matches = re.findall(r"'([^']+)':\s*(\d+)", content)
for char, code in matches:
    if 80 <= int(code) <= 100:
        print(f"{char}: {code} ({chr(int(code))})")
