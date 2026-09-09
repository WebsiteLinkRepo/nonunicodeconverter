from bs4 import BeautifulSoup

with open('/home/samuelvictor/nonunicodeconverter.com/dist/index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

links = soup.find_all('link', attrs={'hreflang': True})
for link in links:
    print(f"{link.get('hreflang')} -> {link.get('href')}")
