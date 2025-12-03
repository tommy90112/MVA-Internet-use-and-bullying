<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import {
  projectInfo,
  datasetStats,
  classificationResults,
  featureImportance,
  clusterResults,
  keyFindings
} from './data/analysisData'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

const sections = [
  { id: 'hero', label: '首頁' },
  { id: 'problem', label: '研究問題' },
  { id: 'data', label: '資料概覽' },
  { id: 'gap', label: 'GAP分析' },
  { id: 'pca', label: 'PCA分析' },
  { id: 'ml', label: '機器學習' },
  { id: 'conclusion', label: '結論' }
]

const activeSection = ref('hero')
const showScrollTop = ref(false)

const scrollToSection = (id) => {
  const element = document.getElementById(id)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
  }
}

const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

onMounted(() => {
  const handleScroll = () => {
    showScrollTop.value = window.scrollY > 500

    sections.forEach(section => {
      const element = document.getElementById(section.id)
      if (element) {
        const rect = element.getBoundingClientRect()
        if (rect.top <= 150 && rect.bottom >= 150) {
          activeSection.value = section.id
        }
      }
    })
  }

  window.addEventListener('scroll', handleScroll)

  // 簡潔的進場動畫
  gsap.utils.toArray('.fade-up').forEach(element => {
    gsap.from(element, {
      scrollTrigger: {
        trigger: element,
        start: 'top 85%',
        toggleActions: 'play none none none'
      },
      y: 30,
      opacity: 0,
      duration: 0.6,
      ease: 'power2.out'
    })
  })

  onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll)
  })
})

// 風險等級顏色
const getRiskColor = (level) => {
  const colors = {
    high: '#e07a5f',
    medium: '#e5b45a',
    low: '#81b29a'
  }
  return colors[level] || '#6b7280'
}
</script>

