import urllib.request
from bs4 import BeautifulSoup
url = "https://www.180dciitkgp.in/team"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
html = resp.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
for p in soup.find_all('p'):
    text = p.get_text()
    if 'Rachit' in text:
        print("Found Rachit in paragraph!")
        parent = p.find_parent('div')
        # walk up and find images
        for i in range(5):
            if not parent: break
            imgs = parent.find_all('img')
            print(f"Level {i}, imgs: {len(imgs)}")
            parent = parent.parent
