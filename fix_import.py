with open('src/pages/Projects.tsx', 'r') as f:
    lines = f.readlines()

# Filter out bad lines
new_lines = []
for line in lines:
    if "from '../data';" in line and "WheelCarousel" in line:
        continue
    new_lines.append(line)

# Ensure only one import WheelCarousel
content = "".join(new_lines)
import re
content = re.sub(r'(import WheelCarousel from \'../components/WheelCarousel\';\s*){2,}', 'import WheelCarousel from \'../components/WheelCarousel\';\n', content)

with open('src/pages/Projects.tsx', 'w') as f:
    f.write(content)
