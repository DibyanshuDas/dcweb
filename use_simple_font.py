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

    # Remove the Montserrat font to fallback to the simple Google Sans / default sans-serif
    content = content.replace('font-montserrat ', '')
    
    # Revert tracking and leading to standard Tailwind classes that look good with simple fonts
    content = content.replace('tracking-[-0.04em]', 'tracking-tighter')
    content = content.replace('leading-[0.85]', 'leading-[0.9]')
    
    # Remove the font-bold override on the transparent spans
    content = content.replace('text-transparent font-bold', 'text-transparent')
    
    # Simplify the stroke style, keeping it colorless (transparent fill) and 2px black outline
    content = re.sub(
        r"style=\{\{\s*WebkitTextStroke:[^\}]+\}\}",
        r"style={{ WebkitTextStroke: '2px #0F1115', WebkitTextFillColor: 'transparent' }}",
        content
    )
    
    with open(filename, 'w') as f:
        f.write(content)

print("Done")
