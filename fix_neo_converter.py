with open('src/utils/anuNeoConverter.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the old specific bridge replacements
import re
content = re.sub(r"processedText = processedText\.replace\(/\\uF04E\\uF0AA/g, '\\uF04E\\uF0FE\\uF0AA'\);.*?\n", "", content)
content = re.sub(r"processedText = processedText\.replace\(/\\uF0A2\\uF0AA/g, '\\uF0A2\\uF0FE\\uF0AA'\);.*?\n", "", content)

# Add the new universal bridge replacement
bridge_logic = """
    // Insert bridge \uF0FE after क (\uF04E) and फ (\uF0A2) if they are NOT followed by matras that attach directly.
    // Matras that DO NOT need a bridge: \uF0E7 (ा), \uF079 (ी), \uF0EC (ु), \uF0EE (ू), \uF077 (ृ), \uF07E (्), \uF0E6 (ं), \uF03A (ः), \uF0E5 (ँ), \uF07D (ॅ)
    // Also \uF0FE itself (so we don't double bridge)
    const noBridgeMatras = '\\uF0E7\\uF079\\uF0EC\\uF0EE\\uF077\\uF07E\\uF0E6\\uF03A\\uF0E5\\uF07D\\uF0FE';
    const bridgeRegex = new RegExp(`([\\uF04E\\uF0A2])([^${noBridgeMatras}])`, 'g');
    processedText = processedText.replace(bridgeRegex, '$1\\uF0FE$2');
    processedText = processedText.replace(/([\\uF04E\\uF0A2])$/g, '$1\\uF0FE');
"""

content = content.replace("    return processedText;", bridge_logic + "\n    return processedText;")

with open('src/utils/anuNeoConverter.ts', 'w', encoding='utf-8') as f:
    f.write(content)
