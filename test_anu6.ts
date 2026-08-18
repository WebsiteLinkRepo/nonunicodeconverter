import { ANU6_UNICODE_TO_NONUNICODE } from './src/utils/mappings/anu6';
import { ANU7_UNICODE_TO_NONUNICODE } from './src/utils/mappings/anu7';
import { convertText } from './src/utils/converter';

const text = "ఆంధ్రప్రదేశ్";
console.log("Anu6:", convertText(text, 'anu6', false).convertedText);
console.log("Anu7:", convertText(text, 'anu7', false).convertedText);
