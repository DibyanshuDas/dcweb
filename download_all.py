import urllib.request
import re
import os
import json
import time

with open('src/data.ts', 'r') as f:
    ts_data = f.read()

# Extract names and slugs
names_slugs = re.findall(r'name:\s*"([^"]+)"(.*?)\bavatar:\s*"([^"]+)"', ts_data, flags=re.DOTALL)

# Fetch site
url = "https://www.180dciitkgp.in/team"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
html = resp.read().decode('utf-8')

img_matches = list(re.finditer(r'<img[^>]+src="(https://lh3\.googleusercontent\.com/sitesv/[^"]+)"[^>]*>', html))

print(f"Found {len(img_matches)} images on site.")

def download(url, path):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        r = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
        with open(path, 'wb') as f:
            f.write(r.read())
        return True
    except Exception as e:
        print(f"Failed to download {url} to {path}: {e}")
        return False

# 1. Download group images
# The first few images in Google Sites are usually the header, etc.
# Let's download the 1st, 2nd, 3rd non-logo images for group photos?
# Wait, let's just use the first 3 images. 
download(img_matches[3].group(1), "public/team/group/1.jpg")
download(img_matches[4].group(1), "public/team/group/2.jpg")
download(img_matches[5].group(1), "public/team/group/3.jpg")

# 2. Download avatars
success = 0
for name, _, slug in names_slugs:
    slug = slug.strip()
    name_pos = html.find(name)
    if name_pos == -1:
        first_name = name.split()[0]
        for m in re.finditer(r'\b' + re.escape(first_name) + r'\b', html, re.IGNORECASE):
            name_pos = m.start()
            break
            
    if name_pos != -1:
        closest_img = None
        closest_dist = float('inf')
        for m in img_matches:
            if m.start() < name_pos and (name_pos - m.start()) < closest_dist:
                closest_dist = name_pos - m.start()
                closest_img = m.group(1)
                
        if closest_img and slug.startswith('/team/'):
            # slug looks like /team/rachit-arora.jpg
            # map to public/team/rachit-arora.jpg
            local_path = "public" + slug
            if download(closest_img, local_path):
                success += 1
            time.sleep(0.05) # avoid rate limit

print(f"Downloaded {success} avatars.")
