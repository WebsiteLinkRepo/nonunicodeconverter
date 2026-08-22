const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  page.on('console', msg => console.log('BROWSER LOG:', msg.text()));
  await page.goto('http://localhost:4321');
  await page.evaluate(() => {
    const input = document.getElementById('input-text');
    input.addEventListener('input', (e) => {
      console.log('Is instance of Event:', e instanceof Event);
      console.log('typeof:', typeof e);
    });
    input.value = 'a';
    input.dispatchEvent(new Event('input'));
  });
  await browser.close();
})();
