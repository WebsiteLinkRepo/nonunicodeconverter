const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const filePath = 'file://' + path.resolve('public/hindi_anu_map.html');
  await page.goto(filePath);
  await page.waitForTimeout(1000); // Wait for font to load
  await page.screenshot({ path: 'hindi_anu_map.png', fullPage: true });
  await browser.close();
  console.log('Screenshot saved to hindi_anu_map.png');
})();
