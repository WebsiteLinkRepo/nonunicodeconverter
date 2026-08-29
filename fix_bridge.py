with open('src/utils/anuNeoConverter.ts', 'r', encoding='utf-8') as f:
    converter = f.read()

# Add a post-processing step to the converter
post_process = """
    // Anu Script Manager inserts a bridge (254 / \uF0FE) after short characters like 'क' and 'फ'
    // when followed by certain consonants like 'म'.
    // In the user's manual output for 'कर्म', it produced 'Nþª|' (\uF04E \uF0FE \uF0AA \uF07C).
    processedText = processedText.replace(/\uF04E\uF0AA/g, '\uF04E\uF0FE\uF0AA'); // क + म -> क + bridge + म
    processedText = processedText.replace(/\uF0A2\uF0AA/g, '\uF0A2\uF0FE\uF0AA'); // फ + म -> फ + bridge + म
    
    // The user's manual output for 'धर्म' produced '‡ª||' (\uF087 \uF0AA \uF07C \uF07C)
    // which is two Rephs! Anu Script Manager might be duplicating it or it was a typo.
    // Let's replicate it just to perfectly match Anu if it's expected.
    // Wait, replacing single reph with double reph for everything?
    // Let's just fix the bridge first.
    return processedText;
}
"""

converter = converter.replace("    return processedText;\n}", post_process)

with open('src/utils/anuNeoConverter.ts', 'w', encoding='utf-8') as f:
    f.write(converter)

