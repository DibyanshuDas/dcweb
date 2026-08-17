import re

with open('src/data.ts', 'r') as f:
    content = f.read()

new_projects = """export const PROJECTS = [
  { tag: "Education • NGO", title: "Learning Outcomes", desc: "M&E framework enabling data-driven improvements across 200+ schools in rural West Bengal.", quote: "Rigour on par with any boutique consulting firm.", author: "Programme Director", year: "2023", impact: "Impacting 200+ schools", logo: "https://images.unsplash.com/photo-1577896851231-70ef18881754?q=80&w=600&auto=format&fit=crop" },
  { tag: "Agriculture • Social Enterprise", title: "Farmer Strategy", desc: "Go-to-market strategy for an agri-enterprise expanding into four districts of Andhra Pradesh.", quote: "Saved us months of guesswork. We launched with confidence.", author: "Founder, Guntur Impact Fund", year: "2022", impact: "4 Districts expanded", logo: "https://images.unsplash.com/photo-1595841696677-6489ff3f8cd1?q=80&w=600&auto=format&fit=crop" },
  { tag: "Government • MP", title: "Tax Process Opt.", desc: "Operations consulting for MP Government's Department of Commercial Tax — streamlining taxpayer processes.", year: "2021", impact: "Streamlined processes", logo: "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?q=80&w=600&auto=format&fit=crop" },
  { tag: "Technology • USA", title: "Trumio AI GTM", desc: "Go-to-market strategy for an AI-based workplace platform in San Francisco — US market entry.", year: "2023", impact: "US Market Entry", logo: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=600&auto=format&fit=crop" },
  { tag: "Social Enterprise • UK", title: "Washing Project", desc: "Market expansion strategy for a UK-based social enterprise providing affordable washing solutions.", year: "2022", impact: "Affordable solutions", logo: "https://images.unsplash.com/photo-1582735689369-4fe89db7114c?q=80&w=600&auto=format&fit=crop" },
  { tag: "Agriculture • Singapore", title: "Soil Regen", desc: "Research and expansion strategy for a Singapore-based agriculture social enterprise.", year: "2021", impact: "Global Expansion", logo: "https://images.unsplash.com/photo-1464226184884-fa280b87c399?q=80&w=600&auto=format&fit=crop" }
];"""

content = re.sub(r'export const PROJECTS = \[.*?\];', new_projects, content, flags=re.DOTALL)

with open('src/data.ts', 'w') as f:
    f.write(content)
print("Done")
