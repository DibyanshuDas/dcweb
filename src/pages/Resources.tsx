import { motion } from 'motion/react';
import { RESOURCES } from '../data';

export default function Resources() {
  return (
    <motion.div initial={{opacity: 0, y: 20}} animate={{opacity: 1, y: 0}} transition={{duration: 0.6}} className="flex flex-col gap-24 pt-32 pb-12 px-6 md:px-16 lg:px-24 xl:px-32 relative z-10">
      <div className="flex flex-col">
        <div className="mb-6 flex items-center gap-4">
          <div className="h-[2px] w-12 bg-[#86BC2A]"></div>
          <span className="text-[#86BC2A] text-[11px] font-black uppercase tracking-[0.5em]">Knowledge</span>
        </div>
        <h1 className="text-[12vw] sm:text-6xl md:text-[100px] font-black uppercase tracking-tighter leading-[0.9] text-[#0F1115] mb-12">
          <span className="text-[#86BC2A]">Open</span><br/>Resources
        </h1>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {RESOURCES.map((r, i) => (
          <a key={i} href={r.link} target="_blank" rel="noopener noreferrer" className="border border-gray-200 bg-white shadow-sm p-10 flex flex-col justify-between h-72 hover:border-[#86BC2A] transition-colors group">
            <div className="flex justify-between items-start">
              <div className="text-[10px] uppercase tracking-widest text-gray-400 font-bold">Res_0{i+1}</div>
              <div className="text-gray-400 group-hover:text-black transition-colors">↗</div>
            </div>
            <div>
              <h3 className="text-2xl font-black uppercase tracking-tight mb-4 group-hover:text-[#86BC2A] text-black transition-colors">{r.title}</h3>
              <p className="text-[10px] uppercase tracking-[0.2em] font-bold text-gray-500 leading-relaxed">{r.desc}</p>
            </div>
          </a>
        ))}
      </div>
    </motion.div>
  );
}