<template>
  <div class="app-container">
    <!-- 簡潔導航列 -->
    <nav class="nav-bar">
      <div class="nav-content">
        <div class="nav-logo">
          <img src="/images/logo.png" alt="Logo" class="logo-img" />
          <span class="logo-text">網路霸凌研究</span>
        </div>
        <div class="nav-links">
          <button
            v-for="section in sections"
            :key="section.id"
            @click="scrollToSection(section.id)"
            :class="['nav-link', { active: activeSection === section.id }]"
          >
            {{ section.label }}
          </button>
        </div>
      </div>
    </nav>

    <!-- ==================== 起：Hero ==================== -->
    <section id="hero" class="hero-section">
      <div class="hero-content">
        <div class="hero-badge">統計學系數據科學所碩士班 ｜ MVA 專題報告呈現</div>
        <h1 class="hero-title">
          網路行為與霸凌傾向<br/>
          <span class="highlight">多變量分析研究</span>
        </h1>
        <p class="hero-desc">
          運用 GAP、PCA、機器學習等方法，探討不同群體的網路使用行為與霸凌傾向關聯
        </p>

        <!-- 核心指標 -->
        <div class="hero-stats">
          <div class="stat-item">
            <div class="stat-number">672</div>
            <div class="stat-label">有效樣本</div>
          </div>
          <div class="stat-divider"></div>
          <div class="stat-item">
            <div class="stat-number">5</div>
            <div class="stat-label">群體分類</div>
          </div>
          <div class="stat-divider"></div>
          <div class="stat-item">
            <div class="stat-number">71%</div>
            <div class="stat-label">預測 AUC</div>
          </div>
        </div>

        <button @click="scrollToSection('problem')" class="hero-cta">
          開始探索
          <svg class="cta-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"/>
          </svg>
        </button>
      </div>
    </section>

    <!-- ==================== 起：研究問題 ==================== -->
    <section id="problem" class="section section-light">
      <div class="section-container">
        <div class="section-header fade-up">
          <span class="section-number">01</span>
          <h2 class="section-title">研究問題</h2>
        </div>

        <div class="problem-grid fade-up">
          <div class="problem-main">
            <div class="question-card">
              <div class="question-icon">❓</div>
              <h3>核心問題</h3>
              <p class="question-text">
                不同人口特徵與網路使用行為的群體，<br/>
                其<strong>網路霸凌傾向</strong>是否存在顯著差異？
              </p>
            </div>
          </div>

          <div class="problem-sub">
            <div class="sub-question">
              <span class="sub-number">1</span>
              <p>如何識別具有不同網路行為模式的群體？</p>
            </div>
            <div class="sub-question">
              <span class="sub-number">2</span>
              <p>哪些因素最能預測高霸凌傾向？</p>
            </div>
            <div class="sub-question">
              <span class="sub-number">3</span>
              <p>能否建立有效的風險預測模型？</p>
            </div>
          </div>
        </div>

        <!-- 研究方法概覽 -->
        <div class="method-overview fade-up">
          <h3 class="method-title">分析方法</h3>
          <div class="method-flow">
            <div class="method-step">
              <div class="step-icon">🔍</div>
              <div class="step-name">GAP 分析</div>
              <div class="step-desc">群體識別</div>
            </div>
            <div class="method-arrow">→</div>
            <div class="method-step">
              <div class="step-icon">📊</div>
              <div class="step-name">PCA 分析</div>
              <div class="step-desc">維度縮減</div>
            </div>
            <div class="method-arrow">→</div>
            <div class="method-step">
              <div class="step-icon">🤖</div>
              <div class="step-name">機器學習</div>
              <div class="step-desc">預測模型</div>
            </div>
            <div class="method-arrow">→</div>
            <div class="method-step">
              <div class="step-icon">💡</div>
              <div class="step-name">SHAP</div>
              <div class="step-desc">模型解釋</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== 承：資料概覽 ==================== -->
    <section id="data" class="section section-cream">
      <div class="section-container">
        <div class="section-header fade-up">
          <span class="section-number">02</span>
          <h2 class="section-title">資料概覽</h2>
          <p class="section-subtitle">台灣傳播調查資料庫 2021</p>
        </div>

        <!-- 資料來源大圖 -->
        <div class="data-main-image fade-up">
          <div class="main-image-card hover-lift">
            <img src="/images/資料介紹.png" alt="資料來源" />
          </div>
        </div>

        <!-- 統計數據卡片 -->
        <div class="data-stats-row fade-up">
          <div class="stat-card-large hover-lift">
            <div class="stat-card-number">1,004</div>
            <div class="stat-card-unit">份</div>
            <div class="stat-card-label">原始樣本</div>
          </div>
          <div class="stat-card-large primary hover-lift">
            <div class="stat-card-number">672</div>
            <div class="stat-card-unit">份</div>
            <div class="stat-card-label">有效樣本</div>
          </div>
          <div class="stat-card-large hover-lift">
            <div class="stat-card-number">68</div>
            <div class="stat-card-unit">個</div>
            <div class="stat-card-label">特徵變數</div>
          </div>
          <div class="stat-card-large hover-lift">
            <div class="stat-card-number">19-61</div>
            <div class="stat-card-unit">歲</div>
            <div class="stat-card-label">年齡範圍</div>
          </div>
        </div>

        <!-- 抽樣方法說明 -->
        <div class="data-method fade-up">
          <div class="method-badge">抽樣方法</div>
          <p>分層三階段 RDD 抽樣法（Stratified Three-Stage Random Digit Dialing），確保樣本具全國代表性</p>
        </div>

        <!-- 樣本分布圖 -->
        <div class="sample-distribution fade-up">
          <div class="distribution-card hover-lift">
            <img src="/images/性別分布圖.png" alt="性別分布" />
            <div class="distribution-label">性別分布</div>
          </div>
          <div class="distribution-card hover-lift">
            <img src="/images/網路使用時長分布圖.png" alt="上網時長" />
            <div class="distribution-label">每日上網時長分布</div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== 轉：GAP 分析（重點） ==================== -->
    <section id="gap" class="section section-feature">
      <div class="section-container">
        <div class="section-header fade-up">
          <span class="section-number">03</span>
          <h2 class="section-title">GAP 廣義關聯圖分析</h2>
          <p class="section-subtitle">識別五種典型網路使用者群體</p>
        </div>

        <!-- GAP 主圖 -->
        <div class="feature-showcase fade-up">
          <div class="showcase-image">
            <img src="/images/GAP.png" alt="GAP 分析結果" />
          </div>
          <div class="showcase-insight">
            <div class="insight-badge">關鍵發現</div>
            <h3>透過熱圖對角線分布，清楚識別出五個行為群體</h3>
            <p>淺黃色區塊代表群體內部高相似性，深色區塊代表群體間的行為差異</p>
          </div>
        </div>

        <!-- 五大群體卡片 -->
        <div class="cluster-grid fade-up">
          <div
            v-for="cluster in clusterResults"
            :key="cluster.cluster"
            class="cluster-card"
            :class="cluster.riskLevel"
          >
            <div class="cluster-header">
              <span class="cluster-label">{{ cluster.label }}</span>
              <span class="cluster-risk" :style="{ color: getRiskColor(cluster.riskLevel) }">
                {{ cluster.riskLevel === 'high' ? '⚠ 高風險' : cluster.riskLevel === 'medium' ? '中風險' : '✓ 低風險' }}
              </span>
            </div>
            <div class="cluster-stats">
              <div class="cluster-stat">
                <span class="stat-val">{{ cluster.size }}</span>
                <span class="stat-name">人數</span>
              </div>
              <div class="cluster-stat">
                <span class="stat-val">{{ cluster.meanAge }}</span>
                <span class="stat-name">平均年齡</span>
              </div>
              <div class="cluster-stat">
                <span class="stat-val">{{ cluster.meanScore.toFixed(1) }}</span>
                <span class="stat-name">霸凌分數</span>
              </div>
            </div>
            <p class="cluster-desc">{{ cluster.description }}</p>
          </div>
        </div>

        <!-- GAP 結論 -->
        <div class="feature-conclusion fade-up">
          <div class="conclusion-icon">📌</div>
          <div class="conclusion-content">
            <h4>GAP 分析結論</h4>
            <p>
              <strong>高風險群體（群1 + 群3）共 255 人，佔總樣本 38%</strong>。
              其中「高風險男性群」霸凌分數最高（51.08），「重度網路使用者」每日上網超過 10 小時。
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== 轉：PCA 分析（重點） ==================== -->
    <section id="pca" class="section section-light">
      <div class="section-container">
        <div class="section-header fade-up">
          <span class="section-number">04</span>
          <h2 class="section-title">PCA 主成分分析</h2>
          <p class="section-subtitle">降低維度，識別網路行為主要模式</p>
        </div>

        <!-- PCA 主圖（上方，全寬） -->
        <div class="pca-main-chart fade-up">
          <div class="pca-chart-large hover-lift">
            <img src="/images/主成分結構.png" alt="主成分結構" />
          </div>
        </div>

        <!-- PCA 結論（大數字） -->
        <div class="pca-highlight fade-up">
          <div class="highlight-number">69.79%</div>
          <div class="highlight-text">前四個主成分累積解釋變異量</div>
        </div>

        <!-- PCA 四大發現（下方，橫向排列） -->
        <div class="pca-findings-row fade-up">
          <div class="pca-finding-card hover-lift">
            <div class="pca-finding-header">
              <span class="pca-finding-badge pc1">PC1</span>
              <span class="pca-finding-pct">31.58%</span>
            </div>
            <div class="pca-finding-bar">
              <div class="pca-finding-fill" style="width: 100%;"></div>
            </div>
            <h4>網路負面行為接觸觀察</h4>
            <p>反映受訪者在網路上觀察到的負面行為頻率，包含攻擊、責罵、諷刺等行為</p>
          </div>

          <div class="pca-finding-card hover-lift">
            <div class="pca-finding-header">
              <span class="pca-finding-badge pc2">PC2</span>
              <span class="pca-finding-pct">18.25%</span>
            </div>
            <div class="pca-finding-bar">
              <div class="pca-finding-fill" style="width: 58%;"></div>
            </div>
            <h4>網路衝突容忍程度</h4>
            <p>反映對網路衝突行為的接受度，高分代表較能容忍對抗性互動</p>
          </div>

          <div class="pca-finding-card hover-lift">
            <div class="pca-finding-header">
              <span class="pca-finding-badge pc3">PC3</span>
              <span class="pca-finding-pct">12.12%</span>
            </div>
            <div class="pca-finding-bar">
              <div class="pca-finding-fill" style="width: 38%;"></div>
            </div>
            <h4>行為-態度矛盾</h4>
            <p>揭示認知上反對網路暴力，但實際互動中仍展現攻擊性行為的現象</p>
          </div>

          <div class="pca-finding-card hover-lift">
            <div class="pca-finding-header">
              <span class="pca-finding-badge pc4">PC4</span>
              <span class="pca-finding-pct">7.85%</span>
            </div>
            <div class="pca-finding-bar">
              <div class="pca-finding-fill" style="width: 25%;"></div>
            </div>
            <h4>群體擴散效應</h4>
            <p>網路負面行為透過群體動力產生擴散，形成連鎖反應</p>
          </div>
        </div>

        <!-- PCA 關鍵洞見 -->
        <div class="pca-insight fade-up">
          <div class="insight-icon">💡</div>
          <div class="insight-content">
            <h4>關鍵洞見</h4>
            <p>PCA 結果顯示網路使用時間與霸凌傾向在第一主成分有較高載荷量，<strong>顯示兩者存在強烈關聯</strong>。長時間使用網路的用戶可能需要更多關注。</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== 轉：機器學習（重點） ==================== -->
    <section id="ml" class="section section-feature">
      <div class="section-container">
        <div class="section-header fade-up">
          <span class="section-number">05</span>
          <h2 class="section-title">機器學習預測模型</h2>
          <p class="section-subtitle">多模型比較與特徵重要性分析</p>
        </div>

        <!-- 模型比較圖（全寬大圖） -->
        <div class="ml-main-chart fade-up">
          <div class="ml-chart-large hover-lift">
            <img src="/images/ml/classification_results.png" alt="模型比較" />
          </div>
        </div>

        <!-- 模型表現列表 -->
        <div class="ml-results-section fade-up">
          <h3>模型表現比較</h3>
          <div class="model-cards">
            <div
              v-for="model in classificationResults"
              :key="model.model"
              class="model-card hover-lift"
              :class="{ best: model.aucRoc >= 0.7 }"
            >
              <div class="model-card-name">{{ model.model }}</div>
              <div class="model-card-metrics">
                <div class="model-metric">
                  <span class="metric-value">{{ (model.accuracy * 100).toFixed(1) }}%</span>
                  <span class="metric-label">Accuracy</span>
                </div>
                <div class="model-metric">
                  <span class="metric-value" :class="{ highlight: model.aucRoc >= 0.7 }">{{ model.aucRoc.toFixed(3) }}</span>
                  <span class="metric-label">AUC-ROC</span>
                </div>
              </div>
            </div>
          </div>
          <div class="best-model-banner">
            <span class="best-badge">🏆 最佳模型</span>
            <span class="best-name">Random Forest（AUC = 0.71）</span>
          </div>
        </div>

        <!-- 特徵重要性（全寬大圖 + 互動長條） -->
        <div class="feature-importance-section fade-up">
          <h3>特徵重要性排名</h3>
          <div class="importance-main-chart hover-lift">
            <img src="/images/ml/rf_feature_importance.png" alt="特徵重要性" />
          </div>
          <div class="importance-interactive">
            <div
              v-for="feature in featureImportance"
              :key="feature.feature"
              class="importance-item hover-lift"
            >
              <div class="importance-info">
                <span class="importance-name">{{ feature.name }}</span>
                <span class="importance-value">{{ (feature.importance * 100).toFixed(1) }}%</span>
              </div>
              <div class="importance-track">
                <div
                  class="importance-fill"
                  :style="{ width: `${feature.importance * 100}%` }"
                ></div>
              </div>
            </div>
          </div>
        </div>

        <!-- SHAP 解釋 -->
        <div class="shap-section fade-up">
          <h3>SHAP 模型解釋</h3>
          <div class="shap-grid-large">
            <div class="shap-card-large hover-lift">
              <img src="/images/ml/shap_summary.png" alt="SHAP Summary" />
              <div class="shap-caption">
                <h4>SHAP Summary Plot</h4>
                <p>年齡越小（紅色），SHAP 值越高，被預測為高風險的機率較高</p>
              </div>
            </div>
            <div class="shap-card-large hover-lift">
              <img src="/images/ml/shap_bar.png" alt="SHAP Bar" />
              <div class="shap-caption">
                <h4>特徵貢獻度</h4>
                <p>年齡是最重要的預測因子，其次是每日上網時間與居住地區</p>
              </div>
            </div>
          </div>
        </div>

        <!-- ML 結論 -->
        <div class="ml-conclusion fade-up">
          <div class="conclusion-box-large">
            <div class="conclusion-header">
              <span class="conclusion-icon">🔑</span>
              <h4>關鍵發現</h4>
            </div>
            <div class="conclusion-items">
              <div class="conclusion-item">
                <div class="item-number">39.7%</div>
                <div class="item-text">
                  <strong>年齡效應最顯著</strong>
                  <p>年輕族群霸凌傾向明顯高於年長者</p>
                </div>
              </div>
              <div class="conclusion-item">
                <div class="item-number">17%</div>
                <div class="item-text">
                  <strong>上網時間次之</strong>
                  <p>每日上網超過 10 小時者風險顯著提升</p>
                </div>
              </div>
              <div class="conclusion-item">
                <div class="item-number">14%</div>
                <div class="item-text">
                  <strong>地區差異存在</strong>
                  <p>都會區與非都會區使用者行為模式不同</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== 合：結論 ==================== -->
    <section id="conclusion" class="section section-conclusion">
      <div class="section-container">
        <div class="section-header fade-up">
          <span class="section-number">06</span>
          <h2 class="section-title">研究結論</h2>
        </div>

        <!-- 四大發現 -->
        <div class="findings-grid fade-up">
          <div
            v-for="(finding, index) in keyFindings"
            :key="finding.title"
            class="finding-item"
          >
            <div class="finding-icon">{{ finding.icon }}</div>
            <div class="finding-body">
              <h4>{{ finding.title }}</h4>
              <p>{{ finding.description }}</p>
            </div>
            <div
              class="finding-impact"
              :class="finding.impact"
            >
              {{ finding.impact === 'high' ? '高影響' : '中影響' }}
            </div>
          </div>
        </div>

        <!-- 統計摘要 -->
        <div class="stats-summary fade-up">
          <div class="summary-grid">
            <div class="summary-item">
              <span class="summary-num">672</span>
              <span class="summary-txt">有效樣本數</span>
            </div>
            <div class="summary-item highlight">
              <span class="summary-num">38%</span>
              <span class="summary-txt">高風險群佔比</span>
            </div>
            <div class="summary-item">
              <span class="summary-num">0.71</span>
              <span class="summary-txt">最佳 AUC-ROC</span>
            </div>
            <div class="summary-item">
              <span class="summary-num">39.7%</span>
              <span class="summary-txt">年齡貢獻度</span>
            </div>
          </div>
        </div>

        <!-- 研究價值 -->
        <div class="research-value fade-up">
          <h3>研究貢獻</h3>
          <div class="value-grid">
            <div class="value-card">
              <div class="value-icon">📚</div>
              <h4>理論層面</h4>
              <p>首次將 GAP 分析應用於網路行為研究，建立更完整的分析框架</p>
            </div>
            <div class="value-card">
              <div class="value-icon">🔧</div>
              <h4>方法創新</h4>
              <p>整合五種多變量分析方法，形成從探索到預測的完整分析鏈</p>
            </div>
            <div class="value-card">
              <div class="value-icon">🎯</div>
              <h4>實務應用</h4>
              <p>識別高風險群體特徵，為預防策略提供實證基礎</p>
            </div>
          </div>
        </div>

        <!-- Footer -->
        <div class="footer fade-up">
          <div class="footer-content">
            <div class="footer-info">
              <h4>{{ projectInfo.author }}</h4>
              <p>{{ projectInfo.institution }}</p>
              <p class="footer-source">資料來源：{{ projectInfo.dataSource }}</p>
            </div>
            <div class="footer-links">
              <a href="https://github.com" target="_blank" class="footer-link">
                <svg class="link-icon" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
                </svg>
                查看原始碼
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 回到頂部按鈕 -->
    <Transition name="fade">
      <button
        v-if="showScrollTop"
        @click="scrollToTop"
        class="scroll-top-btn"
      >
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"/>
        </svg>
      </button>
    </Transition>
  </div>
