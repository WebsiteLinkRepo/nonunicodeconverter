import re

with open('/home/samuelvictor/nonunicodeconverter.com/src/components/TextConverter.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the invalid JS {t.tooltip...}
content = content.replace(
    'disabledFontTooltip.innerHTML = `<div class="absolute -top-1 left-4 w-2 h-2 bg-[#2D3039] border-t border-l border-[#40434F] rotate-45"></div>{t.tooltipExactFont}`;',
    'disabledFontTooltip.innerHTML = `<div class="absolute -top-1 left-4 w-2 h-2 bg-[#2D3039] border-t border-l border-[#40434F] rotate-45"></div>${document.getElementById("i18n-data").dataset.exact}`;'
)

with open('/home/samuelvictor/nonunicodeconverter.com/src/components/TextConverter.astro', 'w', encoding='utf-8') as f:
    f.write(content)
print("fixed js literal")
