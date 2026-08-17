import re

with open('src/data.ts', 'r') as f:
    content = f.read()

def replacer(match):
    name = match.group(1)
    encoded_name = name.replace(' ', '+')
    new_avatar = f'https://ui-avatars.com/api/?name={encoded_name}&background=random'
    return f'name: "{name}"{match.group(2)}avatar: "{new_avatar}"'

content = re.sub(r'name:\s*"([^"]+)"(.*?)\bavatar:\s*"[^"]+"', replacer, content, flags=re.DOTALL)

with open('src/data.ts', 'w') as f:
    f.write(content)
print("Team avatars updated")
