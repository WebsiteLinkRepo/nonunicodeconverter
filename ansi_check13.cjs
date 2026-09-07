const fs = require('fs');

const from = "కౄరమృగము ౠషి 'కోట్'";
const anu6Mapping = {
   "క": "\x48\x9b", //  usually mapped to \x48 and \x9b in CP1252 but let's just see competitor
};
console.log("Competitor: H(48) ›(203a) $(24) ì(ec) ~(7e) ¡(a1) =(3d) °(b0) $(24) Q(51) ®(ae) =(3d) ò(f2)  (20) |(7c) °(b0) ¶(b6) +(2b) ²(b2)  (20) '(27) H(48) Ë(cb) \(5c) ˜(2dc) Ñ(d1)");

// H(48) ›(203a) is "కౄ"?? or "క"?
// Actually క in our mapped table is ? No it's  which maps to H \x9b. \x9b is 203A (›) in cp1252!
// So:
// క: H ›
// ౄ: $
// ర: ì ~
// మ: ¡ = °
// ృ: $
// గ: Q ®
// ము: = ò
// (space)
// ౠ: | ° ¶
// షి: + ²
// (space)
// ': '
// కో: H Ë
// ట్: \ ˜
// ': Ñ

