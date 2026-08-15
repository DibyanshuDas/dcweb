import re

files = [
    'src/pages/Home.tsx',
    'src/pages/Services.tsx', 
    'src/pages/Projects.tsx', 
    'src/pages/Resources.tsx', 
    'src/pages/Contact.tsx'
]

for filename in files:
    with open(filename, 'r') as f:
        content = f.read()

    # Replace the text-transparent and stroke style with the solid green color text-[#86BC2A]
    content = re.sub(
        r'<span className="text-transparent"[^>]+style=\{\{.*?\}\}>',
        r'<span className="text-[#86BC2A]">',
        content
    )
    
    with open(filename, 'w') as f:
        f.write(content)

print("Done")
