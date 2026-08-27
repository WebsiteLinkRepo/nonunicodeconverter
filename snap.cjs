const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({args: ['--no-sandbox']});
  const page = await browser.newPage();
  await page.setViewport({ width: 1200, height: 3500 });
  await page.goto('file://' + __dirname + '/map.html');
  await page.screenshot({path: 'map_snap.png', fullPage: true});
  await browser.close();
})();
