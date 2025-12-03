import { ref, onMounted, onUnmounted } from 'vue'
import gsap from 'gsap'

// 數字動畫 Hook
export function useCountUp(targetValue, duration = 2, decimals = 0) {
  const displayValue = ref(0)

  const animate = () => {
    gsap.to(displayValue, {
      value: targetValue,
      duration,
      ease: 'power2.out',
      onUpdate: () => {
        displayValue.value = Number(displayValue.value.toFixed(decimals))
      }
    })
  }

  return { displayValue, animate }
}

// 滾動觸發動畫 Hook
export function useScrollAnimation() {
  const isVisible = ref(false)
  const elementRef = ref(null)

  let observer = null

  onMounted(() => {
    observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            isVisible.value = true
          }
        })
      },
      { threshold: 0.1 }
    )

    if (elementRef.value) {
      observer.observe(elementRef.value)
    }
  })

  onUnmounted(() => {
    if (observer) {
      observer.disconnect()
    }
  })

  return { isVisible, elementRef }
}

// 進場動畫 Hook
export function useEnterAnimation(selector, options = {}) {
  const {
    y = 50,
    opacity = 0,
    duration = 0.8,
    stagger = 0.1,
    ease = 'power3.out',
    delay = 0
  } = options

  onMounted(() => {
    gsap.from(selector, {
      y,
      opacity,
      duration,
      stagger,
      ease,
      delay
    })
  })
}

// 懸浮動畫 Hook
export function useHoverAnimation() {
  const onMouseEnter = (el) => {
    gsap.to(el, {
      scale: 1.05,
      duration: 0.3,
      ease: 'power2.out'
    })
  }

  const onMouseLeave = (el) => {
    gsap.to(el, {
      scale: 1,
      duration: 0.3,
      ease: 'power2.out'
    })
  }

  return { onMouseEnter, onMouseLeave }
}

// 粒子背景動畫
export function useParticles(containerRef, count = 50) {
  const particles = ref([])

  onMounted(() => {
    for (let i = 0; i < count; i++) {
      particles.value.push({
        id: i,
        x: Math.random() * 100,
        y: Math.random() * 100,
        size: Math.random() * 4 + 2,
        duration: Math.random() * 20 + 10,
        delay: Math.random() * 10
      })
    }
  })

  return { particles }
}

// 打字機效果
export function useTypewriter(text, speed = 50) {
  const displayText = ref('')
  const isComplete = ref(false)

  const start = () => {
    let i = 0
    displayText.value = ''
    isComplete.value = false

    const timer = setInterval(() => {
      if (i < text.length) {
        displayText.value += text.charAt(i)
        i++
      } else {
        clearInterval(timer)
        isComplete.value = true
      }
    }, speed)
  }

  return { displayText, isComplete, start }
}

// 波浪動畫數據生成
export function useWaveData(points = 100, amplitude = 20, frequency = 0.02) {
  const data = ref([])
  let animationFrame = null
  let offset = 0

  const generateWave = () => {
    const newData = []
    for (let i = 0; i < points; i++) {
      newData.push({
        x: i,
        y: Math.sin((i + offset) * frequency) * amplitude + 50
      })
    }
    data.value = newData
    offset += 2
    animationFrame = requestAnimationFrame(generateWave)
  }

  onMounted(() => {
    generateWave()
  })

  onUnmounted(() => {
    if (animationFrame) {
      cancelAnimationFrame(animationFrame)
    }
  })

  return { data }
}
