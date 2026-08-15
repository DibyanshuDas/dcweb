import React, { useState } from 'react';

export default function Contact() {
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
  };

  return (
    <div className="flex flex-col lg:flex-row gap-24 pt-32 pb-12 px-6 md:px-16 lg:px-24 xl:px-32 relative z-10">
      <div className="flex-1 flex flex-col gap-16">
        <div>
          <div className="mb-6 flex items-center gap-4">
            <div className="h-[2px] w-12 bg-[#86BC2A]"></div>
            <span className="text-[#86BC2A] text-[11px] font-black uppercase tracking-[0.5em]">Reach Out</span>
          </div>
          <h1 className="text-6xl md:text-[80px] font-black uppercase tracking-tighter leading-[0.9] mb-8 text-black">
            Get In<br/><span className="text-transparent" style={{ WebkitTextStroke: '2px #0F0F0F' }}>Touch</span>
          </h1>
          <p className="text-[10px] font-bold uppercase tracking-[0.2em] text-gray-500 leading-relaxed max-w-md">
            Client applications are accepted on a rolling basis. Current intake: Spring 2025.
          </p>
        </div>

        <div className="flex flex-col gap-10 border-t border-gray-200 pt-10">
          <div>
            <div className="text-[10px] uppercase tracking-[0.3em] text-gray-400 font-bold mb-3">Email</div>
            <div className="text-xl font-bold tracking-widest uppercase">180dc@iitkgp.ac.in</div>
          </div>
          <div>
            <div className="text-[10px] uppercase tracking-[0.3em] text-gray-400 font-bold mb-3">Location</div>
            <div className="text-xs font-bold uppercase tracking-[0.2em] text-gray-600 leading-loose">
              Indian Institute of Technology Kharagpur<br/>
              Kharagpur, West Bengal – 721302, India
            </div>
          </div>
          <div>
            <div className="text-[10px] uppercase tracking-[0.3em] text-gray-400 font-bold mb-3">Website</div>
            <a href="https://www.180dciitkgp.in" target="_blank" rel="noopener noreferrer" className="text-xs font-bold uppercase tracking-[0.2em] text-[#86BC2A] hover:text-black transition-colors">www.180dciitkgp.in</a>
          </div>
        </div>
      </div>

      <div className="flex-1 bg-white shadow-sm border border-gray-200 p-10 md:p-16">
        {submitted ? (
          <div className="h-full flex flex-col items-center justify-center text-center gap-8 min-h-[400px]">
             <div className="text-[#86BC2A] text-6xl">✓</div>
             <div className="text-3xl font-black uppercase tracking-tight text-black">Message Received</div>
             <p className="text-[10px] uppercase tracking-widest text-gray-500 font-bold">We'll respond within 3-5 business days.</p>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="flex flex-col gap-10">
            <div className="flex gap-8">
              <input required type="text" placeholder="FIRST NAME" className="w-full bg-transparent border-b border-gray-300 pb-4 text-[10px] font-black uppercase tracking-[0.2em] focus:outline-none focus:border-[#86BC2A] transition-colors placeholder:text-gray-400 text-black" />
              <input required type="text" placeholder="LAST NAME" className="w-full bg-transparent border-b border-gray-300 pb-4 text-[10px] font-black uppercase tracking-[0.2em] focus:outline-none focus:border-[#86BC2A] transition-colors placeholder:text-gray-400 text-black" />
            </div>
            <input required type="email" placeholder="EMAIL ADDRESS" className="w-full bg-transparent border-b border-gray-300 pb-4 text-[10px] font-black uppercase tracking-[0.2em] focus:outline-none focus:border-[#86BC2A] transition-colors placeholder:text-gray-400 text-black" />
            <input type="text" placeholder="ORGANISATION" className="w-full bg-transparent border-b border-gray-300 pb-4 text-[10px] font-black uppercase tracking-[0.2em] focus:outline-none focus:border-[#86BC2A] transition-colors placeholder:text-gray-400 text-black" />
            <select required defaultValue="" className="w-full bg-transparent border-b border-gray-300 pb-4 text-[10px] font-black uppercase tracking-[0.2em] focus:outline-none focus:border-[#86BC2A] transition-colors text-gray-800 appearance-none">
              <option value="" disabled>INQUIRY TYPE</option>
              <option value="client" className="bg-white text-black">Become a Client</option>
              <option value="team" className="bg-white text-black">Join the Team</option>
              <option value="partner" className="bg-white text-black">Partnership / Sponsorship</option>
              <option value="media" className="bg-white text-black">Media / Press</option>
              <option value="other" className="bg-white text-black">Other</option>
            </select>
            <textarea required placeholder="MESSAGE" rows={4} className="w-full bg-transparent border-b border-gray-300 pb-4 text-[10px] font-black uppercase tracking-[0.2em] focus:outline-none focus:border-[#86BC2A] transition-colors resize-none placeholder:text-gray-400 text-black"></textarea>
            
            <button type="submit" className="bg-black text-white py-6 rounded-full text-[10px] font-black uppercase tracking-[0.2em] hover:bg-[#86BC2A] transition-colors mt-6">
              Send Message
            </button>
          </form>
        )}
      </div>
    </div>
  );
}