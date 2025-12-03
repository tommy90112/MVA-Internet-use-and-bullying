<script setup>
import { ref, onMounted, computed } from 'vue'
import * as echarts from 'echarts'
import { clusterResults } from '../../data/analysisData'

const chartRef = ref(null)
let chartInstance = null
const selectedCluster = ref(null)

const emit = defineEmits(['clusterSelect'])

const initChart = () => {
  if (!chartRef.value) return

  chartInstance = echarts.init(chartRef.value, 'dark')

  // Generate scatter data for each cluster
  const seriesData = clusterResults.map(cluster => {
    // Generate mock scatter points around cluster center
    const points = []
    const centerAge = cluster.meanAge
    const centerScore = cluster.meanScore

    for (let i = 0; i < cluster.size / 3; i++) {
      points.push([
        centerAge + (Math.random() - 0.5) * 20,
        centerScore + (Math.random() - 0.5) * cluster.stdScore * 2
      ])
    }

    return {
      name: cluster.label,
      type: 'scatter',
      data: points,
      symbolSize: 12,
      itemStyle: {
        color: cluster.color,
        opacity: 0.7
      },
      emphasis: {
        itemStyle: {
          opacity: 1,
          shadowBlur: 10,
          shadowColor: cluster.color
        }
      },
      animationDelay: (idx) => idx * 10
    }
  })

  // Add cluster centers
  const centerSeries = {
    name: '群中心',
    type: 'scatter',
    data: clusterResults.map(c => [c.meanAge, c.meanScore]),
    symbolSize: 30,
    symbol: 'diamond',
    itemStyle: {
      color: '#fff',
      borderWidth: 3,
      borderColor: '#0ea5e9'
    },
    label: {
      show: true,
      formatter: (params) => `群${params.dataIndex}`,
      position: 'top',
      color: '#fff',
      fontSize: 12
    },
    zlevel: 10
  }

  const option = {
    backgroundColor: 'transparent',
    tooltip: {
      trigger: 'item',
      backgroundColor: 'rgba(15, 23, 42, 0.95)',
      borderColor: 'rgba(255, 255, 255, 0.1)',
      textStyle: { color: '#e2e8f0' },
      formatter: (params) => {
        if (params.seriesName === '群中心') {
          const cluster = clusterResults[params.dataIndex]
          return `
            <div class="p-2">
              <div class="font-bold text-lg mb-2" style="color: ${cluster.color}">${cluster.label}</div>
              <div>人數: ${cluster.size} (${cluster.percentage}%)</div>
              <div>平均分數: ${cluster.meanScore.toFixed(1)}</div>
              <div>平均年齡: ${cluster.meanAge}歲</div>
              <div>女性比例: ${cluster.femaleRatio}%</div>
              <div>上網時間: ${cluster.internetHours}hr</div>
            </div>
          `
        }
        return `年齡: ${params.data[0].toFixed(0)}歲<br/>分數: ${params.data[1].toFixed(1)}`
      }
    },
    legend: {
      data: clusterResults.map(c => c.label),
      textStyle: { color: '#94a3b8', fontSize: 11 },
      top: 10,
      itemGap: 15
    },
    grid: {
      left: '5%',
      right: '5%',
      bottom: '10%',
      top: 80,
      containLabel: true
    },
    xAxis: {
      type: 'value',
      name: '年齡',
      nameLocation: 'middle',
      nameGap: 30,
      nameTextStyle: { color: '#94a3b8' },
      min: 20,
      max: 65,
      axisLine: { lineStyle: { color: 'rgba(255,255,255,0.1)' } },
      splitLine: { lineStyle: { color: 'rgba(255,255,255,0.05)' } },
      axisLabel: { color: '#94a3b8' }
    },
    yAxis: {
      type: 'value',
      name: '霸凌傾向分數',
      nameLocation: 'middle',
      nameGap: 40,
      nameTextStyle: { color: '#94a3b8' },
      min: 20,
      max: 80,
      axisLine: { show: false },
      splitLine: { lineStyle: { color: 'rgba(255,255,255,0.05)' } },
      axisLabel: { color: '#94a3b8' }
    },
    series: [...seriesData, centerSeries],
    animationDuration: 2000,
    animationEasing: 'elasticOut'
  }

  chartInstance.setOption(option)

  // Click handler
  chartInstance.on('click', (params) => {
    if (params.seriesName === '群中心') {
      selectedCluster.value = clusterResults[params.dataIndex]
      emit('clusterSelect', selectedCluster.value)
    }
  })

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
      <h3 class="text-lg font-semibold text-white">K-Means 聚類分析</h3>
      <div class="text-xs text-slate-400">點擊群中心查看詳情</div>
    </div>
    <div ref="chartRef" class="w-full h-96"></div>
  </div>
</template>
