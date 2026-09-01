
import { convertText } from './src/utils/converter';

const complexParagraphs = [
    "தமிழ் மொழி உலகின் மிகப் பழமையான மற்றும் மிகவும் சிறப்பு வாய்ந்த செம்மொழிகளுள் ஒன்றாகும்.",
    "இது இந்தியாவின் தமிழ் நாடு மாநிலத்தின் முதன்மை மொழியாகும். இது உலகெங்கிலும் உள்ள பல மக்களால் பேசப்படுகிறது.",
    "ஸ்ரீராமன் மற்றும் லக்ஷ்மணன் ஆகியோர் மஹரிஷி விஸ்வாமித்திரருடன் சென்றனர்.",
    "அங்கு அவர்கள் ஞானம், க்ஷமை, அஸ்திர சாஸ்திரங்கள் ஆகியவற்றைக் கற்றுக்கொண்டனர்.",
    "பாரதியார்: 'யாமறிந்த மொழிகளிலே தமிழ்மொழி போல் இனிதாவது எங்கும் காணோம்'.",
    "1234567890 ௧௨௩௪௫௬௭௮௯௰"
];

console.log("=== COMPREHENSIVE TAMIL CONVERSION TESTS ===");
for (let i = 0; i < complexParagraphs.length; i++) {
    const text = complexParagraphs[i];
    const fwd = convertText(text, 'anutamil', false, false, 'tamil');
    const rev = convertText(fwd.convertedText, 'anutamil', true, false, 'tamil');
    console.log(`
Test #${i+1}:`);
    console.log(`Input:       ${text}`);
    console.log(`Anu Tamil:   ${fwd.convertedText}`);
    console.log(`Roundtrip:   ${rev.convertedText}`);
    console.log(`Matches:     ${rev.convertedText === text}`);
}
