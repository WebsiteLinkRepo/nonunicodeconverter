import re
import urllib.request
import os

os.makedirs('shreelipi_fonts', exist_ok=True)
html = open('shree_page.html').read()
links = re.findall(r'href="(assets/marathi-fonts-shreelipi/[^"]+\.[tT][tT][fF])"', html)
base_url = "https://hindityping.info/download/"

print(f"Found {len(links)} fonts to download.")
for i, link in enumerate(links):
    url = base_url + link
    filename = os.path.basename(link)
    filepath = os.path.join('shreelipi_fonts', filename)
    if not os.path.exists(filepath):
        #print(f"Downloading {filename} ({i+1}/{len(links)})...")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            data = urllib.request.urlopen(req).read()
            with open(filepath, 'wb') as f:
                f.write(data)
        except Exception as e:
            print(f"Error downloading {filename}: {e}")
print("Done downloading!")
