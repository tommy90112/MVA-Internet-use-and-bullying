<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import * as echarts from 'echarts'
import { classificationResults } from '../../data/analysisData'

const chartRef = ref(null)
let chartInstance = null

const props = defineProps({
  metric: {
    type: String,
    default: 'all' // 'accuracy', 'f1Score', 'aucRoc', 'all'
  }
})

const initChart = () => {
  if (!chartRef.value) return

  chartInstance = echarts.init(chartRef.value, 'dark')

  const models = classificationResults.map(r => r.model)
  const colors = classificationResults.map(r => r.color)

  const option = {
    backgroundColor: 'transparent',
    tooltip: {
      trigger: 'axis',
      axisPointer: { type: 'shadow' },
      backgroundColor: 'rgba(15, 23, 42, 0.9)',
      borderColor: 'rgba(255, 255, 255, 0.1)',
      textStyle: { color: '#e2e8f0' },
      formatter: (params) => {
        let result = `<div class="font-semibold mb-2">${params[0].axisValue}</div>`
        params.forEach(param => {
          result += `<div class="flex items-center space-x-2">
            <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:${param.color}"></span>
            <span>${param.seriesName}: ${(param.value * 100).toFixed(1)}%</span>
          </div>`
        })
        return result
      }
    },
    legend: {
      data: ['Accuracy', 'F1 Score', 'AUC-ROC'],
      textStyle: { color: '#94a3b8' },
      top: 10
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      top: 60,
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: models,
      axisLine: { lineStyle: { color: 'rgba(255,255,255,0.1)' } },
      axisLabel: {
        color: '#94a3b8',
        rotate: 15,
        fontSize: 11
      }
    },
    yAxis: {
      type: 'value',
      min: 0,
      max: 1,
      axisLine: { show: false },
      splitLine: { lineStyle: { color: 'rgba(255,255,255,0.05)' } },
      axisLabel: {
        color: '#94a3b8',
        formatter: (val) => `${(val * 100).toFixed(0)}%`
      }
    },
    series: [
      {
        name: 'Accuracy',
        type: 'bar',
        data: classificationResults.map(r => r.accuracy),
        itemStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: '#3b82f6' },
            { offset: 1, color: '#1d4ed8' }
          ]),
          borderRadius: [4, 4, 0, 0]
        },
        animationDelay: (idx) => idx * 100
      },
      {
        name: 'F1 Score',
        type: 'bar',
        data: classificationResults.map(r => r.f1Score),
        itemStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: '#10b981' },
            { offset: 1, color: '#059669' }
          ]),
          borderRadius: [4, 4, 0, 0]
        },
        animationDelay: (idx) => idx * 100 + 50
      },
      {
        name: 'AUC-ROC',
        type: 'bar',
        data: classificationResults.map(r => r.aucRoc),
        itemStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: '#8b5cf6' },
            { offset: 1, color: '#7c3aed' }
          ]),
          borderRadius: [4, 4, 0, 0]
        },
        animationDelay: (idx) => idx * 100 + 100
      }
    ],
    animationEasing: 'elasticOut',
    animationDelayUpdate: (idx) => idx * 5
  }

  chartInstance.setOption(option)

  // Resize handler
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
      <h3 class="text-lg font-semibold text-white">模型效能比較</h3>
      <div class="flex items-center space-x-2">
        <span class="text-xs text-slate-400">5 個模型</span>
      </div>
    </div>
    <div ref="chartRef" class="w-full h-80"></div>
  </div>
</template>
