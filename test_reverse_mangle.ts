import { convertText } from './src/utils/converter';
const input = "jkpo; ekhop cyfpd; kpfg; goikahd kR;Ruk; kpftuk; rpRg;gu tha;w;j erk;ekhopfsus; xd;Rhfuk;. Eju Ew;jpahtpd; jkpo; whlu khwpyj;jpd; kujd;ik ekhopahfuk;. Eju cyefq;fpyuk; cs;s gy kf;fshy; Egrg;glufpRju.";
const res = convertText(input, "bamini", true, false, "tamil");
console.log(res.convertedText);
