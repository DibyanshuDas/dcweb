with open('src/App.tsx', 'r') as f:
    content = f.read()

import re

# We want to conditionally render the Footer based on currentPage.
# Find: <div className="px-6 md:px-16 lg:px-24 xl:px-32">\n          <Footer onNavigate={setCurrentPage} />\n        </div>
# Replace with: {currentPage !== 'Projects' && (\n          <div className="px-6 md:px-16 lg:px-24 xl:px-32">\n            <Footer onNavigate={setCurrentPage} />\n          </div>\n        )}

old_footer = r'<div className="px-6 md:px-16 lg:px-24 xl:px-32">\s*<Footer onNavigate=\{setCurrentPage\} />\s*</div>'
new_footer = "{currentPage !== 'Projects' && (\\n          <div className=\"px-6 md:px-16 lg:px-24 xl:px-32\">\\n            <Footer onNavigate={setCurrentPage} />\\n          </div>\\n        )}"

content = re.sub(old_footer, new_footer, content)

with open('src/App.tsx', 'w') as f:
    f.write(content)
print("Done")
