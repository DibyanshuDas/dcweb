with open('src/components/WheelCarousel.tsx', 'r') as f:
    content = f.read()

import re

# Rewrite WheelCarousel
new_wheel = """import { useState } from 'react';
import { motion, useAnimation, PanInfo, useMotionValue, useTransform } from 'motion/react';

interface Project {
  tag: string;
  title: string;
  desc: string;
  quote?: string;
  author?: string;
}

export default function WheelCarousel({ projects }: { projects: Project[] }) {
  const rotation = useMotionValue(0);
  const controls = useAnimation();
  const anglePerItem = 360 / projects.length;

  const handleDrag = (event: any, info: PanInfo) => {
    const delta = info.delta.x * 0.15;
    rotation.set(rotation.get() + delta);
    controls.set({ rotate: rotation.get() });
  };

  const handleDragEnd = (event: any, info: PanInfo) => {
    const velocity = info.velocity.x * 0.05; 
    let targetRotation = rotation.get() + velocity;
    
    // Snap to nearest item
    const index = Math.round(targetRotation / anglePerItem);
    targetRotation = index * anglePerItem;
    
    import('motion/react').then(({ animate }) => {
        animate(rotation, targetRotation, { type: "spring", stiffness: 50, damping: 15 });
        controls.start({
          rotate: targetRotation,
          transition: { type: "spring", stiffness: 50, damping: 15 }
        });
    });
  };

  return (
    <>
      {/* Mobile Layout: Vertical List */}
      <div className="md:hidden flex flex-col gap-6 pb-24 w-full">
        <p className="text-gray-400 font-mono text-xs uppercase tracking-[0.3em] font-bold text-center mb-2">Scroll to explore</p>
        {projects.map((p, i) => (
          <div key={i} className="w-full bg-[#FDFCF8] border border-gray-200 p-8 shadow-sm flex flex-col">
            <h3 className="text-xl font-black uppercase tracking-tight text-gray-800 leading-tight">{p.title}</h3>
          </div>
        ))}
      </div>

      {/* Desktop Layout: Horizontal Wheel */}
      <div className="hidden md:flex relative w-full h-full min-h-[500px] overflow-hidden justify-center items-end select-none">
        
        <div className="absolute top-[10%] w-full text-center z-20 pointer-events-none flex flex-col items-center">
           <p className="text-gray-400 font-mono text-[10px] uppercase tracking-[0.3em] font-bold">Drag the wheel to navigate</p>
           <div className="w-[1px] h-6 bg-gray-300 mt-3 mb-3"></div>
        </div>

        <motion.div
          className="absolute w-[1000px] h-[1000px] rounded-full border-[20px] border-[#1A1A1A] cursor-grab active:cursor-grabbing flex items-center justify-center bg-transparent z-10"
          style={{ 
              bottom: '-650px', // Adjusted to fit nicely at bottom of screen
              touchAction: 'none',
              rotate: rotation
          }}
          drag="x"
          dragConstraints={{ left: 0, right: 0 }}
          dragElastic={0}
          onDrag={handleDrag}
          onDragEnd={handleDragEnd}
        >
          {/* Spokes */}
          {Array.from({ length: 36 }).map((_, i) => (
            <div key={i} className="absolute w-full h-[2px] bg-[#1A1A1A]/10" style={{ transform: `rotate(${i * 10}deg)` }} />
          ))}
          {/* Inner rims */}
          <div className="absolute w-[940px] h-[940px] rounded-full border-4 border-[#1A1A1A]/20 pointer-events-none"></div>
          <div className="absolute w-[800px] h-[800px] rounded-full border-2 border-[#1A1A1A]/10 pointer-events-none"></div>
          
          {/* Center hub */}
          <div className="absolute w-24 h-24 rounded-full border-[12px] border-[#1A1A1A] bg-[#EBEBEB] z-10"></div>

          {/* Project Cards */}
          {projects.map((p, i) => {
            const angle = anglePerItem * i;
            const cardRotation = useTransform(rotation, (r) => -(r + angle));

            return (
              <div
                key={i}
                className="absolute w-0 h-0 flex justify-center items-center pointer-events-none"
                style={{
                  top: '50%',
                  left: '50%',
                  transform: `rotate(${angle}deg)`
                }}
              >
                <motion.div 
                   className="absolute w-[200px] bg-[#FDFCF8] border border-gray-200 p-6 shadow-2xl flex flex-col pointer-events-auto justify-center items-center text-center -translate-y-[560px]"
                   style={{ rotate: cardRotation }}
                >
                  <h3 className="text-sm font-black uppercase tracking-tight text-gray-800 leading-tight">{p.title}</h3>
                </motion.div>
              </div>
            )
          })}
        </motion.div>
      </div>
    </>
  )
}
"""

with open('src/components/WheelCarousel.tsx', 'w') as f:
    f.write(new_wheel)
print("Done")
