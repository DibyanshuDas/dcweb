import urllib.request
import re
url = "https://www.180dciitkgp.in/team"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
html = resp.read().decode('utf-8')
m = list(re.finditer(r'<img[^>]+src="(https://lh3\.googleusercontent\.com/sitesv/[^"]+)"[^>]*>', html))[6]
start = max(0, m.start() - 500)
end = min(len(html), m.end() + 1000)
print(html[start:end])
