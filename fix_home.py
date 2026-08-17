with open('src/pages/Home.tsx', 'r') as f:
    content = f.read()

# Fix the font color
content = content.replace('text-gray-400">Our Alums work At', 'text-[#0F1115]">Our Alums work At')

# Remove pause-on-hover
content = content.replace(' animate-marquee-left pause-on-hover', ' animate-marquee-left')
content = content.replace(' animate-marquee-right pause-on-hover', ' animate-marquee-right')
# Just in case they are structured differently
content = content.replace('pause-on-hover', '')

with open('src/pages/Home.tsx', 'w') as f:
    f.write(content)
print("Done")
