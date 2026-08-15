import logo180dcFull from '../assets/logos/180dc_full.png';

export default function Footer({ onNavigate }: { onNavigate: (page: string) => void }) {
  return (
    <footer className="border-t border-gray-200 pt-10 pb-16 mt-20 flex flex-col md:flex-row justify-between gap-12 z-10 relative" style={{ fontFamily: "'Open Sans', sans-serif" }}>
      <div className="max-w-xs">
        <div className="mb-6 cursor-pointer" onClick={() => onNavigate('Home')}>
          <img src={logo180dcFull} alt="180 Degrees Consulting" className="h-6 md:h-8 object-contain" />
        </div>
        <p className="text-[10px] leading-relaxed text-gray-500 font-bold tracking-widest uppercase">
          Student consulting org for nonprofits & social enterprises.
        </p>
      </div>

      <div className="flex gap-16">
        <div className="flex flex-col gap-4">
          <span className="text-[9px] uppercase tracking-[0.3em] text-gray-400 font-bold mb-2">Pages</span>
          {['Home', 'Team', 'Projects'].map(p => (
            <button key={p} onClick={() => { onNavigate(p); window.scrollTo(0,0); }} className="text-[10px] text-gray-600 hover:text-black text-left font-bold tracking-widest uppercase">{p}</button>
          ))}
        </div>
        <div className="flex flex-col gap-4">
          <span className="text-[9px] uppercase tracking-[0.3em] text-gray-400 font-bold mb-2">Services</span>
          {['Services', 'Resources'].map(p => (
            <button key={p} onClick={() => { onNavigate(p); window.scrollTo(0,0); }} className="text-[10px] text-gray-600 hover:text-black text-left font-bold tracking-widest uppercase">{p}</button>
          ))}
        </div>
        <div className="flex flex-col gap-4">
          <span className="text-[9px] uppercase tracking-[0.3em] text-gray-400 font-bold mb-2">Connect</span>
          <a href="https://www.linkedin.com/company/180-degrees-consulting-iit-kharagpur" target="_blank" rel="noopener noreferrer" className="text-[10px] text-gray-600 hover:text-black font-bold tracking-widest uppercase">LinkedIn</a>
          <a href="https://www.instagram.com/180dc.iitkgp" target="_blank" rel="noopener noreferrer" className="text-[10px] text-gray-600 hover:text-black font-bold tracking-widest uppercase">Instagram</a>
          <button onClick={() => { onNavigate('Contact'); window.scrollTo(0,0); }} className="text-[10px] text-gray-600 hover:text-black text-left font-bold tracking-widest uppercase">Email</button>
        </div>
      </div>
    </footer>
  );
}
