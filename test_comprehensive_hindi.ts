import { unicodeToAnuNeo } from './src/utils/anuNeoConverter';
import fs from 'fs';

// Comprehensive Hindi test cases covering all consonants, vowels, matras, and ligatures
const testCases = {
  // Basic consonants with inherent 'a'
  'consonants': 'क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न प फ ब भ म य र ल व श ष स ह ड़ ढ़',

  // Vowels (standalone)
  'vowels': 'अ इ उ ऊ ऋ ए ऐ ओ औ',

  // Matras (with consonants)
  'matras': 'का कि कु कू कृ के कै को कौ कॉ',

  // Nasals and special marks
  'nasals': 'कं कः कँ',

  // Simple words
  'simple_words': 'नमस्ते राज पुस्तक सूर्य चाँद मेरा घर',

  // Words with ligatures
  'ligatures': 'क्ष ज्ञ त्र श्र द्र प्र क्र',

  // Complex words with ligatures
  'complex_words': 'क्षेत्र ज्ञान त्रिभुज श्रम द्रव्य प्रदर्शन क्रमिक',

  // Words with different matras combinations
  'matra_combinations': 'काली कुली कीली कूली कैली कोली कौली',

  // Consonant clusters
  'clusters': 'स्कूल त्रिभुज स्वतंत्र क्षमता ज्ञानी श्राप',

  // Words with reph (र् + consonant)
  'reph': 'कर्म धर्म शर्म तर्क तर्कण कर्ता',

  // Words with short 'i' (ि)
  'short_i': 'किताब बिस्तर दिन रिश्ता सितारा विषय',

  // Complete paragraph 1 - About Hindi
  'paragraph_1': 'हिंदी भारत की राष्ट्रभाषा है। यह भारत के उत्तरी भागों में व्यापक रूप से बोली जाती है। हिंदी संस्कृत से व्युत्पन्न है और यह भाषा बहुत समृद्ध है।',

  // Complete paragraph 2 - Story
  'paragraph_2': 'एक समय की बात है, एक छोटा सा गाँव था। उस गाँव में एक बुजुर्ग आदमी रहता था। वह दिन भर बाग में काम करता था। उसके हाथों में कला और कौशल था।',

  // Complete paragraph 3 - Description
  'paragraph_3': 'सूर्य आसमान में चमकता है। उसकी किरणें धरती पर पड़ती हैं। पौधों को सूर्य की आवश्यकता है। बिना सूर्य के जीवन संभव नहीं है।',

  // Words with all consonants
  'all_consonants_combined': 'क्कक ख्खख ग्गग घ्घघ ङ्ङङ च्चच छ्छछ ज्जज झ्झझ ञ्ञञ ट्टट ठ्ठठ ड्डड ढ्ढढ ण्णण त्तत थ्थथ द्ध ध्धध न्नन प्पप फ्फफ ब्बब भ्भभ म्मम य्यय र्रर ल्लल व्वव श्शश ष्षष स्सस ह्हह',

  // Numbers
  'numbers': '०ः १ः २ः ३ः ४ः ५ः ६ः ७ः ८ः ९ः',

  // Mixed complex text
  'mixed': 'आज कल का बच्चा कंप्यूटर सीखता है। कल के बड़े आदमी भी तकनीकी ज्ञान रखते हैं। यह समय की माँग है और हमें इसे स्वीकार करना चाहिए।',
};

console.log('=== Comprehensive Hindi Text Conversion Test ===\n');

let output = `# Hindi Unicode to Anu Neo Non-Unicode Conversion Test\n\nDate: ${new Date().toISOString()}\n\n`;

Object.entries(testCases).forEach(([category, unicodeText]) => {
  const neoText = unicodeToAnuNeo(unicodeText);

  output += `## ${category}\n\n`;
  output += `**Unicode Input:**\n\`\`\`\n${unicodeText}\n\`\`\`\n\n`;
  output += `**Non-Unicode (Anu Neo) Output:**\n\`\`\`\n${neoText}\n\`\`\`\n\n`;

  console.log(`${category}:`);
  console.log(`  Unicode: ${unicodeText}`);
  console.log(`  Anu Neo: ${neoText}`);
  console.log();
});

// Write to markdown file
fs.writeFileSync('./HINDI_CONVERSION_TEST.md', output);
console.log('\n✅ Output saved to HINDI_CONVERSION_TEST.md');
