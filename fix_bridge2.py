import re
with open('src/utils/anuNeoConverter.ts', 'r', encoding='utf-8') as f:
    content = f.read()

old_bridge_logic = r"""    const noBridgeMatras = '\\uF0E7\\uF079\\uF0EC\\uF0EE\\uF077\\uF07E\\uF0E6\\uF03A\\uF0E5\\uF07D\\uF0FE';
    const bridgeRegex = new RegExp(`([\\uF04E\\uF0A2])([^${noBridgeMatras}])`, 'g');
    processedText = processedText.replace(bridgeRegex, '$1\\uF0FE$2');
    processedText = processedText.replace(/([\\uF04E\\uF0A2])$/g, '$1\\uF0FE');"""

new_bridge_logic = r"""    // Ka and Pha need a bridge (\uF0FE) to complete their width (they advance 400, but ink goes to 600).
    // The bridge should be added AFTER any narrow matras (like ु, ू, ृ, ं) attached to them.
    // Do NOT add a bridge if they are followed by wide matras (ा, ी) or halant (्).
    const narrowMatras = '\\uF0EC\\uF0EE\\uF077\\uF0E6\\uF0E5\\uF07D\\uF024';
    // Match Ka/Pha followed by zero or more narrow matras.
    // Lookahead to ensure it's not followed by a wide matra, halant, or an existing bridge.
    const bridgeRegex = new RegExp(`([\\uF04E\\uF0A2][${narrowMatras}]*)(?![\\uF0E7\\uF079\\uF07E\\uF0FE])`, 'g');
    processedText = processedText.replace(bridgeRegex, '$1\\uF0FE');"""

if old_bridge_logic in content:
    content = content.replace(old_bridge_logic, new_bridge_logic)
else:
    print("Could not find old bridge logic!")

with open('src/utils/anuNeoConverter.ts', 'w', encoding='utf-8') as f:
    f.write(content)
