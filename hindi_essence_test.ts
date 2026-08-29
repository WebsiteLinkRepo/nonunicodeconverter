import { convertText } from './src/utils/converter.ts';

const tests = [
  { name: 'Vowels', text: 'अ आ इ ई उ ऊ ऋ ए ऐ ओ औ' },
  { name: 'Consonants', text: 'क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न प फ ब भ म य र ल व श ष स ह' },
  { name: 'Matras (Ka)', text: 'क का कि की कु कू कृ के कै को कौ कं कः' },
  { name: 'Special Conjuncts', text: 'क्ष त्र ज्ञ श्र' },
  { name: 'Reph (Top Ra)', text: 'धर्म कर्म सूर्य' },
  { name: 'Rakar (Bottom Ra)', text: 'प्रकार ग्राम त्रिशूल' },
  { name: 'Half Letters', text: 'सत्य न्याय पुस्तक' },
  { name: 'Vertical Conjuncts', text: 'उद्देश्य मिट्टी चिह्न' },
  { name: 'Candrabindu & Nukta', text: 'आँख चाँद ज़मीन फ़िल्म' }
];

console.log("=== Testing the Essence of Hindi Anu Script Manager ===\n");

tests.forEach(t => {
  const res = convertText(t.text, 'anu7', false, false, 'hindi');
  console.log(`-- ${t.name} --`);
  console.log(`Input: ${t.text}`);
  console.log(`Converted: ${res.convertedText}\n`);
});
