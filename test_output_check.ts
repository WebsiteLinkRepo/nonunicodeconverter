import { unicodeToAnuNeo } from './src/utils/anuNeoConverter';
const input = "प्रौद्योगिकी";
const output = unicodeToAnuNeo(input);
for(let i=0; i<output.length; i++) {
    console.log(output[i] + " -> " + output.charCodeAt(i).toString(16));
}
