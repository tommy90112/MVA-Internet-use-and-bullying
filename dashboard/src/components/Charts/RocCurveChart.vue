<script setup>
import { ref, onMounted } from 'vue'
import * as echarts from 'echarts'
import { rocCurveData } from '../../data/analysisData'

const chartRef = ref(null)
let chartInstance = null

const initChart = () => {
  if (!chartRef.value) return

  chartInstance = echarts.init(chartRef.value, 'dark')

  const rfData = rocCurveData.randomForest.fpr.map((fpr, i) => [fpr, rocCurveData.randomForest.tpr[i]])
  const lrData = rocCurveData.logisticRegression.fpr.map((fpr, i) => [fpr, rocCurveData.logisticRegression.tpr[i]])

  const option = {
    backgroundColor: 'transparent',
    tooltip: {
      trigger: 'axis',
      backgroundColor: 'rgba(15, 23, 42, 0.95)',
      borderColor: 'rgba(255, 255, 255, 0.1)',
      textStyle: { color: '#e2e8f0' },
      formatter: (params) => {
        return `FPR: ${(params[0].data[0] * 100).toFixed(1)}%<br/>
                TPR: ${(params[0].data[1] * 100).toFixed(1)}%`
      }
    },
    legend: {
      data: [
        `Random Forest (AUC=${rocCurveData.randomForest.auc})`,
        `Logistic Regression (AUC=${rocCurveData.logisticRegression.auc})`,
        '隨機猜測'
      ],
      textStyle: { color: '#94a3b8', fontSize: 11 },
      top: 10
    },
    grid: {
      left: '5%',
      right: '5%',
      bottom: '10%',
      top: 60,
      containLabel: true
    },
    xAxis: {
      type: 'value',
      name: 'False Positive Rate',
      nameLocation: 'middle',
      nameGap: 30,
      nameTextStyle: { color: '#94a3b8' },
      min: 0,
      max: 1,
      axisLine: { lineStyle: { color: 'rgba(255,255,255,0.1)' } },
      splitLine: { lineStyle: { color: 'rgba(255,255,255,0.05)' } },
      axisLabel: { color: '#94a3b8' }
    },
    yAxis: {
      type: 'value',
      name: 'True Positive Rate',
      nameLocation: 'middle',
      nameGap: 40,
      nameTextStyle: { color: '#94a3b8' },
      min: 0,
      max: 1,
      axisLine: { show: false },
      splitLine: { lineStyle: { color: 'rgba(255,255,255,0.05)' } },
      axisLabel: { color: '#94a3b8' }
    },
    series: [
      {
        name: `Random Forest (AUC=${rocCurveData.randomForest.auc})`,
        type: 'line',
        data: rfData,
        smooth: true,
        symbol: 'none',
        lineStyle: {
          width: 3,
          color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
            { offset: 0, color: '#10b981' },
            { offset: 1, color: '#059669' }
          ])
        },
        areaStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: 'rgba(16, 185, 129, 0.3)' },
            { offset: 1, color: 'rgba(16, 185, 129, 0)' }
          ])
        },
        animationDuration: 2000
      },
      {
        name: `Logistic Regression (AUC=${rocCurveData.logisticRegression.auc})`,
        type: 'line',
        data: lrData,
        smooth: true,
        symbol: 'none',
        lineStyle: {
          width: 3,
          color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
            { offset: 0, color: '#3b82f6' },
            { offset: 1, color: '#1d4ed8' }
          ])
        },
        areaStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: 'rgba(59, 130, 246, 0.2)' },
            { offset: 1, color: 'rgba(59, 130, 246, 0)' }
          ])
        },
        animationDuration: 2000,
        animationDelay: 300
      },
      {
        name: '隨機猜測',
        type: 'line',
        data: [[0, 0], [1, 1]],
        symbol: 'none',
        lineStyle: {
          width: 2,
          type: 'dashed',
          color: '#64748b'
        }
      }
    ]
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
      <h3 class="text-lg font-semibold text-white">ROC 曲線比較</h3>
      <div class="text-xs text-slate-400">曲線下面積越大越好</div>
    </div>
    <div ref="chartRef" class="w-full h-80"></div>
  </div>
</template>
