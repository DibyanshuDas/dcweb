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

    # Replace the existing style dicts in spans
    # from: style={{ WebkitTextStroke: '1.5px #0F1115' }}
    # or: style={{ WebkitTextStroke: '2px #0F0F0F' }}
    # to: style={{ WebkitTextStroke: '2px black', WebkitTextFillColor: 'transparent' }}
    
    content = re.sub(
        r'style=\{\{\s*WebkitTextStroke:\s*[\'"][^\'"]+[\'"]\s*\}\}',
        r"style={{ WebkitTextStroke: '2px black', WebkitTextFillColor: 'transparent' }}",
        content
    )
    
    with open(filename, 'w') as f:
        f.write(content)
        
print("Done")
