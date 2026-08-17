import { useState } from 'react';
import { STATS, ALUMNI_COMPANIES, BLOG_POSTS } from '../data';
import { motion } from 'motion/react';
import logo180dcGlobe from '../assets/logos/180dc_globe.jpg';

const CompanyLogo = ({ company }: { company: { name: string, logoUrl?: string, website?: string }, key?: string }) => {
  const [imgError, setImgError] = useState(false);

  const Content = () => {
    if (imgError || !company.logoUrl) {
      return (
        <div className="text-xl font-black uppercase tracking-widest text-gray-400 hover:text-gray-800 transition-colors cursor-pointer whitespace-nowrap">
          {company.name}
        </div>
      );
    }

    return (
      <div className="flex items-center justify-center w-40 h-16 hover:scale-110 transition-transform duration-300">
        <img 
          src={company.logoUrl} 
          alt={company.name} 
          className="max-w-full max-h-full object-contain pointer-events-none" 
          onError={() => setImgError(true)} 
        />
      </div>
    );
  };

  if (company.website) {
    return (
      <a href={company.website} target="_blank" rel="noopener noreferrer">
        <Content />
      </a>
    );
  }

  return <Content />;
};

export default function Home({ onNavigate }: { onNavigate: (page: string) => void }) {
  return (
    <div className="flex flex-col gap-32 relative z-10 pt-32 pb-12 px-6 md:px-16 lg:px-24 xl:px-32">
      {/* Hero */}
      <section className="flex flex-col lg:flex-row gap-16 pt-10">
        <motion.div 
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
          className="flex-1 flex flex-col justify-center"
        >
          <motion.div 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.2, duration: 0.6 }}
            className="mb-8 flex items-center gap-4"
          >
            <div className="h-[2px] w-12 bg-[#86BC2A]"></div>
            <span className="text-[#86BC2A] text-[11px] font-black uppercase tracking-[0.5em]">IIT Kharagpur &middot; 180DC Global Network</span>
          </motion.div>
          
          <h1 className="text-[12vw] sm:text-6xl md:text-[80px] lg:text-[100px] font-black leading-[0.9] uppercase tracking-tighter mb-10 text-[#0F1115]">
            Turning<br/>Challenges<br/>Into <br />
            <motion.span
              initial="hidden"
              animate="visible"
              variants={{
                hidden: { opacity: 0 },
                visible: {
                  opacity: 1,
                  transition: { staggerChildren: 0.05, delayChildren: 0.8 }
                }
              }}
              className="text-[#86BC2A] inline-block"
            >
              {"Opportunities".split('').map((char, index) => (
                <motion.span
                  key={index}
                  variants={{
                    hidden: { opacity: 0, y: 20 },
                    visible: { 
                      opacity: 1, 
                      y: 0,
                      transition: { duration: 0.5, ease: "easeOut" }
                    }
                  }}
                  className="inline-block"
                >
                  {char}
                </motion.span>
              ))}
            </motion.span>
          </h1>

          <motion.p 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.4, duration: 0.6 }}
            className="font-montserrat text-xs md:text-sm leading-relaxed text-gray-600 max-w-xl mb-12">
            180 Degrees Consulting offers high-quality consulting services without the premium price tag. Our team comprises carefully selected top-tier university students who volunteer their time because they share our vision and values. We partner with non-profits and social enterprises to provide innovative, practical, and sustainable solutions to the challenges they face.
          </motion.p>

          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.6, duration: 0.6 }}
            className="flex flex-wrap gap-6 items-center"
          >
            <button 
              onClick={() => onNavigate('Projects')}
              className="bg-black text-white px-10 py-5 rounded-full text-[10px] font-black uppercase tracking-[0.2em] hover:bg-[#86BC2A] transition-colors"
            >
              Our Projects
            </button>
            <button 
              onClick={() => onNavigate('Services')}
              className="border border-gray-300 text-black px-10 py-5 rounded-full text-[10px] font-black uppercase tracking-[0.2em] hover:border-black transition-colors"
            >
              Our Services
            </button>
          </motion.div>
        </motion.div>
        
        <motion.div 
          initial={{ opacity: 0, x: 30 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.4, duration: 0.8, ease: "easeOut" }}
          className="w-full lg:w-1/3 flex flex-col justify-end border-l-2 border-gray-200 pl-8 py-8 relative"
        >
           <div className="mb-12">
             <div className="w-64 h-64 md:w-96 md:h-96 mb-8 flex-shrink-0 relative">
               <img src={logo180dcGlobe} alt="180DC Logo Globe" className="w-full h-full object-contain mix-blend-multiply" />
             </div>
             <div className="font-montserrat text-[10px] tracking-widest text-[#86BC2A] mb-4">Why 180 Degrees?</div>
             <p className="font-montserrat text-sm text-gray-600 mb-4 leading-relaxed">"It's because we work to turn good organizations into great organizations, and challenges into opportunities."</p>
             <div className="font-montserrat text-[10px] text-gray-500 tracking-widest">— Nat Ware (Founder & CEO)</div>
           </div>
           
           <div className="grid grid-cols-2 gap-8 pt-8 border-t border-gray-200">
             {STATS.map(stat => (
               <div key={stat.label}>
                 <div className="font-montserrat text-2xl md:text-3xl mb-2 text-black">{stat.value}</div>
                 <div className="font-montserrat text-[9px] uppercase tracking-[0.3em] text-gray-500">{stat.label}</div>
               </div>
             ))}
           </div>
        </motion.div>
      </section>

      {/* Marquees */}
      <section className="border-y border-gray-200 py-12 overflow-hidden relative flex flex-col gap-10 w-screen left-1/2 right-1/2 -ml-[50vw] -mr-[50vw] [mask-image:_linear-gradient(to_right,transparent_0,_black_256px,_black_calc(100%-256px),transparent_100%)]">
        <div className="px-6 md:px-0 text-center mb-2">
          <h2 className="text-xl md:text-2xl font-black uppercase tracking-widest text-[#0F1115]">Our Alums work At</h2>
        </div>

        {/* Top Marquee: Right to Left */}
        <div 
          className="flex whitespace-nowrap gap-8 w-fit items-center animate-marquee-left"
        >
          {[...ALUMNI_COMPANIES.slice(0, 12), ...ALUMNI_COMPANIES.slice(0, 12)].map((company, i) => (
            <CompanyLogo key={`top-${i}`} company={company} />
          ))}
        </div>

        {/* Bottom Marquee: Left to Right */}
        <div 
          className="flex whitespace-nowrap gap-8 w-fit items-center animate-marquee-right"
        >
          {[...ALUMNI_COMPANIES.slice(12), ...ALUMNI_COMPANIES.slice(12)].map((company, i) => (
            <CompanyLogo key={`bottom-${i}`} company={company} />
          ))}
        </div>
      </section>

      {/* Three Cards */}
      <section className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {[
          { title: "Our Services", desc: "Six consulting verticals", page: "Services" },
          { title: "Past Projects", desc: "28+ real-world engagements", page: "Projects" },
          { title: "Team Structure", desc: "Meet our Executive Directors", page: "Team" }
        ].map((card, i) => (
          <motion.div 
            initial={{ opacity: 0, y: 50 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-100px" }}
            transition={{ duration: 0.5, delay: i * 0.1 }}
            key={card.title}
            onClick={() => onNavigate(card.page)}
            className="group cursor-pointer border border-gray-200 bg-white p-10 hover:border-[#86BC2A] transition-colors relative overflow-hidden flex flex-col justify-between h-64 shadow-sm hover:shadow-md"
          >
            <div className="absolute top-8 right-8 text-[#86BC2A] opacity-0 group-hover:opacity-100 transition-opacity">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </div>
            <div className="font-montserrat text-[10px] tracking-widest text-gray-500 font-bold">0{i+1} // {card.desc}</div>
            <h3 className="font-montserrat text-3xl font-bold tracking-tighter mt-auto text-black">{card.title}</h3>
          </motion.div>
        ))}
      </section>

      {/* Blogs */}
      <section>
        <motion.div 
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-100px" }}
          transition={{ duration: 0.6 }}
          className="flex flex-col md:flex-row md:justify-between md:items-end gap-6 mb-12"
        >
          <h2 className="text-5xl md:text-7xl font-black uppercase tracking-tighter text-black">From Our Blog</h2>
          <a href="https://www.180dciitkgp.in/blogs" target="_blank" rel="noopener noreferrer" className="text-[10px] uppercase tracking-widest font-bold text-[#86BC2A] hover:text-black border-b border-[#86BC2A] pb-1 transition-colors w-fit">All Articles</a>
        </motion.div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {BLOG_POSTS.map((post, i) => (
            <motion.a 
              initial={{ opacity: 0, y: 50 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-50px" }}
              transition={{ duration: 0.5, delay: i * 0.1 }}
              key={i} href={post.link} target="_blank" rel="noopener noreferrer" className="border border-gray-200 p-8 flex flex-col justify-between min-h-[300px] hover:border-[#86BC2A] transition-colors cursor-pointer group bg-gray-50 shadow-sm">
              <div className="flex justify-between items-start mb-6">
                <div className="flex gap-4 items-center">
                  <span className="font-montserrat text-[10px] tracking-widest text-[#86BC2A] border border-[#86BC2A] px-2 py-1 rounded-full">{post.category}</span>
                  <span className="font-montserrat text-[10px] tracking-widest text-gray-400">{post.date}</span>
                </div>
                <div className="text-gray-300 group-hover:text-black transition-colors">↗</div>
              </div>
              <h4 className="font-montserrat text-sm font-bold tracking-widest leading-loose text-gray-800 group-hover:text-[#86BC2A] transition-colors mb-4">{post.title}</h4>
              <p className="font-montserrat text-[10px] tracking-[0.2em] text-gray-500 leading-relaxed line-clamp-3">{post.desc}</p>
            </motion.a>
          ))}
        </div>
      </section>

      {/* Closing CTA */}
      <motion.section 
        initial={{ opacity: 0, scale: 0.95 }}
        whileInView={{ opacity: 1, scale: 1 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.6 }}
        className="border border-gray-200 bg-gray-50 p-16 md:p-32 text-center flex flex-col items-center group hover:border-[#86BC2A] transition-colors shadow-sm"
      >
        <h2 className="text-4xl md:text-7xl font-black uppercase tracking-tighter mb-12 max-w-3xl leading-[0.9] text-black">
          Let's Build Something <br/><span className="text-[#86BC2A]">That Matters</span>
        </h2>
        <button 
          onClick={() => onNavigate('Contact')}
          className="bg-black text-white px-12 py-6 rounded-full text-[10px] font-black uppercase tracking-[0.2em] hover:bg-[#86BC2A] transition-colors"
        >
          Contact Us
        </button>
      </motion.section>
    </div>
  );
}