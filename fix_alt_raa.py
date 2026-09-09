import re
with open('/home/samuelvictor/nonunicodeconverter.com/src/components/TextConverter.astro', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '          Alternative Raa Vatthu\n          <svg xmlns="http://www.w3.org/2000/svg"',
    '          {t.altRaaVatthuLabel}\n          <svg xmlns="http://www.w3.org/2000/svg"'
)

with open('/home/samuelvictor/nonunicodeconverter.com/src/components/TextConverter.astro', 'w', encoding='utf-8') as f:
    f.write(content)
