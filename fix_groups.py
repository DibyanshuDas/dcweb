import urllib.request
import re
import os
url = "https://www.180dciitkgp.in/team"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
html = resp.read().decode('utf-8')
img_matches = list(re.finditer(r'<img[^>]+src="(https://lh3\.googleusercontent\.com/sitesv/[^"]+)"[^>]*>', html))

def download(url, path):
    r = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
    with open(path, 'wb') as f:
        f.write(r.read())

download(img_matches[2].group(1), "public/team/group/1.jpg")
download(img_matches[3].group(1), "public/team/group/2.jpg")
download(img_matches[4].group(1), "public/team/group/3.jpg")
