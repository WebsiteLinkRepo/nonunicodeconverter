import re
import urllib.request
import os

html = open('shree_page_2.html').read()
links = re.findall(r'href="(assets/shreelipi-page2/[^"]+\.[tT][tT][fF])"', html)
base_url = "https://hindityping.info/download/"

print(f"Found {len(links)} fonts to download on page 2.")
for i, link in enumerate(links):
    url = base_url + link
    filename = os.path.basename(link)
    filepath = os.path.join('shreelipi_fonts', filename)
    if not os.path.exists(filepath):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            data = urllib.request.urlopen(req).read()
            with open(filepath, 'wb') as f:
                f.write(data)
        except Exception as e:
            print(f"Error downloading {filename}: {e}")
print("Done downloading page 2!")
