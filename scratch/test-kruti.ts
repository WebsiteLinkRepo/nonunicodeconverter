import { convertText } from '../src/utils/converter';

const result = convertText("नमस्ते", "krutidev", false, false, "hindi");
console.log("Hindi to Krutidev (नमस्ते):", result.convertedText);
