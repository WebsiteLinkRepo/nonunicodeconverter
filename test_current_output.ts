import { unicodeToAnuNeo } from './src/utils/anuNeoConverter';
const input = "डॉक्टर विज्ञान छुट्टी उद्श्य धर्म कर्म क्षमा ज्ञान त्रिशूल श्रम द्रौपदी";
const output = unicodeToAnuNeo(input);
console.log("My Output: " + output);
