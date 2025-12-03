<script setup>
import { ref, onMounted } from 'vue'
import FeatureImportanceChart from '../components/Charts/FeatureImportanceChart.vue'
import { featureImportance } from '../data/analysisData'
import * as echarts from 'echarts'
import gsap from 'gsap'

const radarChartRef = ref(null)

const featureDetails = [
  {
    name: '出生年（年齡）',
    importance: 39.66,
    description: '年輕人霸凌傾向顯著較高，可能與網路使用習慣和社會化程度有關',
    direction: '負相關',
    icon: '🎂',
    color: '#3b82f6'
  },
  {
    name: '每日上網時間',
    importance: 17.04,
    description: '上網時間越長，接觸網路負面內容的機會越多，霸凌傾向越高',
    direction: '正相關',
    icon: '⏰',
    color: '#10b981'
  },
  {
    name: '居住地區',
    importance: 14.16,
    description: '不同地區的網路文化和社會環境可能影響使用者行為',
    direction: '複雜',
    icon: '📍',
    color: '#8b5cf6'
  },
  {
    name: '社會焦慮',
    importance: 11.79,
    description: '社會焦慮程度高者可能透過網路霸凌獲取控制感或發洩情緒',
    direction: '正相關',
    icon: '😰',
    color: '#f59e0b'
  },
  {
    name: '教育程度',
    importance: 10.63,
    description: '教育可能影響對網路行為後果的認知和自我調節能力',
    direction: '複雜',
    icon: '🎓',
    color: '#ec4899'
  },
  {
    name: '性別',
    importance: 6.72,
    description: '男性群組平均霸凌傾向較高，可能與社會化和表達方式有關',
    direction: '男性較高',
    icon: '👤',
    color: '#06b6d4'
  }
]

onMounted(() => {
  // Radar Chart
  const chart = echarts.init(radarChartRef.value, 'dark')

  chart.setOption({
    backgroundColor: 'transparent',
    radar: {
      indicator: featureDetails.map(f => ({
        name: f.name.replace('（', '\n(').replace('）', ')'),
        max: 50
      })),
      shape: 'polygon',
      splitNumber: 4,
      axisName: {
        color: '#94a3b8',
        fontSize: 11
      },
      splitLine: {
        lineStyle: { color: 'rgba(255,255,255,0.1)' }
      },
      splitArea: {
        show: true,
        areaStyle: {
          color: ['rgba(14, 165, 233, 0.05)', 'rgba(14, 165, 233, 0.1)']
        }
      },
      axisLine: {
        lineStyle: { color: 'rgba(255,255,255,0.1)' }
      }
    },
    series: [{
      type: 'radar',
      data: [{
        value: featureDetails.map(f => f.importance),
        name: '特徵重要性',
        areaStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: 'rgba(14, 165, 233, 0.6)' },
            { offset: 1, color: 'rgba(139, 92, 246, 0.6)' }
          ])
        },
        lineStyle: {
          color: '#0ea5e9',
          width: 2
        },
        symbol: 'circle',
        symbolSize: 8,
        itemStyle: {
          color: '#fff',
          borderColor: '#0ea5e9',
          borderWidth: 2
        }
      }],
      animationDuration: 2000
    }]
  })

  window.addEventListener('resize', () => chart.resize())

  // Animate feature cards
  gsap.from('.feature-card', {
    y: 30,
    opacity: 0,
    duration: 0.6,
    stagger: 0.1,
    ease: 'power3.out',
    delay: 0.3
  })
})
</script>

