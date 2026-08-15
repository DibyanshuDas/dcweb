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

    # Replace the webkit-text-stroke with SVG-like standard CSS stroke properties
    content = re.sub(
        r"style=\{\{\s*WebkitTextStroke:\s*'[^\']+',\s*WebkitTextFillColor:\s*'transparent'\s*\}\}",
        r"style={{ WebkitTextStroke: '1px black', WebkitTextFillColor: 'transparent', paintOrder: 'stroke fill', strokeLinejoin: 'round' }}",
        content
    )
    
    with open(filename, 'w') as f:
        f.write(content)
        
print("Done")
