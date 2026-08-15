import re

with open('src/pages/Home.tsx', 'r') as f:
    content = f.read()

target = """          <h1 className="text-6xl md:text-[80px] lg:text-[100px] font-black leading-[0.82] uppercase tracking-tighter mb-10 text-gray-900">
            Turning<br/>Challenges<br/>Into <span className="text-transparent" style={{ WebkitTextStroke: '2px #0F0F0F' }}>Oppor-</span><br/><span className="text-transparent" style={{ WebkitTextStroke: '2px #0F0F0F' }}>tunities</span>
          </h1>"""

replacement = """          <h1 className="text-[12vw] sm:text-6xl md:text-[80px] lg:text-[100px] font-montserrat font-black leading-[0.85] uppercase tracking-[-0.04em] mb-10 text-[#0F1115]">
            Turning<br/>Challenges<br/>Into <span className="text-transparent" style={{ WebkitTextStroke: '1.5px #0F1115' }}>Oppor-</span><br/><span className="text-transparent" style={{ WebkitTextStroke: '1.5px #0F1115' }}>tunities</span>
          </h1>"""

if target in content:
    with open('src/pages/Home.tsx', 'w') as f:
        f.write(content.replace(target, replacement))
    print("Success")
else:
    print("Target not found")
