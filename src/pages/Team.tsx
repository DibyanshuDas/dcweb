import { TEAM } from '../data';

export default function Team() {
  return (
    <div className="flex flex-col gap-32 pt-32 pb-12 px-6 md:px-16 lg:px-24 xl:px-32 relative z-10">
      <div className="flex flex-col">
        <div className="mb-6 flex items-center gap-4">
          <div className="h-[2px] w-12 bg-[#86BC2A]"></div>
          <span className="text-[#86BC2A] text-[11px] font-black uppercase tracking-[0.5em]">Our People</span>
        </div>
        <h1 className="text-6xl md:text-[100px] font-black uppercase tracking-tighter leading-none text-black">
          Meet<br/><span className="text-transparent" style={{ WebkitTextStroke: '2px #0F0F0F' }}>The Team</span>
        </h1>
      </div>

      <section>
        <h2 className="text-4xl md:text-5xl font-black uppercase tracking-tighter mb-16 text-black">Executive Directors</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-x-12 gap-y-16 border-t border-gray-200 pt-16">
          {TEAM.directors.map((d, i) => (
            <div key={i} className="flex flex-col gap-4 border-l-2 border-gray-200 pl-6 group">
               <div className="w-12 h-12 rounded-full border-2 border-gray-200 bg-gray-50 flex items-center justify-center text-lg font-black text-[#86BC2A] mb-4">{d.avatar}</div>
               <div className="text-2xl font-black uppercase tracking-tight group-hover:text-[#86BC2A] text-black transition-colors">{d.name}</div>
               <div className="text-[10px] uppercase tracking-[0.2em] text-[#86BC2A] font-bold">{d.role}</div>
               <div className="text-[10px] uppercase tracking-[0.2em] text-gray-500 font-bold">{d.dept}</div>
               <a href={`mailto:${d.email}`} className="text-xs text-gray-400 font-mono font-bold mt-2 hover:text-black transition-colors">{d.email}</a>
            </div>
          ))}
        </div>
      </section>

      <section>
        <h2 className="text-4xl md:text-5xl font-black uppercase tracking-tighter mb-16 text-black">Where Our Alumni Work</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 border-t border-gray-200 pt-16">
          {TEAM.alumni.map((alumnus, i) => (
            <div key={i} className="border border-gray-200 bg-white p-8 text-center flex flex-col items-center hover:border-[#86BC2A] transition-colors group shadow-sm">
              <div className="w-14 h-14 rounded-full border-2 border-gray-200 bg-gray-50 flex items-center justify-center text-xl font-black text-gray-400 group-hover:text-[#86BC2A] transition-colors mb-6">{alumnus.avatar}</div>
              <h4 className="text-sm font-black uppercase tracking-widest text-gray-800 mb-2">{alumnus.name}</h4>
              <div className="text-[10px] font-bold uppercase tracking-[0.2em] text-[#86BC2A]">{alumnus.co}</div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}