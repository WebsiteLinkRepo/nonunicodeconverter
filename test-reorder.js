let resultText = "çdÓï eTÔáà«+ kÍÇÔá+çÔá«+";

// Simulate mapping for these specific characters
resultText = resultText.replace(/ç/g, "\u0C4D\u0C30"); // ్ర
resultText = resultText.replace(/dÓï/g, "\u0C38\u0C40\u0C4D\u0C32\u0C41"); // స్త్రీలు (simplified for test)
resultText = resultText.replace(/Ôá/g, "\u0C24"); // త
resultText = resultText.replace(/«/g, "\u0C4D\u0C2F"); // ్య
resultText = resultText.replace(/\+/g, "\u0C02"); // ం
resultText = resultText.replace(/eT/g, "\u0C2E"); // మ
resultText = resultText.replace(/kÍÇ/g, "\u0C38\u0C4D\u0C35\u0C3E"); // స్వా

// New reorder logic: Raa Vatthu before consonant -> Consonant + Raa Vatthu
resultText = resultText.replace(/(\u0C4D\u0C30)([\u0C15-\u0C39\u0C58-\u0C5A])/g, '$2$1');

console.log(resultText);
