<script setup>
import { ref, onMounted } from 'vue'
import * as echarts from 'echarts'
import { featureImportance } from '../../data/analysisData'

const chartRef = ref(null)
let chartInstance = null

const categoryColors = {
  demographic: '#3b82f6',
  behavior: '#10b981',
  psychology: '#f59e0b'
}

const initChart = () => {
  if (!chartRef.value) return

  chartInstance = echarts.init(chartRef.value, 'dark')

  const sortedFeatures = [...featureImportance].sort((a, b) => a.importance - b.importance)

  const option = {
    backgroundColor: 'transparent',
    tooltip: {
      trigger: 'axis',
      axisPointer: { type: 'shadow' },
      backgroundColor: 'rgba(15, 23, 42, 0.95)',
      borderColor: 'rgba(255, 255, 255, 0.1)',
      textStyle: { color: '#e2e8f0' },
      formatter: (params) => {
        const data = sortedFeatures[params[0].dataIndex]
        const categoryLabels = {
          demographic: '人口統計',
          behavior: '行為特徵',
          psychology: '心理特徵'
        }
        return `
          <div class="p-2">
            <div class="font-bold mb-1">${data.name}</div>
            <div>重要性: ${(data.importance * 100).toFixed(1)}%</div>
            <div>類別: ${categoryLabels[data.category]}</div>
          </div>
        `
      }
    },
    grid: {
      left: '3%',
      right: '15%',
      bottom: '3%',
      top: 30,
      containLabel: true
    },
    xAxis: {
      type: 'value',
      max: 0.5,
      axisLine: { show: false },
      splitLine: { lineStyle: { color: 'rgba(255,255,255,0.05)' } },
      axisLabel: {
        color: '#94a3b8',
        formatter: (val) => `${(val * 100).toFixed(0)}%`
      }
    },
    yAxis: {
      type: 'category',
      data: sortedFeatures.map(f => f.name),
      axisLine: { lineStyle: { color: 'rgba(255,255,255,0.1)' } },
      axisLabel: { color: '#e2e8f0', fontSize: 12 }
    },
    series: [
      {
        type: 'bar',
        data: sortedFeatures.map(f => ({
          value: f.importance,
          itemStyle: {
            color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
              { offset: 0, color: categoryColors[f.category] },
              { offset: 1, color: echarts.color.lift(categoryColors[f.category], 0.2) }
            ]),
            borderRadius: [0, 6, 6, 0]
          }
        })),
        barWidth: 20,
        label: {
          show: true,
          position: 'right',
          color: '#94a3b8',
          formatter: (params) => `${(params.value * 100).toFixed(1)}%`
        },
        animationDelay: (idx) => idx * 150
      }
    ],
    animationEasing: 'elasticOut',
    animationDuration: 1500
  }

  chartInstance.setOption(option)

  window.addEventListener('resize', () => {
    chartInstance?.resize()
  })
}

onMounted(() => {
  setTimeout(initChart, 100)
})
</script>

<template>
  <div class="chart-container">
    <div class="flex items-center justify-between mb-4">
      <h3 class="text-lg font-semibold text-white">特徵重要性排名</h3>
      <div class="flex items-center space-x-4 text-xs">
        <span class="flex items-center">
          <span class="w-3 h-3 rounded-full bg-blue-500 mr-1"></span>
          人口統計
        </span>
        <span class="flex items-center">
          <span class="w-3 h-3 rounded-full bg-green-500 mr-1"></span>
          行為特徵
        </span>
        <span class="flex items-center">
          <span class="w-3 h-3 rounded-full bg-amber-500 mr-1"></span>
          心理特徵
        </span>
      </div>
    </div>
    <div ref="chartRef" class="w-full h-80"></div>
  </div>
</template>
