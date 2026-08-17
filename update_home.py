import re

with open('src/pages/Home.tsx', 'r') as f:
    content = f.read()

target = 'Into <span className="text-[#86BC2A]">Oppor-</span><br/><span className="text-[#86BC2A]">tunities</span>'
replacement = '''Into <br className="md:hidden" />
            <motion.span
              initial="hidden"
              animate="visible"
              variants={{
                hidden: {},
                visible: {
                  transition: { staggerChildren: 0.1, delayChildren: 0.8 }
                }
              }}
              className="text-[#86BC2A] inline-block"
            >
              {"Opportunities".split('').map((char, index) => (
                <motion.span
                  key={index}
                  variants={{
                    hidden: { display: 'none' },
                    visible: { display: 'inline' }
                  }}
                >
                  {char}
                </motion.span>
              ))}
            </motion.span>'''

if target in content:
    content = content.replace(target, replacement)
    with open('src/pages/Home.tsx', 'w') as f:
        f.write(content)
    print("Done Home.tsx")
else:
    print("Target not found. Current text:")
    # print a snippet around 'Into'
    match = re.search(r'(.{0,50}Into.{0,100})', content, re.DOTALL)
    if match:
        print(match.group(1))

