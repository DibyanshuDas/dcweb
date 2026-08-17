import re

with open('src/data.ts', 'r') as f:
    content = f.read()

new_projects = """export const PROJECTS = [
  { tag: "Education • NGO", title: "Learning Outcomes", desc: "M&E framework enabling data-driven improvements across 200+ schools in rural West Bengal.", quote: "Rigour on par with any boutique consulting firm.", author: "Programme Director", year: "2023", impact: "Impacting 200+ schools", logo: "https://ui-avatars.com/api/?name=LO&background=E8E8E8&color=333" },
  { tag: "Agriculture • Social Enterprise", title: "Farmer Strategy", desc: "Go-to-market strategy for an agri-enterprise expanding into four districts of Andhra Pradesh.", quote: "Saved us months of guesswork. We launched with confidence.", author: "Founder, Guntur Impact Fund", year: "2022", impact: "4 Districts expanded", logo: "https://ui-avatars.com/api/?name=FS&background=E8E8E8&color=333" },
  { tag: "Government • MP", title: "Tax Process Opt.", desc: "Operations consulting for MP Government's Department of Commercial Tax — streamlining taxpayer processes.", year: "2021", impact: "Streamlined processes", logo: "https://ui-avatars.com/api/?name=MP&background=E8E8E8&color=333" },
  { tag: "Technology • USA", title: "Trumio AI GTM", desc: "Go-to-market strategy for an AI-based workplace platform in San Francisco — US market entry.", year: "2023", impact: "US Market Entry", logo: "https://ui-avatars.com/api/?name=TR&background=E8E8E8&color=333" },
  { tag: "Social Enterprise • UK", title: "Washing Project", desc: "Market expansion strategy for a UK-based social enterprise providing affordable washing solutions.", year: "2022", impact: "Affordable solutions", logo: "https://ui-avatars.com/api/?name=TW&background=E8E8E8&color=333" },
  { tag: "Agriculture • Singapore", title: "Soil Regen", desc: "Research and expansion strategy for a Singapore-based agriculture social enterprise.", year: "2021", impact: "Global Expansion", logo: "https://ui-avatars.com/api/?name=SR&background=E8E8E8&color=333" }
];"""

content = re.sub(r'export const PROJECTS = \[.*?\];', new_projects, content, flags=re.DOTALL)

with open('src/data.ts', 'w') as f:
    f.write(content)
print("Done")
