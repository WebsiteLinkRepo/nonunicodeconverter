import urllib.request
url = "https://raw.githubusercontent.com/tshrinivasan/bamini2unicode/master/bamini2unicode.py"
try:
    req = urllib.request.urlopen(url)
    print(req.read().decode('utf-8')[:1000])
except Exception as e:
    print(e)
