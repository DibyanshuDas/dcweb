import { useState } from 'react';
import { Menu, X } from 'lucide-react';

export default function Navigation({ currentPage, onNavigate }: { currentPage: string, onNavigate: (page: string) => void }) {
  const [isOpen, setIsOpen] = useState(false);
  const pages = ['Home', 'About', 'Services', 'Projects', 'Team', 'Resources', 'Contact'];

  const handleNav = (page: string) => {
    onNavigate(page);
    setIsOpen(false);
    window.scrollTo(0, 0);
  };

  return (
    <header className="fixed top-0 left-0 right-0 flex justify-between items-center py-6 px-6 md:px-16 lg:px-24 xl:px-32 z-50 bg-[#FDFCF8]/90 backdrop-blur-md border-b border-black/5" style={{ fontFamily: "'Open Sans', sans-serif" }}>
      <div 
        className="cursor-pointer"
        onClick={() => handleNav('Home')}
      >
        <img src="/logos/180dc_full.png" alt="180 Degrees Consulting" className="h-6 md:h-8 object-contain" />
      </div>

      {/* Desktop Nav */}
      <nav className="hidden md:flex gap-10 text-[10px] uppercase tracking-[0.4em] font-bold">
        {pages.map(page => (
          <button 
            key={page} 
            onClick={() => handleNav(page)}
            className={`transition-all ${currentPage === page ? 'text-[#86BC2A] border-b border-[#86BC2A] pb-1' : 'text-gray-500 hover:text-black'}`}
          >
            {page}
          </button>
        ))}
      </nav>

      {/* Mobile Nav Toggle */}
      <button className="md:hidden opacity-80" onClick={() => setIsOpen(!isOpen)}>
        {isOpen ? <X size={24} /> : <Menu size={24} />}
      </button>

      {/* Mobile Nav Menu */}
      {isOpen && (
        <div className="absolute top-20 left-6 right-6 bg-white border border-gray-200 p-6 flex flex-col gap-6 z-50 rounded-2xl shadow-xl">
          {pages.map(page => (
            <button 
              key={page} 
              onClick={() => handleNav(page)}
              className={`text-left text-xs uppercase tracking-[0.3em] font-bold ${currentPage === page ? 'text-[#86BC2A]' : 'text-gray-500 hover:text-black'}`}
            >
              {page}
            </button>
          ))}
        </div>
      )}
    </header>
  );
}
