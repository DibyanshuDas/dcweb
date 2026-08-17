import re
with open('src/pages/Home.tsx', 'r') as f:
    content = f.read()

# Fix the <br> for 'Into Opportunities'
content = content.replace('Into <br className="md:hidden" />', 'Into <br />')

# Fix the logo
# Remove the import just to be clean
content = content.replace("import logo180dcGlobe from '../assets/logos/180dc_globe.jpg';\n", "")
content = content.replace('src={logo180dcGlobe}', 'src="https://www.pngfind.com/pngs/m/258-2583450_180-degrees-consulting-indiana-university-client-application-180.png"')

# I should also remove mix-blend-multiply because the new PNG might have transparency and we don't necessarily want it to multiply.
content = content.replace('className="w-full h-full object-contain mix-blend-multiply"', 'className="w-full h-full object-contain"')

with open('src/pages/Home.tsx', 'w') as f:
    f.write(content)
print("Done")
