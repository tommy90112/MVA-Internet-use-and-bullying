// 雙語翻譯檔案
export const translations = {
  zh: {
    // 導航列
    nav: {
      logo: '網路霸凌研究',
      home: '首頁',
      problem: '研究問題',
      data: '資料概覽',
      gap: 'GAP分析',
      pca: 'PCA分析',
      ml: '機器學習',
      conclusion: '結論'
    },
    // Hero 區塊
    hero: {
      badge: '統計學系數據科學所碩士班 ｜ MVA 專題報告呈現',
      title: '網路行為與霸凌傾向',
      highlight: '多變量分析研究',
      desc: '運用 GAP、PCA、機器學習等方法，探討不同群體的網路使用行為與霸凌傾向關聯',
      samples: '有效樣本',
      clusters: '群體分類',
      auc: '預測 AUC',
      cta: '開始探索'
    },
    // 研究問題
    problem: {
      section: '01',
      title: '研究問題',
      coreQuestion: '核心問題',
      coreText: '不同人口特徵與網路使用行為的群體，其<strong>網路霸凌傾向</strong>是否存在顯著差異？',
      sub1: '如何識別具有不同網路行為模式的群體？',
      sub2: '哪些因素最能預測高霸凌傾向？',
      sub3: '能否建立有效的風險預測模型？',
      methodTitle: '分析方法',
      gap: 'GAP 分析',
      gapDesc: '群體識別',
      pca: 'PCA 分析',
      pcaDesc: '維度縮減',
      ml: '機器學習',
      mlDesc: '預測模型',
      shap: 'SHAP',
      shapDesc: '模型解釋'
    },
    // 資料概覽
    data: {
      section: '02',
      title: '資料概覽',
      subtitle: '台灣傳播調查資料庫 2021',
      original: '原始樣本',
      valid: '有效樣本',
      features: '特徵變數',
      ageRange: '年齡範圍',
      unit: '份',
      unitFeature: '個',
      unitAge: '歲',
      samplingMethod: '抽樣方法',
      samplingDesc: '分層三階段 RDD 抽樣法（Stratified Three-Stage Random Digit Dialing），確保樣本具全國代表性',
      genderDist: '性別分布',
      internetDist: '每日上網時長分布'
    },
    // GAP 分析
    gap: {
      section: '03',
      title: 'GAP 廣義關聯圖分析',
      subtitle: '識別五種典型網路使用者群體',
      keyFinding: '關鍵發現',
      findingTitle: '透過熱圖對角線分布，清楚識別出五個行為群體',
      findingDesc: '淺黃色區塊代表群體內部高相似性，深色區塊代表群體間的行為差異',
      highRisk: '⚠ 高風險',
      mediumRisk: '中風險',
      lowRisk: '✓ 低風險',
      people: '人數',
      avgAge: '平均年齡',
      bullyScore: '霸凌分數',
      conclusionTitle: 'GAP 分析結論',
      conclusionText: '<strong>高風險群體（群1 + 群3）共 255 人，佔總樣本 38%</strong>。其中「高風險男性群」霸凌分數最高（51.08），「重度網路使用者」每日上網超過 10 小時。'
    },
    // PCA 分析
    pca: {
      section: '04',
      title: 'PCA 主成分分析',
      subtitle: '降低維度，識別網路行為主要模式',
      variance: '前四個主成分累積解釋變異量',
      pc1Title: '網路負面行為接觸觀察',
      pc1Desc: '反映受訪者在網路上觀察到的負面行為頻率，包含攻擊、責罵、諷刺等行為',
      pc2Title: '網路衝突容忍程度',
      pc2Desc: '反映對網路衝突行為的接受度，高分代表較能容忍對抗性互動',
      pc3Title: '行為-態度矛盾',
      pc3Desc: '揭示認知上反對網路暴力，但實際互動中仍展現攻擊性行為的現象',
      pc4Title: '群體擴散效應',
      pc4Desc: '網路負面行為透過群體動力產生擴散，形成連鎖反應',
      insightTitle: '關鍵洞見',
      insightText: 'PCA 結果顯示網路使用時間與霸凌傾向在第一主成分有較高載荷量，<strong>顯示兩者存在強烈關聯</strong>。長時間使用網路的用戶可能需要更多關注。'
    },
    // 機器學習
    ml: {
      section: '05',
      title: '機器學習預測模型',
      subtitle: '多模型比較與特徵重要性分析',
      modelComparison: '模型表現比較',
      bestModel: '🏆 最佳模型',
      featureRanking: '特徵重要性排名',
      shapTitle: 'SHAP 模型解釋',
      shapSummary: 'SHAP Summary Plot',
      shapSummaryDesc: '年齡越小（紅色），SHAP 值越高，被預測為高風險的機率較高',
      featureContrib: '特徵貢獻度',
      featureContribDesc: '年齡是最重要的預測因子，其次是每日上網時間與居住地區',
      keyFinding: '關鍵發現',
      ageEffect: '年齡效應最顯著',
      ageEffectDesc: '年輕族群霸凌傾向明顯高於年長者',
      internetEffect: '上網時間次之',
      internetEffectDesc: '每日上網超過 10 小時者風險顯著提升',
      regionEffect: '地區差異存在',
      regionEffectDesc: '都會區與非都會區使用者行為模式不同'
    },
    // 結論
    conclusion: {
      section: '06',
      title: '研究結論',
      validSamples: '有效樣本數',
      highRiskRatio: '高風險群佔比',
      bestAuc: '最佳 AUC-ROC',
      ageContrib: '年齡貢獻度',
      researchValue: '研究貢獻',
      theoryTitle: '理論層面',
      theoryDesc: '首次將 GAP 分析應用於網路行為研究，建立更完整的分析框架',
      methodTitle: '方法創新',
      methodDesc: '整合五種多變量分析方法，形成從探索到預測的完整分析鏈',
      practiceTitle: '實務應用',
      practiceDesc: '識別高風險群體特徵，為預防策略提供實證基礎',
      viewSource: '查看原始碼'
    },
    // 研究發現
    findings: {
      ageEffect: '年齡效應顯著',
      ageEffectDesc: '年輕族群（32歲以下）霸凌傾向明顯高於年長者',
      internetEffect: '上網時間關聯',
      internetEffectDesc: '每日上網超過10小時者，霸凌傾向顯著提升',
      genderEffect: '性別差異',
      genderEffectDesc: '男性群組平均霸凌傾向分數高於女性群組',
      psychEffect: '心理因素',
      psychEffectDesc: '社會焦慮程度與霸凌傾向呈正相關',
      highImpact: '高影響',
      mediumImpact: '中影響'
    },
    // 群體標籤
    clusters: {
      cluster0: '一般女性群',
      cluster0Desc: '以中年女性為主，網路使用適度，霸凌傾向中等',
      cluster1: '重度網路使用者',
      cluster1Desc: '年輕族群，每日上網超過10小時，霸凌傾向較高',
      cluster2: '低風險年長群',
      cluster2Desc: '年長族群，網路使用保守，霸凌傾向最低',
      cluster3: '高風險男性群',
      cluster3Desc: '全為男性，霸凌傾向最高，需重點關注',
      cluster4: '一般女性群 B',
      cluster4Desc: '全為女性，網路使用適度，霸凌傾向中等'
    },
    // 特徵名稱
    features: {
      age: '出生年（年齡）',
      internet: '每日上網時間',
      region: '居住地區',
      anxiety: '社會焦慮程度',
      education: '教育程度',
      gender: '性別'
    }
  },
  en: {
    // Navigation
    nav: {
      logo: 'Cyberbullying Research',
      home: 'Home',
      problem: 'Research',
      data: 'Data',
      gap: 'GAP',
      pca: 'PCA',
      ml: 'ML Models',
      conclusion: 'Conclusion'
    },
    // Hero Section
    hero: {
      badge: "Dept. of Statistics, Master's in Data Science | MVA Final Report",
      title: 'Internet Behavior & Bullying Tendency',
      highlight: 'Multivariate Analysis Study',
      desc: 'Using GAP, PCA, and Machine Learning to explore the relationship between internet usage behavior and cyberbullying tendency',
      samples: 'Valid Samples',
      clusters: 'User Clusters',
      auc: 'Prediction AUC',
      cta: 'Start Exploring'
    },
    // Research Questions
    problem: {
      section: '01',
      title: 'Research Questions',
      coreQuestion: 'Core Question',
      coreText: 'Do groups with different demographic and internet usage characteristics exhibit significant differences in <strong>cyberbullying tendency</strong>?',
      sub1: 'How can we identify groups with different internet behavior patterns?',
      sub2: 'Which factors best predict high cyberbullying tendency?',
      sub3: 'Can we build an effective risk prediction model?',
      methodTitle: 'Methodology',
      gap: 'GAP Analysis',
      gapDesc: 'Clustering',
      pca: 'PCA Analysis',
      pcaDesc: 'Dimension Reduction',
      ml: 'Machine Learning',
      mlDesc: 'Prediction Model',
      shap: 'SHAP',
      shapDesc: 'Model Interpretation'
    },
    // Data Overview
    data: {
      section: '02',
      title: 'Data Overview',
      subtitle: 'Taiwan Communication Survey 2021',
      original: 'Original Sample',
      valid: 'Valid Sample',
      features: 'Features',
      ageRange: 'Age Range',
      unit: '',
      unitFeature: '',
      unitAge: 'yrs',
      samplingMethod: 'Sampling Method',
      samplingDesc: 'Stratified Three-Stage Random Digit Dialing (RDD), ensuring national representativeness',
      genderDist: 'Gender Distribution',
      internetDist: 'Daily Internet Usage Distribution'
    },
    // GAP Analysis
    gap: {
      section: '03',
      title: 'GAP Analysis',
      subtitle: 'Identifying Five Distinct Internet User Groups',
      keyFinding: 'Key Finding',
      findingTitle: 'Five behavioral clusters clearly identified through heatmap diagonal patterns',
      findingDesc: 'Light yellow blocks represent high within-group similarity; dark blocks indicate behavioral differences between groups',
      highRisk: '⚠ High Risk',
      mediumRisk: 'Medium Risk',
      lowRisk: '✓ Low Risk',
      people: 'Size',
      avgAge: 'Avg Age',
      bullyScore: 'Bully Score',
      conclusionTitle: 'GAP Analysis Conclusion',
      conclusionText: '<strong>High-risk groups (Cluster 1 + 3) total 255 people, accounting for 38% of the sample</strong>. The "High-Risk Male Group" has the highest bullying score (51.08), while "Heavy Internet Users" spend over 10 hours online daily.'
    },
    // PCA Analysis
    pca: {
      section: '04',
      title: 'PCA Analysis',
      subtitle: 'Dimensionality Reduction & Internet Behavior Pattern Identification',
      variance: 'Cumulative variance explained by first 4 components',
      pc1Title: 'Exposure to Negative Online Behavior',
      pc1Desc: 'Reflects the frequency of observing negative behaviors online, including attacks, scolding, and sarcasm',
      pc2Title: 'Online Conflict Tolerance',
      pc2Desc: 'Reflects acceptance of online conflict behavior; higher scores indicate greater tolerance for confrontational interactions',
      pc3Title: 'Behavior-Attitude Discrepancy',
      pc3Desc: 'Reveals cognitive opposition to online violence while still exhibiting aggressive behavior in actual interactions',
      pc4Title: 'Group Diffusion Effect',
      pc4Desc: 'Negative online behaviors spread through group dynamics, creating chain reactions',
      insightTitle: 'Key Insight',
      insightText: 'PCA results show that internet usage time and bullying tendency have high loadings on PC1, <strong>indicating a strong correlation</strong>. Heavy internet users may require more attention.'
    },
    // Machine Learning
    ml: {
      section: '05',
      title: 'Machine Learning Models',
      subtitle: 'Model Comparison & Feature Importance Analysis',
      modelComparison: 'Model Performance Comparison',
      bestModel: '🏆 Best Model',
      featureRanking: 'Feature Importance Ranking',
      shapTitle: 'SHAP Model Interpretation',
      shapSummary: 'SHAP Summary Plot',
      shapSummaryDesc: 'Younger age (red) corresponds to higher SHAP values, indicating higher probability of being predicted as high-risk',
      featureContrib: 'Feature Contribution',
      featureContribDesc: 'Age is the most important predictor, followed by daily internet hours and region',
      keyFinding: 'Key Findings',
      ageEffect: 'Age Effect Most Significant',
      ageEffectDesc: 'Younger groups have significantly higher bullying tendency than older groups',
      internetEffect: 'Internet Time Secondary',
      internetEffectDesc: 'Users with >10 hours daily internet usage show significantly elevated risk',
      regionEffect: 'Regional Differences Exist',
      regionEffectDesc: 'Urban and rural users exhibit different behavioral patterns'
    },
    // Conclusion
    conclusion: {
      section: '06',
      title: 'Research Conclusions',
      validSamples: 'Valid Samples',
      highRiskRatio: 'High-Risk Ratio',
      bestAuc: 'Best AUC-ROC',
      ageContrib: 'Age Contribution',
      researchValue: 'Research Contributions',
      theoryTitle: 'Theoretical',
      theoryDesc: 'First application of GAP analysis to internet behavior research, establishing a more comprehensive analytical framework',
      methodTitle: 'Methodological',
      methodDesc: 'Integration of five multivariate analysis methods, forming a complete analytical chain from exploration to prediction',
      practiceTitle: 'Practical',
      practiceDesc: 'Identification of high-risk group characteristics, providing empirical basis for prevention strategies',
      viewSource: 'View Source Code'
    },
    // Research Findings
    findings: {
      ageEffect: 'Significant Age Effect',
      ageEffectDesc: 'Younger users (under 32) show significantly higher bullying tendency than older users',
      internetEffect: 'Internet Time Correlation',
      internetEffectDesc: 'Users with >10 hours daily internet usage show significantly elevated bullying tendency',
      genderEffect: 'Gender Difference',
      genderEffectDesc: 'Male groups have higher average bullying tendency scores than female groups',
      psychEffect: 'Psychological Factor',
      psychEffectDesc: 'Social anxiety level is positively correlated with bullying tendency',
      highImpact: 'High Impact',
      mediumImpact: 'Medium Impact'
    },
    // Cluster Labels
    clusters: {
      cluster0: 'General Female Group',
      cluster0Desc: 'Mainly middle-aged women, moderate internet use, medium bullying tendency',
      cluster1: 'Heavy Internet Users',
      cluster1Desc: 'Younger group, >10 hours online daily, higher bullying tendency',
      cluster2: 'Low-Risk Elderly',
      cluster2Desc: 'Older group, conservative internet use, lowest bullying tendency',
      cluster3: 'High-Risk Male Group',
      cluster3Desc: 'All male, highest bullying tendency, requires special attention',
      cluster4: 'General Female Group B',
      cluster4Desc: 'All female, moderate internet use, medium bullying tendency'
    },
    // Feature Names
    features: {
      age: 'Birth Year (Age)',
      internet: 'Daily Internet Hours',
      region: 'Region',
      anxiety: 'Social Anxiety Level',
      education: 'Education Level',
      gender: 'Gender'
    }
  }
}

