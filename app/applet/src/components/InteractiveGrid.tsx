import { useEffect, useRef } from 'react';

export default function InteractiveGrid() {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let width: number, height: number;
    let points: Point[] = [];
    const spacing = 45; 
    
    // mouse.radius controls the physical push, fadeRadius controls the transparency glow
    const mouse = { x: null as number | null, y: null as number | null, radius: 120, fadeRadius: 250 };

    function resize() {
      if (!canvas) return;
      width = window.innerWidth;
      height = window.innerHeight;
      canvas.width = width;
      canvas.height = height;
      initGrid();
    }

    class Point {
      x: number;
      y: number;
      originX: number;
      originY: number;
      vx: number;
      vy: number;
      alpha: number;
      friction: number;
      spring: number;

      constructor(x: number, y: number) {
        this.x = x;
        this.y = y;
        this.originX = x;
        this.originY = y;
        this.vx = 0;
        this.vy = 0;
        this.alpha = 0.15; // Base transparency
        
        this.friction = 0.82;
        this.spring = 0.08;
      }

      update() {
        let dx = this.originX - this.x;
        let dy = this.originY - this.y;

        // Spring physics pulling back to origin
        this.vx += dx * this.spring;
        this.vy += dy * this.spring;

        // Default alpha when mouse is away
        this.alpha = 0.15; 

        if (mouse.x !== null && mouse.y !== null) {
          let distX = this.x - mouse.x;
          let distY = this.y - mouse.y;
          let distance = Math.sqrt(distX * distX + distY * distY);

          // --- Transparency Logic ---
          if (distance < mouse.fadeRadius) {
            // Calculate how close the mouse is as a ratio (0 to 1)
            let distanceRatio = 1 - (distance / mouse.fadeRadius);
            // Increase alpha based on proximity (peaks at 0.8)
            this.alpha = 0.15 + (distanceRatio * 0.65);
          }

          // --- Physics Logic ---
          if (distance < mouse.radius) {
            let force = (mouse.radius - distance) / mouse.radius;
            this.vx += (distX / distance) * force * 3;
            this.vy += (distY / distance) * force * 3;
          }
        }

        // Apply friction
        this.vx *= this.friction;
        this.vy *= this.friction;

        // Update position
        this.x += this.vx;
        this.y += this.vy;
      }

      draw() {
        if (!ctx) return;
        ctx.beginPath();
        ctx.arc(this.x, this.y, 2, 0, Math.PI * 2);
        // Apply the dynamic alpha calculated in the update phase
        ctx.fillStyle = `rgba(145, 143, 138, ${this.alpha})`;
        ctx.fill();
      }
    }

    function initGrid() {
      points = [];
      for (let x = -spacing; x < width + spacing; x += spacing) {
        for (let y = -spacing; y < height + spacing; y += spacing) {
          points.push(new Point(x, y));
        }
      }
    }

    let animationFrameId: number;

    function animate() {
      if (!ctx) return;
      ctx.clearRect(0, 0, width, height);

      points.forEach(point => {
        point.update();
        point.draw();
      });

      animationFrameId = requestAnimationFrame(animate);
    }

    window.addEventListener('resize', resize);

    const handleMouseMove = (e: MouseEvent) => {
      mouse.x = e.clientX;
      mouse.y = e.clientY;
    };

    const handleMouseOut = () => {
      mouse.x = null;
      mouse.y = null;
    };

    window.addEventListener('mousemove', handleMouseMove);
    window.addEventListener('mouseout', handleMouseOut);

    resize();
    animate();

    return () => {
      window.removeEventListener('resize', resize);
      window.removeEventListener('mousemove', handleMouseMove);
      window.removeEventListener('mouseout', handleMouseOut);
      cancelAnimationFrame(animationFrameId);
    };
  }, []);

  return (
    <canvas 
      ref={canvasRef} 
      className="fixed inset-0 w-full h-full pointer-events-none z-0" 
    />
  );
}
