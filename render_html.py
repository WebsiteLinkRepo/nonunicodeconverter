import json
html = """
<html>
<head>
<style>
@font-face {
    font-family: 'NeoGaneshBold';
    src: url('./dist/Fonts folder/AnuSM/ttf/NEOGANBO.TTF');
}
body { font-family: sans-serif; }
table { border-collapse: collapse; }
td { border: 1px solid #ccc; padding: 10px; text-align: center; }
.neo { font-family: 'NeoGaneshBold'; font-size: 40px; color: blue; }
.code { font-size: 16px; color: #666; }
</style>
</head>
<body>
<table>
"""
for i in range(32, 256):
    if i % 8 == 0: html += "<tr>\n"
    # use PUA offset
    char_str = f"&#{61440 + i};"
    html += f"<td><div class='neo'>{char_str}</div><div class='code'>{i}</div></td>\n"
    if i % 8 == 7: html += "</tr>\n"
html += "</table></body></html>"
with open('map.html', 'w') as f:
    f.write(html)
