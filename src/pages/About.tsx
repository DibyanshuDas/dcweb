import { motion } from 'motion/react';
import { ArrowRight } from 'lucide-react';

export default function About({ onNavigate }: { onNavigate: (page: string) => void }) {
  return (
    
    <motion.div initial={{opacity: 0, y: 20}} animate={{opacity: 1, y: 0}} transition={{duration: 0.6}} className="w-full min-h-screen relative">
      
      {/* Fixed Hero Section */}
      <div className="w-full fixed top-0 left-0 h-[60vh] z-0 overflow-hidden bg-gradient-to-r from-[#5f9730] to-[#264b15] flex items-center justify-center pt-20">
        {/* Abstract waves SVG overlay */}
        <div className="absolute inset-0 opacity-30 pointer-events-none" style={{ 
          backgroundImage: `url('data:image/svg+xml,%3Csvg width="100%25" height="100%25" viewBox="0 0 100 100" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg"%3E%3Cpath d="M-10,40 Q25,10 60,60 T110,30" fill="none" stroke="%23ffffff" stroke-width="0.1"/%3E%3Cpath d="M-10,42 Q25,12 60,62 T110,32" fill="none" stroke="%23ffffff" stroke-width="0.1"/%3E%3Cpath d="M-10,44 Q25,14 60,64 T110,34" fill="none" stroke="%23ffffff" stroke-width="0.1"/%3E%3Cpath d="M-10,46 Q25,16 60,66 T110,36" fill="none" stroke="%23ffffff" stroke-width="0.1"/%3E%3Cpath d="M-10,48 Q25,18 60,68 T110,38" fill="none" stroke="%23ffffff" stroke-width="0.1"/%3E%3Cpath d="M-10,50 Q25,20 60,70 T110,40" fill="none" stroke="%23ffffff" stroke-width="0.1"/%3E%3Cpath d="M-10,52 Q25,22 60,72 T110,42" fill="none" stroke="%23ffffff" stroke-width="0.1"/%3E%3Cpath d="M-10,54 Q25,24 60,74 T110,44" fill="none" stroke="%23ffffff" stroke-width="0.1"/%3E%3Cpath d="M-10,56 Q25,26 60,76 T110,46" fill="none" stroke="%23ffffff" stroke-width="0.1"/%3E%3Cpath d="M-10,58 Q25,28 60,78 T110,48" fill="none" stroke="%23ffffff" stroke-width="0.1"/%3E%3Cpath d="M-10,60 Q25,30 60,80 T110,50" fill="none" stroke="%23ffffff" stroke-width="0.1"/%3E%3C/svg%3E')`
        }}></div>
        <h1 className="text-4xl md:text-5xl font-bold tracking-wide text-white/90 relative z-10">
          About Us
        </h1>
      </div>

      {/* Spacer to push content down below fixed hero */}
      <div className="w-full h-[60vh] pointer-events-none"></div>

      {/* Content that scrolls over the hero */}
      <div className="relative z-10 bg-[#FDFCF8] w-full flex flex-col shadow-2xl">
        
        {/* Mission & Vision Split Section */}
        <div className="w-full flex flex-col md:flex-row">
          {/* Mission */}
          <div className="w-full md:w-1/2 bg-[#E8E8E8] py-24 px-10 md:px-20 flex flex-col items-center justify-center text-center">
            <h2 className="text-3xl md:text-4xl font-bold text-[#333333] mb-8 tracking-tight">Our Mission</h2>
            <p className="text-[#555555] leading-relaxed text-base md:text-lg max-w-sm">
              To help non-profits and social enterprises overcome challenges for the greatest possible social impact by providing affordable and high quality consulting services.
            </p>
          </div>
          {/* Vision */}
          <div className="w-full md:w-1/2 bg-[#629A28] py-24 px-10 md:px-20 flex flex-col items-center justify-center text-center">
            <h2 className="text-3xl md:text-4xl font-bold text-white mb-8 tracking-tight">Our Vision</h2>
            <p className="text-white leading-relaxed text-base md:text-lg max-w-sm">
              To ensure that the movement towards resolving pressing world issues such as poverty, global warming, etc. is unfettered by economic or social constraints and thereby develop the next generation of leaders.
            </p>
          </div>
        </div>

      {/* Intro Description */}
      <div className="w-full bg-white pt-24 pb-12">
        <div className="max-w-[1000px] mx-auto px-6 md:px-12 flex flex-col items-center text-center">
          <h2 className="text-4xl md:text-5xl font-black tracking-tighter text-[#1A1A1A] leading-[1.1] mb-10">
            What makes 180Degrees, <br/><span className="inline-block transform scale-y-[-1] scale-x-[-1] mt-2">180Degrees</span> ?
          </h2>
          <div className="flex flex-col gap-6 text-[#4A4A4A] text-base md:text-lg leading-relaxed max-w-3xl">
            <p>
              180 Degrees Consulting, IIT Kharagpur, founded in April 2020 is an organisation that aims to provide quality consultancy services to socially conscious corporations and NGOs in order to help them achieve the impact they seek to create. Being students of the oldest, largest and most versatile of IITs, the team consists of people who are driven, capable and have diverse skill sets across various fields.
            </p>
            <p>
              This is a platform where students can gain leadership skills, consulting experience and professional etiquette with a chance to drive value through the quality of their collaborative work.
            </p>
          </div>
        </div>
      </div>

      <div className="max-w-[1200px] mx-auto px-6 md:px-12 mt-32 pb-32">
        <div className="bg-[#1A1A1A] text-white p-10 md:p-16 mb-24 rounded-sm">
          <h2 className="text-2xl md:text-3xl font-black tracking-tight mb-12 text-center">What is 180 DC?</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
            <div className="flex flex-col gap-4 text-center">
              <div className="text-4xl text-[#86BC2A] font-black">#1</div>
              <p className="text-sm text-gray-400 leading-relaxed uppercase tracking-widest font-bold">World's largest consultancy for socially conscious enterprises & non-profit organizations</p>
            </div>
            <div className="flex flex-col gap-4 text-center border-y md:border-y-0 md:border-x border-white/10 py-8 md:py-0 md:px-8">
              <div className="text-4xl text-[#86BC2A] font-black">HQ</div>
              <p className="text-sm text-gray-400 leading-relaxed uppercase tracking-widest font-bold">High-quality strategic advice to help clients overcome challenges and reach full potential</p>
            </div>
            <div className="flex flex-col gap-4 text-center">
              <div className="text-4xl text-[#86BC2A] font-black">100M+</div>
              <p className="text-sm text-gray-400 leading-relaxed uppercase tracking-widest font-bold">2.6M+ hours spent, $100M+ worth consultancy services provided at nominal rates</p>
            </div>
          </div>
        </div>

        <div>
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-black tracking-tighter mb-4">Team Structure</h2>
            <div className="w-12 h-1 bg-[#86BC2A] mx-auto"></div>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {[
              {
                role: 'Mentors',
                desc: 'Alumnus from 180DC, IIT Kharagpur, most of whom are working in reputed consulting firms across the globe. They guide us in the projects.'
              },
              {
                role: 'Advisors',
                desc: '4th and 5th year students who are associated with 180DC, most of them having secured internships/placements in big multinational corporations. They make sure the organization is operating smoothly.'
              },
              {
                role: 'Directors',
                desc: '3rd year students, handling the Growth and Research, Finance and Global Coordination and Client Acquisition and Strategy aspects of the organization. They oversee all the projects and all progress of the organization.'
              },
              {
                role: 'Executive Heads',
                desc: '2nd year students, leading a group of consultants in the successful completion of the projects, each handling one project at a time. They are also responsible for the quality training and growth of the consultants.'
              },
              {
                role: 'Consultants',
                desc: '1st year students, chosen through a rigorous selection process consisting of 3 rounds. They are the ones who work on the projects under the guidance of the Executive Heads.'
              }
            ].map((item, idx) => (
              <div key={idx} className="border border-gray-200 p-8 hover:border-[#86BC2A] transition-colors group bg-white shadow-sm hover:shadow-md">
                <h3 className="text-lg font-black tracking-tight mb-4 group-hover:text-[#86BC2A] transition-colors">{item.role}</h3>
                <p className="text-sm text-gray-500 leading-relaxed">{item.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
    </motion.div>
  );
}
