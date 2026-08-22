const fs = require('fs');

let content = fs.readFileSync('src/utils/converter.ts', 'utf8');

// Add imports
content = content.replace("import { getMapping", "import { unicodeToKrutidev } from './krutiDevConverter';\nimport { unicodeToBamini } from './baminiConverter';\nimport { getMapping");

// Replace the forward conversion block
const blockOffsetsRegex = /const blockOffsets: Record<string, number> = \{[\s\S]*?if \(!reverse\) \{/m;
const beforeBlockOffsets = content.substring(0, content.search(blockOffsetsRegex));
const fromBlockOffsets = content.substring(content.search(blockOffsetsRegex));

// We'll just carefully replace the entire `if (!reverse) {` block inside `convertText`.
// It's safer to just inject our custom logic right at the start of `convertText`.

const newConvertText = `export function convertText(
  inputText: string,
  encoding: FontEncoding = 'anu7',
  reverse: boolean = false,
  useAltRaaVatthu: boolean = false,
  script: ScriptLanguage = 'telugu'
): ConversionResult {
  const startTime = performance.now();

  if (!inputText || inputText.trim() === '') {
    return {
      convertedText: '',
      errors: [],
      stats: { inputCharCount: 0, outputCharCount: 0, wordCount: 0, lineCount: 0, unmappedCount: 0, processingTimeMs: 0 }
    };
  }

  // Handle specific languages with dedicated engines (Forward Conversion)
  if (!reverse) {
    if (encoding === 'krutidev' && script === 'hindi') {
      const convertedText = unicodeToKrutidev(inputText);
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
    }
    
    if (encoding === 'bamini' && script === 'tamil') {
      const convertedText = unicodeToBamini(inputText);
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
    }
  }

`;

content = content.replace(/export function convertText\([\s\S]*?if \(!inputText \|\| inputText\.trim\(\) === ''\) \{[\s\S]*?\}[\s\S]*?const mapping = getMapping\(encoding, reverse\);/, newConvertText + "\n  const mapping = getMapping(encoding, reverse);");

fs.writeFileSync('src/utils/converter.ts', content);
console.log("Patched converter.ts");
