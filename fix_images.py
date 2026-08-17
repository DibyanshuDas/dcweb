import re

with open('src/data.ts', 'r') as f:
    content = f.read()

new_projects = """export const PROJECTS = [
  { tag: "Government", title: "Guntur Impact Fund", desc: "Conducted market research and financial planning to generate employment for the rural population of Guntur.", impact: "Market Research & Strategy", logo: "https://picsum.photos/seed/guntur/600/400" },
  { tag: "Automotive", title: "CARS24", desc: "Created a benchmarking framework for 28 safety-product categories and developed a data-driven rating model.", impact: "Benchmarking Framework", logo: "https://picsum.photos/seed/cars24/600/400" },
  { tag: "Logistics", title: "Kakinada Seaport", desc: "On-site assessment of cargo logistics, creating a tracking system and ML model to analyze truck flow.", impact: "Logistics Assessment", logo: "https://picsum.photos/seed/kakinada/600/400" },
  { tag: "Technology", title: "Trumio Inc.", desc: "Startup connecting corporate companies with college students through a project portal for real-world experience.", impact: "Platform Strategy", logo: "https://picsum.photos/seed/trumio/600/400" },
  { tag: "Retail", title: "CHK", desc: "Curated a Go-To Market (GTM) strategy including financial, market and competitor analysis of the sneaker market.", impact: "GTM Strategy", logo: "https://picsum.photos/seed/chk/600/400" },
  { tag: "Mobility", title: "Indeanta", desc: "Campus mobility solutions leading to a 25% reduction in transport prices.", impact: "Price Reduction Model", logo: "https://picsum.photos/seed/indeanta/600/400" },
  { tag: "Technology", title: "BR Business Solutions", desc: "Helped the client launch their website from 0 to 1 with website layouts and inventory management.", impact: "Website Launch", logo: "https://picsum.photos/seed/brbusiness/600/400" },
  { tag: "Government", title: "Commercial Tax Dept.", desc: "Operations consulting for MP Government's Department of Commercial Tax.", impact: "Process Optimisation", logo: "https://picsum.photos/seed/comtax/600/400" },
  { tag: "Social Enterprise", title: "Washing Machine Project", desc: "Market expansion strategy for a UK-based social enterprise providing affordable washing solutions.", impact: "Expansion Strategy", logo: "https://picsum.photos/seed/washing/600/400" }
];"""

content = re.sub(r'export const PROJECTS = \[.*?\];', new_projects, content, flags=re.DOTALL)

with open('src/data.ts', 'w') as f:
    f.write(content)
print("Done")
