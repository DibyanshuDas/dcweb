with open('src/components/WheelCarousel.tsx', 'r') as f:
    content = f.read()

import re

new_wheel = """import { useRef } from 'react';
import { motion, useScroll, useTransform, useSpring } from 'motion/react';

interface Project {
  tag: string;
  title: string;
  desc: string;
}

export default function WheelCarousel({ projects }: { projects: Project[] }) {
  const scrollRef = useRef<HTMLDivElement>(null);
  
  const { scrollX } = useScroll({ container: scrollRef });
  const smoothScroll = useSpring(scrollX, { damping: 25, stiffness: 120, mass: 0.5 });
  
  const anglePerItem = 360 / projects.length;
  const rotation = useTransform(smoothScroll, (x) => -x * (anglePerItem / 400));

  const handleWheel = (e: React.WheelEvent) => {
    if (scrollRef.current) {
       if (Math.abs(e.deltaY) > Math.abs(e.deltaX)) {
          scrollRef.current.scrollLeft += e.deltaY;
       }
    }
  };

  return (
    <>
      <style>{`
        .hide-scrollbar::-webkit-scrollbar { display: none; }
        .car-tyre-tread {
          background: repeating-linear-gradient(
            to right,
            transparent,
            transparent 10px,
            rgba(0,0,0,0.4) 10px,
            rgba(0,0,0,0.4) 20px
          );
        }
      `}</style>
      
      {/* Mobile Layout */}
      <div className="md:hidden flex flex-col gap-4 pb-24 w-full px-6 pt-12">
        <p className="text-gray-400 font-mono text-[10px] uppercase tracking-[0.3em] font-bold text-center mb-4">Scroll to explore</p>
        {projects.map((p, i) => (
          <div key={i} className="w-full bg-[#FDFCF8] border border-gray-200 p-6 shadow-sm flex items-center justify-center text-center">
            <h3 className="text-xs font-black uppercase tracking-widest text-gray-800 leading-tight">{p.title}</h3>
          </div>
        ))}
      </div>

      {/* Desktop Layout */}
      <div 
         ref={scrollRef}
         onWheel={handleWheel}
         className="hidden md:block absolute inset-0 overflow-x-auto overflow-y-hidden hide-scrollbar"
         style={{ scrollbarWidth: 'none', msOverflowStyle: 'none' }}
      >
        <div style={{ width: `calc(100vw + ${projects.length * 400}px)`, height: '100%' }} className="relative flex">
          
          <div className="sticky left-0 w-screen h-full flex justify-center items-end overflow-hidden pointer-events-none">
            
            <div className="absolute bottom-[380px] w-full text-center z-20 flex flex-col items-center pointer-events-none">
               <p className="text-gray-400 font-mono text-[9px] uppercase tracking-[0.4em] font-bold">Scroll horizontally to navigate</p>
               <div className="w-[1px] h-4 bg-gray-300 mt-2 mb-2"></div>
            </div>

            <motion.div
              className="absolute w-[900px] h-[900px] flex items-center justify-center bg-transparent z-10 pointer-events-auto"
              style={{ 
                  bottom: '-550px',
                  rotate: rotation
              }}
            >
              {/* 1. Rubber Tyre */}
              <div className="absolute inset-0 rounded-full bg-[#1a1a1a] shadow-[inset_0_0_40px_rgba(0,0,0,0.8),0_20px_50px_rgba(0,0,0,0.5)] flex items-center justify-center overflow-hidden">
                 <div className="absolute w-[860px] h-[860px] rounded-full border-[15px] border-[#111] opacity-50"></div>
                 <div className="absolute w-[890px] h-[890px] rounded-full border-[20px] border-dashed border-[#111] opacity-30"></div>
              </div>
              
              {/* 2. Dark Void inside the rim */}
              <div className="absolute w-[680px] h-[680px] rounded-full bg-[#0a0a0a] shadow-[inset_0_0_50px_rgba(0,0,0,0.9)] flex items-center justify-center">
                 
                 {/* 3. Brake Disc */}
                 <div className="absolute w-[520px] h-[520px] rounded-full bg-gradient-to-br from-[#555] to-[#444] border-4 border-[#333] flex items-center justify-center">
                    {/* Brake Disc details (dots) */}
                    <div className="absolute inset-0 rounded-full" style={{
                        backgroundImage: 'radial-gradient(#333 15%, transparent 16%)',
                        backgroundSize: '20px 20px',
                        opacity: 0.5
                    }}></div>
                    <div className="absolute w-[300px] h-[300px] rounded-full bg-[#333] border-4 border-[#222]"></div>
                    {/* Brake Caliper */}
                    <div className="absolute w-[140px] h-[220px] bg-[#1a1a1a] rounded-3xl right-[30px] top-[150px] shadow-lg border border-[#333]"></div>
                 </div>
              </div>
              
              {/* 4. Alloy Rim Outer Edge */}
              <div className="absolute w-[680px] h-[680px] rounded-full border-[25px] border-[#d8d8d8] shadow-[inset_0_5px_15px_rgba(0,0,0,0.4),0_0_20px_rgba(0,0,0,0.8)]"></div>
              
              {/* 5. 5 Split Spokes */}
              {Array.from({ length: 5 }).map((_, i) => (
                <div key={i} className="absolute w-full h-full flex justify-center items-center pointer-events-none" style={{ transform: `rotate(${i * 72}deg)` }}>
                   {/* Spoke Left */}
                   <div className="absolute w-[35px] h-[320px] bg-gradient-to-b from-[#e8e8e8] to-[#c0c0c0] origin-bottom bottom-1/2 rounded-t-md shadow-[0_5px_15px_rgba(0,0,0,0.5)]"
                        style={{ transform: 'rotate(-8deg) translateY(-10px)' }}>
                       <div className="absolute inset-y-0 left-0 w-[5px] bg-gradient-to-r from-white to-transparent opacity-60"></div>
                   </div>
                   {/* Spoke Right */}
                   <div className="absolute w-[35px] h-[320px] bg-gradient-to-b from-[#e8e8e8] to-[#c0c0c0] origin-bottom bottom-1/2 rounded-t-md shadow-[0_5px_15px_rgba(0,0,0,0.5)]"
                        style={{ transform: 'rotate(8deg) translateY(-10px)' }}>
                       <div className="absolute inset-y-0 right-0 w-[5px] bg-gradient-to-l from-[#999] to-transparent opacity-60"></div>
                   </div>
                </div>
              ))}

              {/* 6. Center Hub */}
              <div className="absolute w-[160px] h-[160px] bg-gradient-to-br from-[#f0f0f0] to-[#c0c0c0] rounded-full shadow-[0_0_20px_rgba(0,0,0,0.6)] flex items-center justify-center border-4 border-[#e8e8e8]">
                 {/* Center Cap */}
                 <div className="absolute w-[80px] h-[80px] bg-gradient-to-br from-[#ddd] to-[#eee] rounded-full shadow-inner border border-[#ccc]"></div>
                 
                 {/* 5 Lug Nuts */}
                 {Array.from({ length: 5 }).map((_, i) => (
                    <div key={i} className="absolute w-[20px] h-[20px] bg-gradient-to-br from-[#222] to-[#444] rounded-full shadow-inner"
                         style={{ transform: `rotate(${i * 72}deg) translateY(-50px)` }}>
                    </div>
                 ))}
              </div>

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
                       className="absolute w-[200px] bg-[#FDFCF8] border border-gray-200 p-4 shadow-xl flex justify-center items-center pointer-events-auto -translate-y-[490px] hover:border-[#86BC2A] transition-colors"
                       style={{ rotate: cardRotation }}
                    >
                      <h3 className="text-[11px] font-black uppercase tracking-widest text-gray-800 leading-tight text-center">{p.title}</h3>
                    </motion.div>
                  </div>
                )
              })}
            </motion.div>
          </div>
        </div>
      </div>
    </>
  )
}
"""

with open('src/components/WheelCarousel.tsx', 'w') as f:
    f.write(new_wheel)
print("Done")
