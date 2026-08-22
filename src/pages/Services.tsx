import { motion } from 'motion/react';
import { SERVICES, ENGAGEMENT_TIMELINE, FAQS } from '../data';
import { useState } from 'react';
import { Search, FileText, BarChart2, Flag } from 'lucide-react';

export default function Services() {
  const [openFaq, setOpenFaq] = useState<number | null>(null);

  return (
    <motion.div initial={{opacity: 0, y: 20}} animate={{opacity: 1, y: 0}} transition={{duration: 0.6}} className="flex flex-col gap-32 pt-32 pb-12 px-6 md:px-16 lg:px-24 xl:px-32 relative z-10">
      <div className="flex flex-col">
        <div className="mb-6 flex items-center gap-4">
          <div className="h-[2px] w-12 bg-[#86BC2A]"></div>
          <span className="text-[#86BC2A] text-[11px] font-black uppercase tracking-[0.5em]">What We Do</span>
        </div>
        <h1 className="text-[12vw] sm:text-6xl md:text-[100px] font-black uppercase tracking-tighter leading-[0.9] text-[#0F1115] mb-12">
          Our<br/><span className="text-[#86BC2A]">Services</span>
        </h1>
      </div>

      <section className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 pt-8">
        {SERVICES.map((s, i) => (
          <div key={i} className="flex flex-col gap-6 group border border-gray-200 bg-white p-10 hover:border-[#86BC2A] transition-colors shadow-sm hover:shadow-md h-full">
            <div className="font-montserrat text-[10px] text-gray-400 font-bold tracking-widest">0{i+1}</div>
            <h3 className="font-montserrat text-2xl font-bold tracking-tight group-hover:text-[#86BC2A] text-black transition-colors">{s.vertical}</h3>
            <ul className="flex flex-col gap-4 border-l-2 border-gray-200 group-hover:border-[#86BC2A] transition-colors pl-6 mt-auto">
              {s.offerings.map((offering, j) => (
                <li key={j} className="font-montserrat text-[10px] tracking-[0.2em] uppercase text-gray-600 leading-relaxed">{offering}</li>
              ))}
            </ul>
          </div>
        ))}
      </section>

      <section className="py-12">
        <div className="bg-white rounded-[2rem] shadow-sm border border-gray-100 p-12 md:p-20 flex flex-col items-center relative overflow-hidden">
          <div className="text-center mb-16 relative z-10">
            <h4 className="text-[#86BC2A] text-xs font-semibold tracking-[0.2em] uppercase mb-4 font-montserrat">Process</h4>
            <h2 className="text-4xl md:text-5xl font-serif text-[#0F1115] tracking-tight">Engagement Timeline</h2>
          </div>

          <div className="relative w-full max-w-5xl mx-auto">
            {/* Connecting Line */}
            <div className="absolute top-[24px] left-[12%] right-[12%] h-[1px] bg-gray-200 hidden md:block"></div>

            <div className="flex flex-col md:flex-row justify-between relative z-10 gap-12 md:gap-4">
              {ENGAGEMENT_TIMELINE.map((step, i) => {
                const Icon = [Search, FileText, BarChart2, Flag][i];
                
                return (
                  <div key={i} className="group flex flex-col items-center text-center flex-1 cursor-default">
                    {/* Number Circle */}
                    <div className="w-12 h-12 rounded-full border flex items-center justify-center font-montserrat font-medium text-lg mb-8 transition-colors relative z-10 bg-white border-gray-200 text-gray-800 group-hover:bg-[#86BC2A] group-hover:border-[#86BC2A] group-hover:text-white">
                      {i + 1}
                    </div>

                    {/* Icon Circle */}
                    <div className="w-16 h-16 rounded-full bg-[#86BC2A]/5 group-hover:bg-[#86BC2A]/10 flex items-center justify-center text-[#86BC2A] mb-6 transition-colors">
                      {Icon && <Icon className="w-6 h-6" strokeWidth={1.5} />}
                    </div>

                    {/* Text content */}
                    <h3 className="text-lg md:text-xl font-bold text-gray-900 mb-3 flex items-center justify-center gap-2 font-montserrat tracking-tight">
                      {step.step}
                      <span className="w-2 h-2 rounded-full bg-[#86BC2A] opacity-0 group-hover:opacity-100 transition-opacity"></span>
                    </h3>
                    <p className="text-sm text-gray-500 leading-relaxed max-w-[200px] mx-auto font-montserrat">
                      {step.weeks}
                    </p>
                  </div>
                );
              })}
            </div>
          </div>
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
    </motion.div>
  );
}