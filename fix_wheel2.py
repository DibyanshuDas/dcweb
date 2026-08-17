with open('src/components/WheelCarousel.tsx', 'r') as f:
    content = f.read()

import re

new_wheel = """import { useState } from 'react';
import { motion, useAnimation, PanInfo, useMotionValue, useTransform } from 'motion/react';

interface Project {
  tag: string;
  title: string;
  desc: string;
  quote?: string;
  author?: string;
  year?: string;
  impact?: string;
  logo?: string;
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
          <div key={i} className="w-full bg-[#FDFCF8] border border-gray-200 p-6 shadow-sm flex items-center gap-4">
            <div className="flex-shrink-0 flex items-center justify-center text-xs font-bold text-gray-400 rotate-[-90deg] tracking-widest">{p.year}</div>
            <img src={p.logo} alt="Logo" className="w-16 h-16 object-cover border border-gray-200 shadow-sm" />
            <div className="flex flex-col justify-center text-left">
              <h3 className="text-sm font-black uppercase tracking-tight text-gray-800 leading-tight">{p.title}</h3>
              <p className="text-[10px] font-bold text-gray-500 mt-1 uppercase tracking-wider">{p.impact}</p>
            </div>
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
          className="absolute w-[1200px] h-[1200px] rounded-full cursor-grab active:cursor-grabbing flex items-center justify-center bg-transparent z-10"
          style={{ 
              bottom: '-750px', // Adjusted to fit nicely at bottom of screen
              touchAction: 'none',
              rotate: rotation
          }}
          drag="x"
          dragConstraints={{ left: 0, right: 0 }}
          dragElastic={0}
          onDrag={handleDrag}
          onDragEnd={handleDragEnd}
        >
          {/* Tyre Outer Layer */}
          <div className="absolute w-[1200px] h-[1200px] rounded-full" 
               style={{
                   background: 'radial-gradient(circle, transparent 65%, #222 66%, #111 68%, #000 70%, #111 72%, transparent 73%)',
                   boxShadow: 'inset 0 0 50px rgba(0,0,0,0.5)'
               }}>
          </div>
          
          {/* Tyre Treads */}
          <div className="absolute w-[1160px] h-[1160px] rounded-full opacity-60" 
               style={{
                   background: 'repeating-conic-gradient(from 0deg, transparent 0deg 2deg, #1a1a1a 2deg 4deg)',
                   maskImage: 'radial-gradient(circle, transparent 65%, black 66%, black 72%, transparent 73%)',
                   WebkitMaskImage: 'radial-gradient(circle, transparent 65%, black 66%, black 72%, transparent 73%)'
               }}>
          </div>
          
          {/* Inner metallic rim */}
          <div className="absolute w-[1080px] h-[1080px] rounded-full border-[8px] border-gray-300 shadow-inner"></div>
          <div className="absolute w-[1064px] h-[1064px] rounded-full border-4 border-gray-400"></div>

          {/* Spokes */}
          {Array.from({ length: 36 }).map((_, i) => (
            <div key={i} className="absolute w-[1064px] h-[2px] bg-gray-400" style={{ transform: `rotate(${i * 10}deg)` }} />
          ))}
          
          {/* Center hub */}
          <div className="absolute w-24 h-24 rounded-full border-[12px] border-gray-400 bg-gray-200 z-10 shadow-xl"></div>

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
                   className="absolute w-[300px] bg-[#FDFCF8] border border-gray-200 p-4 shadow-2xl flex items-center gap-4 pointer-events-auto -translate-y-[640px] hover:border-[#86BC2A] transition-colors"
                   style={{ rotate: cardRotation }}
                >
                  <div className="flex-shrink-0 flex items-center justify-center text-xs font-bold text-gray-400 rotate-[-90deg] tracking-widest">{p.year}</div>
                  <div className="w-[1px] h-12 bg-gray-200 flex-shrink-0"></div>
                  <img src={p.logo} alt="Logo" className="w-16 h-16 object-cover bg-white shadow-sm flex-shrink-0" />
                  <div className="flex flex-col justify-center text-left">
                    <h3 className="text-sm font-black uppercase tracking-tight text-gray-800 leading-tight">{p.title}</h3>
                    <p className="text-[10px] font-bold text-gray-500 mt-1 uppercase tracking-wider">{p.impact}</p>
                  </div>
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
