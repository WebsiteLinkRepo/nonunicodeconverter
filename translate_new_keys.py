import os
import re

locales = {
    'en': {
        'pagemakerBtnText': '"Open PageMaker Auto Font Changer"',
        'pagemakerTooltip': '"Use converted text directly with Adobe PageMaker 7.0 without manually changing fonts."',
        'pagemakerPopupTitle': '"Adobe PageMaker 7.0"',
        'pagemakerPopupDesc': '"PageMaker Auto Font Changer is not installed or could not be opened. Install this software in your PC to make it work."',
        'pagemakerInstallBtn': '"Install PageMaker Auto Font Changer"',
        'pagemakerTryAgainBtn': '"Try Again"',
        'pwaInstallTitle': '"Install as App"',
        'pwaInstallDesc': '"Install this website as an app on your device for quick access."',
        'pwaInstallBtn': '"Install Web App"',
        'fontHelperTitle': '"PageMaker Auto Font Changer"',
        'fontHelperDesc': '"A native Windows helper for Adobe PageMaker 7.0. It bridges the modern web clipboard with legacy Rich Text Format (RTF) requirements."',
        'fontHelperBtn': '"Download Setup (.exe)"'
    },
    'hi': {
        'pagemakerBtnText': '"PageMaker ऑटो फ़ॉन्ट चेंजर खोलें"',
        'pagemakerTooltip': '"फ़ॉन्ट को मैन्युअल रूप से बदले बिना सीधे Adobe PageMaker 7.0 के साथ परिवर्तित टेक्स्ट का उपयोग करें।"',
        'pagemakerPopupTitle': '"Adobe PageMaker 7.0"',
        'pagemakerPopupDesc': '"PageMaker ऑटो फ़ॉन्ट चेंजर स्थापित नहीं है या खोला नहीं जा सका। इसे काम करने के लिए इस सॉफ़्टवेयर को अपने पीसी में स्थापित करें।"',
        'pagemakerInstallBtn': '"PageMaker ऑटो फ़ॉन्ट चेंजर स्थापित करें"',
        'pagemakerTryAgainBtn': '"पुनः प्रयास करें"',
        'pwaInstallTitle': '"ऐप के रूप में स्थापित करें"',
        'pwaInstallDesc': '"त्वरित पहुँच के लिए इस वेबसाइट को अपने डिवाइस पर एक ऐप के रूप में स्थापित करें।"',
        'pwaInstallBtn': '"वेब ऐप इंस्टॉल करें"',
        'fontHelperTitle': '"PageMaker ऑटो फ़ॉन्ट चेंजर"',
        'fontHelperDesc': '"Adobe PageMaker 7.0 के लिए एक देशी Windows सहायक। यह आधुनिक वेब क्लिपबोर्ड को विरासत रिच टेक्स्ट फॉर्मेट (RTF) आवश्यकताओं के साथ जोड़ता है।"',
        'fontHelperBtn': '"सेटअप डाउनलोड करें (.exe)"'
    },
    'te': {
        'pagemakerBtnText': '"PageMaker ఆటో ఫాంట్ ఛేంజర్ తెరవండి"',
        'pagemakerTooltip': '"ఫాంట్‌లను మాన్యువల్‌గా మార్చకుండా నేరుగా Adobe PageMaker 7.0తో మార్చబడిన వచనాన్ని ఉపయోగించండి."',
        'pagemakerPopupTitle': '"Adobe PageMaker 7.0"',
        'pagemakerPopupDesc': '"PageMaker ఆటో ఫాంట్ ఛేంజర్ ఇన్‌స్టాల్ చేయబడలేదు లేదా తెరవబడలేదు. ఇది పని చేయడానికి మీ PCలో ఈ సాఫ్ట్‌వేర్‌ను ఇన్‌స్టాల్ చేయండి."',
        'pagemakerInstallBtn': '"PageMaker ఆటో ఫాంట్ ఛేంజర్‌ని ఇన్‌స్టాల్ చేయండి"',
        'pagemakerTryAgainBtn': '"మళ్లీ ప్రయత్నించండి"',
        'pwaInstallTitle': '"యాప్‌గా ఇన్‌స్టాల్ చేయండి"',
        'pwaInstallDesc': '"త్వరిత యాక్సెస్ కోసం మీ పరికరంలో ఈ వెబ్‌సైట్‌ను యాప్‌గా ఇన్‌స్టాల్ చేయండి."',
        'pwaInstallBtn': '"వెబ్ యాప్‌ను ఇన్‌స్టాల్ చేయండి"',
        'fontHelperTitle': '"PageMaker ఆటో ఫాంట్ ఛేంజర్"',
        'fontHelperDesc': '"Adobe PageMaker 7.0 కోసం స్థానిక Windows సహాయకుడు. ఇది ఆధునిక వెబ్ క్లిప్‌బోర్డ్‌ను పాత రిచ్ టెక్స్ట్ ఫార్మాట్ (RTF) అవసరాలతో కలుపుతుంది."',
        'fontHelperBtn': '"సెటప్‌ను డౌన్‌లోడ్ చేయండి (.exe)"'
    },
    'ta': {
        'pagemakerBtnText': '"PageMaker ஆட்டோ எழுத்துரு மாற்றியைத் திற"',
        'pagemakerTooltip': '"எழுத்துருக்களை கைமுறையாக மாற்றாமல், மாற்றப்பட்ட உரையை நேரடியாக Adobe PageMaker 7.0 உடன் பயன்படுத்தவும்."',
        'pagemakerPopupTitle': '"Adobe PageMaker 7.0"',
        'pagemakerPopupDesc': '"PageMaker ஆட்டோ எழுத்துரு மாற்றி நிறுவப்படவில்லை அல்லது திறக்க முடியவில்லை. இது வேலை செய்ய இந்த மென்பொருளை உங்கள் கணினியில் நிறுவவும்."',
        'pagemakerInstallBtn': '"PageMaker ஆட்டோ எழுத்துரு மாற்றியை நிறுவு"',
        'pagemakerTryAgainBtn': '"மீண்டும் முயற்சிக்கவும்"',
        'pwaInstallTitle': '"பயன்பாடாக நிறுவு"',
        'pwaInstallDesc': '"விரைவான அணுகலுக்காக இந்த இணையதளத்தை உங்கள் சாதனத்தில் ஒரு பயன்பாடாக நிறுவவும்."',
        'pwaInstallBtn': '"இணைய பயன்பாட்டை நிறுவு"',
        'fontHelperTitle': '"PageMaker ஆட்டோ எழுத்துரு மாற்றி"',
        'fontHelperDesc': '"Adobe PageMaker 7.0 க்கான சொந்த விண்டோஸ் உதவியாளர். இது நவீன இணைய கிளிப்போர்டை மரபு ரிச் டெக்ஸ்ட் ஃபார்மேட் (RTF) தேவைகளுடன் இணைக்கிறது."',
        'fontHelperBtn': '"அமைப்பை பதிவிறக்கம் செய் (.exe)"'
    },
    'kn': {
        'pagemakerBtnText': '"PageMaker ಆಟೋ ಫಾಂಟ್ ಚೇಂಜರ್ ತೆರೆಯಿರಿ"',
        'pagemakerTooltip': '"ಫಾಂಟ್‌ಗಳನ್ನು ಹಸ್ತಚಾಲಿತವಾಗಿ ಬದಲಾಯಿಸದೆ ಅಡೋಬ್ ಪೇಜ್ ಮೇಕರ್ 7.0 ನೊಂದಿಗೆ ಪರಿವರ್ತಿಸಲಾದ ಪಠ್ಯವನ್ನು ನೇರವಾಗಿ ಬಳಸಿ."',
        'pagemakerPopupTitle': '"Adobe PageMaker 7.0"',
        'pagemakerPopupDesc': '"PageMaker ಆಟೋ ಫಾಂಟ್ ಚೇಂಜರ್ ಅನ್ನು ಸ್ಥಾಪಿಸಲಾಗಿಲ್ಲ ಅಥವಾ ತೆರೆಯಲಾಗಲಿಲ್ಲ. ಇದು ಕೆಲಸ ಮಾಡಲು ಈ ಸಾಫ್ಟ್‌ವೇರ್ ಅನ್ನು ನಿಮ್ಮ PC ಯಲ್ಲಿ ಸ್ಥಾಪಿಸಿ."',
        'pagemakerInstallBtn': '"PageMaker ಆಟೋ ಫಾಂಟ್ ಚೇಂಜರ್ ಸ್ಥಾಪಿಸಿ"',
        'pagemakerTryAgainBtn': '"ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ"',
        'pwaInstallTitle': '"ಅಪ್ಲಿಕೇಶನ್ ಆಗಿ ಸ್ಥಾಪಿಸಿ"',
        'pwaInstallDesc': '"ತ್ವರಿತ ಪ್ರವೇಶಕ್ಕಾಗಿ ಈ ವೆಬ್‌ಸೈಟ್ ಅನ್ನು ನಿಮ್ಮ ಸಾಧನದಲ್ಲಿ ಅಪ್ಲಿಕೇಶನ್ ಆಗಿ ಸ್ಥಾಪಿಸಿ."',
        'pwaInstallBtn': '"ವೆಬ್ ಅಪ್ಲಿಕೇಶನ್ ಸ್ಥಾಪಿಸಿ"',
        'fontHelperTitle': '"PageMaker ಆಟೋ ಫಾಂಟ್ ಚೇಂಜರ್"',
        'fontHelperDesc': '"Adobe PageMaker 7.0 ಗಾಗಿ ಸ್ಥಳೀಯ ವಿಂಡೋಸ್ ಸಹಾಯಕ. ಇದು ಆಧುನಿಕ ವೆಬ್ ಕ್ಲಿಪ್‌ಬೋರ್ಡ್ ಅನ್ನು ಲೆಗಸಿ ರಿಚ್ ಟೆಕ್ಸ್ಟ್ ಫಾರ್ಮ್ಯಾಟ್ (RTF) ಅವಶ್ಯಕತೆಗಳೊಂದಿಗೆ ಸೇರಿಸುತ್ತದೆ."',
        'fontHelperBtn': '"ಸೆಟಪ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ (.exe)"'
    },
    'ml': {
        'pagemakerBtnText': '"PageMaker ഓട്ടോ ഫോണ്ട് ചേഞ്ചർ തുറക്കുക"',
        'pagemakerTooltip': '"ഫോണ്ടുകൾ സ്വമേധയാ മാറ്റാതെ Adobe PageMaker 7.0 ഉപയോഗിച്ച് പരിവർത്തനം ചെയ്ത വാചകം നേരിട്ട് ഉപയോഗിക്കുക."',
        'pagemakerPopupTitle': '"Adobe PageMaker 7.0"',
        'pagemakerPopupDesc': '"PageMaker ഓട്ടോ ഫോണ്ട് ചേഞ്ചർ ഇൻസ്റ്റാൾ ചെയ്തിട്ടില്ല അല്ലെങ്കിൽ തുറക്കാൻ കഴിഞ്ഞില്ല. ഇത് പ്രവർത്തിക്കാൻ നിങ്ങളുടെ പിസിയിൽ ഈ സോഫ്റ്റ്വെയർ ഇൻസ്റ്റാൾ ചെയ്യുക."',
        'pagemakerInstallBtn': '"PageMaker ഓട്ടോ ഫോണ്ട് ചേഞ്ചർ ഇൻസ്റ്റാൾ ചെയ്യുക"',
        'pagemakerTryAgainBtn': '"വീണ്ടും ശ്രമിക്കുക"',
        'pwaInstallTitle': '"ആപ്പായി ഇൻസ്റ്റാൾ ചെയ്യുക"',
        'pwaInstallDesc': '"വേഗത്തിലുള്ള ആക്സസിനായി നിങ്ങളുടെ ഉപകരണത്തിൽ ഈ വെബ്സൈറ്റ് ഒരു ആപ്പായി ഇൻസ്റ്റാൾ ചെയ്യുക."',
        'pwaInstallBtn': '"വെബ് ആപ്പ് ഇൻസ്റ്റാൾ ചെയ്യുക"',
        'fontHelperTitle': '"PageMaker ഓട്ടോ ഫോണ്ട് ചേഞ്ചർ"',
        'fontHelperDesc': '"Adobe PageMaker 7.0-നുള്ള ഒരു നേറ്റീവ് Windows സഹായി. ഇത് ആധുനിക വെബ് ക്ലിപ്പ്ബോർഡിനെ ലെഗസി റിച്ച് ടെക്സ്റ്റ് ഫോർമാറ്റ് (RTF) ആവശ്യകതകളുമായി ബന്ധിപ്പിക്കുന്നു."',
        'fontHelperBtn': '"സെറ്റപ്പ് ഡൗൺലോഡ് ചെയ്യുക (.exe)"'
    },
    'mr': {
        'pagemakerBtnText': '"PageMaker ऑटो फॉन्ट चेंजर उघडा"',
        'pagemakerTooltip': '"फॉन्ट स्वहस्ते न बदलता Adobe PageMaker 7.0 सह रूपांतरित मजकूर थेट वापरा."',
        'pagemakerPopupTitle': '"Adobe PageMaker 7.0"',
        'pagemakerPopupDesc': '"PageMaker ऑटो फॉन्ट चेंजर स्थापित केलेले नाही किंवा उघडता आले नाही. हे काम करण्यासाठी हे सॉफ्टवेअर आपल्या पीसीवर स्थापित करा."',
        'pagemakerInstallBtn': '"PageMaker ऑटो फॉन्ट चेंजर स्थापित करा"',
        'pagemakerTryAgainBtn': '"पुन्हा प्रयत्न करा"',
        'pwaInstallTitle': '"अॅप म्हणून स्थापित करा"',
        'pwaInstallDesc': '"द्रुत प्रवेशासाठी ही वेबसाइट आपल्या डिव्हाइसवर अॅप म्हणून स्थापित करा."',
        'pwaInstallBtn': '"वेब अॅप स्थापित करा"',
        'fontHelperTitle': '"PageMaker ऑटो फॉन्ट चेंजर"',
        'fontHelperDesc': '"Adobe PageMaker 7.0 साठी एक मूळ Windows सहाय्यक. हे आधुनिक वेब क्लिपबोर्डला जुन्या रिच टेक्स्ट फॉरमॅट (RTF) आवश्यकतांसह जोडते."',
        'fontHelperBtn': '"सेटअप डाउनलोड करा (.exe)"'
    },
    'gu': {
        'pagemakerBtnText': '"PageMaker ઓટો ફોન્ટ ચેન્જર ખોલો"',
        'pagemakerTooltip': '"ફોન્ટ્સને મેન્યુઅલી બદલ્યા વિના સીધા જ Adobe PageMaker 7.0 સાથે કન્વર્ટ કરેલ ટેક્સ્ટનો ઉપયોગ કરો."',
        'pagemakerPopupTitle': '"Adobe PageMaker 7.0"',
        'pagemakerPopupDesc': '"PageMaker ઓટો ફોન્ટ ચેન્જર ઇન્સ્ટોલ કરેલ નથી અથવા ખોલી શકાયું નથી. તેને કામ કરવા માટે તમારા પીસી પર આ સોફ્ટવેર ઇન્સ્ટોલ કરો."',
        'pagemakerInstallBtn': '"PageMaker ઓટો ફોન્ટ ચેન્જર ઇન્સ્ટોલ કરો"',
        'pagemakerTryAgainBtn': '"ફરી પ્રયાસ કરો"',
        'pwaInstallTitle': '"એપ્લિકેશન તરીકે ઇન્સ્ટોલ કરો"',
        'pwaInstallDesc': '"ઝડપી ઍક્સેસ માટે તમારા ઉપકરણ પર એપ્લિકેશન તરીકે આ વેબસાઇટને ઇન્સ્ટોલ કરો."',
        'pwaInstallBtn': '"વેબ એપ્લિકેશન ઇન્સ્ટોલ કરો"',
        'fontHelperTitle': '"PageMaker ઓટો ફોન્ટ ચેન્જર"',
        'fontHelperDesc': '"Adobe PageMaker 7.0 માટે મૂળ Windows સહાયક. તે આધુનિક વેબ ક્લિપબોર્ડને લેગસી રિચ ટેક્સ્ટ ફોર્મેટ (RTF) આવશ્યકતાઓ સાથે જોડે છે."',
        'fontHelperBtn': '"સેટઅપ ડાઉનલોડ કરો (.exe)"'
    }
}

for lang, keys in locales.items():
    filepath = f"src/utils/locales/{lang}.ts"
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # insert before the last closing brace
    # find last occurrence of }
    last_brace_idx = content.rfind('}')
    
    append_str = ",\n" + ",\n".join([f"  {k}: {v}" for k, v in keys.items()]) + "\n"
    
    new_content = content[:last_brace_idx] + append_str + content[last_brace_idx:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Updated translations successfully.")
