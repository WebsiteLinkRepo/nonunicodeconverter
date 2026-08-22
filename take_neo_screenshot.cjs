const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const filePath = 'file://' + path.resolve('public/font_ext_samples.html');
  await page.goto(filePath);
  await page.waitForTimeout(2000);
  await page.screenshot({ path: 'neo_samples.png', fullPage: true });
  await browser.close();
  console.log('Screenshot saved to neo_samples.png');
})();
