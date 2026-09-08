import fs from 'fs';
import { convertText } from './src/utils/converter.js';

// We need the generateRTF function from Astro file 
const text = fs.readFileSync('src/components/TextConverter.astro', 'utf8');

const rtfMatch = text.match(/function generateRTF[\s\S]*?return rtf \+ '\\n}';\n  }/);
if (rtfMatch) {
  console.log("Found RTF generator");
}
