const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  page.on('console', msg => console.log('BROWSER LOG:', msg.text()));
  page.on('pageerror', err => console.log('BROWSER ERROR:', err));
  await page.goto('http://localhost:4321');
  await page.waitForTimeout(1000);
  await page.fill('textarea#input-text', 'அனைவருக்கும்');
  await page.waitForTimeout(1000);
  const out = await page.inputValue('textarea#output-text');
  console.log("Output is:", out);
  await browser.close();
})();
