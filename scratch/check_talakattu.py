import os
import re

out_path = 'scratch/TELUGU_COMPLEX_PARAS_OUTPUT.txt'
with open(out_path, 'r', encoding='utf-8') as f:
    text = f.read()

# We want to see every base consonant (as defined in our TS file) and whether it's followed by 'æ'
# We have a known list of base consonants:
base_chars = "a Q V R Z ^ b \\ m p r u y | ~ ™ £ § ® ¯ ² ¸ º ¿ Ä Å ˆ Ë Ð Ô Ù Ü ˜ Ã „ ‚"

base_consonants = {c: c for c in base_chars.split(' ')}
has_talakattu = {c: False for c in base_chars.split(' ')}
for c in base_chars.split(' '):
    if c + 'æ' in text:
        has_talakattu[c] = True

# Also we want to test TELUGU_ALL_IN_ONE_OUTPUT.txt if it exists. Wait, it doesn't.
# Let's just output the truth from the text!
print("From complex paras output:")
for k, v in has_talakattu.items():
    print(k, "needs talakattu:", v)

