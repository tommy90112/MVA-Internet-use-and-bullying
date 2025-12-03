<script setup>
import { ref, onMounted } from 'vue'
import gsap from 'gsap'
import StatCard from '../components/StatCard.vue'
import { datasetStats, projectInfo } from '../data/analysisData'
import * as echarts from 'echarts'

const distributionChartRef = ref(null)
const genderChartRef = ref(null)

onMounted(() => {
  // Distribution Chart
  const distributionChart = echarts.init(distributionChartRef.value, 'dark')

  // Generate histogram data based on target stats
  const bins = []
  const counts = []
  for (let i = 20; i <= 110; i += 10) {
    bins.push(`${i}-${i+10}`)
    // Simulate normal distribution around mean 47.5
    const x = i + 5
    const count = Math.round(120 * Math.exp(-Math.pow(x - 47.5, 2) / (2 * 100)))
    counts.push(count)
  }

  distributionChart.setOption({
    backgroundColor: 'transparent',
    tooltip: {
      trigger: 'axis',
      axisPointer: { type: 'shadow' }
    },
    grid: { left: '3%', right: '4%', bottom: '3%', top: 30, containLabel: true },
    xAxis: {
      type: 'category',
      data: bins,
      axisLine: { lineStyle: { color: 'rgba(255,255,255,0.1)' } },
      axisLabel: { color: '#94a3b8', rotate: 30 }
    },
    yAxis: {
      type: 'value',
      axisLine: { show: false },
      splitLine: { lineStyle: { color: 'rgba(255,255,255,0.05)' } },
      axisLabel: { color: '#94a3b8' }
    },
    series: [{
      type: 'bar',
      data: counts,
      itemStyle: {
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          { offset: 0, color: '#0ea5e9' },
          { offset: 1, color: '#0369a1' }
        ]),
        borderRadius: [4, 4, 0, 0]
      },
      animationDelay: (idx) => idx * 100
    }]
  })

  // Gender Chart
  const genderChart = echarts.init(genderChartRef.value, 'dark')
  genderChart.setOption({
    backgroundColor: 'transparent',
    tooltip: { trigger: 'item' },
    series: [{
      type: 'pie',
      radius: ['50%', '75%'],
      center: ['50%', '50%'],
      data: [
        { value: datasetStats.genderRatio.male, name: '男性', itemStyle: { color: '#3b82f6' } },
        { value: datasetStats.genderRatio.female, name: '女性', itemStyle: { color: '#ec4899' } }
      ],
      label: {
        color: '#e2e8f0',
        formatter: '{b}\n{d}%'
      },
      labelLine: { lineStyle: { color: 'rgba(255,255,255,0.3)' } },
      emphasis: {
        itemStyle: {
          shadowBlur: 20,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      },
      animationType: 'scale',
      animationDuration: 1500
    }]
  })

  window.addEventListener('resize', () => {
    distributionChart.resize()
    genderChart.resize()
  })
})
</script>

