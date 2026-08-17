with open('src/components/WheelCarousel.tsx', 'r') as f:
    content = f.read()

import re

new_component = """import { useState, useEffect } from 'react';
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

    controls.start({
      rotate: targetRotation,
      transition: { type: "spring", stiffness: 50, damping: 15 }
    });
    // Update the motion value during animation is handled by framer motion if we animate the motion value, 
    // but controls.start animates the component. It's better to animate the motion value directly!
  };

  return (
    <div className="relative w-full h-[700px] md:h-[900px] overflow-hidden flex justify-center items-end select-none">
      
      {/* Decorative center top text */}
      <div className="absolute top-[5%] w-full text-center z-20 pointer-events-none flex flex-col items-center">
         <p className="text-gray-400 font-mono text-xs uppercase tracking-[0.3em] font-bold">Drag the wheel to navigate</p>
         <div className="w-[1px] h-12 bg-gray-300 mt-4 mb-4"></div>
      </div>

      {/* The rotating wheel container */}
      <motion.div
        className="absolute w-[1200px] h-[1200px] md:w-[1600px] md:h-[1600px] rounded-full border-[30px] border-[#1A1A1A] cursor-grab active:cursor-grabbing flex items-center justify-center bg-transparent z-10"
        style={{ 
            bottom: '-800px',
            touchAction: 'none',
            rotate: rotation
        }}
        drag="x"
        dragConstraints={{ left: 0, right: 0 }}
        dragElastic={0}
        onDrag={handleDrag}
        onDragEnd={(e, info) => {
            const velocity = info.velocity.x * 0.05; 
            let targetRotation = rotation.get() + velocity;
            const index = Math.round(targetRotation / anglePerItem);
            targetRotation = index * anglePerItem;
            
            // Animate the motion value directly so the cards counter-rotate smoothly
            import('motion/react').then(({ animate }) => {
                animate(rotation, targetRotation, { type: "spring", stiffness: 50, damping: 15 });
            });
        }}
      >
        {/* Spokes */}
        {Array.from({ length: 36 }).map((_, i) => (
          <div key={i} className="absolute w-full h-[2px] bg-[#1A1A1A]/10" style={{ transform: `rotate(${i * 10}deg)` }} />
        ))}
        {/* Inner rims */}
        <div className="absolute w-[1100px] h-[1100px] md:w-[1500px] md:h-[1500px] rounded-full border-4 border-[#1A1A1A]/20 pointer-events-none"></div>
        <div className="absolute w-[900px] h-[900px] md:w-[1300px] md:h-[1300px] rounded-full border-2 border-[#1A1A1A]/10 pointer-events-none"></div>
        
        {/* Center hub */}
        <div className="absolute w-40 h-40 rounded-full border-[16px] border-[#1A1A1A] bg-[#EBEBEB] z-10"></div>

        {/* Project Cards */}
        {projects.map((p, i) => {
          const angle = anglePerItem * i;
          // Counter rotate so cards stay upright
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
              {/* Actual Card, translated OUT from center, and counter-rotated to stay upright */}
              <motion.div 
                 className="absolute w-[280px] md:w-[320px] bg-[#FDFCF8] border border-gray-200 p-8 shadow-2xl flex flex-col pointer-events-auto -translate-y-[640px] md:-translate-y-[860px]"
                 style={{ rotate: cardRotation }}
              >
                <div className="text-[9px] text-[#86BC2A] uppercase tracking-[0.2em] font-bold mb-6 border border-[#86BC2A] w-fit px-3 py-1 rounded-full">{p.tag}</div>
                <h3 className="text-xl md:text-2xl font-black uppercase tracking-tight mb-4 text-gray-800 leading-tight">{p.title}</h3>
                <p className="text-[10px] font-bold uppercase tracking-[0.2em] text-gray-500 leading-relaxed">{p.desc}</p>
                {p.quote && (
                  <div className="mt-8 border-l-2 border-[#86BC2A] pl-4">
                    <p className="text-[10px] font-bold uppercase tracking-[0.2em] text-gray-600 italic mb-2">"{p.quote}"</p>
                    <span className="text-[8px] uppercase tracking-[0.3em] text-[#86BC2A] font-bold">— {p.author}</span>
                  </div>
                )}
              </motion.div>
            </div>
          )
        })}
      </motion.div>
    </div>
  )
}
"""

with open('src/components/WheelCarousel.tsx', 'w') as f:
    f.write(new_component)
print("Done")
