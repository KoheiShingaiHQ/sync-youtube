const puppeteer = require('puppeteer');
const validUrl = require('valid-url');


(async () => {
  if (process.argv.length != 4) {
    console.log('Usage: $ npm start -- {Target URL} {URL Hash}');
    process.exit();
  }
  
  url = process.argv[2]
  hash = process.argv[3]
  
  if(!validUrl.isUri(url)) {
    console.log(url + ' is not a valid URL.');
    process.exit();
  }

  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(url);

  const text = await page.evaluate(() => {
    var url = location.href;
    var title = document.title.split('"').join('\\"');
    var content = document.body.innerText.split('\n').join(' ');
    content = content.split('"').join('\\"');
    return '{"url": "' + url + '",' +
      '"title": "' + title + '",' +
      '"content": "' + content + '"}'
  });
  
  console.log(text);
  await page.setViewport({width: 1980, height: 100, isMobile: false})
  await page.screenshot({path: './storage/' + hash + '.desktop.png', fullPage: true});
  await page.setViewport({width: 840, height: 100, isMobile: true})
  await page.screenshot({path: './storage/' + hash + '.mobile.png', fullPage: true});

  browser.close();
})();