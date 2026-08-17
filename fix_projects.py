with open('src/pages/Projects.tsx', 'r') as f:
    content = f.read()

import re
# Change className of motion.div to h-screen and hidden overflow for desktop
# Find: className="flex flex-col gap-24 pt-32 pb-12 px-6 md:px-16 lg:px-24 xl:px-32 h-full relative z-10"
# Or whatever it is right now.

# We will just rewrite the whole file, it's very short.
new_projects = """import { motion } from 'motion/react';
import { PROJECTS } from '../data';
import WheelCarousel from '../components/WheelCarousel';

export default function Projects() {
  return (
    <motion.div initial={{opacity: 0, y: 20}} animate={{opacity: 1, y: 0}} transition={{duration: 0.6}} className="flex flex-col pt-24 md:pt-32 px-6 md:px-16 lg:px-24 xl:px-32 w-full min-h-screen md:h-screen md:overflow-hidden relative z-10 bg-transparent">
      
      <div className="flex flex-col flex-shrink-0 relative z-20">
        <div className="mb-4 md:mb-6 flex items-center gap-4">
          <div className="h-[2px] w-12 bg-[#86BC2A]"></div>
          <span className="text-[#86BC2A] text-[11px] font-black uppercase tracking-[0.5em]">Our Portfolio</span>
        </div>
        <h1 className="text-[10vw] sm:text-6xl md:text-[80px] lg:text-[100px] font-black uppercase tracking-tighter leading-[0.9] text-[#0F1115]">
          28+ <span className="text-[#86BC2A]">Global</span><br className="hidden md:block"/>Engagements
        </h1>
      </div>
      
      {/* Flex-1 ensures it takes remaining space, overflow-hidden stops scrolling */}
      <div className="flex-1 relative w-full mt-10 md:mt-0 flex items-end justify-center z-10">
         <WheelCarousel projects={PROJECTS} />
      </div>
      
    </motion.div>
  );
}
"""

with open('src/pages/Projects.tsx', 'w') as f:
    f.write(new_projects)
print("Done")
