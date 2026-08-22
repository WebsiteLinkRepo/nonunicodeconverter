const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const filePath = 'file://' + path.resolve('public/font_samples_all.html');
  await page.goto(filePath);
  await page.waitForTimeout(2000);
  await page.screenshot({ path: 'font_samples_all.png', fullPage: true });
  await browser.close();
  console.log('Screenshot saved to font_samples_all.png');
})();
