import { ANU7_UNICODE_TO_NONUNICODE } from './src/utils/mappings/anu7';

const text = "ఇది ప్రధానంగా ఆంధ్రప్రదేశ్ మరియు తెలంగాణ రాష్ట్రాలలో మాట్లాడుతారు. ఈ భాషకు చక్కని సాహిత్యం, వ్యాకరణం మరియు గొప్ప చరిత్ర ఉంది.";

let result = text;
for (const entry of ANU7_UNICODE_TO_NONUNICODE) {
    result = result.split(entry.from).join(entry.to);
}
console.log(result);
