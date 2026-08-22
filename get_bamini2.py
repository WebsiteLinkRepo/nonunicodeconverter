import urllib.request
import json
url = "https://api.github.com/search/code?q=bamini+unicode+tamil"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    response = urllib.request.urlopen(req)
    data = json.loads(response.read().decode('utf-8'))
    for item in data.get('items', [])[:3]:
        print(item['html_url'])
        print(item['repository']['full_name'], item['path'])
except Exception as e:
    print(e)
