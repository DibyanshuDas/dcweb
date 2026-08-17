import re

with open('src/data.ts', 'r') as f:
    content = f.read()

new_projects = """export const PROJECTS = [
  { tag: "Government", title: "Guntur Impact Fund", desc: "Conducted market research and financial planning to generate employment for the rural population of Guntur.", impact: "Market Research & Strategy", logo: "https://images.unsplash.com/photo-1595841696677-6489ff3f8cd1?q=80&w=600&auto=format&fit=crop" },
  { tag: "Automotive", title: "CARS24", desc: "Created a benchmarking framework for 28 safety-product categories and developed a data-driven rating model.", impact: "Benchmarking Framework", logo: "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?q=80&w=600&auto=format&fit=crop" },
  { tag: "Logistics", title: "Kakinada Seaport", desc: "On-site assessment of cargo logistics, creating a tracking system and ML model to analyze truck flow.", impact: "Logistics Assessment", logo: "https://images.unsplash.com/photo-1586528116311-ad8ed7f66a78?q=80&w=600&auto=format&fit=crop" },
  { tag: "Technology", title: "Trumio Inc.", desc: "Startup connecting corporate companies with college students through a project portal for real-world experience.", impact: "Platform Strategy", logo: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=600&auto=format&fit=crop" },
  { tag: "Retail", title: "CHK", desc: "Curated a Go-To Market (GTM) strategy including financial, market and competitor analysis of the sneaker market.", impact: "GTM Strategy", logo: "https://images.unsplash.com/photo-1552346154-21d32810baa3?q=80&w=600&auto=format&fit=crop" },
  { tag: "Mobility", title: "Indeanta", desc: "Campus mobility solutions leading to a 25% reduction in transport prices.", impact: "Price Reduction Model", logo: "https://images.unsplash.com/photo-1519003722824-194d4455a60c?q=80&w=600&auto=format&fit=crop" },
  { tag: "Technology", title: "BR Business Solutions", desc: "Helped the client launch their website from 0 to 1 with website layouts and inventory management.", impact: "Website Launch", logo: "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=600&auto=format&fit=crop" },
  { tag: "Government", title: "Commercial Tax Dept.", desc: "Operations consulting for MP Government's Department of Commercial Tax.", impact: "Process Optimisation", logo: "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?q=80&w=600&auto=format&fit=crop" },
  { tag: "Social Enterprise", title: "Washing Machine Project", desc: "Market expansion strategy for a UK-based social enterprise providing affordable washing solutions.", impact: "Expansion Strategy", logo: "https://images.unsplash.com/photo-1582735689369-4fe89db7114c?q=80&w=600&auto=format&fit=crop" }
];"""

content = re.sub(r'export const PROJECTS = \[.*?\];', new_projects, content, flags=re.DOTALL)

with open('src/data.ts', 'w') as f:
    f.write(content)
print("Done")
