import urllib.request
import re
url = "https://www.180dciitkgp.in/team"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
html = resp.read().decode('utf-8')
img_matches = list(re.finditer(r'<img[^>]+src="(https://lh3\.googleusercontent\.com/sitesv/[^"]+)"[^>]*>', html))

import os
for i in range(10):
    url = img_matches[i].group(1)
    os.system(f'curl -s "{url}" -o test_img_{i}.jpg')
    os.system(f'file test_img_{i}.jpg')
