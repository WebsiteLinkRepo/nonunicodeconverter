import urllib.request, json
url = "https://api.github.com/search/code?q=bamini+unicode+tamil+language:javascript"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        for item in data.get('items', [])[:5]:
            print(f"https://raw.githubusercontent.com/{item['repository']['full_name']}/master/{item['path']}")
except Exception as e:
    print(e)
