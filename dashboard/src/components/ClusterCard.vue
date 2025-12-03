<script setup>
import { ref, computed, onMounted } from 'vue'
import gsap from 'gsap'

const props = defineProps({
  cluster: { type: Object, required: true },
  index: { type: Number, default: 0 }
})

const cardRef = ref(null)
const isExpanded = ref(false)

const riskClasses = {
  low: 'from-green-500 to-green-600',
  medium: 'from-yellow-500 to-yellow-600',
  high: 'from-red-500 to-red-600'
}

const riskLabels = {
  low: '低風險',
  medium: '中風險',
  high: '高風險'
}

onMounted(() => {
  gsap.from(cardRef.value, {
    y: 50,
    opacity: 0,
    duration: 0.6,
    delay: props.index * 0.15,
    ease: 'power3.out'
  })
})

const toggleExpand = () => {
  isExpanded.value = !isExpanded.value
}
</script>

<template>
  <div
    ref="cardRef"
    @click="toggleExpand"
    class="glass-card cursor-pointer group relative overflow-hidden"
  >
    <!-- Risk indicator bar -->
    <div
      :class="[
        'absolute top-0 left-0 right-0 h-1 bg-gradient-to-r',
        riskClasses[cluster.riskLevel]
      ]"
    />

    <div class="pt-2">
      <!-- Header -->
      <div class="flex items-start justify-between mb-4">
        <div>
          <div class="flex items-center space-x-2 mb-1">
            <span
              class="w-4 h-4 rounded-full"
              :style="{ backgroundColor: cluster.color }"
            />
            <h3 class="text-lg font-semibold text-white">{{ cluster.label }}</h3>
          </div>
          <span
            :class="[
              'inline-block px-2 py-0.5 text-xs rounded-full bg-gradient-to-r text-white',
              riskClasses[cluster.riskLevel]
            ]"
          >
            {{ riskLabels[cluster.riskLevel] }}
          </span>
        </div>
        <div class="text-right">
          <div class="text-2xl font-bold text-white">{{ cluster.size }}</div>
          <div class="text-xs text-slate-400">{{ cluster.percentage }}%</div>
        </div>
      </div>

      <!-- Stats Grid -->
      <div class="grid grid-cols-2 gap-3 mb-4">
        <div class="bg-white/5 rounded-lg p-3">
          <div class="text-xs text-slate-400 mb-1">霸凌分數</div>
          <div class="text-lg font-semibold text-white">{{ cluster.meanScore.toFixed(1) }}</div>
        </div>
        <div class="bg-white/5 rounded-lg p-3">
          <div class="text-xs text-slate-400 mb-1">平均年齡</div>
          <div class="text-lg font-semibold text-white">{{ cluster.meanAge }}歲</div>
        </div>
        <div class="bg-white/5 rounded-lg p-3">
          <div class="text-xs text-slate-400 mb-1">女性比例</div>
          <div class="text-lg font-semibold text-white">{{ cluster.femaleRatio }}%</div>
        </div>
        <div class="bg-white/5 rounded-lg p-3">
          <div class="text-xs text-slate-400 mb-1">上網時間</div>
          <div class="text-lg font-semibold text-white">{{ cluster.internetHours }}hr</div>
        </div>
      </div>

      <!-- Expandable Description -->
      <Transition
        enter-active-class="transition-all duration-300"
        enter-from-class="opacity-0 max-h-0"
        enter-to-class="opacity-100 max-h-40"
        leave-active-class="transition-all duration-200"
        leave-from-class="opacity-100 max-h-40"
        leave-to-class="opacity-0 max-h-0"
      >
        <div v-if="isExpanded" class="overflow-hidden">
          <div class="pt-4 border-t border-white/10">
            <p class="text-sm text-slate-300">{{ cluster.description }}</p>
          </div>
        </div>
      </Transition>

      <!-- Expand indicator -->
      <div class="flex justify-center mt-2">
        <svg
          :class="[
            'w-5 h-5 text-slate-500 transition-transform duration-300',
            isExpanded ? 'rotate-180' : ''
          ]"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
        </svg>
      </div>
    </div>

    <!-- Hover glow -->
    <div
      class="absolute -inset-1 rounded-2xl opacity-0 group-hover:opacity-30 transition-opacity duration-500 blur-xl"
      :style="{ backgroundColor: cluster.color }"
    />
  </div>
</template>
