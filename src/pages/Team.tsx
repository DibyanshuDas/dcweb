import { TEAM } from '../data';

const LinkedInIcon = () => (
  <svg className="w-8 h-8 text-black hover:opacity-80 transition-opacity" viewBox="0 0 24 24" fill="currentColor">
    <circle cx="12" cy="12" r="12" />
    <path d="M8.3 17H5.6V9h2.7v8zm-1.3-9.2c-.9 0-1.5-.6-1.5-1.4 0-.8.6-1.4 1.5-1.4s1.5.6 1.5 1.4c0 .8-.6 1.4-1.5 1.4zM19.4 17h-2.7v-4c0-1-.3-1.8-1.3-1.8-.7 0-1.1.5-1.3 1 0 .2-.1.4-.1.6v4.1h-2.7s.1-7.2 0-8h2.7v1.1c.4-.5 1-1.3 2.4-1.3 1.8 0 3.1 1.1 3.1 3.6v4.7z" fill="white" />
  </svg>
);

export default function Team() {
  return (
    <div className="bg-[#EAEAEA] min-h-screen pt-32 pb-24 px-6 md:px-16 lg:px-24 xl:px-32 relative z-10 font-sans">
      
      {/* HEADER */}
      <div className="flex justify-center mb-16 text-center">
        <h1 className="text-4xl md:text-5xl font-black uppercase tracking-tighter text-black">
          Meet <span className="text-[#86BC2A]">The Team</span>
        </h1>
      </div>

      {/* GROUP PHOTOS */}
      <div className="flex flex-col gap-4 mb-24 max-w-6xl mx-auto">
        <div className="w-full aspect-[2/1] sm:aspect-[21/9] bg-gray-200 overflow-hidden">
          <img src="/team/group/1.jpg" alt="180DC Group" className="w-full h-full object-cover object-top" />
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div className="w-full aspect-[4/3] sm:aspect-[3/2] bg-gray-200 overflow-hidden">
            <img src="/team/group/2.jpg" alt="180DC Group" className="w-full h-full object-cover" />
          </div>
          <div className="w-full aspect-[4/3] sm:aspect-[3/2] bg-gray-200 overflow-hidden">
            <img src="/team/group/3.jpg" alt="180DC Group" className="w-full h-full object-cover object-center" />
          </div>
        </div>
      </div>

      {/* EXECUTIVE DIRECTORS */}
      <section className="mb-24 max-w-6xl mx-auto">
        <h2 className="text-4xl md:text-5xl font-black uppercase tracking-tighter mb-16 text-center text-[#86BC2A]">
          Executive Directors
        </h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-x-12 gap-y-16">
          {TEAM.directors.map((d, i) => (
            <div key={i} className="flex flex-col items-center text-center group">
               <div className="w-full aspect-[4/5] bg-gray-300 mb-6 overflow-hidden">
                 {d.avatar.includes('/') ? (
                   <img src={d.avatar} alt={d.name} className="w-full h-full object-cover"  />
                 ) : (
                   <div className="w-full h-full flex items-center justify-center text-4xl font-bold text-gray-500">{d.avatar}</div>
                 )}
               </div>
               <div className="text-xl font-bold text-black mb-1">{d.name}</div>
               <a href={`mailto:${d.email}`} className="text-[13px] text-[#86BC2A] underline mb-4 hover:opacity-80">{d.email}</a>
               <div className="text-[13px] text-gray-800 mb-6">{d.role === "Executive Director" ? d.dept : `${d.role} | ${d.dept}`}</div>
               <a href="#" className="inline-block mt-auto">
                 <LinkedInIcon />
               </a>
            </div>
          ))}
        </div>
      </section>

      {/* OUR ADVISORS */}
      <section className="mb-24 max-w-6xl mx-auto">
        <h2 className="text-4xl md:text-5xl font-black uppercase tracking-tighter mb-16 text-center text-[#86BC2A]">
          Our Advisors
        </h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-x-12 gap-y-16">
          {TEAM.advisors.map((advisor, i) => (
            <div key={i} className="flex flex-col items-center text-center group">
               <div className="w-full aspect-[4/5] bg-gray-300 mb-6 overflow-hidden">
                 {advisor.avatar.includes('/') ? (
                   <img src={advisor.avatar} alt={advisor.name} className="w-full h-full object-cover object-top"  />
                 ) : (
                   <div className="w-full h-full flex items-center justify-center text-4xl font-bold text-gray-500">{advisor.avatar}</div>
                 )}
               </div>
               <div className="text-xl font-bold text-black mb-1">{advisor.name}</div>
               <a href={`mailto:${advisor.email}`} className="text-[13px] text-[#86BC2A] underline mb-6 hover:opacity-80">{advisor.email}</a>
               <a href="#" className="inline-block mt-auto">
                 <LinkedInIcon />
               </a>
            </div>
          ))}
        </div>
      </section>

      {/* OUR ALUMNI */}
      <section className="max-w-6xl mx-auto">
        <h2 className="text-4xl md:text-5xl font-black uppercase tracking-tighter mb-16 text-center text-[#86BC2A]">
          Our Alumni
        </h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-x-8 gap-y-16">
          {TEAM.alumni.map((alumnus, i) => (
            <div key={i} className="flex flex-col items-center text-center group">
              <div className="w-full aspect-[4/5] bg-gray-300 mb-6 overflow-hidden">
                {alumnus.avatar.includes('/') ? (
                   <img src={alumnus.avatar} alt={alumnus.name} className="w-full h-full object-cover object-top grayscale"  />
                 ) : (
                   <div className="w-full h-full flex items-center justify-center text-4xl font-bold text-gray-500 bg-gray-200">{alumnus.avatar}</div>
                 )}
              </div>
              <h4 className="text-lg font-bold text-black mb-3">{alumnus.name}</h4>
              <div className="text-xs text-gray-700 mb-6 max-w-[90%] leading-relaxed">{alumnus.co}</div>
              <a href="#" className="inline-block mt-auto">
                <LinkedInIcon />
              </a>
            </div>
          ))}
        </div>
      </section>

    </div>
  );
}
