import re

with open('src/pages/Projects.tsx', 'r') as f:
    content = f.read()

# Add import
if "import WheelCarousel" not in content:
    content = content.replace("import { PROJECTS }", "import { PROJECTS } from '../data';\nimport WheelCarousel from '../components/WheelCarousel';")
    # Actually wait, `import { PROJECTS } from '../data';` is already there. Let's just do:
    content = content.replace("import { PROJECTS } from '../data';", "import { PROJECTS } from '../data';\nimport WheelCarousel from '../components/WheelCarousel';")

# Replace the grid with WheelCarousel
# The grid is: `<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"> ... </div>`
grid_pattern = r'<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">.*?</motion\.div>'

content = re.sub(
    grid_pattern,
    '<WheelCarousel projects={PROJECTS} />\n    </motion.div>',
    content,
    flags=re.DOTALL
)

with open('src/pages/Projects.tsx', 'w') as f:
    f.write(content)
print("Done")
