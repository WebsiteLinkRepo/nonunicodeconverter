# Interactive Test 16: Anu Script Tamil - Paragraphs

## Overview
Test suite verifying 100% roundtrip conversion for complex flowing sentences containing mixed vowels, grantha consonants, special ligatures, punctuation, spaces, and pre-base signs.

### Test Case 1: General Paragraph
**Input (Unicode Tamil):** 
தமிழ் மொழி உலகின் மிகப் பழமையான மற்றும் மிகவும் சிறப்பு வாய்ந்த செம்மொழிகளுள் ஒன்றாகும்.

**Anu Legacy Output:**
`jkpo; nkhop cyfpd; kpfg; giokahd kw;Wk; kpfTk; rpwg;G tha;e;j nrk;nkhopfSs; xd;whFk;.`

**Round-trip Result:** 
தமிழ் மொழி உலகின் மிகப் பழமையான மற்றும் மிகவும் சிறப்பு வாய்ந்த செம்மொழிகளுள் ஒன்றாகும்.
✅ **PASS (100% Match)**

---

### Test Case 2: Country Description
**Input (Unicode Tamil):** 
இது இந்தியாவின் தமிழ் நாடு மாநிலத்தின் முதன்மை மொழியாகும்.

**Anu Legacy Output:**
`,J ,e;jpahtpd; jkpo; ehL khepyj;jpd; Kijd;k nkhopahFk;.`

**Round-trip Result:** 
இது இந்தியாவின் தமிழ் நாடு மாநிலத்தின் முதன்மை மொழியாகும்.
✅ **PASS (100% Match)**

---

### Test Case 3: Advanced Grantha Paragraph
**Input (Unicode Tamil):** 
ஸ்ரீராமன் மற்றும் லக்ஷ்மணன் ஆகியோர் மஹரிஷி விஸ்வாமித்திரருடன் சென்றனர்.

**Anu Legacy Output:**
`=uhkd; kw;Wk; yf;\;kzd; MfpNahu; k\`;up\p tp];thkpj;jpuUld; nrd;wdu;.`

**Round-trip Result:** 
ஸ்ரீராமன் மற்றும் லக்ஷ்மணன் ஆகியோர் மஹரிஷி விஸ்வாமித்திரருடன் சென்றனர்.
✅ **PASS (100% Match)**

---

### Test Case 4: Complex Formatting
**Input (Unicode Tamil):** 
அங்கு அவர்கள் ஞானம், க்ஷமை, அஸ்திர சாஸ்திரங்கள் ஆகியவற்றைக் கற்றுக்கொண்டனர்.

**Anu Legacy Output:**
`mq;F mtu;fs; Qhdk;> f;\ik> m];jpu rh];jpuq;fs; Mfpaitw;wf; fw;Wf;nfhz;ldu;.`

**Round-trip Result:** 
அங்கு அவர்கள் ஞானம், க்ஷமை, அஸ்திர சாஸ்திரங்கள் ஆகியவற்றைக் கற்றுக்கொண்டனர்.
✅ **PASS (100% Match)**
