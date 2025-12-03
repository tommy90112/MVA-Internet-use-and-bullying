<script setup>
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import gsap from 'gsap'

const route = useRoute()
const router = useRouter()
const isMenuOpen = ref(false)

const navItems = [
  { path: '/', label: '首頁', icon: '🏠' },
  { path: '/overview', label: '資料概覽', icon: '📊' },
  { path: '/models', label: 'ML 模型', icon: '🤖' },
  { path: '/clusters', label: '聚類分析', icon: '👥' },
  { path: '/features', label: '特徵分析', icon: '🎯' },
  { path: '/findings', label: '研究發現', icon: '💡' }
]

const isActive = (path) => route.path === path

const navigateTo = (path) => {
  router.push(path)
  isMenuOpen.value = false
}

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}
</script>

<template>
  <nav class="fixed top-0 left-0 right-0 z-50 glass border-b border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <!-- Logo -->
        <div
          class="flex items-center space-x-3 cursor-pointer group"
          @click="navigateTo('/')"
        >
          <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-primary-500 to-purple-500
                      flex items-center justify-center text-white font-bold text-lg
                      group-hover:scale-110 transition-transform duration-300">
            CB
          </div>
          <div class="hidden sm:block">
            <div class="text-white font-semibold">網路霸凌分析</div>
            <div class="text-xs text-slate-400">Cyberbullying Analysis</div>
          </div>
        </div>

        <!-- Desktop Navigation -->
        <div class="hidden md:flex items-center space-x-1">
          <button
            v-for="item in navItems"
            :key="item.path"
            @click="navigateTo(item.path)"
            :class="[
              'nav-link flex items-center space-x-2 rounded-lg',
              isActive(item.path) ? 'active bg-white/10 text-primary-400' : ''
            ]"
          >
            <span>{{ item.icon }}</span>
            <span>{{ item.label }}</span>
          </button>
        </div>

        <!-- GitHub Link -->
        <div class="hidden md:flex items-center space-x-4">
          <a
            href="https://github.com"
            target="_blank"
            class="glass-button px-4 py-2 text-sm flex items-center space-x-2"
          >
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
            </svg>
            <span>GitHub</span>
          </a>
        </div>

        <!-- Mobile Menu Button -->
        <button
          @click="toggleMenu"
          class="md:hidden p-2 rounded-lg text-slate-400 hover:text-white hover:bg-white/10 transition-colors"
        >
          <svg v-if="!isMenuOpen" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
          </svg>
          <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>
      </div>
    </div>

    <!-- Mobile Menu -->
    <Transition
      enter-active-class="transition-all duration-300 ease-out"
      enter-from-class="opacity-0 -translate-y-4"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition-all duration-200 ease-in"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-4"
    >
      <div v-if="isMenuOpen" class="md:hidden glass border-t border-white/10">
        <div class="px-4 py-4 space-y-2">
          <button
            v-for="item in navItems"
            :key="item.path"
            @click="navigateTo(item.path)"
            :class="[
              'w-full flex items-center space-x-3 px-4 py-3 rounded-xl transition-colors',
              isActive(item.path)
                ? 'bg-primary-500/20 text-primary-400'
                : 'text-slate-300 hover:bg-white/10'
            ]"
          >
            <span class="text-xl">{{ item.icon }}</span>
            <span>{{ item.label }}</span>
          </button>
        </div>
      </div>
    </Transition>
  </nav>
</template>
