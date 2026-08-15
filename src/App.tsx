/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import Home from './pages/Home';
import About from './pages/About';
import Services from './pages/Services';
import Projects from './pages/Projects';
import Team from './pages/Team';
import Contact from './pages/Contact';
import Resources from './pages/Resources';
import Navigation from './components/Navigation';
import Footer from './components/Footer';
import CustomCursor from './components/CustomCursor';

export default function App() {
  const [currentPage, setCurrentPage] = useState('Home');

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [currentPage]);

  const renderPage = () => {
    switch (currentPage) {
      case 'Home': return <Home onNavigate={setCurrentPage} />;
      case 'About': return <About onNavigate={setCurrentPage} />;
      case 'Services': return <Services />;
      case 'Projects': return <Projects />;
      case 'Team': return <Team />;
      case 'Contact': return <Contact />;
      case 'Resources': return <Resources />;
      default: return <Home onNavigate={setCurrentPage} />;
    }
  };

  return (
    <div className="min-h-screen flex flex-col selection:bg-[#86BC2A] selection:text-white relative bg-[#FDFCF8] text-[#0F0F0F]">
      <CustomCursor />
      
      {/* Warm Ivory Paper Background & Art Direction */}
      <div className="fixed inset-0 pointer-events-none z-0 overflow-hidden">
        {/* Subtle Gray Dot Grid */}
        <div className="absolute inset-0 bg-[radial-gradient(#d1d5db_1px,transparent_1px)] [background-size:32px_32px] opacity-40"></div>
        
        {/* Faint Dashed Bézier Curves */}
        <svg className="absolute w-full h-full opacity-30" preserveAspectRatio="none" viewBox="0 0 1440 800" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M-100 800C200 500 400 200 800 100C1200 0 1400 300 1600 -100" stroke="#9ca3af" strokeWidth="1" strokeDasharray="4 8" fill="none" />
          <path d="M-200 600C100 800 600 400 1000 500C1400 600 1300 200 1500 0" stroke="#9ca3af" strokeWidth="1" strokeDasharray="4 8" fill="none" />
          <path d="M0 1000C400 800 600 900 1000 600C1400 300 1200 -100 1600 -200" stroke="#9ca3af" strokeWidth="1" strokeDasharray="4 8" fill="none" />
        </svg>
      </div>

      <div className="w-full flex-1 flex flex-col relative z-10">
        <Navigation currentPage={currentPage} onNavigate={setCurrentPage} />
        <main className="flex-1 overflow-x-hidden">
          <AnimatePresence mode="wait">
            <motion.div
              key={currentPage}
              initial={{ opacity: 0, y: 15 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -15 }}
              transition={{ duration: 0.3, ease: "easeInOut" }}
            >
              {renderPage()}
            </motion.div>
          </AnimatePresence>
        </main>
        <div className="px-6 md:px-16 lg:px-24 xl:px-32">
          <Footer onNavigate={setCurrentPage} />
        </div>
      </div>
    </div>
  );
}
