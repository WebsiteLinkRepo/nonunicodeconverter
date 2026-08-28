import re

with open('generate_neo_final3.py', 'r') as f:
    content = f.read()

matches = re.findall(r"'([^']+)':\s*(\d+)", content)
for char, code in matches:
    if 95 <= int(code) <= 120:
        print(f"{char}: {code} ({chr(int(code))})")