export const getClusterLabel = (cluster, lang) => {
  const labels = {
    zh: ['一般女性群', '重度網路使用者', '低風險年長群', '高風險男性群', '一般女性群 B'],
    en: ['General Female Group', 'Heavy Internet Users', 'Low-Risk Elderly', 'High-Risk Male Group', 'General Female Group B']
  }
  return labels[lang][cluster] || labels['zh'][cluster]
}

export const getClusterDesc = (cluster, lang) => {
  const descs = {
    zh: [
      '以中年女性為主，網路使用適度，霸凌傾向中等',
      '年輕族群，每日上網超過10小時，霸凌傾向較高',
      '年長族群，網路使用保守，霸凌傾向最低',
      '全為男性，霸凌傾向最高，需重點關注',
      '全為女性，網路使用適度，霸凌傾向中等'
    ],
    en: [
      'Mainly middle-aged women, moderate internet use, medium bullying tendency',
      'Younger group, >10 hours online daily, higher bullying tendency',
      'Older group, conservative internet use, lowest bullying tendency',
      'All male, highest bullying tendency, requires special attention',
      'All female, moderate internet use, medium bullying tendency'
    ]
  }
  return descs[lang][cluster] || descs['zh'][cluster]
}

export const getFeatureName = (feature, lang) => {
  const names = {
    zh: {
      'q2': '出生年（年齡）',
      'q7': '每日上網時間',
      'q3': '居住地區',
      'q27_1': '社會焦慮程度',
      'q4': '教育程度',
      'q1': '性別'
    },
    en: {
      'q2': 'Birth Year (Age)',
      'q7': 'Daily Internet Hours',
      'q3': 'Region',
      'q27_1': 'Social Anxiety Level',
      'q4': 'Education Level',
      'q1': 'Gender'
    }
  }
  return names[lang][feature] || names['zh'][feature] || feature
}
