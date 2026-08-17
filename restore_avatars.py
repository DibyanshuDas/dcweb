import re

with open('src/data.ts', 'r') as f:
    content = f.read()

def replacer(match):
    name = match.group(1)
    # lowercase and hyphenate
    slug = name.lower().replace(' ', '-')
    slug = re.sub(r'[^a-z0-9\.-]', '', slug)
    return f'name: "{name}"{match.group(2)}avatar: "/team/{slug}.jpg"'

def replacer_alumni(match):
    name = match.group(1)
    slug = name.lower().replace(' ', '-')
    slug = re.sub(r'[^a-z0-9\.-]', '', slug)
    return f'name: "{name}"{match.group(2)}avatar: "/team/alumni/{slug}.jpg"'

parts = content.split('alumni: [')
if len(parts) == 2:
    part1 = re.sub(r'name:\s*"([^"]+)"(.*?)\bavatar:\s*"[^"]+"', replacer, parts[0], flags=re.DOTALL)
    part2 = re.sub(r'name:\s*"([^"]+)"(.*?)\bavatar:\s*"[^"]+"', replacer_alumni, parts[1], flags=re.DOTALL)
    content = part1 + 'alumni: [' + part2
else:
    content = re.sub(r'name:\s*"([^"]+)"(.*?)\bavatar:\s*"[^"]+"', replacer, content, flags=re.DOTALL)

with open('src/data.ts', 'w') as f:
    f.write(content)
print("Avatars restored to local paths.")
