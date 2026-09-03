import { unicodeToShreeLipi } from '../src/utils/shreeLipiConverter.js';
const text = "मराठी ही महाराष्ट्राची राजभाषा असून तिला खूप मोठा आणि समृद्ध इतिहास लाभला आहे.";
const res = unicodeToShreeLipi(text, "marathi");
console.log("Converted:", res);
