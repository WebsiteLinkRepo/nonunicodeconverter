import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch({headless: "new"});
  const page = await browser.newPage();
  await page.goto('file://' + process.cwd() + '/scratch/render_test.html');
  await page.screenshot({path: 'scratch/actual.png'});
  await browser.close();
})();
