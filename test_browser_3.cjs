const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  page.on('console', msg => console.log('BROWSER LOG:', msg.text()));
  await page.goto('http://localhost:4321');
  await page.evaluate(() => {
    const val = 'அனைவருக்கும்';
    const hasTelugu = /[\u0C00-\u0C7F]/.test(val);
    const hasTamil = /[\u0B80-\u0BFF]/.test(val);
    console.log("hasTelugu:", hasTelugu, "hasTamil:", hasTamil);
  });
  await browser.close();
})();
