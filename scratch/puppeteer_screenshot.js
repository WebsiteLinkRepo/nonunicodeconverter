import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('file://' + process.cwd() + '/scratch/test_space.html');
  await page.screenshot({ path: 'scratch/test_space2.png' });
  await browser.close();
})();
