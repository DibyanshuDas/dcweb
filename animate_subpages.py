import glob
import re

pages = ['src/pages/Services.tsx', 'src/pages/Projects.tsx', 'src/pages/Resources.tsx', 'src/pages/Contact.tsx', 'src/pages/Team.tsx']

for p in pages:
    with open(p, 'r') as f:
        content = f.read()
        
    if "import { motion } from 'motion/react';" not in content:
        # Find first import and insert after it
        content = content.replace("import ", "import { motion } from 'motion/react';\nimport ", 1)
        
    # Animate main h1 container / flex-col if possible
    # We can just animate the main wrapper in these pages. Most start with `<div className="flex flex-col...`
    # Let's target the inner wrappers.
    # Services/Projects/Resources/Contact share a similar header:
    # <div className="flex flex-col"> or <div className="flex-1 flex flex-col gap-16">
    
    # Just wrap the first major section. It's safer to animate the h1 and its siblings.
    # Or just use motion.div for the very top level `div` returning from the component!
    
    # Replacing the top level div:
    # return (\n    <div className=... -> return (\n    <motion.div initial={{opacity: 0, y: 20}} animate={{opacity: 1, y: 0}} transition={{duration: 0.6}} className=...
    content = re.sub(
        r'return \(\s*<div (className="[^"]+ relative z-10")',
        r'return (\n    <motion.div initial={{opacity: 0, y: 20}} animate={{opacity: 1, y: 0}} transition={{duration: 0.6}} \1',
        content
    )
    content = re.sub(
        r'return \(\s*<div (className="[^"]+ min-h-screen[^"]*relative z-10[^"]*")',
        r'return (\n    <motion.div initial={{opacity: 0, y: 20}} animate={{opacity: 1, y: 0}} transition={{duration: 0.6}} \1',
        content
    )
    # The ending `</div>\n  );` needs to be `</motion.div>\n  );`
    # This might match multiple things. Let's do a safer ending replacement:
    content = re.sub(r'</div>\s*\);\s*\}', r'</motion.div>\n  );\n}', content)

    with open(p, 'w') as f:
        f.write(content)
        
print("Done Subpages")
