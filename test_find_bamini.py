# Let's search the repo for any other hints of Bamini or use python to download a known good bamini mapping.
import urllib.request
url = "https://raw.githubusercontent.com/arulalant/txt2unicode/master/txt2unicode/encodings/bamini.py"
try:
    req = urllib.request.urlopen(url)
    print(req.read().decode('utf-8'))
except Exception as e:
    print(e)
