with open('src/pages/Home.tsx', 'r') as f:
    content = f.read()

# Add import back
if "import logo180dcGlobe" not in content:
    content = content.replace(
        "import { motion } from 'motion/react';",
        "import { motion } from 'motion/react';\nimport logo180dcGlobe from '../assets/logos/180dc_globe.jpg';"
    )

# Replace the img tag
content = content.replace(
    '<img src="https://www.pngfind.com/pngs/m/258-2583450_180-degrees-consulting-indiana-university-client-application-180.png" alt="180DC Logo Globe" className="w-full h-full object-contain mix-blend-multiply" />',
    '<img src={logo180dcGlobe} alt="180DC Logo Globe" className="w-full h-full object-contain mix-blend-multiply" />'
)

# Just in case it lacked mix-blend-multiply
content = content.replace(
    '<img src="https://www.pngfind.com/pngs/m/258-2583450_180-degrees-consulting-indiana-university-client-application-180.png" alt="180DC Logo Globe" className="w-full h-full object-contain" />',
    '<img src={logo180dcGlobe} alt="180DC Logo Globe" className="w-full h-full object-contain mix-blend-multiply" />'
)

with open('src/pages/Home.tsx', 'w') as f:
    f.write(content)
print("Done")
