with open("src/utils/converter.ts", "r") as f:
    text = f.read()

text = text.replace("import { unicodeToBamini } from './baminiConverter';", "import { unicodeToBamini } from './baminiConverter';\nimport { unicodeToAnuTamil, anuTamilToUnicode } from './anuTamilConverter';")

# Add dedicated engine branch
branch = """    if (encoding === 'anutamil' && script === 'tamil') {
      const convertedText = unicodeToAnuTamil(processedInput);
      const endTime = performance.now();
      return {
        convertedText,
        errors: [],
        stats: {
          inputCharCount: inputText.length,
          outputCharCount: convertedText.length,
          wordCount: inputText.trim().split(/\\s+/).length,
          lineCount: inputText.split('\\n').length,
          unmappedCount: 0,
          processingTimeMs: Math.max(0.1, Number((endTime - startTime).toFixed(2)))
        }
      };
    }"""

text = text.replace("    if (encoding === 'bamini' && script === 'tamil') {", f"{branch}\n    if (encoding === 'bamini' && script === 'tamil') {{")

# Add reverse support
reverse_branch = """    if (encoding === 'anutamil' && script === 'tamil') {
      const convertedText = anuTamilToUnicode(processedInput);
      const endTime = performance.now();
      return {
        convertedText,
        errors: [],
        stats: {
          inputCharCount: inputText.length,
          outputCharCount: convertedText.length,
          wordCount: inputText.trim().split(/\\s+/).length,
          lineCount: inputText.split('\\n').length,
          unmappedCount: 0,
          processingTimeMs: Math.max(0.1, Number((endTime - startTime).toFixed(2)))
        }
      };
    }"""

text = text.replace("  } else {\n    // -------------------------------------------------------------\n    // REVERSE CONVERSION (Legacy Anu 7.0 -> Unicode)\n    // -------------------------------------------------------------", f"  }} else {{\n{reverse_branch}\n    // -------------------------------------------------------------\n    // REVERSE CONVERSION (Legacy Anu 7.0 -> Unicode)\n    // -------------------------------------------------------------")

with open("src/utils/converter.ts", "w") as f:
    f.write(text)

print("Patched src/utils/converter.ts")
