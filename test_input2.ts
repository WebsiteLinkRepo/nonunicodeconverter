import { unicodeToIsmMalayalam } from './src/utils/ismMalayalamConverter';

const input = "കേരളം പ്രകൃതിഭംഗി നിറഞ്ഞ ഒരു നാടാണ്. പച്ചപ്പുനിറഞ്ഞ വയലുകളും മനോഹരമായ കടൽത്തീരങ്ങളും ഇവിടെയുണ്ട്. തെങ്ങുകളും കുന്നുകളും ഈ നാടിന് പ്രത്യേക ഭംഗി നൽകുന്നു. ഇവിടെയുള്ള ജനങ്ങൾ സ്നേഹമുള്ളവരാണ്.";
console.log(unicodeToIsmMalayalam(input));
