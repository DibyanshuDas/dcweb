import urllib.request
import re
import json

with open('src/data.ts', 'r') as f:
    ts_data = f.read()

# Extract names from ts_data
names = re.findall(r'name:\s*"([^"]+)"', ts_data)

url = "https://www.180dciitkgp.in/team"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    resp = urllib.request.urlopen(req)
    html = resp.read().decode('utf-8')
except Exception as e:
    print("Error fetching:", e)
    exit(1)

img_matches = list(re.finditer(r'<img[^>]+src="(https://lh3\.googleusercontent\.com/sitesv/[^"]+)"[^>]*>', html))

replacements = {}

for name in names:
    # Google Sites might have the name split or in spans, but let's try direct find first
    # Some names might be all caps or something
    name_pos = html.find(name)
    if name_pos == -1:
        # try case insensitive or partial
        first_name = name.split()[0]
        # find all occurrences of first_name
        for m in re.finditer(r'\b' + re.escape(first_name) + r'\b', html, re.IGNORECASE):
            name_pos = m.start()
            break

    if name_pos != -1:
        # find the image immediately preceding this name
        closest_img = None
        closest_dist = float('inf')
        for m in img_matches:
            if m.start() < name_pos and (name_pos - m.start()) < closest_dist:
                closest_dist = name_pos - m.start()
                closest_img = m.group(1)
        
        if closest_img and closest_dist < 5000: # sanity check on distance
            replacements[name] = closest_img

# Now update data.ts
def replacer(match):
    name = match.group(1)
    if name in replacements:
        return f'name: "{name}"{match.group(2)}avatar: "{replacements[name]}"'
    return match.group(0)

new_ts_data = re.sub(r'name:\s*"([^"]+)"(.*?)\bavatar:\s*"[^"]+"', replacer, ts_data, flags=re.DOTALL)

with open('src/data.ts', 'w') as f:
    f.write(new_ts_data)

print(f"Updated {len(replacements)} avatars from Google Sites.")

