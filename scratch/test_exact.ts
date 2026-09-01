import { unicodeToShreeLipi } from '../src/utils/shreeLipiConverter';

const input = 'आज कल का बच्चा कंप्यूटर सीखता है। कल के बड़े आदमी भी तकनीकी ज्ञान रखते हैं। यह समय की माँग है और हमें इसे स्वीकार करना चाहिए।';
const expected = 'AmO H$b H$m ~ƒm H§$ß`yQ>a grIVm h¡& H$b Ho$ ~‹So> AmX_r ^r VH$ZrH$r kmZ aIVo h¢& `h g_` H$r _m±J h¡ Am¡a h_o§ Bgo ñdrH$ma H$aZm Mm{hE&';

const actual = unicodeToShreeLipi(input);
console.log('Actual:  ', actual);
console.log('Expected:', expected);
console.log('100% Exact Match?:', actual === expected);
