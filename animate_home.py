with open('src/pages/Home.tsx', 'r') as f:
    content = f.read()

# Make sure framer-motion is imported
if "import { motion } from 'motion/react';" not in content:
    content = content.replace("import { STATS", "import { motion } from 'motion/react';\nimport { STATS")

# Hero Section
content = content.replace(
    '<div className="flex-1 flex flex-col justify-center">',
    '''<motion.div 
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
          className="flex-1 flex flex-col justify-center"
        >'''
)
content = content.replace(
    '<div className="mb-8 flex items-center gap-4">',
    '''<motion.div 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.2, duration: 0.6 }}
            className="mb-8 flex items-center gap-4"
          >'''
)
# End of mb-8 flex
content = content.replace(
    '</span>\n          </div>',
    '</span>\n          </motion.div>'
)

content = content.replace(
    '<p className="text-xs',
    '''<motion.p 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.4, duration: 0.6 }}
            className="text-xs'''
)
content = content.replace(
    'they face.\n          </p>',
    'they face.\n          </motion.p>'
)

content = content.replace(
    '<div className="flex flex-wrap gap-6 items-center">',
    '''<motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.6, duration: 0.6 }}
            className="flex flex-wrap gap-6 items-center"
          >'''
)
content = content.replace(
    'Our Services\n            </button>\n          </div>\n        </div>',
    'Our Services\n            </button>\n          </motion.div>\n        </motion.div>'
)

content = content.replace(
    '<div className="w-full lg:w-1/3 flex flex-col justify-end border-l-2 border-gray-200 pl-8 py-8 relative">',
    '''<motion.div 
          initial={{ opacity: 0, x: 30 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.4, duration: 0.8, ease: "easeOut" }}
          className="w-full lg:w-1/3 flex flex-col justify-end border-l-2 border-gray-200 pl-8 py-8 relative"
        >'''
)
content = content.replace(
    '</div>\n             ))}\n           </div>\n        </div>\n      </section>',
    '</div>\n             ))}\n           </div>\n        </motion.div>\n      </section>'
)

# Three Cards
content = content.replace(
    '<div \n            key={card.title}',
    '''<motion.div 
            initial={{ opacity: 0, y: 50 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-100px" }}
            transition={{ duration: 0.5, delay: i * 0.1 }}
            key={card.title}'''
)
content = content.replace(
    '<h3 className="text-3xl font-black uppercase tracking-tighter mt-auto text-black">{card.title}</h3>\n          </div>',
    '<h3 className="text-3xl font-black uppercase tracking-tighter mt-auto text-black">{card.title}</h3>\n          </motion.div>'
)

# Blogs Section
content = content.replace(
    '<div className="flex flex-col md:flex-row md:justify-between md:items-end gap-6 mb-12">',
    '''<motion.div 
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-100px" }}
          transition={{ duration: 0.6 }}
          className="flex flex-col md:flex-row md:justify-between md:items-end gap-6 mb-12"
        >'''
)
content = content.replace(
    'All Articles</a>\n        </div>',
    'All Articles</a>\n        </motion.div>'
)

content = content.replace(
    '<a key={i} href={post.link}',
    '''<motion.a 
              initial={{ opacity: 0, y: 50 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-50px" }}
              transition={{ duration: 0.5, delay: i * 0.1 }}
              key={i} href={post.link}'''
)
content = content.replace(
    '</p>\n            </a>',
    '</p>\n            </motion.a>'
)

# Closing CTA
content = content.replace(
    '<section className="border border-gray-200 bg-gray-50 p-16 md:p-32 text-center flex flex-col items-center group hover:border-[#86BC2A] transition-colors shadow-sm">',
    '''<motion.section 
        initial={{ opacity: 0, scale: 0.95 }}
        whileInView={{ opacity: 1, scale: 1 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.6 }}
        className="border border-gray-200 bg-gray-50 p-16 md:p-32 text-center flex flex-col items-center group hover:border-[#86BC2A] transition-colors shadow-sm"
      >'''
)
content = content.replace(
    '</button>\n      </section>\n    </div>',
    '</button>\n      </motion.section>\n    </div>'
)

with open('src/pages/Home.tsx', 'w') as f:
    f.write(content)
print("Done Home")
