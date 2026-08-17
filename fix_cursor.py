with open('src/components/CustomCursor.tsx', 'r') as f:
    content = f.read()

# Make the Custom Cursor a crosshair instead of a dot
# I will change the svg inside the CustomCursor to a crosshair.
import re

new_svg = '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
          <path d="M12 2v20M2 12h20"/>
        </svg>'''

# Currently it renders: <div className="w-4 h-4 bg-black rounded-full mix-blend-difference" />
content = re.sub(r'<div className="w-4 h-4 bg-black[^"]*" />', new_svg, content)

# Remove the bg-white/20 and blur from the outer ring to make it clean
content = content.replace('bg-white/20 backdrop-blur-sm', '')

with open('src/components/CustomCursor.tsx', 'w') as f:
    f.write(content)
print("Done")
