import re

with open('scratch/ULTIMATE_OUTPUT.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Look for occurrences of 'यु' mapping in output
matches = re.findall(r'.{0,5}`w.{0,5}', text)
print("Matches for `w (यु):", matches)
