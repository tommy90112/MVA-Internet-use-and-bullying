<script setup>
import { ref, onMounted, watch } from 'vue'
import gsap from 'gsap'

const props = defineProps({
  value: { type: [Number, String], required: true },
  label: { type: String, required: true },
  icon: { type: String, default: '📊' },
  suffix: { type: String, default: '' },
  prefix: { type: String, default: '' },
  decimals: { type: Number, default: 0 },
  color: { type: String, default: 'primary' },
  delay: { type: Number, default: 0 }
})

const displayValue = ref(0)
const cardRef = ref(null)

const colorClasses = {
  primary: 'from-primary-500 to-primary-600',
  green: 'from-green-500 to-green-600',
  purple: 'from-purple-500 to-purple-600',
  orange: 'from-orange-500 to-orange-600',
  red: 'from-red-500 to-red-600'
}

onMounted(() => {
  // Animate card entrance
  gsap.from(cardRef.value, {
    y: 30,
    opacity: 0,
    duration: 0.6,
    delay: props.delay,
    ease: 'power3.out'
  })

  // Animate number
  if (typeof props.value === 'number') {
    gsap.to(displayValue, {
      value: props.value,
      duration: 2,
      delay: props.delay + 0.3,
      ease: 'power2.out'
    })
  } else {
    displayValue.value = props.value
  }
})

watch(() => props.value, (newValue) => {
  if (typeof newValue === 'number') {
    gsap.to(displayValue, {
      value: newValue,
      duration: 1,
      ease: 'power2.out'
    })
  }
})
</script>

<template>
  <div
    ref="cardRef"
    class="stat-card group cursor-pointer"
  >
    <!-- Icon -->
    <div
      :class="[
        'w-12 h-12 rounded-xl flex items-center justify-center text-2xl mb-4',
        'bg-gradient-to-br',
        colorClasses[color]
      ]"
    >
      {{ icon }}
    </div>

    <!-- Value -->
    <div class="text-3xl font-bold text-white mb-2 counter">
      {{ prefix }}{{ typeof value === 'number' ? displayValue.toFixed(decimals) : displayValue }}{{ suffix }}
    </div>

    <!-- Label -->
    <div class="text-slate-400 text-sm">{{ label }}</div>

    <!-- Hover glow effect -->
    <div
      :class="[
        'absolute -inset-1 rounded-2xl opacity-0 group-hover:opacity-20 transition-opacity duration-500 blur-xl',
        'bg-gradient-to-br',
        colorClasses[color]
      ]"
    />
  </div>
</template>
