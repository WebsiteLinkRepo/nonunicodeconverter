const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  page.on('console', msg => console.log('BROWSER LOG:', msg.text()));
  await page.goto('http://localhost:4321');
  await page.waitForTimeout(1000);
  await page.fill('textarea#input-text', 'அனைவருக்கும்');
  await page.waitForTimeout(1000);
  const scriptSelect = await page.inputValue('select#script-select');
  const fontVersion = await page.inputValue('select#font-version-select');
  const out = await page.inputValue('textarea#output-text');
  console.log("Script Select:", scriptSelect);
  console.log("Font Version:", fontVersion);
  console.log("Output is:", out);
  await browser.close();
})();
