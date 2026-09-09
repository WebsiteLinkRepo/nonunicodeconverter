import re

tooltips_dict = {
    "en": {
        "tooltipExactFont": "Select exact font to paste formatted text directly into Word/Photoshop with this font.",
        "tooltipAltRaaTitle": "Only check this box if you are using these fonts:",
        "tooltipAltRaaWhy": "These specific fonts have their Ra Vatthu (్ర) drawn on the right side of the letter. This formats the text properly for them.",
        "tooltipDisabled": "(disabled)",
        "tooltipUncheckAlt": "Uncheck Alt Raa Vatthu to use this font",
        "tooltipCheckAlt": "Check Alt Raa Vatthu to use this font"
    },
    "hi": {
        "tooltipExactFont": "वर्ड/फोटोशॉप में सीधे फॉर्मैटेड टेक्स्ट पेस्ट करने के लिए सटीक फॉन्ट चुनें।",
        "tooltipAltRaaTitle": "इस बॉक्स को तभी चेक करें जब आप इन फॉन्ट्स का उपयोग कर रहे हों:",
        "tooltipAltRaaWhy": "इन विशिष्ट फॉन्ट्स में र वत्थु (్ర) अक्षर के दाईं ओर होता है। यह टेक्स्ट को ठीक से फॉर्मैट करता है।",
        "tooltipDisabled": "(अक्षम)",
        "tooltipUncheckAlt": "इस फॉन्ट का उपयोग करने के लिए Alt Raa Vatthu को अनचेक करें",
        "tooltipCheckAlt": "इस फॉन्ट का उपयोग करने के लिए Alt Raa Vatthu को चेक करें"
    },
    "te": {
        "tooltipExactFont": "వర్డ్/ఫోటోషాప్‌లో నేరుగా ఫార్మాట్ చేయబడిన టెక్స్ట్‌ని పేస్ట్ చేయడానికి ఖచ్చితమైన ఫాంట్‌ను ఎంచుకోండి.",
        "tooltipAltRaaTitle": "మీరు ఈ ఫాంట్‌లను ఉపయోగిస్తుంటే మాత్రమే ఈ బాక్స్‌ను చెక్ చేయండి:",
        "tooltipAltRaaWhy": "ఈ నిర్దిష్ట ఫాంట్‌లలో ర వత్తు (్ర) అక్షరానికి కుడివైపున ఉంటుంది. ఇది వాటిని సరిగ్గా ఫార్మాట్ చేస్తుంది.",
        "tooltipDisabled": "(నిలిపివేయబడింది)",
        "tooltipUncheckAlt": "ఈ ఫాంట్‌ని ఉపయోగించడానికి Alt Raa Vatthu చెక్‌ను తీసివేయండి",
        "tooltipCheckAlt": "ఈ ఫాంట్‌ని ఉపయోగించడానికి Alt Raa Vatthu చెక్ చేయండి"
    },
    "ta": {
        "tooltipExactFont": "வேர்ட்/போட்டோஷாப்பில் நேரடியாக உரையை ஒட்ட சரியான எழுத்துருவை தேர்ந்தெடுக்கவும்.",
        "tooltipAltRaaTitle": "நீங்கள் இந்த எழுத்துருக்களை பயன்படுத்தினால் மட்டுமே இதை தேர்ந்தெடுக்கவும்:",
        "tooltipAltRaaWhy": "இந்த குறிப்பிட்ட எழுத்துருக்களில் ர வத்து (్ర) எழுத்தின் வலது பக்கத்தில் இருக்கும்.",
        "tooltipDisabled": "(முடக்கப்பட்டுள்ளது)",
        "tooltipUncheckAlt": "இந்த எழுத்துருவை பயன்படுத்த Alt Raa Vatthu-ஐ நீக்கவும்",
        "tooltipCheckAlt": "இந்த எழுத்துருவை பயன்படுத்த Alt Raa Vatthu-ஐ தேர்ந்தெடுக்கவும்"
    },
    "kn": {
        "tooltipExactFont": "ವರ್ಡ್/ಫೋಟೋಶಾಪ್‌ನಲ್ಲಿ ನೇರವಾಗಿ ಪಠ್ಯವನ್ನು ಅಂಟಿಸಲು ನಿಖರವಾದ ಫಾಂಟ್ ಆಯ್ಕೆಮಾಡಿ.",
        "tooltipAltRaaTitle": "ನೀವು ಈ ಫಾಂಟ್‌ಗಳನ್ನು ಬಳಸುತ್ತಿದ್ದರೆ ಮಾತ್ರ ಇದನ್ನು ಚೆಕ್ ಮಾಡಿ:",
        "tooltipAltRaaWhy": "ಈ ನಿರ್ದಿಷ್ಟ ಫಾಂಟ್‌ಗಳಲ್ಲಿ ರ ವತ್ತು (್ರ) ಅಕ್ಷರದ ಬಲಭಾಗದಲ್ಲಿರುತ್ತದೆ.",
        "tooltipDisabled": "(ನಿಷ್ಕ್ರಿಯಗೊಳಿಸಲಾಗಿದೆ)",
        "tooltipUncheckAlt": "ಈ ಫಾಂಟ್ ಬಳಸಲು Alt Raa Vatthu ಅನ್ನು ಅನ್ಚೆಕ್ ಮಾಡಿ",
        "tooltipCheckAlt": "ಈ ಫಾಂಟ್ ಬಳಸಲು Alt Raa Vatthu ಅನ್ನು ಚೆಕ್ ಮಾಡಿ"
    },
    "ml": {
        "tooltipExactFont": "വേഡ്/ഫോട്ടോഷോപ്പിൽ നേരിട്ട് ടെക്സ്റ്റ് പേസ്റ്റ് ചെയ്യാൻ കൃത്യമായ ഫോണ്ട് തിരഞ്ഞെടുക്കുക.",
        "tooltipAltRaaTitle": "നിങ്ങൾ ഈ ഫോണ്ടുകൾ ഉപയോഗിക്കുന്നുവെങ്കിൽ മാത്രം ഇത് തിരഞ്ഞെടുക്കുക:",
        "tooltipAltRaaWhy": "ഈ പ്രത്യേക ഫോണ്ടുകളിൽ ര വത്തു (്ര) അക്ഷരത്തിന്റെ വലതുഭാഗത്തായിരിക്കും.",
        "tooltipDisabled": "(അപ്രാപ്തമാക്കി)",
        "tooltipUncheckAlt": "ഈ ഫോണ്ട് ഉപയോഗിക്കാൻ Alt Raa Vatthu അൺചെക്ക് ചെയ്യുക",
        "tooltipCheckAlt": "ഈ ഫോണ്ട് ഉപയോഗിക്കാൻ Alt Raa Vatthu ചെക്ക് ചെയ്യുക"
    },
    "mr": {
        "tooltipExactFont": "वर्ड/फोटोशॉपमध्ये थेट फॉरमॅट केलेला मजकूर पेस्ट करण्यासाठी अचूक फॉन्ट निवडा.",
        "tooltipAltRaaTitle": "तुम्ही हे फॉन्ट वापरत असल्यासच या बॉक्सवर खूण करा:",
        "tooltipAltRaaWhy": "या विशिष्ट फॉन्टमध्ये र वत्थु (్ర) अक्षराच्या उजव्या बाजूला असतो.",
        "tooltipDisabled": "(अक्षम)",
        "tooltipUncheckAlt": "हा फॉन्ट वापरण्यासाठी Alt Raa Vatthu अनचेक करा",
        "tooltipCheckAlt": "हा फॉन्ट वापरण्यासाठी Alt Raa Vatthu चेक करा"
    },
    "gu": {
        "tooltipExactFont": "વર્ડ/ફોટોશોપમાં સીધો ટેક્સ્ટ પેસ્ટ કરવા માટે ચોક્કસ ફોન્ટ પસંદ કરો.",
        "tooltipAltRaaTitle": "જો તમે આ ફોન્ટનો ઉપયોગ કરી રહ્યા હોવ તો જ આ બોક્સને ચેક કરો:",
        "tooltipAltRaaWhy": "આ ચોક્કસ ફોન્ટ્સમાં ર વત્થુ (్ర) અક્ષરની જમણી બાજુએ હોય છે.",
        "tooltipDisabled": "(અક્ષમ)",
        "tooltipUncheckAlt": "આ ફોન્ટનો ઉપયોગ કરવા માટે Alt Raa Vatthu ને અનચેક કરો",
        "tooltipCheckAlt": "આ ફોન્ટનો ઉપયોગ કરવા માટે Alt Raa Vatthu ને ચેક કરો"
    }
}

with open('/home/samuelvictor/nonunicodeconverter.com/src/utils/i18n.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Update Interface ONLY (first occurrence of '  fonts: {')
interface_str = """
  tooltipExactFont: string;
  tooltipAltRaaTitle: string;
  tooltipAltRaaWhy: string;
  tooltipDisabled: string;
  tooltipUncheckAlt: string;
  tooltipCheckAlt: string;
  fonts: {"""

content = content.replace("  fonts: {", interface_str.lstrip('\n'), 1)

# Now iterate languages and inject string values just before their fonts block
for lang, obj in tooltips_dict.items():
    pattern = rf"({lang}:\s*{{.*?)(    fonts: {{)"
    replacement = ""
    for k, v in obj.items():
        replacement += f'    {k}: "{v}",\n'
    
    content = re.sub(pattern, r'\1' + replacement + r'\2', content, flags=re.DOTALL)

with open('/home/samuelvictor/nonunicodeconverter.com/src/utils/i18n.ts', 'w', encoding='utf-8') as f:
    f.write(content)
print("safe update complete")
