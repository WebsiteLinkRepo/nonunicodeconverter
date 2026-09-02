import os

with open('scratch/TELUGU_ALL_IN_ONE_OUTPUT.txt', 'r', encoding='utf-8') as f:
    text1 = f.read().strip()

with open('scratch/OUR_OUTPUT.txt', 'r', encoding='utf-8') as f:
    text2 = f.read().strip()

print(f"Competitor len: {len(text1)}, Our len: {len(text2)}")
print(f"Are they identical? {text1 == text2}")

if text1 != text2:
    for i, (c1, c2) in enumerate(zip(text1, text2)):
        if c1 != c2:
            print(f"Difference at pos {i}: comp={repr(c1)} (0x{ord(c1):X}), our={repr(c2)} (0x{ord(c2):X})")
            break
