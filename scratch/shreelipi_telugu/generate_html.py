import os
from fontTools.ttLib import TTFont
import base64

font_path = '/home/samuelvictor/Downloads/Shree-Tel-0908 Regular/Shree-Tel-0908 Regular.ttf'

with open(font_path, "rb") as f:
    font_b64 = base64.b64encode(f.read()).decode('ascii')

html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Shree-Tel-0908 Glyph Map</title>
    <style>
        @font-face {{
            font-family: 'ShreeTel';
            src: url(data:font/truetype;charset=utf-8;base64,{font_b64}) format('truetype');
        }}
        body {{
            font-family: sans-serif;
            background: #f4f4f4;
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            padding: 20px;
        }}
        .glyph-box {{
            background: white;
            border: 1px solid #ccc;
            width: 100px;
            height: 120px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            box-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        }}
        .code {{
            font-size: 10px;
            color: #666;
            margin-bottom: 5px;
        }}
        .char {{
            font-family: 'ShreeTel';
            font-size: 40px;
            color: black;
            line-height: 1;
        }}
        .char-str {{
            font-size: 10px;
            color: blue;
            margin-top: 5px;
        }}
		.input-section {{
			width: 100%;
			margin-bottom: 20px;
		}}
		textarea {{
            font-family: 'ShreeTel';
            font-size: 30px;
			width: 100%;
			height: 100px;
		}}
    </style>
</head>
<body>
	<div class="input-section">
		<h2>Test Input</h2>
		<textarea id="tester" placeholder="Type letters here to see them in Shree-Tel..."></textarea>
	</div>
"""

tt = TTFont(font_path)
cmap = tt.getBestCmap()

# Generate the boxes
for code in sorted(cmap.keys()):
    char = chr(code)
    # properly escape char for HTML string
    char_str = repr(char)
    hex_code = hex(code)

    html += f"""
    <div class="glyph-box">
        <div class="code">{hex_code} ({code})</div>
        <div class="char">&#{code};</div>
        <div class="char-str">{char_str}</div>
    </div>
    """

html += """
</body>
</html>
"""

with open('scratch/shreelipi_telugu/glyph_map_interactive.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Generated HTML mapping at scratch/shreelipi_telugu/glyph_map_interactive.html")
