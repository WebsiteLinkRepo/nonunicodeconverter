import { convertUnicodeToShreeLipiTelugu0908 } from '../src/utils/shreeLipiTelugu0908Converter.ts';
const input = "క ఖ";
const legacy = convertUnicodeToShreeLipiTelugu0908(input).text;
console.log("Legacy chars:", Array.from(legacy).map(c => c.charCodeAt(0).toString(16)).join(" "));
