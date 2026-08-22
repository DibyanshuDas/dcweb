import { motion } from 'motion/react';
import { PROJECTS } from '../data';
import WheelCarousel from '../components/WheelCarousel';

export default function Projects() {
  return (
    <motion.div initial={{opacity: 0, y: 20}} animate={{opacity: 1, y: 0}} transition={{duration: 0.6}} className="flex flex-col pt-32 px-6 md:px-16 lg:px-24 xl:px-32 w-full min-h-screen relative z-10 bg-transparent overflow-hidden">
      
      <div className="flex flex-col flex-shrink-0 relative z-20 pointer-events-none mb-10">
        <div className="mb-4 flex items-center gap-4">
          <div className="h-[2px] w-12 bg-[#86BC2A]"></div>
          <span className="text-[#86BC2A] text-[11px] font-black uppercase tracking-[0.5em]">Our Portfolio</span>
        </div>
        <h1 className="text-[12vw] sm:text-6xl md:text-[80px] lg:text-[100px] font-black uppercase tracking-tighter leading-[0.9] text-[#0F1115]">
          28+ <span className="text-[#86BC2A]">Global</span><br className="hidden md:block"/>Engagements
        </h1>
      </div>
      
      {/* The Wheel Container */}
      <div className="flex-1 w-full min-h-[500px] md:min-h-[600px] mt-12 flex items-end justify-center z-10 pointer-events-none"> 
         <div className="w-full h-full pointer-events-auto flex items-end justify-center">
            <WheelCarousel projects={PROJECTS} />
         </div>
      </div>
      
    </motion.div>
  );
}
