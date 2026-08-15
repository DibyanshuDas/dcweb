import { PROJECTS } from '../data';

export default function Projects() {
  return (
    <div className="flex flex-col gap-24 pt-10 h-full relative z-10">
      <div className="flex flex-col">
        <div className="mb-6 flex items-center gap-4">
          <div className="h-[2px] w-12 bg-[#86BC2A]"></div>
          <span className="text-[#86BC2A] text-[11px] font-black uppercase tracking-[0.5em]">Our Portfolio</span>
        </div>
        <h1 className="text-6xl md:text-[100px] font-black uppercase tracking-tighter leading-none text-black">
          28+ <span className="text-transparent" style={{ WebkitTextStroke: '2px #0F0F0F' }}>Global</span><br/>Engagements
        </h1>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {PROJECTS.map((p, i) => (
          <div key={i} className="border border-gray-200 bg-white p-10 flex flex-col justify-between hover:border-[#86BC2A] transition-colors relative group min-h-[320px] shadow-sm">
            <div>
              <div className="text-[10px] text-[#86BC2A] uppercase tracking-widest font-bold mb-6 border border-[#86BC2A] w-fit px-3 py-1 rounded-full">{p.tag}</div>
              <h3 className="text-2xl font-black uppercase tracking-tight mb-4 group-hover:text-black text-gray-800 transition-colors">{p.title}</h3>
              <p className="text-[10px] font-bold uppercase tracking-[0.2em] text-gray-500 leading-relaxed mb-8">{p.desc}</p>
            </div>
            {p.quote && (
              <div className="mt-auto border-l-2 border-gray-200 pl-4">
                <p className="text-[11px] font-bold uppercase tracking-widest text-gray-600 italic mb-2">"{p.quote}"</p>
                <span className="text-[9px] uppercase tracking-[0.3em] text-gray-400 font-bold">— {p.author}</span>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}