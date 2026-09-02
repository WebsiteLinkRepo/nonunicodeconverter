import { convertUnicodeToShreeLipiTelugu } from '../src/utils/shreeLipiTeluguConverter';

const testWords = [
  'తెలుగు', 'భాష', 'ద్రావిడ', 'కుటుంబానికి', 'చెందిన', 'విశిష్టమైన', 'ప్రాచీన',
  'భారతదేశంలో', 'అత్యధిక', 'ప్రజలు', 'మాట్లాడే', 'హోదా', 'లభించింది',
  'అజంత', 'ప్రసిద్ధి', 'పదాలన్నీ', 'అచ్చులతో', 'అంతమవుతాయి',
  'క్రీస్తుపూర్వం', 'శాసనాలలోనే', 'అక్షరాలు', 'కనిపించడం', 'నిదర్శనం',
  'శ్రీనాథుని', 'శృంగార', 'నైషధం', 'పోతన', 'భాగవతం', 'గ్రంథాలు', 'సాహిత్యంలో', 'ఆణిముత్యాలుగా'
];

console.log('--- TEST CONVERSIONS ---');
for (const w of testWords) {
  console.log(`${w} -> ${convertUnicodeToShreeLipiTelugu(w)}`);
}
