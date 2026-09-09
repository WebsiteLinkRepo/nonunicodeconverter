import re

with open('/home/samuelvictor/nonunicodeconverter.com/src/components/TextConverter.astro', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    "Select exact font to paste formatted text directly into Word/Photoshop with this font.",
    "{t.tooltipExactFont}"
)
content = content.replace(
    "Only check this box if you are using these fonts:",
    "{t.tooltipAltRaaTitle}"
)
content = content.replace(
    "These specific fonts have their Ra Vatthu (్ర) drawn on the right side of the letter. This formats the text properly for them.",
    "{t.tooltipAltRaaWhy}"
)
with open('/home/samuelvictor/nonunicodeconverter.com/src/components/TextConverter.astro', 'w', encoding='utf-8') as f:
    f.write(content)
print("done html tooltips")
