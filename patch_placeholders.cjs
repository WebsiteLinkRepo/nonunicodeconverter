const fs = require('fs');

let content = fs.readFileSync('src/components/TextConverter.astro', 'utf8');

const placeholderLogicReplacement = `
    const PLACEHOLDERS: Record<string, string> = {
      telugu: "Paste Telugu Unicode text here... (e.g. అందరికీ నమస్కారం)",
      hindi: "Paste Hindi Unicode text here... (e.g. हिंदी भारत की राजभाषा है)",
      tamil: "Paste Tamil Unicode text here... (e.g. அனைவருக்கும் வணக்கம்)",
      kannada: "Paste Kannada Unicode text here... (e.g. ಎಲ್ಲರಿಗೂ ನಮಸ್ಕಾರ)",
      malayalam: "Paste Malayalam Unicode text here... (e.g. എല്ലാവർക്കും നമസ്കാരം)"
    };
    
    const scriptNames: Record<string, string> = { 
      hindi: 'Hindi', tamil: 'Tamil', kannada: 'Kannada', malayalam: 'Malayalam', telugu: 'Telugu' 
    };
    
    if (script === 'telugu') {
      sampleTeluguBtn?.classList.remove('hidden');
      sampleHindiBtn?.classList.add('hidden');
      if (altRaaVatthuWrapper) altRaaVatthuWrapper.style.display = 'flex';
    } else if (script === 'hindi') {
      sampleTeluguBtn?.classList.add('hidden');
      sampleHindiBtn?.classList.remove('hidden');
      if (altRaaVatthuWrapper) altRaaVatthuWrapper.style.display = 'none';
    } else {
      sampleTeluguBtn?.classList.add('hidden');
      sampleHindiBtn?.classList.add('hidden');
      if (altRaaVatthuWrapper) altRaaVatthuWrapper.style.display = 'none';
    }
    
    if (inputText) inputText.placeholder = PLACEHOLDERS[script] || PLACEHOLDERS['telugu'];

    if (!val) {
`;

content = content.replace(/if \(script === 'hindi'\) \{[\s\S]*?if \(!val\) \{/, placeholderLogicReplacement);

const titleLogicReplacement = `
    const isTelugu = script === 'telugu';

    const altRaaVatthuChk = document.getElementById('alt-raa-vatthu-chk') as HTMLInputElement;
    const useAltRaaVatthu = (altRaaVatthuChk && isTelugu) ? altRaaVatthuChk.checked : false;
    const effectiveFontStyle = useAltRaaVatthu ? 'bapu' : selectedFontStyle;

    const scriptNameUpper = scriptNames[script].toUpperCase();

    if (reverse) {
      autoStatus.textContent = \`Non-Unicode ➔ \${scriptNames[script]} Unicode\`;
      if (inputBoxTitle) inputBoxTitle.textContent = 'NON-UNICODE TEXT INPUT';
      if (outputBoxTitle) outputBoxTitle.textContent = \`\${scriptNameUpper} UNICODE OUTPUT\`;
    } else {
      autoStatus.textContent = \`\${scriptNames[script]} Unicode ➔ \${activeFontNameLabel(effectiveFontStyle)}\`;
      if (inputBoxTitle) inputBoxTitle.textContent = \`\${scriptNameUpper} UNICODE INPUT\`;
      if (outputBoxTitle) outputBoxTitle.textContent = 'NON-UNICODE OUTPUT';
    }
`;

content = content.replace(/const scriptName = script === 'hindi' \? 'Hindi' : 'Telugu';[\s\S]*?if \(outputBoxTitle\) outputBoxTitle\.textContent = t\.outputBoxHeader \|\| 'NON-UNICODE OUTPUT';\n    \}/, titleLogicReplacement);

fs.writeFileSync('src/components/TextConverter.astro', content);
console.log("Patched placeholders");
