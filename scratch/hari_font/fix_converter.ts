import fs from 'fs';
const converterPath = 'src/utils/converter.ts';
let code = fs.readFileSync(converterPath, 'utf8');

if (!code.includes('unicodeToHari')) {
    code = code.replace(
        "import { unicodeToIsmMalayalam } from './ismMalayalamConverter';",
        "import { unicodeToIsmMalayalam } from './ismMalayalamConverter';\nimport { unicodeToHari } from './hariGujaratiConverter';"
    );
    
    const targetBlock = "if ((encoding === 'shreelipi' || encoding === 'shreelipimar') && (script === 'hindi' || script === 'marathi')) {";
    
    const hariBlock = `
    if (encoding === 'hari' && script === 'gujarati') {
      const convertedText = unicodeToHari(processedInput);
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
    `;
    code = code.replace(targetBlock, hariBlock + '\n    ' + targetBlock);
    fs.writeFileSync(converterPath, code);
    console.log("Updated converter.ts");
} else {
    console.log("Already updated");
}
