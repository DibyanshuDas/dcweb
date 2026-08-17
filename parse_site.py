import urllib.request
import re

url = "https://www.180dciitkgp.in/team"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
html = resp.read().decode('utf-8')

# The names are likely in text nodes. Let's look for known names and see if we can find the closest preceding image.
known_names = ["Arghyadip Pal", "Adarsh Jha", "Rishi", "Mayank", "Mani", "Udai", "Prakhar"]

# find all img tags with googleusercontent
img_matches = list(re.finditer(r'<img[^>]+src="(https://lh3\.googleusercontent\.com/sitesv/[^"]+)"[^>]*>', html))
text_blocks = list(re.finditer(r'>([^<]{3,30})<', html))

print(f"Found {len(img_matches)} images")
for name in known_names:
    name_pos = html.find(name)
    if name_pos != -1:
        # find the image right before this name
        closest_img = None
        for m in img_matches:
            if m.start() < name_pos:
                closest_img = m.group(1)
        print(f"{name}: {closest_img}")

