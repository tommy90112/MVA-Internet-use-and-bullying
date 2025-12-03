<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const canvasRef = ref(null)
let animationId = null
let particles = []

class Particle {
  constructor(canvas) {
    this.canvas = canvas
    this.reset()
  }

  reset() {
    this.x = Math.random() * this.canvas.width
    this.y = Math.random() * this.canvas.height
    this.size = Math.random() * 2 + 1
    this.speedX = (Math.random() - 0.5) * 0.5
    this.speedY = (Math.random() - 0.5) * 0.5
    this.opacity = Math.random() * 0.5 + 0.2
  }

  update() {
    this.x += this.speedX
    this.y += this.speedY

    if (this.x < 0 || this.x > this.canvas.width) this.speedX *= -1
    if (this.y < 0 || this.y > this.canvas.height) this.speedY *= -1
  }

  draw(ctx) {
    ctx.beginPath()
    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2)
    ctx.fillStyle = `rgba(14, 165, 233, ${this.opacity})`
    ctx.fill()
  }
}

const initCanvas = () => {
  const canvas = canvasRef.value
  if (!canvas) return

  const ctx = canvas.getContext('2d')

  const resize = () => {
    canvas.width = window.innerWidth
    canvas.height = window.innerHeight
  }

  resize()
  window.addEventListener('resize', resize)

  // Create particles
  particles = []
  for (let i = 0; i < 80; i++) {
    particles.push(new Particle(canvas))
  }

  const animate = () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    // Draw connections
    particles.forEach((particle, i) => {
      particles.slice(i + 1).forEach(otherParticle => {
        const dx = particle.x - otherParticle.x
        const dy = particle.y - otherParticle.y
        const distance = Math.sqrt(dx * dx + dy * dy)

        if (distance < 150) {
          ctx.beginPath()
          ctx.moveTo(particle.x, particle.y)
          ctx.lineTo(otherParticle.x, otherParticle.y)
          ctx.strokeStyle = `rgba(14, 165, 233, ${0.1 * (1 - distance / 150)})`
          ctx.lineWidth = 0.5
          ctx.stroke()
        }
      })
    })

    // Update and draw particles
    particles.forEach(particle => {
      particle.update()
      particle.draw(ctx)
    })

    animationId = requestAnimationFrame(animate)
  }

  animate()
}

onMounted(() => {
  initCanvas()
})

onUnmounted(() => {
  if (animationId) {
    cancelAnimationFrame(animationId)
  }
})
</script>

<template>
  <canvas
    ref="canvasRef"
    class="fixed top-0 left-0 w-full h-full pointer-events-none z-0"
  />
</template>
