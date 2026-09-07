import { convertText } from './src/utils/converter';

const testCases = [
  { enc: 'krutidev', lang: 'hindi', text: 'नमस्ते! हिंदी बहुत ही सुंदर और प्राचीन भाषा है।' },
  { enc: 'shreelipi', lang: 'hindi', text: 'నమస్కారం! తెలుగు చాలా అందమైన మరియు ప్రాచీన భాష.' },
  { enc: 'shreelipimar', lang: 'marathi', text: 'नमस्कार! मराठी खूप सुंदर आणि प्राचीन भाषा आहे.' },
  { enc: 'anu7', lang: 'telugu', text: 'నమస్కారం! తెలుగు చాలా అందమైన మరియు ప్రాచీన భాష.' },
  { enc: 'anu6', lang: 'telugu', text: 'నమస్కారం! తెలుగు చాలా అందమైన మరియు ప్రాచీన భాష.' },
  { enc: 'anuneo', lang: 'hindi', text: 'नमस्ते! हिंदी बहुत ही सुंदर और प्राचीन भाषा है।' },
  { enc: 'bamini', lang: 'tamil', text: 'வணக்கம்! தமிழ் மிகவும் அழகான மற்றும் பழமையான மொழி.' },
  { enc: 'shreelipitam', lang: 'tamil', text: 'வணக்கம்! தமிழ் மிகவும் அழகான மற்றும் பழமையான மொழி.' },
  { enc: 'ism', lang: 'malayalam', text: 'നമസ്കാരം! മലയാളം വളരെ മനോഹരവും പുരാതനവുമായ ഭാഷയാണ്.' },
  { enc: 'nudi', lang: 'kannada', text: 'ನಮಸ್ಕಾರ! ಕನ್ನಡವು ಬಹಳ ಸುಂದರವಾದ ಮತ್ತು ಪ್ರಾಚೀನ ಭಾಷೆಯಾಗಿದೆ.' },
  { enc: 'hari', lang: 'gujarati', text: 'નમસ્તે! ગુજરાતી ખૂબ સુંદર અને પ્રાચીન ભાષા છે.' }
];

async function runTests() {
  let allPass = true;
  for (const tc of testCases) {
    try {
      const res1 = convertText(tc.text, tc.enc as any, false, false, tc.lang as any);
      const nonUnicode = res1.convertedText;
      const res2 = convertText(nonUnicode, tc.enc as any, true, false, tc.lang as any);
      const backToUnicode = res2.convertedText;
      if (backToUnicode.normalize('NFC') !== tc.text.normalize('NFC')) {
        console.error(`\n❌ [${tc.enc} - ${tc.lang}] Roundtrip Failed!`);
        console.error(`Original: ${tc.text}`);
        console.error(`Non-Unicode: ${nonUnicode}`);
        console.error(`Restored: ${backToUnicode}`);
        allPass = false;
      } else {
        console.log(`✅ [${tc.enc}] OK`);
      }
    } catch (e) {
      console.error(`\n❌ [${tc.enc} - ${tc.lang}] Error:`, e);
      allPass = false;
    }
  }
  if (allPass) {
    console.log('\n🌟 ALL LANGUAGES ROUNDTRIP VERIFIED!');
  } else {
    console.log('\n⚠️ SOME LANGUAGES FAILED TO ROUNDTRIP PERFECTLY.');
  }
}
runTests();
