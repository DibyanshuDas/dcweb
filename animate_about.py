with open('src/pages/About.tsx', 'r') as f:
    content = f.read()

if "import { motion } from 'motion/react';" not in content:
    content = content.replace("import ", "import { motion } from 'motion/react';\nimport ", 1)

content = content.replace(
    'return (\n    <div className="w-full min-h-screen pb-20">',
    'return (\n    <motion.div initial={{opacity: 0, y: 20}} animate={{opacity: 1, y: 0}} transition={{duration: 0.6}} className="w-full min-h-screen pb-20">'
)

content = content.replace(
    '</div>\n  );\n}',
    '</motion.div>\n  );\n}'
)

with open('src/pages/About.tsx', 'w') as f:
    f.write(content)