</template>

<style scoped>
/* ===== 全域容器 ===== */
.app-container {
  min-height: 100vh;
  background: #FAF8F5;
}

/* ===== 導航列 ===== */
.nav-bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  background: rgba(250, 248, 245, 0.95);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(0,0,0,0.06);
}

.nav-content {
  max-width: 1600px;
  margin: 0 auto;
  padding: 1rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.logo-img {
  width: 2.25rem;
  height: 2.25rem;
  object-fit: contain;
}

.logo-text {
  font-size: 2.5rem;
  font-weight: 600;
  color: #343a40;
}

.nav-links {
  display: flex;
  gap: 0.5rem;
}

.nav-link {
  padding: 0.625rem 1.25rem;
  font-size: 1rem;
  color: #6c757d;
  border: none;
  background: transparent;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.2s;
}

.nav-link:hover {
  color: #343a40;
  background: rgba(0,0,0,0.04);
}

.nav-link.active {
  color: #5D8696;
  background: rgba(93, 134, 150, 0.12);
  font-weight: 600;
}

/* ===== Hero Section ===== */
.hero-section {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 6rem 1.5rem 4rem;
  background: linear-gradient(180deg, #FAF8F5 0%, #F0EFEC 100%);
}

.hero-content {
  max-width: 800px;
  text-align: center;
}

.hero-badge {
  display: inline-block;
  padding: 0.5rem 1rem;
  background: rgba(93, 134, 150, 0.1);
  color: #5D8696;
  font-size: 0.875rem;
  border-radius: 2rem;
  margin-bottom: 2rem;
}

.hero-title {
  font-size: 3rem;
  font-weight: 700;
  color: #343a40;
  line-height: 1.2;
  margin-bottom: 1.5rem;
}

.hero-title .highlight {
  background: linear-gradient(135deg, #5D8696 0%, #81b29a 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-desc {
  font-size: 1.25rem;
  color: #6c757d;
  margin-bottom: 3rem;
  line-height: 1.6;
}

.hero-stats {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  margin-bottom: 3rem;
}

.stat-item {
  text-align: center;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: #343a40;
}

.stat-label {
  font-size: 0.875rem;
  color: #6c757d;
  margin-top: 0.25rem;
}

.stat-divider {
  width: 1px;
  height: 3rem;
  background: #E8E6E3;
}

.hero-cta {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem 2rem;
  background: linear-gradient(135deg, #5D8696 0%, #81b29a 100%);
  color: white;
  font-size: 1rem;
  font-weight: 500;
  border: none;
  border-radius: 0.75rem;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.hero-cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(93, 134, 150, 0.3);
}

.cta-arrow {
  width: 1.25rem;
  height: 1.25rem;
}

/* ===== Section 通用樣式 ===== */
.section {
  padding: 6rem 1.5rem;
}

.section-light {
  background: #FAF8F5;
}

.section-cream {
  background: linear-gradient(180deg, #F5F3F0 0%, #FAF8F5 100%);
}

.section-feature {
  background: linear-gradient(180deg, #e8f4f0 0%, #d8ebe5 50%, #e8f4f0 100%);
}

.section-conclusion {
  background: linear-gradient(180deg, #FAF8F5 0%, #F0EFEC 100%);
}

.section-container {
  max-width: 1200px;
  margin: 0 auto;
}

.section-header {
  text-align: center;
  margin-bottom: 4rem;
}

.section-number {
  display: inline-block;
  font-size: 0.875rem;
  font-weight: 600;
  color: #81b29a;
  margin-bottom: 0.5rem;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #343a40;
  margin-bottom: 0.5rem;
}

.section-subtitle {
  font-size: 1.125rem;
  color: #6c757d;
}

/* ===== 研究問題 ===== */
.problem-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  margin-bottom: 4rem;
}

.question-card {
  background: white;
  padding: 3rem;
  border-radius: 1.5rem;
  text-align: center;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.question-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.question-card h3 {
  font-size: 1.25rem;
  color: #6c757d;
  margin-bottom: 1rem;
}

.question-text {
  font-size: 1.5rem;
  color: #343a40;
  line-height: 1.6;
}

.question-text strong {
  color: #5D8696;
}

.problem-sub {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.sub-question {
  display: flex;
  align-items: center;
  gap: 1rem;
  background: white;
  padding: 1.5rem;
  border-radius: 1rem;
  box-shadow: 0 2px 10px rgba(0,0,0,0.03);
}

.sub-number {
  width: 2rem;
  height: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #C5DED6;
  color: #5D8696;
  font-weight: 600;
  border-radius: 0.5rem;
  flex-shrink: 0;
}

.sub-question p {
  color: #495057;
  font-size: 1rem;
}

.method-overview {
  background: white;
  padding: 2rem 3rem;
  border-radius: 1.5rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.method-title {
  text-align: center;
  font-size: 1.25rem;
  color: #343a40;
  margin-bottom: 2rem;
}

.method-flow {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.method-step {
  text-align: center;
  padding: 1rem 1.5rem;
}

.step-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.step-name {
  font-weight: 600;
  color: #343a40;
  font-size: 0.9rem;
}

.step-desc {
  font-size: 0.8rem;
  color: #6c757d;
}

.method-arrow {
  color: #C5DED6;
  font-size: 1.5rem;
  font-weight: 300;
}

/* ===== 資料概覽 ===== */
.data-grid {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 3rem;
  align-items: start;
}

.source-card {
  background: white;
  padding: 1rem;
  border-radius: 1rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
  margin-bottom: 1.5rem;
}

.source-img {
  width: 100%;
  border-radius: 0.5rem;
}

.source-info {
  background: white;
  padding: 1.5rem;
  border-radius: 1rem;
}

.source-info h4 {
  font-size: 1rem;
  color: #343a40;
  margin-bottom: 0.5rem;
}

.source-info p {
  color: #6c757d;
  font-size: 0.9rem;
}

.data-stat-card {
  background: white;
  padding: 1.5rem;
  border-radius: 1rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
  margin-bottom: 1.5rem;
}

.data-stat-row {
  display: flex;
  justify-content: space-between;
  padding: 0.75rem 0;
  border-bottom: 1px solid #F0EFEC;
}

.data-stat-row:last-child {
  border-bottom: none;
}

.data-stat-label {
  color: #6c757d;
}

.data-stat-value {
  font-weight: 600;
  color: #343a40;
}

.data-stat-value.highlight {
  color: #5D8696;
}

.sample-charts {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.mini-chart {
  background: white;
  padding: 0.75rem;
  border-radius: 0.75rem;
  text-align: center;
}

.mini-chart img {
  width: 100%;
  border-radius: 0.5rem;
  margin-bottom: 0.5rem;
}

.mini-chart span {
  font-size: 0.75rem;
  color: #6c757d;
}

/* ===== GAP 分析 ===== */
.feature-showcase {
  margin-bottom: 3rem;
}

.showcase-image {
  background: white;
  padding: 1.5rem;
  border-radius: 1.5rem;
  box-shadow: 0 4px 30px rgba(0,0,0,0.08);
  margin-bottom: 1.5rem;
}

.showcase-image img {
  width: 100%;
  border-radius: 0.75rem;
}

.showcase-insight {
  background: white;
  padding: 2rem;
  border-radius: 1rem;
  border-left: 4px solid #81b29a;
}

.insight-badge {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  background: rgba(129, 178, 154, 0.2);
  color: #5D8696;
  font-size: 0.75rem;
  font-weight: 600;
  border-radius: 1rem;
  margin-bottom: 0.75rem;
}

.showcase-insight h3 {
  font-size: 1.25rem;
  color: #343a40;
  margin-bottom: 0.5rem;
}

.showcase-insight p {
  color: #6c757d;
}

.cluster-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.25rem;
  margin-bottom: 3rem;
}

.cluster-card {
  background: white;
  padding: 1.5rem;
  border-radius: 1rem;
  box-shadow: 0 2px 15px rgba(0,0,0,0.05);
  border-top: 3px solid #E8E6E3;
}

.cluster-card.high {
  border-top-color: #e07a5f;
}

.cluster-card.medium {
  border-top-color: #e5b45a;
}

.cluster-card.low {
  border-top-color: #81b29a;
}

.cluster-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.cluster-label {
  font-weight: 600;
  color: #343a40;
}

.cluster-risk {
  font-size: 0.75rem;
  font-weight: 500;
}

.cluster-stats {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #F0EFEC;
}

.cluster-stat {
  text-align: center;
}

.stat-val {
  display: block;
  font-size: 1.25rem;
  font-weight: 600;
  color: #343a40;
}

.stat-name {
  font-size: 0.7rem;
  color: #6c757d;
}

.cluster-desc {
  font-size: 0.85rem;
  color: #6c757d;
  line-height: 1.5;
}

.feature-conclusion {
  display: flex;
  gap: 1.5rem;
  background: white;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.conclusion-icon {
  font-size: 2rem;
  flex-shrink: 0;
}

.conclusion-content h4 {
  font-size: 1.125rem;
  color: #343a40;
  margin-bottom: 0.5rem;
}

.conclusion-content p {
  color: #495057;
  line-height: 1.6;
}

.conclusion-content strong {
  color: #e07a5f;
}

/* ===== PCA 分析 ===== */
.pca-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  margin-bottom: 3rem;
}

.pca-chart {
  background: white;
  padding: 1.5rem;
  border-radius: 1.5rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.pca-chart img {
  width: 100%;
  border-radius: 0.75rem;
}

.pca-findings {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.finding-card {
  background: white;
  padding: 1.25rem;
  border-radius: 1rem;
  box-shadow: 0 2px 10px rgba(0,0,0,0.03);
}

.finding-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.finding-num {
  font-weight: 700;
  color: #5D8696;
}

.finding-pct {
  font-size: 0.875rem;
  color: #81b29a;
  font-weight: 600;
}

.finding-card h4 {
  font-size: 1rem;
  color: #343a40;
  margin-bottom: 0.25rem;
}

.finding-card p {
  font-size: 0.85rem;
  color: #6c757d;
  line-height: 1.5;
}

.pca-summary {
  display: flex;
  align-items: center;
  gap: 3rem;
  background: white;
  padding: 2rem 3rem;
  border-radius: 1.5rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.summary-stat {
  text-align: center;
  flex-shrink: 0;
}

.summary-number {
  display: block;
  font-size: 3rem;
  font-weight: 700;
  color: #5D8696;
}

.summary-label {
  font-size: 0.875rem;
  color: #6c757d;
}

.summary-text p {
  color: #495057;
  line-height: 1.6;
}

.summary-text strong {
  color: #343a40;
}

/* ===== 機器學習 ===== */
.ml-comparison {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  margin-bottom: 4rem;
}

.ml-chart {
  background: white;
  padding: 1.5rem;
  border-radius: 1.5rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.ml-chart img {
  width: 100%;
  border-radius: 0.75rem;
}

.ml-results h3 {
  font-size: 1.25rem;
  color: #343a40;
  margin-bottom: 1.5rem;
}

.model-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: 1.5rem;
}

.model-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background: white;
  border-radius: 0.75rem;
  border: 1px solid #F0EFEC;
}

.model-item.best {
  border-color: #81b29a;
  background: rgba(129, 178, 154, 0.05);
}

.model-name {
  font-weight: 500;
  color: #343a40;
}

.model-metrics {
  display: flex;
  gap: 1rem;
}

.metric {
  font-size: 0.85rem;
  color: #6c757d;
}

.metric.auc.highlight {
  color: #81b29a;
  font-weight: 600;
}

.best-model {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem;
  background: rgba(129, 178, 154, 0.15);
  border-radius: 0.75rem;
}

.best-badge {
  font-size: 0.875rem;
}

.best-name {
  font-weight: 600;
  color: #343a40;
}

.feature-importance {
  margin-bottom: 4rem;
}

.feature-importance h3 {
  font-size: 1.25rem;
  color: #343a40;
  margin-bottom: 1.5rem;
}

.importance-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
}

.importance-chart {
  background: white;
  padding: 1.5rem;
  border-radius: 1.5rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.importance-chart img {
  width: 100%;
  border-radius: 0.75rem;
}

.importance-bars {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.importance-bar {
  background: white;
  padding: 1rem 1.25rem;
  border-radius: 0.75rem;
}

.bar-label {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.bar-name {
  font-weight: 500;
  color: #343a40;
}

.bar-value {
  font-weight: 600;
  color: #5D8696;
}

.bar-track {
  height: 8px;
  background: #F0EFEC;
  border-radius: 4px;
  overflow: hidden;
}

.bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #C8DDF0, #81b29a);
  border-radius: 4px;
  transition: width 1s ease-out;
}

.shap-section h3 {
  font-size: 1.25rem;
  color: #343a40;
  margin-bottom: 1.5rem;
}

.shap-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin-bottom: 3rem;
}

.shap-card {
  background: white;
  border-radius: 1rem;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.shap-card img {
  width: 100%;
}

.shap-caption {
  padding: 1.25rem;
}

.shap-caption h4 {
  font-size: 1rem;
  color: #343a40;
  margin-bottom: 0.5rem;
}

.shap-caption p {
  font-size: 0.875rem;
  color: #6c757d;
  line-height: 1.5;
}

.ml-conclusion {
  background: white;
  border-radius: 1.5rem;
  padding: 2rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.conclusion-box h4 {
  font-size: 1.25rem;
  color: #343a40;
  margin-bottom: 1rem;
}

.conclusion-box ul {
  list-style: none;
  padding: 0;
}

.conclusion-box li {
  padding: 0.75rem 0;
  border-bottom: 1px solid #F0EFEC;
  color: #495057;
  line-height: 1.6;
}

.conclusion-box li:last-child {
  border-bottom: none;
}

.conclusion-box strong {
  color: #343a40;
}

/* ===== 結論 ===== */
.findings-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  margin-bottom: 4rem;
}

.finding-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  background: white;
  padding: 1.5rem;
  border-radius: 1rem;
  box-shadow: 0 2px 15px rgba(0,0,0,0.05);
}

.finding-icon {
  font-size: 2rem;
  flex-shrink: 0;
}

.finding-body {
  flex: 1;
}

.finding-body h4 {
  font-size: 1rem;
  color: #343a40;
  margin-bottom: 0.25rem;
}

.finding-body p {
  font-size: 0.9rem;
  color: #6c757d;
  line-height: 1.5;
}

.finding-impact {
  padding: 0.25rem 0.75rem;
  font-size: 0.75rem;
  font-weight: 500;
  border-radius: 1rem;
  flex-shrink: 0;
}

.finding-impact.high {
  background: rgba(224, 122, 95, 0.15);
  color: #e07a5f;
}

.finding-impact.medium {
  background: rgba(229, 180, 90, 0.15);
  color: #c99a3a;
}

.stats-summary {
  margin-bottom: 4rem;
}

.summary-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
}

.summary-item {
  background: white;
  padding: 2rem;
  border-radius: 1rem;
  text-align: center;
  box-shadow: 0 2px 15px rgba(0,0,0,0.05);
}

.summary-item.highlight {
  background: linear-gradient(135deg, #e07a5f 0%, #e5b45a 100%);
}

.summary-item.highlight .summary-num,
.summary-item.highlight .summary-txt {
  color: white;
}

.summary-num {
  display: block;
  font-size: 2.5rem;
  font-weight: 700;
  color: #343a40;
  margin-bottom: 0.25rem;
}

.summary-txt {
  font-size: 0.875rem;
  color: #6c757d;
}

.research-value {
  margin-bottom: 4rem;
}

.research-value h3 {
  font-size: 1.5rem;
  color: #343a40;
  text-align: center;
  margin-bottom: 2rem;
}

.value-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.value-card {
  background: white;
  padding: 2rem;
  border-radius: 1rem;
  text-align: center;
  box-shadow: 0 2px 15px rgba(0,0,0,0.05);
}

.value-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.value-card h4 {
  font-size: 1.125rem;
  color: #343a40;
  margin-bottom: 0.5rem;
}

.value-card p {
  font-size: 0.9rem;
  color: #6c757d;
  line-height: 1.6;
}

/* ===== Footer ===== */
.footer {
  padding-top: 4rem;
  border-top: 1px solid #E8E6E3;
}

.footer-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.footer-info h4 {
  font-size: 1.125rem;
  color: #343a40;
  margin-bottom: 0.25rem;
}

.footer-info p {
  color: #6c757d;
  font-size: 0.9rem;
}

.footer-source {
  margin-top: 0.5rem;
  font-size: 0.8rem !important;
  color: #adb5bd !important;
}

.footer-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: #343a40;
  color: white;
  text-decoration: none;
  border-radius: 0.5rem;
  font-size: 0.9rem;
  transition: background 0.2s;
}

.footer-link:hover {
  background: #495057;
}

.link-icon {
  width: 1.25rem;
  height: 1.25rem;
}

/* ===== 回到頂部 ===== */
.scroll-top-btn {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 3rem;
  height: 3rem;
  background: white;
  border: 1px solid #E8E6E3;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  transition: transform 0.2s, box-shadow 0.2s;
  z-index: 50;
}

.scroll-top-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.15);
}

.scroll-top-btn svg {
  width: 1.25rem;
  height: 1.25rem;
  color: #5D8696;
}

/* ===== 動畫 ===== */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* ===== 互動式 Hover 動畫 ===== */
.hover-lift {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.hover-lift:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 40px rgba(0,0,0,0.12);
}

/* ===== 資料概覽（新版大圖佈局） ===== */
.data-main-image {
  margin-bottom: 2.5rem;
}

.main-image-card {
  background: white;
  padding: 1.5rem;
  border-radius: 1.5rem;
  box-shadow: 0 4px 30px rgba(0,0,0,0.08);
}

.main-image-card img {
  width: 100%;
  border-radius: 1rem;
}

.data-stats-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card-large {
  background: white;
  padding: 2rem 1.5rem;
  border-radius: 1rem;
  text-align: center;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
}

.stat-card-large.primary {
  background: linear-gradient(135deg, #5D8696 0%, #81b29a 100%);
}

.stat-card-large.primary .stat-card-number,
.stat-card-large.primary .stat-card-unit,
.stat-card-large.primary .stat-card-label {
  color: white;
}

.stat-card-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: #343a40;
  line-height: 1;
}

.stat-card-unit {
  font-size: 1rem;
  color: #6c757d;
  font-weight: 500;
}

.stat-card-label {
  font-size: 0.9rem;
  color: #6c757d;
  margin-top: 0.25rem;
}

.data-method {
  background: white;
  padding: 1.5rem 2rem;
  border-radius: 1rem;
  margin-bottom: 2.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  box-shadow: 0 2px 10px rgba(0,0,0,0.03);
}

.method-badge {
  padding: 0.5rem 1rem;
  background: rgba(93, 134, 150, 0.15);
  color: #5D8696;
  font-size: 0.875rem;
  font-weight: 600;
  border-radius: 2rem;
  flex-shrink: 0;
}

.data-method p {
  color: #495057;
  font-size: 1rem;
  line-height: 1.6;
}

.sample-distribution {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.distribution-card {
  background: white;
  padding: 1rem;
  border-radius: 1rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
  text-align: center;
}

.distribution-card img {
  width: 100%;
  border-radius: 0.75rem;
  margin-bottom: 0.75rem;
}

.distribution-label {
  font-size: 0.9rem;
  color: #6c757d;
  font-weight: 500;
}

/* ===== PCA 分析（新版大圖佈局） ===== */
.pca-main-chart {
  margin-bottom: 2.5rem;
}

.pca-chart-large {
  background: white;
  padding: 2rem;
  border-radius: 1.5rem;
  box-shadow: 0 4px 30px rgba(0,0,0,0.08);
}

.pca-chart-large img {
  width: 100%;
  border-radius: 1rem;
}

.pca-highlight {
  text-align: center;
  margin-bottom: 3rem;
  padding: 2rem;
}

.highlight-number {
  font-size: 4.5rem;
  font-weight: 800;
  background: linear-gradient(135deg, #5D8696 0%, #81b29a 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1.1;
}

.highlight-text {
  font-size: 1.25rem;
  color: #6c757d;
  margin-top: 0.5rem;
}

.pca-findings-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  margin-bottom: 3rem;
}

.pca-finding-card {
  background: white;
  padding: 1.5rem;
  border-radius: 1rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.pca-finding-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.pca-finding-badge {
  padding: 0.35rem 0.75rem;
  font-size: 0.8rem;
  font-weight: 700;
  border-radius: 0.5rem;
  color: white;
}

.pca-finding-badge.pc1 { background: #5D8696; }
.pca-finding-badge.pc2 { background: #81b29a; }
.pca-finding-badge.pc3 { background: #e5b45a; }
.pca-finding-badge.pc4 { background: #e07a5f; }

.pca-finding-pct {
  font-size: 1rem;
  font-weight: 700;
  color: #343a40;
}

.pca-finding-bar {
  height: 6px;
  background: #F0EFEC;
  border-radius: 3px;
  margin-bottom: 1rem;
  overflow: hidden;
}

.pca-finding-fill {
  height: 100%;
  background: linear-gradient(90deg, #5D8696, #81b29a);
  border-radius: 3px;
  transition: width 1s ease-out;
}

.pca-finding-card h4 {
  font-size: 1rem;
  color: #343a40;
  margin-bottom: 0.5rem;
}

.pca-finding-card p {
  font-size: 0.85rem;
  color: #6c757d;
  line-height: 1.5;
}

.pca-insight {
  display: flex;
  gap: 1.5rem;
  background: white;
  padding: 2rem;
  border-radius: 1rem;
  border-left: 4px solid #81b29a;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.insight-icon {
  font-size: 2.5rem;
  flex-shrink: 0;
}

.insight-content h4 {
  font-size: 1.125rem;
  color: #343a40;
  margin-bottom: 0.5rem;
}

.insight-content p {
  color: #495057;
  line-height: 1.6;
}

.insight-content strong {
  color: #5D8696;
}

/* ===== ML 機器學習（新版大圖佈局） ===== */
.ml-main-chart {
  margin-bottom: 3rem;
}

.ml-chart-large {
  background: white;
  padding: 2rem;
  border-radius: 1.5rem;
  box-shadow: 0 4px 30px rgba(0,0,0,0.08);
}

.ml-chart-large img {
  width: 100%;
  border-radius: 1rem;
}

.ml-results-section {
  margin-bottom: 4rem;
}

.ml-results-section h3 {
  font-size: 1.5rem;
  color: #343a40;
  margin-bottom: 1.5rem;
}

.model-cards {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.model-card {
  background: white;
  padding: 1.25rem;
  border-radius: 1rem;
  box-shadow: 0 2px 15px rgba(0,0,0,0.05);
  text-align: center;
  border: 2px solid transparent;
}

.model-card.best {
  border-color: #81b29a;
  background: rgba(129, 178, 154, 0.05);
}

.model-card-name {
  font-size: 0.9rem;
  font-weight: 600;
  color: #343a40;
  margin-bottom: 1rem;
}

.model-card-metrics {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.model-metric {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
}

.metric-value {
  font-size: 1.25rem;
  font-weight: 700;
  color: #5D8696;
}

.metric-value.highlight {
  color: #81b29a;
}

.metric-label {
  font-size: 0.7rem;
  color: #6c757d;
  text-transform: uppercase;
}

.best-model-banner {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  padding: 1.25rem;
  background: linear-gradient(135deg, rgba(129, 178, 154, 0.2), rgba(93, 134, 150, 0.15));
  border-radius: 1rem;
}

.best-badge {
  font-size: 1rem;
}

.best-name {
  font-size: 1.125rem;
  font-weight: 700;
  color: #343a40;
}

.feature-importance-section {
  margin-bottom: 4rem;
}

.feature-importance-section h3 {
  font-size: 1.5rem;
  color: #343a40;
  margin-bottom: 1.5rem;
}

.importance-main-chart {
  background: white;
  padding: 1.5rem;
  border-radius: 1.5rem;
  box-shadow: 0 4px 30px rgba(0,0,0,0.08);
  margin-bottom: 2rem;
}

.importance-main-chart img {
  width: 100%;
  border-radius: 1rem;
}

.importance-interactive {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.importance-item {
  background: white;
  padding: 1.25rem;
  border-radius: 0.75rem;
  box-shadow: 0 2px 10px rgba(0,0,0,0.03);
}

.importance-info {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.importance-name {
  font-weight: 500;
  color: #343a40;
  font-size: 0.9rem;
}

.importance-value {
  font-weight: 700;
  color: #5D8696;
  font-size: 0.9rem;
}

.importance-track {
  height: 8px;
  background: #F0EFEC;
  border-radius: 4px;
  overflow: hidden;
}

.importance-fill {
  height: 100%;
  background: linear-gradient(90deg, #5D8696, #81b29a);
  border-radius: 4px;
  transition: width 1s ease-out;
}

.shap-grid-large {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin-bottom: 3rem;
}

.shap-card-large {
  background: white;
  border-radius: 1.5rem;
  overflow: hidden;
  box-shadow: 0 4px 30px rgba(0,0,0,0.08);
}

.shap-card-large img {
  width: 100%;
}

.shap-card-large .shap-caption {
  padding: 1.5rem;
}

.shap-card-large .shap-caption h4 {
  font-size: 1.125rem;
  color: #343a40;
  margin-bottom: 0.5rem;
}

.shap-card-large .shap-caption p {
  font-size: 0.95rem;
  color: #6c757d;
  line-height: 1.6;
}

.conclusion-box-large {
  background: white;
  padding: 2.5rem;
  border-radius: 1.5rem;
  box-shadow: 0 4px 30px rgba(0,0,0,0.08);
}

.conclusion-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
}

.conclusion-header .conclusion-icon {
  font-size: 2rem;
}

.conclusion-header h4 {
  font-size: 1.5rem;
  color: #343a40;
  margin: 0;
}

.conclusion-items {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}

.conclusion-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}

.item-number {
  font-size: 2rem;
  font-weight: 800;
  background: linear-gradient(135deg, #5D8696 0%, #81b29a 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1;
  flex-shrink: 0;
}

.item-text strong {
  display: block;
  font-size: 1rem;
  color: #343a40;
  margin-bottom: 0.25rem;
}

.item-text p {
  font-size: 0.9rem;
  color: #6c757d;
  margin: 0;
  line-height: 1.5;
}

/* ===== RWD ===== */
@media (max-width: 1024px) {
  .problem-grid,
  .data-grid,
  .pca-content,
  .ml-comparison,
  .importance-grid,
  .shap-grid,
  .shap-grid-large {
    grid-template-columns: 1fr;
  }

  .findings-grid {
    grid-template-columns: 1fr;
  }

  .summary-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .value-grid {
    grid-template-columns: 1fr;
  }

  .data-stats-row {
    grid-template-columns: repeat(2, 1fr);
  }

  .pca-findings-row {
    grid-template-columns: repeat(2, 1fr);
  }

  .model-cards {
    grid-template-columns: repeat(3, 1fr);
  }

  .importance-interactive {
    grid-template-columns: repeat(2, 1fr);
  }

  .conclusion-items {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 2rem;
  }

  .hero-stats {
    flex-direction: column;
    gap: 1.5rem;
  }

  .stat-divider {
    width: 3rem;
    height: 1px;
  }

  .nav-links {
    display: none;
  }

  .section {
    padding: 4rem 1rem;
  }

  .section-title {
    font-size: 1.75rem;
  }

  .method-flow {
    flex-direction: column;
  }

  .method-arrow {
    transform: rotate(90deg);
  }

  .cluster-grid {
    grid-template-columns: 1fr;
  }

  .summary-grid {
    grid-template-columns: 1fr;
  }

  .footer-content {
    flex-direction: column;
    gap: 1.5rem;
    text-align: center;
  }

  /* 新版佈局 RWD */
  .data-stats-row {
    grid-template-columns: 1fr;
  }

  .stat-card-number {
    font-size: 2rem;
  }

  .sample-distribution {
    grid-template-columns: 1fr;
  }

  .highlight-number {
    font-size: 3rem;
  }

  .pca-findings-row {
    grid-template-columns: 1fr;
  }

  .model-cards {
    grid-template-columns: 1fr;
  }

  .importance-interactive {
    grid-template-columns: 1fr;
  }

  .pca-insight,
  .data-method {
    flex-direction: column;
    text-align: center;
  }

  .pca-insight {
    border-left: none;
    border-top: 4px solid #81b29a;
  }
}
</style>
