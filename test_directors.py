import urllib.request
import re
url = "https://www.180dciitkgp.in/team"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
html = resp.read().decode('utf-8')
img_matches = list(re.finditer(r'<img[^>]+src="(https://lh3\.googleusercontent\.com/sitesv/[^"]+)"[^>]*>', html))

names = ["Rachit Arora", "Nidhi Swamy", "Dhruv Gupta", "Kabir Ladha"]
for name in names:
    pos = html.find(name)
    print(f"\n{name} pos: {pos}")
    for i, m in enumerate(img_matches):
        dist = pos - m.start()
        if -5000 < dist < 5000:
            print(f"Img {i} dist: {dist}")
