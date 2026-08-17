with open('src/pages/Home.tsx', 'r') as f:
    content = f.read()

content = content.replace(
    'className="flex items-center justify-center w-40 h-16 opacity-50 hover:opacity-100 transition-opacity grayscale hover:grayscale-0"',
    'className="flex items-center justify-center w-40 h-16 hover:scale-110 transition-transform duration-300"'
)

with open('src/pages/Home.tsx', 'w') as f:
    f.write(content)
print("Done")
