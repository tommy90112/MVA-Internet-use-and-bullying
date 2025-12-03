<script setup>
import { ref } from 'vue'
import ClusterScatterChart from '../components/Charts/ClusterScatterChart.vue'
import ClusterCard from '../components/ClusterCard.vue'
import { clusterResults } from '../data/analysisData'

const selectedCluster = ref(null)

const handleClusterSelect = (cluster) => {
  selectedCluster.value = cluster
}

const getRiskColor = (level) => {
  const colors = {
    low: 'text-green-400',
    medium: 'text-yellow-400',
    high: 'text-red-400'
  }
  return colors[level]
}
</script>

<template>
  <div class="min-h-screen pt-20 pb-12 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- Header -->
      <div class="mb-12">
        <h1 class="text-4xl font-bold text-white mb-4">K-Means 聚類分析</h1>
        <p class="text-slate-400 max-w-2xl">
          將使用者分為 5 個群組，識別不同風險特徵的群體畫像
        </p>
      </div>

      <!-- Summary Stats -->
      <div class="grid grid-cols-2 md:grid-cols-5 gap-4 mb-12">
        <div
          v-for="cluster in clusterResults"
          :key="cluster.cluster"
          class="glass-card text-center"
        >
          <div
            class="w-8 h-8 rounded-full mx-auto mb-2"
            :style="{ backgroundColor: cluster.color }"
          />
          <div class="text-lg font-bold text-white">{{ cluster.size }}</div>
          <div class="text-xs text-slate-400">群 {{ cluster.cluster }}</div>
        </div>
      </div>

      <!-- Scatter Chart -->
      <div class="mb-12">
        <ClusterScatterChart @cluster-select="handleClusterSelect" />
      </div>

      <!-- Cluster Cards Grid -->
      <div class="mb-12">
        <h2 class="text-2xl font-bold text-white mb-6">群組詳細資訊</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <ClusterCard
            v-for="(cluster, index) in clusterResults"
            :key="cluster.cluster"
            :cluster="cluster"
            :index="index"
          />
        </div>
      </div>

      <!-- Risk Analysis -->
      <div class="glass-card">
        <h2 class="text-xl font-bold text-white mb-6">風險群組分析</h2>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <!-- High Risk -->
          <div class="bg-red-500/10 border border-red-500/30 rounded-xl p-6">
            <div class="flex items-center space-x-3 mb-4">
              <span class="text-3xl">⚠️</span>
              <div>
                <h3 class="text-lg font-semibold text-red-400">高風險群</h3>
                <p class="text-sm text-slate-400">需重點關注</p>
              </div>
            </div>
            <div class="space-y-3">
              <div class="flex justify-between">
                <span class="text-slate-300">群 3 (男性群)</span>
                <span class="text-white font-semibold">182 人</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-300">群 1 (重度上網)</span>
                <span class="text-white font-semibold">73 人</span>
              </div>
              <div class="pt-3 border-t border-white/10">
                <div class="text-sm text-slate-400">共計</div>
                <div class="text-2xl font-bold text-red-400">255 人 (38%)</div>
              </div>
            </div>
          </div>

          <!-- Medium Risk -->
          <div class="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-6">
            <div class="flex items-center space-x-3 mb-4">
              <span class="text-3xl">⚡</span>
              <div>
                <h3 class="text-lg font-semibold text-yellow-400">中風險群</h3>
                <p class="text-sm text-slate-400">持續觀察</p>
              </div>
            </div>
            <div class="space-y-3">
              <div class="flex justify-between">
                <span class="text-slate-300">群 0</span>
                <span class="text-white font-semibold">133 人</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-300">群 4</span>
                <span class="text-white font-semibold">138 人</span>
              </div>
              <div class="pt-3 border-t border-white/10">
                <div class="text-sm text-slate-400">共計</div>
                <div class="text-2xl font-bold text-yellow-400">271 人 (40%)</div>
              </div>
            </div>
          </div>

          <!-- Low Risk -->
          <div class="bg-green-500/10 border border-green-500/30 rounded-xl p-6">
            <div class="flex items-center space-x-3 mb-4">
              <span class="text-3xl">✅</span>
              <div>
                <h3 class="text-lg font-semibold text-green-400">低風險群</h3>
                <p class="text-sm text-slate-400">正常使用</p>
              </div>
            </div>
            <div class="space-y-3">
              <div class="flex justify-between">
                <span class="text-slate-300">群 2 (年長群)</span>
                <span class="text-white font-semibold">146 人</span>
              </div>
              <div class="pt-3 border-t border-white/10">
                <div class="text-sm text-slate-400">共計</div>
                <div class="text-2xl font-bold text-green-400">146 人 (22%)</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Key Insights -->
        <div class="mt-8 pt-6 border-t border-white/10">
          <h3 class="text-lg font-semibold text-white mb-4">關鍵發現</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="flex items-start space-x-3">
              <span class="text-primary-400 mt-1">→</span>
              <p class="text-slate-300 text-sm">
                <span class="text-white font-medium">性別差異顯著：</span>
                男性群組 (群3) 霸凌傾向分數最高，達 51.08 分
              </p>
            </div>
            <div class="flex items-start space-x-3">
              <span class="text-primary-400 mt-1">→</span>
              <p class="text-slate-300 text-sm">
                <span class="text-white font-medium">上網時間影響：</span>
                群1 每日上網 10.2 小時，霸凌傾向明顯較高
              </p>
            </div>
            <div class="flex items-start space-x-3">
              <span class="text-primary-400 mt-1">→</span>
              <p class="text-slate-300 text-sm">
                <span class="text-white font-medium">年齡保護因子：</span>
                年長族群 (52歲) 霸凌傾向最低，僅 43.48 分
              </p>
            </div>
            <div class="flex items-start space-x-3">
              <span class="text-primary-400 mt-1">→</span>
              <p class="text-slate-300 text-sm">
                <span class="text-white font-medium">預防策略：</span>
                應針對年輕男性與重度網路使用者加強教育
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
