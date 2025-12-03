# 網路使用行為與霸凌傾向之多變量分析研究

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Data Source](https://img.shields.io/badge/資料來源-TCS%202021-green.svg)](https://www.crctaiwan.nctu.edu.tw/)
[![Analysis](https://img.shields.io/badge/分析方法-MVA-orange.svg)](#研究方法)
[![Vue.js](https://img.shields.io/badge/儀表板-Vue.js-42b883.svg)](#互動式儀表板)
[![線上展示](https://img.shields.io/badge/展示-線上版-brightgreen.svg)](https://timwei0801.github.io/MVA-Internet-use-and-bullying/)

> **[English README](README.md)**
>
> **[線上展示 / Live Demo](https://timwei0801.github.io/MVA-Internet-use-and-bullying/)**

---

## 目錄

- [摘要](#摘要)
- [研究背景](#研究背景)
- [資料說明](#資料說明)
- [研究方法](#研究方法)
- [主要發現](#主要發現)
- [互動式儀表板](#互動式儀表板)
- [專案結構](#專案結構)
- [安裝與使用](#安裝與使用)
- [引用](#引用)
- [作者](#作者)
- [授權](#授權)

---

## 摘要

本研究運用多變量分析技術，探討台灣成年人網路使用行為模式與霸凌傾向之間的關聯。使用**台灣傳播調查資料庫 2021**（N=672）數據，應用**廣義關聯圖（GAP）**、**主成分分析（PCA）**、**因素分析（FA）**、**典型相關分析（CCA）**以及**機器學習分類模型**，識別出不同的使用者群體與預測因子。

<p align="center">
  <img src="images/研究動機.png" alt="研究動機" width="80%"/>
</p>

### 主要結果

| 指標 | 數值 |
|------|------|
| 識別出的使用者群體 | **5 組** |
| 最佳預測模型表現（AUC-ROC） | **71%** |
| 最重要預測因子 | **年齡（39.7%）** |
| 高風險上網時數門檻 | **每日 >10 小時** |

---

## 研究背景

### 研究問題

1. 能否依據行為模式與人口特徵識別出不同的網路使用者群體？
2. 哪些因素最能預測高霸凌傾向？
3. 能否建立有效的風險預測模型以進行早期介入？

### 研究缺口與貢獻

| 文獻缺口 | 本研究貢獻 |
|---------|-----------|
| 聚焦青少年族群 | 擴展至 19-61 歲成年人 |
| 多變量方法應用有限 | 整合完整 MVA 分析框架 |
| 缺乏跨世代分析 | 建立五群體類型學 |

---

## 資料說明

### 資料來源

**台灣傳播調查資料庫 2021**

- **執行單位**：國立陽明交通大學傳播研究中心
- **抽樣方法**：分層三階段隨機撥號抽樣（RDD）

### 樣本特徵

| 屬性 | 數值 |
|------|------|
| 原始樣本 | 1,004 份 |
| 有效樣本 | 672 份 |
| 特徵變數 | 68 個 |
| 年齡範圍 | 19-61 歲 |
| 性別比例 | 男性 38.5%、女性 61.5% |

<p align="center">
  <img src="images/資料介紹.png" alt="資料概覽" width="70%"/>
</p>

<p align="center">
  <img src="images/性別分布圖.png" alt="性別分布" width="45%"/>
  <img src="images/網路使用時長分布圖.png" alt="網路使用時長分布" width="45%"/>
</p>

### 目標變數

**網路霸凌傾向分數**（由問卷題項加權計算之複合指標）

| 統計量 | 數值 |
|--------|------|
| 平均數 | 47.51 |
| 標準差 | 10.15 |
| 最小值 / 最大值 | 21.7 / 104.9 |
| Q1、中位數、Q3 | 40.9、46.45、53.6 |

---

## 研究方法

### 分析框架

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   廣義關聯圖     │ -> │  主成分/因素分析 │ -> │   典型相關分析   │ -> │    機器學習      │
│   (GAP)         │    │  (PCA/FA)       │    │   (CCA)         │    │   (ML)          │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
     群體識別              維度縮減              變數組關係            分類預測與解釋
```

### 1. 廣義關聯圖（GAP）

利用二元 GAP 視覺化，根據行為相似性矩陣識別資料中的自然群體。透過熱圖對角線模式揭示不同使用者群體。

<p align="center">
  <img src="images/GAP.png" alt="GAP 分析" width="80%"/>
</p>

### 2. 主成分分析（PCA）

萃取四個主成分，累積解釋變異量達 **69.79%**：

| 主成分 | 解釋變異量 | 詮釋 |
|--------|-----------|------|
| PC1 | 31.58% | 網路負面行為接觸程度 |
| PC2 | 18.25% | 網路衝突容忍度 |
| PC3 | 12.12% | 行為-態度矛盾 |
| PC4 | 7.85% | 群體擴散效應 |

<p align="center">
  <img src="images/主成分結構.png" alt="主成分結構" width="80%"/>
</p>

### 3. 因素分析（FA）

識別出四個潛在因素：

- **因素一**：網路行為規範認知
- **因素二**：霸凌行為表現
- **因素三**：負面影響認知
- **因素四**：衝突容忍度

<p align="center">
  <img src="images/因素分析結構.png" alt="因素分析結構" width="80%"/>
</p>

### 4. 典型相關分析（CCA）

探索兩組變數間的關係：

- **第一組**：網路使用模式（休閒時間、工作/學習時間、使用頻率）
- **第二組**：負面情緒指標

**第一典型相關係數**：r = 0.292（p < 0.001）

### 5. 機器學習分類

二元分類任務：**高風險** vs. **一般** 霸凌傾向

| 模型 | 準確率 | F1-Score | AUC-ROC |
|------|--------|----------|---------|
| **隨機森林** | 73.3% | 0.500 | **0.709** |
| 羅吉斯迴歸 | 68.2% | 0.506 | 0.706 |
| 梯度提升 | 74.1% | 0.407 | 0.677 |
| XGBoost | 68.9% | 0.475 | 0.664 |
| LightGBM | 68.9% | 0.475 | 0.683 |

<p align="center">
  <img src="images/ml/classification_results.png" alt="分類結果" width="80%"/>
</p>

### 6. SHAP 可解釋性分析

應用 SHAP（SHapley Additive exPlanations）進行模型解釋，揭示各特徵對預測結果的貢獻，實現透明化的決策洞察。

<p align="center">
  <img src="images/ml/shap_summary.png" alt="SHAP 摘要" width="45%"/>
  <img src="images/ml/shap_bar.png" alt="SHAP 長條圖" width="45%"/>
</p>

---

## 主要發現

### 聚類分析結果

| 群體 | 標籤 | 人數 | 佔比 | 平均分數 | 平均年齡 | 風險等級 |
|------|------|------|------|----------|----------|----------|
| 0 | 一般女性群 A | 133 | 19.8% | 46.02 | 39 | 中 |
| 1 | 重度網路使用者 | 73 | 10.9% | 50.32 | 32 | **高** |
| 2 | 低風險年長群 | 146 | 21.7% | 43.48 | 52 | 低 |
| 3 | 高風險男性群 | 182 | 27.1% | 51.08 | 39 | **高** |
| 4 | 一般女性群 B | 138 | 20.5% | 46.99 | 40 | 中 |

### 特徵重要性（隨機森林）

| 排名 | 特徵 | 重要性 | 類別 |
|------|------|--------|------|
| 1 | 年齡（出生年） | 39.66% | 人口統計 |
| 2 | 每日上網時數 | 17.04% | 行為特徵 |
| 3 | 居住地區 | 14.16% | 人口統計 |
| 4 | 社會焦慮程度 | 11.79% | 心理特徵 |
| 5 | 教育程度 | 10.63% | 人口統計 |
| 6 | 性別 | 6.72% | 人口統計 |

<p align="center">
  <img src="images/ml/rf_feature_importance.png" alt="特徵重要性" width="70%"/>
</p>

<p align="center">
  <img src="images/ml/clustering_visualization.png" alt="聚類視覺化" width="80%"/>
</p>

### 關鍵洞見

1. **年齡效應**：年輕使用者（<35 歲）霸凌傾向分數顯著高於年長者
2. **使用強度**：每日上網超過 10 小時者呈現較高風險特徵（群體 1：平均分數 50.32）
3. **性別差異**：以男性為主的群體 3 展現最高的平均霸凌傾向分數（51.08）
4. **態度行為落差**：PC3 揭示網路行為態度表述與實際行為模式間的顯著差異

---

## 互動式儀表板

提供 Vue.js 互動式儀表板，以現代化視覺效果與流暢動畫呈現分析結果。

### 功能特色

- **單頁敘事設計** - 滾動式故事流程呈現
- **互動式視覺化** - 懸停效果與動態動畫
- **響應式版面** - 行動裝置友善介面
- **GSAP 動畫** - 流暢的滾動觸發轉場

### 快速開始

```bash
cd dashboard
npm install
npm run dev
```

**訪問網址**：`http://localhost:5173`

### 儀表板區塊

1. **首頁（Hero）** - 研究概覽與核心指標
2. **研究問題** - 研究問題與方法框架
3. **資料概覽** - 資料集說明與樣本特徵
4. **GAP 分析** - 聚類分析視覺化與群體特徵
5. **PCA 分析** - 主成分結構與詮釋
6. **機器學習** - 模型比較與特徵重要性
7. **結論** - 主要發現與研究貢獻

---

## 專案結構

```
MVA-Cyberbullying-Analysis/
├── README.md                        # 英文文件
├── README_zh-TW.md                  # 中文文件
├── images/                          # 分析輸出圖表
│   ├── GAP.png
│   ├── 主成分結構.png
│   ├── 因素分析結構.png
│   └── ml/
│       ├── classification_results.png
│       ├── rf_feature_importance.png
│       ├── shap_summary.png
│       └── shap_bar.png
├── ML/                              # 機器學習腳本
│   ├── classification_model.py
│   └── shap_analysis.py
├── dashboard/                       # Vue.js 互動式儀表板
│   ├── src/
│   │   ├── App.vue                 # 主元件
│   │   └── data/
│   │       └── analysisData.js     # 數據常數
│   ├── public/images/              # 靜態資源
│   └── package.json
└── data/                            # 原始數據（未包含）
```

---

## 安裝與使用

### 前置需求

- Node.js >= 18.0
- Python >= 3.9（選用，供 ML 腳本使用）

### 儀表板設置

```bash
# 克隆專案
git clone https://github.com/yourusername/mva-cyberbullying-analysis.git
cd mva-cyberbullying-analysis

# 安裝依賴
cd dashboard
npm install

# 啟動開發伺服器
npm run dev

# 建置生產版本
npm run build
```

### ML 分析（選用）

```bash
# 建立虛擬環境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安裝依賴
pip install -r requirements.txt

# 執行分析
python ML/classification_model.py
```

---

## 引用

如使用本研究，請引用：

```bibtex
@thesis{hong2024cyberbullying,
  title     = {網路使用行為與霸凌傾向之多變量分析研究},
  author    = {洪維琪 (TimWei)},
  year      = {2024},
  school    = {淡江大學},
  department = {統計學系數據科學碩士班},
  type      = {課程專題},
  note      = {多變量分析期末報告}
}
```

---

## 作者

**TimWei（洪維琪）**

- **學程**：數據科學碩士班
- **系所**：統計學系
- **學校**：淡江大學

---

## 授權

本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 文件。

---

## 致謝

- **資料來源**：台灣傳播調查資料庫（TCS）
- **課程**：多變量分析（MVA），2024 秋季
- **機構**：淡江大學統計學系

---

<p align="center">
  <i>本研究致力於理解網路霸凌行為模式，以發展更有效的預防與介入策略。</i>
</p>
