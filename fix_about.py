import re

with open('src/pages/About.tsx', 'r') as f:
    content = f.read()

new_structure = """
    <motion.div initial={{opacity: 0, y: 20}} animate={{opacity: 1, y: 0}} transition={{duration: 0.6}} className="w-full min-h-screen relative">
      
      {/* Fixed Hero Section */}
      <div className="w-full fixed top-0 left-0 h-[60vh] z-0 overflow-hidden bg-gradient-to-r from-[#5f9730] to-[#264b15] flex items-center justify-center pt-20">
        {/* Abstract waves SVG overlay */}
        <div className="absolute inset-0 opacity-30 pointer-events-none" style={{ 
          backgroundImage: "url('data:image/svg+xml,%3Csvg width=\"100%\" height=\"100%\" viewBox=\"0 0 100 100\" preserveAspectRatio=\"none\" xmlns=\"http://www.w3.org/2000/svg\"%3E%3Cpath d=\"M-10,40 Q25,10 60,60 T110,30\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,42 Q25,12 60,62 T110,32\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,44 Q25,14 60,64 T110,34\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,46 Q25,16 60,66 T110,36\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,48 Q25,18 60,68 T110,38\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,50 Q25,20 60,70 T110,40\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,52 Q25,22 60,72 T110,42\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,54 Q25,24 60,74 T110,44\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,56 Q25,26 60,76 T110,46\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,58 Q25,28 60,78 T110,48\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3Cpath d=\"M-10,60 Q25,30 60,80 T110,50\" fill=\"none\" stroke=\"%23ffffff\" stroke-width=\"0.1\"/%3E%3C/svg%3E')"
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
"""

# Replace everything from `<motion.div ... className="w-full min-h-screen pb-20">` down to the start of Intro Description
start_str = r'<motion\.div initial={{opacity: 0, y: 20}} animate={{opacity: 1, y: 0}} transition={{duration: 0\.6}} className="w-full min-h-screen pb-20">\s*{/\* Hero Section \*/}.*?{/\* Intro Description \*/}'

content = re.sub(start_str, new_structure + "\n      {/* Intro Description */}", content, flags=re.DOTALL)

# Add pb-20 to the wrapper `div.relative.z-10.bg-[#FDFCF8]` by finding it or just letting it end naturally, wait, the parent `motion.div` has no pb-20 now.
# So I should make sure the ending of `motion.div` is correct.
# Actually let's just make the closing CTA have pb-20 or something. 
# There is a `mt-32` in the Team structure section. We will add pb-20 there.
content = content.replace(
    '<div className="max-w-[1200px] mx-auto px-6 md:px-12 mt-32">',
    '<div className="max-w-[1200px] mx-auto px-6 md:px-12 mt-32 pb-32">'
)

# And we need to close the `div` we opened: `<div className="relative z-10 bg-[#FDFCF8] w-full flex flex-col shadow-2xl">`
# Let's add `</div>` right before `</motion.div>`
content = content.replace(
    '</motion.div>',
    '</div>\n    </motion.div>'
)

with open('src/pages/About.tsx', 'w') as f:
    f.write(content)
print("Done")
