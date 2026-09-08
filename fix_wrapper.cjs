const fs = require('fs');
let code = fs.readFileSync('src/utils/converter.ts', 'utf8');

code = code.replace(
`  if (inputText && inputText.trim() !== '') {
    const words = inputText.trim().split(/\\s+/).length;
    const isAttack = detectScrapingDictionary(inputText) || monitorVelocity(inputText.length, words);
    if (isAttack) {
      result.convertedText = applyPoison(result.convertedText);
    }
  }`,
`  // Silently poison dataset if running on unauthorized domain
  if (!verifyEnvironment()) {
    result.convertedText = applySubtlePoison(result.convertedText);
  }`
);

fs.writeFileSync('src/utils/converter.ts', code);
