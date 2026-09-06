import { convertUnicodeToShreeLipiTelugu0908 } from '../src/utils/shreeLipiTelugu0908Converter';
const badOutput = "కఖ గఘ జచఛజ ఝ ఇట ఠడఢణతథదధనఎ ఫ బ భమొ యరల వశష స హా ళక్షఱ";
const legacy = convertUnicodeToShreeLipiTelugu0908(badOutput).text;
console.log("Legacy of bad output:", legacy);
console.log("Legacy of bad output (codepoints):", [...legacy].map(c => c.charCodeAt(0).toString(16)).join(' '));
