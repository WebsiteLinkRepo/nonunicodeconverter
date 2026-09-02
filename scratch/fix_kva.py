import re

with open('src/utils/mappings/shreeLipi.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix 'क्व' mappings
replacements = {
    'to: "¹$m"': 'to: "Šdm"',
    'to: "{¹$"': 'to: "{Šd"',
    'to: "¹$r"': 'to: "Šdr"',
    'to: "¹$w"': 'to: "Šdw"',
    'to: "¹$y"': 'to: "Šdy"',
    'to: "¹$o"': 'to: "Šdo"',
    'to: "¹$¡"': 'to: "Šd¡"',
    'to: "¹$mo"': 'to: "Šdmo"',
    'to: "¹$m¡"': 'to: "Šdm¡"',
    'to: "¹$§"': 'to: "Šd§"',
    'to: "¹$©"': 'to: "Šd©"',
}

# We need to specifically target 'from: "क्व"' etc because ¹$ is also used for something else? Wait.
# If ¹$ is 'क्क', then where is 'क्क' mapped?
# "क्क" is mapped to "¸$" ! So ¹$ was incorrectly assigned!
# Let's cleanly replace the kva mappings:

text = text.replace('{ from: "क्वा", to: "¹$m" }', '{ from: "क्वा", to: "Šdm" }')
text = text.replace('{ from: "क्वि", to: "{¹$" }', '{ from: "क्वि", to: "{Šd" }')
text = text.replace('{ from: "क्वी", to: "¹$r" }', '{ from: "क्वी", to: "Šdr" }')
text = text.replace('{ from: "क्वु", to: "¹$w" }', '{ from: "क्वु", to: "Šdw" }')
text = text.replace('{ from: "क्वू", to: "¹$y" }', '{ from: "क्वू", to: "Šdy" }')
text = text.replace('{ from: "क्वे", to: "¹$o" }', '{ from: "क्वे", to: "Šdo" }')
text = text.replace('{ from: "क्वै", to: "¹$¡" }', '{ from: "क्वै", to: "Šd¡" }')
text = text.replace('{ from: "क्वो", to: "¹$mo" }', '{ from: "क्वो", to: "Šdmo" }')
text = text.replace('{ from: "क्वौ", to: "¹$m¡" }', '{ from: "क्वौ", to: "Šdm¡" }')
text = text.replace('{ from: "क्वं", to: "¹$§" }', '{ from: "क्वं", to: "Šd§" }')
text = text.replace('{ from: "क्व", to: "¹$" }', '{ from: "क्व", to: "Šd" }')
text = text.replace('{ from: "र्क्व", to: "¹$©" }', '{ from: "र्क्व", to: "Šd©" }')


with open('src/utils/mappings/shreeLipi.ts', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed 'क्व' mappings!")
