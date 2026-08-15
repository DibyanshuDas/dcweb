import { ArrowRight } from 'lucide-react';

export default function About({ onNavigate }: { onNavigate: (page: string) => void }) {
  return (
    <div className="w-full min-h-screen pb-20">
      
      {/* Hero Section */}
      <div className="w-full bg-[#E8EDEC] relative overflow-hidden" style={{
        backgroundImage: "url('data:image/svg+xml,%3Csvg width=\"100%\" height=\"100%\" viewBox=\"0 0 100 100\" preserveAspectRatio=\"none\" xmlns=\"http://www.w3.org/2000/svg\"%3E%3Cpath d=\"M0,50 Q25,20 50,50 T100,50\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.5\" stroke-dasharray=\"2,4\" opacity=\"0.5\"/%3E%3Cpath d=\"M0,80 Q35,50 70,80 T100,20\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.5\" stroke-dasharray=\"2,4\" opacity=\"0.5\"/%3E%3Cpath d=\"M20,0 Q50,40 20,100\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.5\" stroke-dasharray=\"2,4\" opacity=\"0.5\"/%3E%3C/svg%3E')"
      }}>
        <div className="max-w-[1200px] mx-auto pt-48 pb-32 px-6 md:px-12 relative z-10">
          <div className="text-[#86BC2A] text-xs uppercase tracking-[0.3em] font-bold mb-6">About Us</div>
          <h1 className="text-5xl md:text-6xl lg:text-[80px] font-black tracking-tighter text-[#1A1A1A] max-w-4xl leading-[1.05] mb-12">
            What makes 180Degrees, <br/><span className="inline-block transform scale-y-[-1] scale-x-[-1] mt-2">180Degrees</span> ?
          </h1>
          <div className="flex flex-col gap-6 max-w-2xl text-[#4A4A4A] text-base md:text-lg leading-relaxed">
            <p>
              180 Degrees Consulting, IIT Kharagpur, founded in April 2020 is an organisation that aims to provide quality consultancy services to socially conscious corporations and NGOs in order to help them achieve the impact they seek to create. Being students of the oldest, largest and most versatile of IITs, the team consists of people who are driven, capable and have diverse skill sets across various fields.
            </p>
            <p>
              This is a platform where students can gain leadership skills, consulting experience and professional etiquette with a chance to drive value through the quality of their collaborative work.
            </p>
          </div>
        </div>
      </div>

      {/* Mission & Vision Section */}
      <div className="w-full bg-[#E8EDEC]">
        <div className="max-w-[1200px] mx-auto pb-32 px-6 md:px-12 grid grid-cols-1 md:grid-cols-2 gap-16 md:gap-24 relative z-10">
          <div className="hidden md:block absolute top-0 bottom-0 left-1/2 w-px bg-black/5 -translate-x-1/2"></div>
          
          <div className="relative">
            <h2 className="text-3xl md:text-4xl font-black tracking-tight mb-8 text-[#1A1A1A]">Our Mission</h2>
            <p className="text-[#4A4A4A] mb-8 leading-relaxed text-base md:text-lg">
              To create tangible social impact and improve the lives of citizens across the world by providing quality consultancy services and, in the process creating individuals who become future value creators in society.
            </p>
            <p className="text-[#1A1A1A] font-bold text-sm uppercase tracking-wider mb-4">To help startups and socially-minded organizations:</p>
            <ul className="flex flex-col gap-3">
              {['Maximize Earnings', 'Create More Impact', 'Tackle Business Problems', 'Capitalize on opportunities'].map((item, i) => (
                <li key={i} className="flex items-center gap-3 text-sm text-[#4A4A4A]">
                  <div className="w-1.5 h-1.5 rounded-full bg-[#86BC2A]"></div>
                  {item}
                </li>
              ))}
            </ul>
          </div>

          <div className="relative">
            <h2 className="text-3xl md:text-4xl font-black tracking-tight mb-8 text-[#1A1A1A]">Our Vision</h2>
            <p className="text-[#4A4A4A] mb-8 leading-relaxed text-base md:text-lg">
              To provide students with a platform to hone their professional skills and acquire the best-in-class capabilities to maximise the impact created in their prospective careers while delivering quality consultancy services to socially conscious organisations.
            </p>
            <ul className="flex flex-col gap-3">
              {[
                'Inclusive, supportive and value-driven branch',
                'Consultants being encouraged to uphold responsibility',
                'Focused on professional development',
                'Empowered to do work that will make a true difference in society'
              ].map((item, i) => (
                <li key={i} className="flex items-center gap-3 text-sm text-[#4A4A4A]">
                  <div className="w-1.5 h-1.5 rounded-full bg-[#86BC2A]"></div>
                  {item}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>

      <div className="max-w-[1200px] mx-auto px-6 md:px-12 mt-32">
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
  );
}
