<script setup>
import { ref, onMounted } from 'vue'
import { keyFindings, methodologies, projectInfo } from '../data/analysisData'
import gsap from 'gsap'

onMounted(() => {
  gsap.from('.finding-card', {
    y: 50,
    opacity: 0,
    duration: 0.8,
    stagger: 0.15,
    ease: 'power3.out'
  })
})

const recommendations = [
  {
    target: '教育單位',
    icon: '🏫',
    actions: [
      '針對年輕族群加強網路素養教育',
      '建立校園網路霸凌通報機制',
      '提供社會焦慮諮詢資源'
    ]
  },
  {
    target: '平台業者',
    icon: '💻',
    actions: [
      '開發使用時間提醒功能',
      '優化內容過濾與舉報機制',
      '建立高風險使用者早期預警'
    ]
  },
  {
    target: '家長',
    icon: '👨‍👩‍👧',
    actions: [
      '關注孩子每日上網時長',
      '留意社會焦慮等心理狀態',
      '建立開放的親子溝通管道'
    ]
  }
]
</script>

<template>
  <div class="min-h-screen pt-20 pb-12 px-4">
    <div class="max-w-7xl mx-auto">
      <!-- Header -->
      <div class="mb-12">
        <h1 class="text-4xl font-bold text-white mb-4">研究發現與建議</h1>
        <p class="text-slate-400 max-w-2xl">
          基於數據分析的關鍵發現與實務應用建議
        </p>
      </div>

      <!-- Key Findings -->
      <div class="mb-16">
        <h2 class="text-2xl font-bold text-white mb-8">關鍵發現</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div
            v-for="(finding, index) in keyFindings"
            :key="finding.title"
            class="finding-card glass-card relative overflow-hidden"
          >
            <!-- Impact indicator -->
            <div
              :class="[
                'absolute top-0 left-0 w-1 h-full',
                finding.impact === 'high' ? 'bg-red-500' :
                finding.impact === 'medium' ? 'bg-yellow-500' : 'bg-green-500'
              ]"
            />

            <div class="pl-4">
              <div class="flex items-start space-x-4">
                <div class="text-4xl">{{ finding.icon }}</div>
                <div>
                  <div class="flex items-center space-x-2 mb-2">
                    <h3 class="text-xl font-semibold text-white">{{ finding.title }}</h3>
                    <span
                      :class="[
                        'text-xs px-2 py-0.5 rounded-full',
                        finding.impact === 'high' ? 'bg-red-500/20 text-red-400' :
                        finding.impact === 'medium' ? 'bg-yellow-500/20 text-yellow-400' : 'bg-green-500/20 text-green-400'
                      ]"
                    >
                      {{ finding.impact === 'high' ? '高影響' : finding.impact === 'medium' ? '中影響' : '低影響' }}
                    </span>
                  </div>
                  <p class="text-slate-400">{{ finding.description }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Statistical Summary -->
      <div class="glass-card mb-16">
        <h2 class="text-xl font-bold text-white mb-6">統計摘要</h2>
        <div class="overflow-x-auto">
          <table class="w-full text-left">
            <thead>
              <tr class="border-b border-white/10">
                <th class="pb-4 text-slate-400 font-medium">指標</th>
                <th class="pb-4 text-slate-400 font-medium">數值</th>
                <th class="pb-4 text-slate-400 font-medium">說明</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-white/5">
              <tr>
                <td class="py-4 text-white">樣本數</td>
                <td class="py-4 text-primary-400 font-semibold">672</td>
                <td class="py-4 text-slate-400">有效問卷回覆數</td>
              </tr>
              <tr>
                <td class="py-4 text-white">最佳模型 AUC</td>
                <td class="py-4 text-primary-400 font-semibold">0.71</td>
                <td class="py-4 text-slate-400">Random Forest 模型表現</td>
              </tr>
              <tr>
                <td class="py-4 text-white">高風險群比例</td>
                <td class="py-4 text-red-400 font-semibold">38%</td>
                <td class="py-4 text-slate-400">群3 + 群1 共 255 人</td>
              </tr>
              <tr>
                <td class="py-4 text-white">最重要特徵</td>
                <td class="py-4 text-purple-400 font-semibold">年齡 (39.7%)</td>
                <td class="py-4 text-slate-400">年輕人霸凌傾向顯著較高</td>
              </tr>
              <tr>
                <td class="py-4 text-white">高風險閾值</td>
                <td class="py-4 text-orange-400 font-semibold">> 53.6</td>
                <td class="py-4 text-slate-400">前 25% 分數門檻</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Recommendations -->
      <div class="mb-16">
        <h2 class="text-2xl font-bold text-white mb-8">實務建議</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div
            v-for="rec in recommendations"
            :key="rec.target"
            class="glass-card"
          >
            <div class="text-4xl mb-4">{{ rec.icon }}</div>
            <h3 class="text-xl font-semibold text-white mb-4">{{ rec.target }}</h3>
            <ul class="space-y-3">
              <li
                v-for="action in rec.actions"
                :key="action"
                class="flex items-start space-x-2"
              >
                <span class="text-primary-400 mt-1">→</span>
                <span class="text-slate-300 text-sm">{{ action }}</span>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Methodology Summary -->
      <div class="glass-card mb-16">
        <h2 class="text-xl font-bold text-white mb-6">研究方法總覽</h2>
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
          <div
            v-for="method in methodologies"
            :key="method.name"
            class="text-center p-4 bg-white/5 rounded-xl"
          >
            <div class="text-3xl mb-2">{{ method.icon }}</div>
            <div class="text-sm font-medium text-white">{{ method.name }}</div>
            <div class="text-xs text-green-400 mt-1">✓ 已完成</div>
          </div>
        </div>
      </div>

      <!-- Limitations -->
      <div class="glass-card mb-16">
        <h2 class="text-xl font-bold text-white mb-6">研究限制</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="space-y-4">
            <div class="flex items-start space-x-3">
              <span class="text-yellow-400">⚠️</span>
              <div>
                <h4 class="text-white font-medium">橫斷面設計</h4>
                <p class="text-slate-400 text-sm">無法觀察行為的動態變化</p>
              </div>
            </div>
            <div class="flex items-start space-x-3">
              <span class="text-yellow-400">⚠️</span>
              <div>
                <h4 class="text-white font-medium">自填問卷偏誤</h4>
                <p class="text-slate-400 text-sm">可能存在社會期許效應</p>
              </div>
            </div>
          </div>
          <div class="space-y-4">
            <div class="flex items-start space-x-3">
              <span class="text-yellow-400">⚠️</span>
              <div>
                <h4 class="text-white font-medium">缺失值較多</h4>
                <p class="text-slate-400 text-sm">部分社群媒體使用變數缺失率達 45%</p>
              </div>
            </div>
            <div class="flex items-start space-x-3">
              <span class="text-yellow-400">⚠️</span>
              <div>
                <h4 class="text-white font-medium">因果推論限制</h4>
                <p class="text-slate-400 text-sm">僅能建立相關性，非因果關係</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Footer CTA -->
      <div class="text-center">
        <div class="glass p-12 relative overflow-hidden">
          <div class="absolute inset-0 bg-gradient-to-r from-primary-500/10 to-purple-500/10" />
          <div class="relative z-10">
            <h2 class="text-3xl font-bold text-white mb-4">
              感謝您的閱讀
            </h2>
            <p class="text-slate-400 mb-6 max-w-xl mx-auto">
              本研究由 {{ projectInfo.author }} 完成
              <br />
              {{ projectInfo.institution }}
            </p>
            <div class="flex justify-center space-x-4">
              <a
                href="https://github.com"
                target="_blank"
                class="glass-button flex items-center space-x-2"
              >
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
                </svg>
                <span>查看原始碼</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
