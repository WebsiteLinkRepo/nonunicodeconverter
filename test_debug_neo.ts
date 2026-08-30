import { unicodeToAnuNeo } from './src/utils/anuNeoConverter';

// Test problem words from the hindi_alphabet_test.md
const testWords: [string, string][] = [
  // [unicode, description]
  ['संयुक्ताक्षरों', 'conjuncts - expected Ìæ®ìMoçqºçõ'],
  ['अर्धवर्णों', 'reph - half letters'],
  ['निर्मित', 'reph on mi'],
  ['के', 'ke - expected Nzþ'],
  ['वाङ्मय', 'ng+ma conjunct'],
  ['आयुर्वेद', 'reph on ve'],
  ['ग्रंथों', 'gra conjunct'],
  ['क्लिष्ट', 'kli+shTa conjunct'],
  ['किंकर्तव्यविमूढ़ता', 'complex word'],
  ['शृंगारिक', 'shRi conjunct'],
  ['प्रदर्शन', 'pra+reph on sha'],
  ['अग्नि', 'gni conjunct'],
  ['भाँति', 'chandrabindu'],
  ['निर्द्वन्द्व', 'complex conjunct'],
  ['युधिष्ठिर', 'shThir - ta vattu'],
  ['अश्वत्थामा', 'ashvat-tha'],
  ['भर्त्सना', 'bhartsana'],
  ['क्रौंच', 'kraunch'],
  ['मार्मिक', 'reph on mi'],
  ['दृष्टांत', 'dRi+shTaant'],
  ['उपस्थित', 'sthit'],
  ['यहाँ', 'yahaan chandrabindu'],
  ['मात्राएँ', 'matraen chandrabindu'],
  ['रेफ़', 'reph with nukta'],
  ['विभिन्न', 'vibhinna - na vattu'],
  ['आशीर्वाद', 'reph on va'],
  ['पुनर्निर्माण', 'reph'],
  ['स्रोत', 'srot'],
  ['कृत्रिम', 'kRitrim'],
  ['सूक्ष्मताओं', 'sookshmataaon - expected ÌîßªoçEçõ'],
  ['वर्णमाला', 'reph on Na'],
  ['हैं', 'hain - expected Òø'],
  ['क्ष्त्र्ज्ञ्श्र्', 'extreme conjunct'],
  ['खण्डित', 'khaNDit - Na vattu'],
  ['सं', 'san - expected Ìæ'],
  ['लांघना', 'laanghana - expected ÂçæVŒç'],
  ['नितांत', 'nitaant - expected uŒoçæo'],
  ['असंगत', 'asangat - expected EÌæTo'],
  ['महर्षि', 'maharshi - reph on shi'],
  ['अष्टावक्र', 'ashTaavakra'],
  ['र्', 'standalone half-ra'],
  ['प्र', 'pra ligature'],
  ['द्र', 'dra ligature'],
  ['क्र', 'kra ligature'],
];

console.log('=== Anu Neo Hindi Converter Debug Test ===\n');

for (const [word, desc] of testWords) {
  const result = unicodeToAnuNeo(word);
  // Show hex codes
  const hexCodes = [...result].map(c => 'U+' + c.charCodeAt(0).toString(16).toUpperCase().padStart(4, '0')).join(' ');
  console.log(`${word} => "${result}" [${hexCodes}]`);
  console.log(`  (${desc})\n`);
}
