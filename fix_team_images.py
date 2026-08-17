import re

with open('src/pages/Team.tsx', 'r') as f:
    content = f.read()

# Add referrerPolicy="no-referrer" to all img tags where d.avatar, advisor.avatar, or alumnus.avatar is used
content = re.sub(r'(<img src=\{[^}]+\.avatar\} alt=\{[^}]+\} className="[^"]+")', r'\1 referrerPolicy="no-referrer"', content)

with open('src/pages/Team.tsx', 'w') as f:
    f.write(content)
print("Done")
