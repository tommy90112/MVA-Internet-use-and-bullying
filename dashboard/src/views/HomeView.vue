<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import gsap from 'gsap'
import { projectInfo, datasetStats, methodologies } from '../data/analysisData'

const router = useRouter()
const heroRef = ref(null)
const statsRef = ref(null)
const methodsRef = ref(null)

onMounted(() => {
  // Hero animation
  gsap.from('.hero-title', {
    y: 100,
    opacity: 0,
    duration: 1,
    ease: 'power4.out'
  })

  gsap.from('.hero-subtitle', {
    y: 50,
    opacity: 0,
    duration: 1,
    delay: 0.3,
    ease: 'power4.out'
  })

  gsap.from('.hero-description', {
    y: 30,
    opacity: 0,
    duration: 0.8,
    delay: 0.5,
    ease: 'power3.out'
  })

  gsap.from('.hero-buttons', {
    y: 30,
    opacity: 0,
    duration: 0.8,
    delay: 0.7,
    ease: 'power3.out'
  })

  gsap.from('.hero-stats', {
    scale: 0.8,
    opacity: 0,
    duration: 0.8,
    delay: 0.9,
    ease: 'back.out(1.7)'
  })
})

const navigateTo = (path) => {
  router.push(path)
}
</script>

<template>
  <div class="min-h-screen">
    <!-- Hero Section -->
    <section ref="heroRef" class="relative min-h-screen flex items-center justify-center px-4 overflow-hidden">
      <!-- Gradient orbs -->
      <div class="absolute top-1/4 left-1/4 w-96 h-96 bg-primary-500/30 rounded-full blur-3xl animate-pulse-slow" />
      <div class="absolute bottom-1/4 right-1/4 w-96 h-96 bg-purple-500/20 rounded-full blur-3xl animate-pulse-slow" style="animation-delay: 1s" />

      <div class="relative z-10 text-center max-w-5xl mx-auto">
        <!-- Badge -->
        <div class="hero-subtitle inline-flex items-center space-x-2 px-4 py-2 rounded-full bg-white/5 border border-white/10 mb-8">
          <span class="w-2 h-2 bg-green-400 rounded-full animate-pulse" />
          <span class="text-sm text-slate-300">{{ projectInfo.dataSource }}</span>
        </div>

        <!-- Title -->
        <h1 class="hero-title text-5xl md:text-7xl font-bold mb-6">
          <span class="text-white">網路霸凌傾向</span>
          <br />
          <span class="gradient-text">預測分析平台</span>
        </h1>

        <!-- Subtitle -->
        <p class="hero-description text-xl text-slate-400 mb-8 max-w-2xl mx-auto">
          {{ projectInfo.description }}
        </p>

        <!-- CTA Buttons -->
        <div class="hero-buttons flex flex-col sm:flex-row items-center justify-center gap-4 mb-12">
          <button
            @click="navigateTo('/overview')"
            class="px-8 py-4 bg-gradient-to-r from-primary-500 to-purple-500 rounded-xl
                   text-white font-semibold text-lg
                   hover:shadow-lg hover:shadow-primary-500/30 hover:scale-105
                   transition-all duration-300"
          >
            開始探索
            <span class="ml-2">→</span>
          </button>
          <button
            @click="navigateTo('/models')"
            class="glass-button text-lg"
          >
            查看 ML 模型
          </button>
        </div>

        <!-- Quick Stats -->
        <div class="hero-stats grid grid-cols-2 md:grid-cols-4 gap-4 max-w-3xl mx-auto">
          <div class="glass-card text-center">
            <div class="text-3xl font-bold gradient-text">{{ datasetStats.totalSamples }}</div>
            <div class="text-sm text-slate-400">樣本數</div>
          </div>
          <div class="glass-card text-center">
            <div class="text-3xl font-bold gradient-text">{{ datasetStats.totalFeatures }}</div>
            <div class="text-sm text-slate-400">特徵變數</div>
          </div>
          <div class="glass-card text-center">
            <div class="text-3xl font-bold gradient-text">5</div>
            <div class="text-sm text-slate-400">ML 模型</div>
          </div>
          <div class="glass-card text-center">
            <div class="text-3xl font-bold gradient-text">71%</div>
            <div class="text-sm text-slate-400">最佳 AUC</div>
          </div>
        </div>
      </div>

      <!-- Scroll indicator -->
      <div class="absolute bottom-8 left-1/2 -translate-x-1/2 animate-bounce">
        <svg class="w-6 h-6 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3" />
        </svg>
      </div>
    </section>

    <!-- Methodologies Section -->
    <section ref="methodsRef" class="py-24 px-4">
      <div class="max-w-6xl mx-auto">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-bold text-white mb-4">分析方法</h2>
          <p class="text-slate-400 max-w-2xl mx-auto">
            結合傳統統計方法與現代機器學習技術，全面分析網路霸凌傾向
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div
            v-for="(method, index) in methodologies"
            :key="method.name"
            class="glass-card group"
          >
            <div class="text-4xl mb-4">{{ method.icon }}</div>
            <h3 class="text-xl font-semibold text-white mb-2">{{ method.name }}</h3>
            <p class="text-slate-400 text-sm mb-4">{{ method.description }}</p>
            <div class="flex items-center space-x-2">
              <span class="w-2 h-2 bg-green-400 rounded-full" />
              <span class="text-xs text-green-400">已完成</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-24 px-4">
      <div class="max-w-4xl mx-auto text-center">
        <div class="glass p-12 relative overflow-hidden">
          <!-- Background gradient -->
          <div class="absolute inset-0 bg-gradient-to-r from-primary-500/10 to-purple-500/10" />

          <div class="relative z-10">
            <h2 class="text-3xl md:text-4xl font-bold text-white mb-4">
              準備好探索數據了嗎？
            </h2>
            <p class="text-slate-400 mb-8 max-w-xl mx-auto">
              深入了解網路行為與霸凌傾向的關聯，發現隱藏在數據中的洞見
            </p>
            <button
              @click="navigateTo('/overview')"
              class="px-8 py-4 bg-gradient-to-r from-primary-500 to-purple-500 rounded-xl
                     text-white font-semibold text-lg
                     hover:shadow-lg hover:shadow-primary-500/30 hover:scale-105
                     transition-all duration-300"
            >
              立即開始 →
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="py-12 px-4 border-t border-white/10">
      <div class="max-w-6xl mx-auto">
        <div class="flex flex-col md:flex-row items-center justify-between">
          <div class="text-center md:text-left mb-4 md:mb-0">
            <div class="text-white font-semibold">{{ projectInfo.author }}</div>
            <div class="text-sm text-slate-400">{{ projectInfo.institution }}</div>
          </div>
          <div class="text-sm text-slate-400">
            資料來源：{{ projectInfo.dataSource }}
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>
