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
import InteractiveGrid from './components/InteractiveGrid';

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
    <div className="min-h-screen flex flex-col selection:bg-[#86BC2A] selection:text-white relative bg-[#FDFCF8] text-[#0F0F0F] cursor-crosshair">
      <CustomCursor />
      
      {/* Interactive Grid Background */}
      <InteractiveGrid />

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
        {currentPage !== 'Projects' && (
          <div className="px-6 md:px-16 lg:px-24 xl:px-32">
            <Footer onNavigate={setCurrentPage} />
          </div>
        )}
      </div>
    </div>
  );
}