<template>
  <div class="min-h-screen pt-20 pb-12 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- Header -->
      <div class="mb-12">
        <h1 class="text-4xl font-bold text-white mb-4">特徵重要性分析</h1>
        <p class="text-slate-400 max-w-2xl">
          了解哪些因素對預測網路霸凌傾向最具影響力
        </p>
      </div>

      <!-- Charts Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-12">
        <FeatureImportanceChart />

        <!-- Radar Chart -->
        <div class="chart-container">
          <h3 class="text-lg font-semibold text-white mb-4">特徵雷達圖</h3>
          <div ref="radarChartRef" class="w-full h-80"></div>
        </div>
      </div>

      <!-- Feature Details -->
      <div class="mb-12">
        <h2 class="text-2xl font-bold text-white mb-6">特徵詳細解釋</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div
            v-for="(feature, index) in featureDetails"
            :key="feature.name"
            class="feature-card glass-card group"
          >
            <!-- Header -->
            <div class="flex items-start justify-between mb-4">
              <div class="flex items-center space-x-3">
                <div
                  class="w-12 h-12 rounded-xl flex items-center justify-center text-2xl"
                  :style="{ backgroundColor: feature.color + '20' }"
                >
                  {{ feature.icon }}
                </div>
                <div>
                  <h3 class="font-semibold text-white">{{ feature.name }}</h3>
                  <span
                    class="text-xs px-2 py-0.5 rounded-full"
                    :style="{ backgroundColor: feature.color + '30', color: feature.color }"
                  >
                    {{ feature.direction }}
                  </span>
                </div>
              </div>
            </div>

            <!-- Progress Bar -->
            <div class="mb-4">
              <div class="flex justify-between text-sm mb-1">
                <span class="text-slate-400">重要性</span>
                <span class="text-white font-semibold">{{ feature.importance.toFixed(1) }}%</span>
              </div>
              <div class="h-2 bg-white/10 rounded-full overflow-hidden">
                <div
                  class="h-full rounded-full transition-all duration-1000"
                  :style="{
                    width: `${feature.importance * 2}%`,
                    backgroundColor: feature.color
                  }"
                />
              </div>
            </div>

            <!-- Description -->
            <p class="text-slate-400 text-sm leading-relaxed">
              {{ feature.description }}
            </p>
          </div>
        </div>
      </div>

      <!-- SHAP-like Interpretation -->
      <div class="glass-card">
        <h2 class="text-xl font-bold text-white mb-6">SHAP 特徵解釋</h2>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <!-- Positive Impact -->
          <div>
            <h3 class="text-lg font-semibold text-red-400 mb-4 flex items-center">
              <span class="mr-2">📈</span>
              增加霸凌傾向的因素
            </h3>
            <div class="space-y-3">
              <div class="flex items-center justify-between p-3 bg-red-500/10 rounded-lg">
                <span class="text-slate-300">年輕年齡 (< 35歲)</span>
                <div class="flex items-center">
                  <div class="w-24 h-2 bg-white/10 rounded-full overflow-hidden mr-2">
                    <div class="h-full bg-red-500 rounded-full" style="width: 85%"></div>
                  </div>
                  <span class="text-red-400 font-semibold">+8.5</span>
                </div>
              </div>
              <div class="flex items-center justify-between p-3 bg-red-500/10 rounded-lg">
                <span class="text-slate-300">長時間上網 (> 5hr)</span>
                <div class="flex items-center">
                  <div class="w-24 h-2 bg-white/10 rounded-full overflow-hidden mr-2">
                    <div class="h-full bg-red-500 rounded-full" style="width: 60%"></div>
                  </div>
                  <span class="text-red-400 font-semibold">+6.2</span>
                </div>
              </div>
              <div class="flex items-center justify-between p-3 bg-red-500/10 rounded-lg">
                <span class="text-slate-300">高社會焦慮</span>
                <div class="flex items-center">
                  <div class="w-24 h-2 bg-white/10 rounded-full overflow-hidden mr-2">
                    <div class="h-full bg-red-500 rounded-full" style="width: 45%"></div>
                  </div>
                  <span class="text-red-400 font-semibold">+4.5</span>
                </div>
              </div>
              <div class="flex items-center justify-between p-3 bg-red-500/10 rounded-lg">
                <span class="text-slate-300">男性</span>
                <div class="flex items-center">
                  <div class="w-24 h-2 bg-white/10 rounded-full overflow-hidden mr-2">
                    <div class="h-full bg-red-500 rounded-full" style="width: 30%"></div>
                  </div>
                  <span class="text-red-400 font-semibold">+3.0</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Negative Impact -->
          <div>
            <h3 class="text-lg font-semibold text-green-400 mb-4 flex items-center">
              <span class="mr-2">📉</span>
              降低霸凌傾向的因素
            </h3>
            <div class="space-y-3">
              <div class="flex items-center justify-between p-3 bg-green-500/10 rounded-lg">
                <span class="text-slate-300">年長年齡 (> 50歲)</span>
                <div class="flex items-center">
                  <div class="w-24 h-2 bg-white/10 rounded-full overflow-hidden mr-2">
                    <div class="h-full bg-green-500 rounded-full" style="width: 75%"></div>
                  </div>
                  <span class="text-green-400 font-semibold">-7.5</span>
                </div>
              </div>
              <div class="flex items-center justify-between p-3 bg-green-500/10 rounded-lg">
                <span class="text-slate-300">適度上網 (< 3hr)</span>
                <div class="flex items-center">
                  <div class="w-24 h-2 bg-white/10 rounded-full overflow-hidden mr-2">
                    <div class="h-full bg-green-500 rounded-full" style="width: 50%"></div>
                  </div>
                  <span class="text-green-400 font-semibold">-5.0</span>
                </div>
              </div>
              <div class="flex items-center justify-between p-3 bg-green-500/10 rounded-lg">
                <span class="text-slate-300">低社會焦慮</span>
                <div class="flex items-center">
                  <div class="w-24 h-2 bg-white/10 rounded-full overflow-hidden mr-2">
                    <div class="h-full bg-green-500 rounded-full" style="width: 40%"></div>
                  </div>
                  <span class="text-green-400 font-semibold">-4.0</span>
                </div>
              </div>
              <div class="flex items-center justify-between p-3 bg-green-500/10 rounded-lg">
                <span class="text-slate-300">高等教育</span>
                <div class="flex items-center">
                  <div class="w-24 h-2 bg-white/10 rounded-full overflow-hidden mr-2">
                    <div class="h-full bg-green-500 rounded-full" style="width: 25%"></div>
                  </div>
                  <span class="text-green-400 font-semibold">-2.5</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
