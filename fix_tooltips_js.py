import re

with open('/home/samuelvictor/nonunicodeconverter.com/src/components/TextConverter.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert the hidden i18n div right before the script tag
i18n_div = """
    <!-- JS i18n data -->
    <div id="i18n-data" class="hidden" 
      data-disabled={t.tooltipDisabled}
      data-uncheck={t.tooltipUncheckAlt}
      data-check={t.tooltipCheckAlt}
      data-exact={t.tooltipExactFont}>
    </div>
"""

content = content.replace("<script>", i18n_div + "\n  <script>")

# Replace JS strings
content = content.replace(
    "const hoverReason = isAltRaa ? 'Uncheck Alt Raa Vatthu to use this font' : 'Check Alt Raa Vatthu to use this font';",
    "const i18nData = document.getElementById('i18n-data');\n    const hoverReason = isAltRaa ? i18nData.dataset.uncheck : i18nData.dataset.check;"
)

content = content.replace(
    "${opt.label} (disabled)</option>",
    "${opt.label} ${document.getElementById('i18n-data').dataset.disabled}</option>"
)

content = content.replace(
    "Select exact font to paste formatted text directly into Word/Photoshop with this font.",
    "${document.getElementById('i18n-data').dataset.exact}"
)

with open('/home/samuelvictor/nonunicodeconverter.com/src/components/TextConverter.astro', 'w', encoding='utf-8') as f:
    f.write(content)
print("done js tooltips")
