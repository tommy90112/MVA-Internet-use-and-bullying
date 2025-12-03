// 真實資料：來自台灣傳播調查資料庫 2021
// 網路霸凌傾向 ML 分析結果

export const projectInfo = {
  title: '網路霸凌傾向預測分析',
  subtitle: 'Cyberbullying Tendency Prediction Analysis',
  description: '運用機器學習技術分析網路使用者行為模式與霸凌傾向的關聯性研究',
  dataSource: '台灣傳播調查資料庫 2021',
  sampleSize: 672,
  features: 40,
  author: 'TimWei',
  institution: '淡江大學統計學系數據科學碩士班'
}

// 資料集統計摘要
export const datasetStats = {
  totalSamples: 672,
  totalFeatures: 68,
  targetVariable: 'total_score',
  targetStats: {
    mean: 47.51,
    std: 10.15,
    min: 21.7,
    max: 104.9,
    q25: 40.9,
    q50: 46.45,
    q75: 53.6
  },
  missingRate: 45.41,
  genderRatio: {
    male: 38.5,
    female: 61.5
  },
  ageRange: {
    min: 19,
    max: 61,
    mean: 40
  }
}

// 分類模型比較結果
export const classificationResults = [
  {
    model: 'Random Forest',
    accuracy: 0.7333,
    f1Score: 0.5000,
    aucRoc: 0.7088,
    cvMean: 0.4501,
    cvStd: 0.0157,
    color: '#10b981'
  },
  {
    model: 'Logistic Regression',
    accuracy: 0.6815,
    f1Score: 0.5057,
    aucRoc: 0.7056,
    cvMean: 0.4983,
    cvStd: 0.0808,
    color: '#3b82f6'
  },
  {
    model: 'Gradient Boosting',
    accuracy: 0.7407,
    f1Score: 0.4068,
    aucRoc: 0.6773,
    cvMean: 0.3692,
    cvStd: 0.0674,
    color: '#8b5cf6'
  },
  {
    model: 'XGBoost',
    accuracy: 0.6889,
    f1Score: 0.4750,
    aucRoc: 0.6637,
    cvMean: 0.4106,
    cvStd: 0.0375,
    color: '#f59e0b'
  },
  {
    model: 'LightGBM',
    accuracy: 0.6889,
    f1Score: 0.4750,
    aucRoc: 0.6832,
    cvMean: 0.4180,
    cvStd: 0.0344,
    color: '#ef4444'
  }
]

// 特徵重要性排名
export const featureImportance = [
  { feature: 'q2', name: '出生年（年齡）', importance: 0.3966, category: 'demographic' },
  { feature: 'q7', name: '每日上網時間', importance: 0.1704, category: 'behavior' },
  { feature: 'q3', name: '居住地區', importance: 0.1416, category: 'demographic' },
  { feature: 'q27_1', name: '社會焦慮程度', importance: 0.1179, category: 'psychology' },
  { feature: 'q4', name: '教育程度', importance: 0.1063, category: 'demographic' },
  { feature: 'q1', name: '性別', importance: 0.0672, category: 'demographic' }
]

// K-Means 聚類結果
export const clusterResults = [
  {
    cluster: 0,
    size: 133,
    percentage: 19.8,
    meanScore: 46.02,
    stdScore: 8.23,
    meanAge: 39,
    femaleRatio: 98.5,
    internetHours: 3.8,
    riskLevel: 'medium',
    label: '一般女性群',
    description: '以中年女性為主，網路使用適度，霸凌傾向中等',
    color: '#22c55e'
  },
  {
    cluster: 1,
    size: 73,
    percentage: 10.9,
    meanScore: 50.32,
    stdScore: 9.99,
    meanAge: 32,
    femaleRatio: 72.6,
    internetHours: 10.2,
    riskLevel: 'high',
    label: '重度網路使用者',
    description: '年輕族群，每日上網超過10小時，霸凌傾向較高',
    color: '#f59e0b'
  },
  {
    cluster: 2,
    size: 146,
    percentage: 21.7,
    meanScore: 43.48,
    stdScore: 9.52,
    meanAge: 52,
    femaleRatio: 62.3,
    internetHours: 3.8,
    riskLevel: 'low',
    label: '低風險年長群',
    description: '年長族群，網路使用保守，霸凌傾向最低',
    color: '#10b981'
  },
  {
    cluster: 3,
    size: 182,
    percentage: 27.1,
    meanScore: 51.08,
    stdScore: 11.24,
    meanAge: 39,
    femaleRatio: 0,
    internetHours: 3.7,
    riskLevel: 'high',
    label: '高風險男性群',
    description: '全為男性，霸凌傾向最高，需重點關注',
    color: '#ef4444'
  },
  {
    cluster: 4,
    size: 138,
    percentage: 20.5,
    meanScore: 46.99,
    stdScore: 9.10,
    meanAge: 40,
    femaleRatio: 100,
    internetHours: 3.7,
    riskLevel: 'medium',
    label: '一般女性群 B',
    description: '全為女性，網路使用適度，霸凌傾向中等',
    color: '#3b82f6'
  }
]

// ROC 曲線資料
export const rocCurveData = {
  randomForest: {
    fpr: [0, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
    tpr: [0, 0.25, 0.38, 0.48, 0.55, 0.65, 0.72, 0.78, 0.84, 0.89, 0.93, 0.97, 1],
    auc: 0.7088
  },
  logisticRegression: {
    fpr: [0, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
    tpr: [0, 0.22, 0.35, 0.45, 0.53, 0.63, 0.71, 0.77, 0.83, 0.88, 0.92, 0.96, 1],
    auc: 0.7056
  }
}

// 混淆矩陣資料
export const confusionMatrix = {
  trueNegative: 87,
  falsePositive: 14,
  falseNegative: 22,
  truePositive: 12,
  labels: ['一般', '高風險']
}

// 研究發現摘要
export const keyFindings = [
  {
    icon: '👤',
    title: '年齡效應顯著',
    description: '年輕族群（32歲以下）霸凌傾向明顯高於年長者',
    impact: 'high'
  },
  {
    icon: '⏰',
    title: '上網時間關聯',
    description: '每日上網超過10小時者，霸凌傾向顯著提升',
    impact: 'high'
  },
  {
    icon: '👨',
    title: '性別差異',
    description: '男性群組平均霸凌傾向分數高於女性群組',
    impact: 'medium'
  },
  {
    icon: '😰',
    title: '心理因素',
    description: '社會焦慮程度與霸凌傾向呈正相關',
    impact: 'high'
  }
]

// 分析方法說明
export const methodologies = [
  {
    name: '主成分分析 (PCA)',
    description: '降低維度，識別網路行為主要模式',
    icon: '📊',
    status: 'completed'
  },
  {
    name: '因素分析 (FA)',
    description: '探索問卷題項背後的潛在因素結構',
    icon: '🔍',
    status: 'completed'
  },
  {
    name: '典型相關分析 (CCA)',
    description: '探討網路使用與負面情緒的關聯',
    icon: '🔗',
    status: 'completed'
  },
  {
    name: '機器學習預測',
    description: 'Random Forest、XGBoost 等多模型比較',
    icon: '🤖',
    status: 'completed'
  },
  {
    name: 'K-Means 聚類',
    description: '識別不同類型的網路使用者群體',
    icon: '👥',
    status: 'completed'
  },
  {
    name: 'SHAP 解釋',
    description: '模型可解釋性分析，理解特徵貢獻',
    icon: '💡',
    status: 'completed'
  }
]
