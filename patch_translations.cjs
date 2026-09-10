const fs = require('fs');
const path = require('path');

const locales = {
  en: {
    autoCopyLabel: "Auto-copy Output",
    swapBtnLabel: "Swap",
    cleanEnglishBtn: "Clean English",
    outputLabel: "Output",
    inputLabel: "Input",
    unicodeLabel: "Unicode",
    placeholderInput: "Paste your {{script}} Unicode text here...",
    placeholderOutput: "Converted {{font}} text will appear here automatically...",
    placeholderInputReverse: "Paste your {{font}} text here...",
    placeholderOutputReverse: "Converted {{script}} Unicode text will appear here automatically..."
  },
  te: {
    autoCopyLabel: "ఆటో-కాపీ",
    swapBtnLabel: "మార్చు (Swap)",
    cleanEnglishBtn: "ఇంగ్లీష్ తొలగించు",
    outputLabel: "అవుట్‌పుట్",
    inputLabel: "ఇన్‌పుట్",
    unicodeLabel: "యూనికోడ్",
    placeholderInput: "మీ {{script}} యూనికోడ్ టెక్స్ట్‌ని ఇక్కడ పేస్ట్ చేయండి...",
    placeholderOutput: "మార్చబడిన {{font}} టెక్స్ట్ ఇక్కడ ఆటోమేటిక్‌గా కనిపిస్తుంది...",
    placeholderInputReverse: "మీ {{font}} టెక్స్ట్‌ని ఇక్కడ పేస్ట్ చేయండి...",
    placeholderOutputReverse: "మార్చబడిన {{script}} యూనికోడ్ టెక్స్ట్ ఇక్కడ ఆటోమేటిక్‌గా కనిపిస్తుంది..."
  },
  hi: {
    autoCopyLabel: "ऑटो-कॉपी",
    swapBtnLabel: "स्वैप (Swap)",
    cleanEnglishBtn: "अंग्रेजी हटाएं",
    outputLabel: "आउटपुट",
    inputLabel: "इनपुट",
    unicodeLabel: "यूनिकोड",
    placeholderInput: "अपना {{script}} यूनिकोड टेक्स्ट यहाँ पेस्ट करें...",
    placeholderOutput: "परिवर्तित {{font}} टेक्स्ट यहाँ अपने आप दिखाई देगा...",
    placeholderInputReverse: "अपना {{font}} टेक्स्ट यहाँ पेस्ट करें...",
    placeholderOutputReverse: "परिवर्तित {{script}} यूनिकोड टेक्स्ट यहाँ अपने आप दिखाई देगा..."
  },
  ta: {
    autoCopyLabel: "ஆட்டோ-காபி",
    swapBtnLabel: "மாற்று (Swap)",
    cleanEnglishBtn: "ஆங்கிலத்தை நீக்கு",
    outputLabel: "வெளியீடு",
    inputLabel: "உள்ளீடு",
    unicodeLabel: "யூனிகோட்",
    placeholderInput: "உங்கள் {{script}} யூனிகோட் உரையை இங்கே ஒட்டவும்...",
    placeholderOutput: "மாற்றப்பட்ட {{font}} உரை இங்கே தோன்றும்...",
    placeholderInputReverse: "உங்கள் {{font}} உரையை இங்கே ஒட்டவும்...",
    placeholderOutputReverse: "மாற்றப்பட்ட {{script}} யூனிகோட் உரை இங்கே தோன்றும்..."
  },
  kn: {
    autoCopyLabel: "ಆಟೋ-ಕಾಪಿ",
    swapBtnLabel: "ಬದಲಾಯಿಸಿ (Swap)",
    cleanEnglishBtn: "ಇಂಗ್ಲಿಷ್ ತೆಗೆಯಿರಿ",
    outputLabel: "ಔಟ್ಪುಟ್",
    inputLabel: "ಇನ್ಪುಟ್",
    unicodeLabel: "ಯುನಿಕೋಡ್",
    placeholderInput: "ನಿಮ್ಮ {{script}} ಯುನಿಕೋಡ್ ಪಠ್ಯವನ್ನು ಇಲ್ಲಿ ಅಂಟಿಸಿ...",
    placeholderOutput: "ಪರಿವರ್ತಿತ {{font}} ಪಠ್ಯ ಇಲ್ಲಿ ಕಾಣಿಸುತ್ತದೆ...",
    placeholderInputReverse: "ನಿಮ್ಮ {{font}} ಪಠ್ಯವನ್ನು ಇಲ್ಲಿ ಅಂಟಿಸಿ...",
    placeholderOutputReverse: "ಪರಿವರ್ತಿತ {{script}} ಯುನಿಕೋಡ್ ಪಠ್ಯ ಇಲ್ಲಿ ಕಾಣಿಸುತ್ತದೆ..."
  },
  ml: {
    autoCopyLabel: "ഓട്ടോ-കോപ്പി",
    swapBtnLabel: "മാറ്റുക (Swap)",
    cleanEnglishBtn: "ഇംഗ്ലീഷ് ഒഴിവാക്കുക",
    outputLabel: "ഔട്ട്പുട്ട്",
    inputLabel: "ഇൻപുട്ട്",
    unicodeLabel: "യൂണിക്കോഡ്",
    placeholderInput: "നിങ്ങളുടെ {{script}} യൂണിക്കോഡ് ടെക്സ്റ്റ് ഇവിടെ പേസ്റ്റ് ചെയ്യുക...",
    placeholderOutput: "മാറ്റിയ {{font}} ടെക്സ്റ്റ് ഇവിടെ കാണും...",
    placeholderInputReverse: "നിങ്ങളുടെ {{font}} ടെക്സ്റ്റ് ഇവിടെ പേസ്റ്റ് ചെയ്യുക...",
    placeholderOutputReverse: "മാറ്റിയ {{script}} യൂണിക്കോഡ് ടെക്സ്റ്റ് ഇവിടെ കാണും..."
  },
  mr: {
    autoCopyLabel: "ऑटो-कॉपी",
    swapBtnLabel: "स्वॅप (Swap)",
    cleanEnglishBtn: "इंग्रजी काढा",
    outputLabel: "आउटपुट",
    inputLabel: "इनपुट",
    unicodeLabel: "युनिकोड",
    placeholderInput: "तुमचा {{script}} युनिकोड मजकूर येथे पेस्ट करा...",
    placeholderOutput: "रूपांतरित {{font}} मजकूर येथे दिसेल...",
    placeholderInputReverse: "तुमचा {{font}} मजकूर येथे पेस्ट करा...",
    placeholderOutputReverse: "रूपांतरित {{script}} युनिकोड मजकूर येथे दिसेल..."
  },
  gu: {
    autoCopyLabel: "ઓટો-કોપી",
    swapBtnLabel: "સ્વેપ (Swap)",
    cleanEnglishBtn: "અંગ્રેજી કાઢી નાખો",
    outputLabel: "આઉટપુટ",
    inputLabel: "ઇનપુટ",
    unicodeLabel: "યુનિકોડ",
    placeholderInput: "તમારો {{script}} યુનિકોડ ટેક્સ્ટ અહી પેસ્ટ કરો...",
    placeholderOutput: "રૂપાંતરિત {{font}} ટેક્સ્ટ અહી દેખાશે...",
    placeholderInputReverse: "તમારો {{font}} ટેક્સ્ટ અહી પેસ્ટ કરો...",
    placeholderOutputReverse: "રૂપાંતરિત {{script}} યુનિકોડ ટેક્સ્ટ અહી દેખાશે..."
  }
};

const dir = path.join(__dirname, 'src', 'utils', 'locales');
Object.keys(locales).forEach(lang => {
  const filePath = path.join(dir, `${lang}.ts`);
  let content = fs.readFileSync(filePath, 'utf-8');
  
  const toAdd = Object.entries(locales[lang])
    .map(([k, v]) => `  ${k}: "${v}"`)
    .join(',\n');
  
  // Find the end of the exports by replacing "};" at the end of the file
  content = content.replace(/};\s*$/, `,\n${toAdd}\n};\n`);
  fs.writeFileSync(filePath, content, 'utf-8');
});
console.log("Patched all locales.");