<template>
  <div class="min-h-screen pt-20 pb-12 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- Header -->
      <div class="mb-12">
        <h1 class="text-4xl font-bold text-white mb-4">資料概覽</h1>
        <p class="text-slate-400 max-w-2xl">
          深入了解「{{ projectInfo.dataSource }}」的資料特性與分布
        </p>
      </div>

      <!-- Stats Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
        <StatCard
          :value="datasetStats.totalSamples"
          label="有效樣本數"
          icon="👥"
          color="primary"
          :delay="0"
        />
        <StatCard
          :value="datasetStats.totalFeatures"
          label="分析變數"
          icon="📊"
          color="purple"
          :delay="0.1"
        />
        <StatCard
          :value="datasetStats.targetStats.mean"
          label="平均霸凌分數"
          icon="📈"
          :decimals="1"
          color="orange"
          :delay="0.2"
        />
        <StatCard
          :value="datasetStats.missingRate"
          label="缺失值比例"
          suffix="%"
          icon="⚠️"
          :decimals="1"
          color="red"
          :delay="0.3"
        />
      </div>

      <!-- Charts Row -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-12">
        <!-- Distribution Chart -->
        <div class="chart-container">
          <h3 class="text-lg font-semibold text-white mb-4">霸凌傾向分數分布</h3>
          <div ref="distributionChartRef" class="w-full h-72"></div>
          <div class="mt-4 grid grid-cols-3 gap-4 text-center">
            <div>
              <div class="text-2xl font-bold text-white">{{ datasetStats.targetStats.min }}</div>
              <div class="text-xs text-slate-400">最小值</div>
            </div>
            <div>
              <div class="text-2xl font-bold gradient-text">{{ datasetStats.targetStats.mean }}</div>
              <div class="text-xs text-slate-400">平均值</div>
            </div>
            <div>
              <div class="text-2xl font-bold text-white">{{ datasetStats.targetStats.max }}</div>
              <div class="text-xs text-slate-400">最大值</div>
            </div>
          </div>
        </div>

        <!-- Gender Distribution -->
        <div class="chart-container">
          <h3 class="text-lg font-semibold text-white mb-4">性別分布</h3>
          <div ref="genderChartRef" class="w-full h-72"></div>
          <div class="mt-4 flex justify-center space-x-8">
            <div class="flex items-center space-x-2">
              <span class="w-3 h-3 bg-blue-500 rounded-full"></span>
              <span class="text-slate-300">男性 {{ datasetStats.genderRatio.male }}%</span>
            </div>
            <div class="flex items-center space-x-2">
              <span class="w-3 h-3 bg-pink-500 rounded-full"></span>
              <span class="text-slate-300">女性 {{ datasetStats.genderRatio.female }}%</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Target Variable Stats -->
      <div class="glass-card mb-12">
        <h3 class="text-lg font-semibold text-white mb-6">目標變數統計摘要</h3>
        <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-7 gap-4">
          <div class="bg-white/5 rounded-lg p-4 text-center">
            <div class="text-xs text-slate-400 mb-1">樣本數</div>
            <div class="text-xl font-bold text-white">{{ datasetStats.totalSamples }}</div>
          </div>
          <div class="bg-white/5 rounded-lg p-4 text-center">
            <div class="text-xs text-slate-400 mb-1">平均值</div>
            <div class="text-xl font-bold text-primary-400">{{ datasetStats.targetStats.mean }}</div>
          </div>
          <div class="bg-white/5 rounded-lg p-4 text-center">
            <div class="text-xs text-slate-400 mb-1">標準差</div>
            <div class="text-xl font-bold text-white">{{ datasetStats.targetStats.std }}</div>
          </div>
          <div class="bg-white/5 rounded-lg p-4 text-center">
            <div class="text-xs text-slate-400 mb-1">最小值</div>
            <div class="text-xl font-bold text-green-400">{{ datasetStats.targetStats.min }}</div>
          </div>
          <div class="bg-white/5 rounded-lg p-4 text-center">
            <div class="text-xs text-slate-400 mb-1">Q1 (25%)</div>
            <div class="text-xl font-bold text-white">{{ datasetStats.targetStats.q25 }}</div>
          </div>
          <div class="bg-white/5 rounded-lg p-4 text-center">
            <div class="text-xs text-slate-400 mb-1">中位數</div>
            <div class="text-xl font-bold text-white">{{ datasetStats.targetStats.q50 }}</div>
          </div>
          <div class="bg-white/5 rounded-lg p-4 text-center">
            <div class="text-xs text-slate-400 mb-1">最大值</div>
            <div class="text-xl font-bold text-red-400">{{ datasetStats.targetStats.max }}</div>
          </div>
        </div>
      </div>

      <!-- Age Range Info -->
      <div class="glass-card">
        <h3 class="text-lg font-semibold text-white mb-6">樣本特性</h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="flex items-center space-x-4">
            <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-blue-500 to-blue-600 flex items-center justify-center text-2xl">
              🎂
            </div>
            <div>
              <div class="text-sm text-slate-400">年齡範圍</div>
              <div class="text-xl font-semibold text-white">{{ datasetStats.ageRange.min }} - {{ datasetStats.ageRange.max }} 歲</div>
            </div>
          </div>
          <div class="flex items-center space-x-4">
            <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-purple-500 to-purple-600 flex items-center justify-center text-2xl">
              📱
            </div>
            <div>
              <div class="text-sm text-slate-400">資料來源</div>
              <div class="text-xl font-semibold text-white">台灣傳播調查</div>
            </div>
          </div>
          <div class="flex items-center space-x-4">
            <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-green-500 to-green-600 flex items-center justify-center text-2xl">
              📅
            </div>
            <div>
              <div class="text-sm text-slate-400">調查年份</div>
              <div class="text-xl font-semibold text-white">2021</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
