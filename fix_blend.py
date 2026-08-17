with open('src/pages/Home.tsx', 'r') as f:
    content = f.read()

content = content.replace(
    '<img src="https://www.pngfind.com/pngs/m/258-2583450_180-degrees-consulting-indiana-university-client-application-180.png" alt="180DC Logo Globe" className="w-full h-full object-contain" />',
    '<img src="https://www.pngfind.com/pngs/m/258-2583450_180-degrees-consulting-indiana-university-client-application-180.png" alt="180DC Logo Globe" className="w-full h-full object-contain mix-blend-multiply" />'
)

with open('src/pages/Home.tsx', 'w') as f:
    f.write(content)
print("Done")
