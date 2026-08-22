import { unicodeToIsmMalayalam } from './src/utils/ismMalayalamConverter';

const input = "മലയാളം ഭാഷയിലുള്ള ഒരു ലളിതമായ ഖണ്ഡിക താഴെ നൽകുന്നു. കേരളത്തിന്റെ പ്രകൃതിഭംഗിയെക്കുറിച്ചുള്ള വരികളാണിത്.";
console.log(unicodeToIsmMalayalam(input));
