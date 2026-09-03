import { unicodeToShreeLipi } from '../src/utils/shreeLipiConverter.js';

const testCases = [
  { name: "Screenshot sentence", input: "मराठी ही महाराष्ट्राची राजभाषा असून तिला खूप मोठा आणि समृद्ध इतिहास लाभला आहे." },
  { name: "Eyelash-ra words", input: "कुऱ्हाड, वऱ्हाड, तऱ्हा, चऱ्हाट, काऱ्हाळा, संक्रांत, गऱ्हाणे" },
  { name: "Halant Lla words", input: "डोळ्यांत, कळ्या, गळफास, चाळणी, काळभैरव, जांभळा" },
  { name: "Complex conjuncts", input: "उच्छ्वास, वैशिष्ट्य, स्फूर्ति, आर्द्र, दृष्टिकोन, प्रज्ञा, स्वातंत्र्य, अस्तित्व, ज्येष्ठ" }
];

for (const t of testCases) {
  const converted = unicodeToShreeLipi(t.input, "marathi");
  console.log(`[${t.name}]`);
  console.log(`  Unicode:   ${t.input}`);
  console.log(`  Converted: ${converted}`);
}
