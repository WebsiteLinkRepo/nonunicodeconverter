import { unicodeToAnuNeo } from './src/utils/anuNeoConverter';
const input = "नमस्ते! हिंदी बहुत ही सुंदर और प्राचीन भाषा है।";
const output = unicodeToAnuNeo(input);
for(let i=0; i<output.length; i++) {
    console.log(output[i] + " -> " + output.charCodeAt(i));
}
