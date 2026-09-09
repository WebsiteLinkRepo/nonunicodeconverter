import re

with open('/home/samuelvictor/nonunicodeconverter.com/src/components/TextConverter.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace optgroupLabel
content = re.sub(
    r'const optgroupLabel = isAltRaa\s*\n\s*\? "➜ Turn OFF \'Alt Raa Vatthu\' to unlock these fonts:"\s*\n\s*: "➜ Turn ON \'Alt Raa Vatthu\' to unlock these fonts:";',
    "const i18nData = document.getElementById('i18n-data');\n      const optgroupLabel = isAltRaa ? `➜ ${i18nData.dataset.uncheck}` : `➜ ${i18nData.dataset.check}`;",
    content
)

# Replace hoverReason
content = re.sub(
    r'let hoverReason = isAltRaa\s*\n\s*\? "Turn OFF \'Alternative Raa Vatthu\' to use these fonts \(we use the standard procedure to paste in these fonts\)\."\s*\n\s*: "Turn ON \'Alternative Raa Vatthu\' to use these fonts \(we use a different procedure to paste in these fonts\)\.";',
    "let hoverReason = isAltRaa ? i18nData.dataset.uncheck : i18nData.dataset.check;",
    content
)

with open('/home/samuelvictor/nonunicodeconverter.com/src/components/TextConverter.astro', 'w', encoding='utf-8') as f:
    f.write(content)
print("done hover reason")
