import { SERVICES, ENGAGEMENT_TIMELINE, FAQS } from '../data';
import { useState } from 'react';

export default function Services() {
  const [openFaq, setOpenFaq] = useState<number | null>(null);

  return (
    <div className="flex flex-col gap-32 pt-32 pb-12 px-6 md:px-16 lg:px-24 xl:px-32 relative z-10">
      <div className="flex flex-col">
        <div className="mb-6 flex items-center gap-4">
          <div className="h-[2px] w-12 bg-[#86BC2A]"></div>
          <span className="text-[#86BC2A] text-[11px] font-black uppercase tracking-[0.5em]">What We Do</span>
        </div>
        <h1 className="text-6xl md:text-[100px] font-black uppercase tracking-tighter text-black leading-none mb-12">
          Our<br/><span className="text-transparent" style={{ WebkitTextStroke: '2px #0F0F0F' }}>Services</span>
        </h1>
      </div>

      <section className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-x-12 gap-y-16 border-t border-gray-200 pt-16">
        {SERVICES.map((s, i) => (
          <div key={i} className="flex flex-col gap-6 group">
            <div className="text-[10px] text-gray-400 font-mono font-bold tracking-widest">0{i+1}</div>
            <h3 className="text-2xl font-black uppercase tracking-tight group-hover:text-[#86BC2A] text-black transition-colors">{s.vertical}</h3>
            <ul className="flex flex-col gap-4 border-l-2 border-gray-200 pl-6">
              {s.offerings.map((offering, j) => (
                <li key={j} className="text-[10px] font-bold tracking-[0.2em] uppercase text-gray-600 leading-relaxed">{offering}</li>
              ))}
            </ul>
          </div>
        ))}
      </section>

      <section>
        <h2 className="text-4xl md:text-6xl font-black uppercase tracking-tighter mb-16 text-black">Engagement Timeline</h2>
        <div className="flex flex-col md:flex-row justify-between border-t border-gray-200">
          {ENGAGEMENT_TIMELINE.map((step, i) => (
            <div key={i} className="flex-1 border-b md:border-b-0 md:border-r border-gray-200 p-10 flex flex-col gap-4 hover:bg-gray-50 transition-colors">
              <div className="text-2xl font-black uppercase tracking-tight text-[#86BC2A]">{i+1}. {step.step}</div>
              <div className="text-[10px] font-bold uppercase tracking-widest text-gray-500 leading-loose">{step.weeks}</div>
            </div>
          ))}
        </div>
      </section>

      <section className="max-w-4xl">
        <h2 className="text-4xl md:text-6xl font-black uppercase tracking-tighter mb-16 text-black">FAQ</h2>
        <div className="flex flex-col border-t border-gray-200">
          {FAQS.map((faq, i) => (
            <div key={i} className="border-b border-gray-200">
              <button 
                className="w-full py-10 flex justify-between items-center text-left"
                onClick={() => setOpenFaq(openFaq === i ? null : i)}
              >
                <span className="text-lg md:text-xl font-bold tracking-tight text-gray-800 hover:text-black transition-colors">{faq.q}</span>
                <span className="text-[#86BC2A] font-mono text-2xl font-bold">{openFaq === i ? '-' : '+'}</span>
              </button>
              {openFaq === i && (
                <div className="pb-10 text-base text-gray-600 leading-relaxed">
                  {faq.a}
                </div>
              )}
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}