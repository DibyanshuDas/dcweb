import re

with open('src/pages/Projects.tsx', 'r') as f:
    content = f.read()

content = content.replace('pt-24 md:pt-32', 'pt-16 md:pt-16')
content = content.replace('mt-4 md:mt-12', 'mt-2 md:mt-4')

with open('src/pages/Projects.tsx', 'w') as f:
    f.write(content)
print("Projects fixed")

with open('src/components/WheelCarousel.tsx', 'r') as f:
    content = f.read()

content = content.replace('const anglePerItem = 22;', 'const anglePerItem = 28;')

with open('src/components/WheelCarousel.tsx', 'w') as f:
    f.write(content)
print("WheelCarousel fixed")
