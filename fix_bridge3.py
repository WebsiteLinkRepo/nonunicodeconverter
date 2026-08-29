with open('src/utils/anuNeoConverter.ts', 'r', encoding='utf-8') as f:
    lines = f.readlines()

out_lines = []
skip = False
for line in lines:
    if "const noBridgeMatras =" in line:
        skip = True
    if skip and "return processedText;" in line:
        skip = False
        out_lines.append("""    // Ka and Pha need a bridge (\\uF0FE) to complete their width (they advance 400, but ink goes to 600).
    // The bridge should be added AFTER any narrow matras (like ु, ू, ृ, ं) attached to them.
    // Do NOT add a bridge if they are followed by wide matras (ा, ी) or halant (्).
    const narrowMatras = '\\uF0EC\\uF0EE\\uF077\\uF0E6\\uF0E5\\uF07D\\uF024\\uF03A';
    const bridgeRegex = new RegExp(`([\\uF04E\\uF0A2][${narrowMatras}]*)(?![\\uF0E7\\uF079\\uF07E\\uF0FE])`, 'g');
    processedText = processedText.replace(bridgeRegex, '$1\\uF0FE');

""")
    if not skip:
        out_lines.append(line)

with open('src/utils/anuNeoConverter.ts', 'w', encoding='utf-8') as f:
    f.write("".join(out_lines))
