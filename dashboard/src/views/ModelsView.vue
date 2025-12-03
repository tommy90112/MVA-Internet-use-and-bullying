<script setup>
import { ref, onMounted } from 'vue'
import ModelComparisonChart from '../components/Charts/ModelComparisonChart.vue'
import RocCurveChart from '../components/Charts/RocCurveChart.vue'
import { classificationResults, confusionMatrix } from '../data/analysisData'
import * as echarts from 'echarts'
import gsap from 'gsap'

const confusionChartRef = ref(null)
const selectedModel = ref(classificationResults[0])

const selectModel = (model) => {
  selectedModel.value = model
}

onMounted(() => {
  // Confusion Matrix Heatmap
  const chart = echarts.init(confusionChartRef.value, 'dark')

  const data = [
    [0, 0, confusionMatrix.trueNegative],
    [0, 1, confusionMatrix.falseNegative],
    [1, 0, confusionMatrix.falsePositive],
    [1, 1, confusionMatrix.truePositive]
  ]

  chart.setOption({
    backgroundColor: 'transparent',
    tooltip: {
      formatter: (params) => {
        const labels = ['一般', '高風險']
        return `實際: ${labels[params.data[1]]}<br/>預測: ${labels[params.data[0]]}<br/>數量: ${params.data[2]}`
      }
    },
    grid: { left: '15%', right: '10%', bottom: '15%', top: 30 },
    xAxis: {
      type: 'category',
      data: confusionMatrix.labels,
      name: '預測',
      nameLocation: 'middle',
      nameGap: 30,
      axisLine: { lineStyle: { color: 'rgba(255,255,255,0.1)' } },
      axisLabel: { color: '#e2e8f0' }
    },
    yAxis: {
      type: 'category',
      data: confusionMatrix.labels,
      name: '實際',
      nameLocation: 'middle',
      nameGap: 40,
      axisLine: { lineStyle: { color: 'rgba(255,255,255,0.1)' } },
      axisLabel: { color: '#e2e8f0' }
    },
    visualMap: {
      min: 0,
      max: 100,
      show: false,
      inRange: {
        color: ['#1e3a5f', '#0ea5e9']
      }
    },
    series: [{
      type: 'heatmap',
      data: data,
      label: {
        show: true,
        color: '#fff',
        fontSize: 16,
        fontWeight: 'bold'
      },
      itemStyle: {
        borderRadius: 8,
        borderWidth: 2,
        borderColor: 'rgba(255,255,255,0.1)'
      },
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowColor: 'rgba(0,0,0,0.5)'
        }
      }
    }]
  })

  window.addEventListener('resize', () => chart.resize())

  // Animate cards
  gsap.from('.model-card', {
    y: 30,
    opacity: 0,
    duration: 0.6,
    stagger: 0.1,
    ease: 'power3.out'
  })
})
</script>

<template>
  <div class="min-h-screen pt-20 pb-12 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- Header -->
      <div class="mb-12">
        <h1 class="text-4xl font-bold text-white mb-4">機器學習模型</h1>
        <p class="text-slate-400 max-w-2xl">
          使用多種分類演算法預測高風險使用者，比較各模型效能表現
        </p>
      </div>

      <!-- Model Cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4 mb-12">
        <div
          v-for="model in classificationResults"
          :key="model.model"
          @click="selectModel(model)"
          :class="[
            'model-card glass-card cursor-pointer transition-all duration-300',
            selectedModel.model === model.model ? 'ring-2 ring-primary-500 bg-white/10' : ''
          ]"
        >
          <div class="flex items-center justify-between mb-3">
            <div
              class="w-3 h-3 rounded-full"
              :style="{ backgroundColor: model.color }"
            />
            <span
              :class="[
                'text-xs px-2 py-0.5 rounded-full',
                model.aucRoc > 0.7 ? 'bg-green-500/20 text-green-400' : 'bg-yellow-500/20 text-yellow-400'
              ]"
            >
              AUC {{ (model.aucRoc * 100).toFixed(0) }}%
            </span>
          </div>
          <h3 class="text-sm font-semibold text-white mb-2">{{ model.model }}</h3>
          <div class="space-y-1">
            <div class="flex justify-between text-xs">
              <span class="text-slate-400">Accuracy</span>
              <span class="text-white">{{ (model.accuracy * 100).toFixed(1) }}%</span>
            </div>
            <div class="flex justify-between text-xs">
              <span class="text-slate-400">F1 Score</span>
              <span class="text-white">{{ (model.f1Score * 100).toFixed(1) }}%</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Charts Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-12">
        <ModelComparisonChart />
        <RocCurveChart />
      </div>

      <!-- Confusion Matrix & Selected Model Details -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <!-- Confusion Matrix -->
        <div class="chart-container">
          <h3 class="text-lg font-semibold text-white mb-4">混淆矩陣 (Random Forest)</h3>
          <div ref="confusionChartRef" class="w-full h-72"></div>
          <div class="mt-4 grid grid-cols-2 gap-4 text-sm">
            <div class="bg-white/5 rounded-lg p-3">
              <div class="text-slate-400">準確率 (Precision)</div>
              <div class="text-xl font-bold text-white">
                {{ ((confusionMatrix.truePositive / (confusionMatrix.truePositive + confusionMatrix.falsePositive)) * 100).toFixed(1) }}%
              </div>
            </div>
            <div class="bg-white/5 rounded-lg p-3">
              <div class="text-slate-400">召回率 (Recall)</div>
              <div class="text-xl font-bold text-white">
                {{ ((confusionMatrix.truePositive / (confusionMatrix.truePositive + confusionMatrix.falseNegative)) * 100).toFixed(1) }}%
              </div>
            </div>
          </div>
        </div>

        <!-- Model Interpretation -->
        <div class="glass-card">
          <h3 class="text-lg font-semibold text-white mb-6">模型解讀</h3>

          <div class="space-y-6">
            <div>
              <h4 class="text-primary-400 font-medium mb-2">📊 效能評估</h4>
              <p class="text-slate-300 text-sm leading-relaxed">
                最佳模型 <span class="text-white font-semibold">Random Forest</span> 達到
                <span class="text-primary-400 font-semibold">AUC-ROC 0.71</span>，
                表示有 71% 的機率能正確區分高風險與一般使用者。
              </p>
            </div>

            <div>
              <h4 class="text-green-400 font-medium mb-2">✅ 優點</h4>
              <ul class="text-slate-300 text-sm space-y-1">
                <li>• 使用獨立特徵預測，避免資料洩漏</li>
                <li>• 模型穩定，交叉驗證變異小</li>
                <li>• 特徵重要性可解釋</li>
              </ul>
            </div>

            <div>
              <h4 class="text-yellow-400 font-medium mb-2">⚠️ 限制</h4>
              <ul class="text-slate-300 text-sm space-y-1">
                <li>• F1 分數偏低，類別不平衡影響</li>
                <li>• 召回率有提升空間</li>
                <li>• 部分行為特徵缺失值較多</li>
              </ul>
            </div>

            <div>
              <h4 class="text-purple-400 font-medium mb-2">💡 實務應用</h4>
              <p class="text-slate-300 text-sm leading-relaxed">
                此模型可作為早期預警系統，識別潛在高風險使用者，
                結合年齡、上網時間、社會焦慮等特徵進行風險評估。
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
