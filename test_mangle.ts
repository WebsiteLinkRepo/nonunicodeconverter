import { convertText } from './src/utils/converter';
const input = "தமிழ் மொழி உலகின் மிகப் பழமையான மற்றும் மிகவும் சிறப்பு வாய்ந்த செம்மொழிகளுள் ஒன்றாகும். இது இந்தியாவின் தமிழ் நாடு மாநிலத்தின் முதன்மை மொழியாகும். இது உலகெங்கிலும் உள்ள பல மக்களால் பேசப்படுகிறது.";
const res = convertText(input, "bamini", false, false, "tamil");
console.log(res.convertedText);
