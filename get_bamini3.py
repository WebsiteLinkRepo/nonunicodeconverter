import urllib.request
import json
url = "https://raw.githubusercontent.com/tshrinivasan/bamini2unicode/master/bamini2unicode.py"
url2 = "https://raw.githubusercontent.com/thamizha/thamizha/master/old/bamini.map"
url3 = "https://raw.githubusercontent.com/arulalant/txt2unicode/master/txt2unicode/bamini.py"
url4 = "https://raw.githubusercontent.com/senthilnayagam/tamil-font-converter/master/src/bamini.js"

for u in [url, url2, url3, url4]:
    try:
        print(f"Trying {u}")
        req = urllib.request.urlopen(u)
        print(req.read().decode('utf-8')[:500])
        break
    except Exception as e:
        print(e)
