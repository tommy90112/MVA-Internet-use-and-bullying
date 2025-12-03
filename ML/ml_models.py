"""
網路霸凌傾向預測 - 機器學習模型
=====================================
使用 Random Forest、XGBoost、LightGBM 進行預測
並進行 K-Means 聚類分析

資料來源：台灣傳播調查資料庫 2021 年真實數據
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import Ridge, Lasso, LogisticRegression
from sklearn.metrics import (mean_squared_error, r2_score, mean_absolute_error,
                           classification_report, confusion_matrix, accuracy_score,
                           roc_auc_score, f1_score, precision_score, recall_score)
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings('ignore')

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft JhengHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 建立輸出資料夾
import os
OUTPUT_DIR = 'output'
os.makedirs(OUTPUT_DIR, exist_ok=True)


class CyberbullyingMLAnalyzer:
    """網路霸凌傾向 ML 分析器"""

    def __init__(self, data_path):
        """載入真實資料"""
        print("=" * 60)
        print("載入真實資料集...")
        print("=" * 60)
        self.df = pd.read_csv(data_path)
        print(f"資料維度: {self.df.shape}")
        print(f"樣本數: {self.df.shape[0]}")
        print(f"變數數: {self.df.shape[1]}")

        # 目標變數統計
        print(f"\n目標變數 (total_score) 統計:")
        print(self.df['total_score'].describe())

    def prepare_features(self):
        """準備特徵變數 - 只使用獨立於 total_score 計算的變數"""
        print("\n" + "=" * 60)
        print("準備特徵變數...")
        print("=" * 60)

        # ============================================
        # 重要：特徵選擇策略
        # ============================================
        # total_score 由 q17, q19, q22, q23, q25, q26 計算
        # 因此我們只使用這些變數以外的特徵來預測
        # 這樣可以避免資料洩漏 (data leakage)
        # ============================================

        # 人口統計變數
        demo_vars = ['q1', 'q2', 'q3', 'q4']  # 性別、出生年、地區、教育

        # 上網時間
        time_vars = ['q7']

        # 即時通訊軟體使用 (q9系列)
        q9_vars = [col for col in self.df.columns if col.startswith('q9_') and col != 'q9_90']

        # 社群媒體使用 (q10系列)
        q10_vars = [col for col in self.df.columns if col.startswith('q10_') and col != 'q10_90']

        # 影音平台使用 (q11系列)
        q11_vars = [col for col in self.df.columns if col.startswith('q11_') and col != 'q11_90']

        # 心理健康與網路依賴 (獨立變數)
        psych_vars = ['q28_1', 'q28_2', 'q28_3', 'q28_5',  # 心理健康
                     'q29_1', 'q29_2', 'q29_3', 'q29_4',   # 網路依賴
                     'q27_1']  # 社會焦慮

        # 合併所有特徵
        all_features = demo_vars + time_vars + q9_vars + q10_vars + q11_vars + psych_vars

        # 只保留存在的欄位
        self.feature_cols = [col for col in all_features if col in self.df.columns]

        print(f"選取的特徵變數數量: {len(self.feature_cols)}")

        # 特徵名稱對照表
        self.feature_names = {
            'q1': '性別', 'q2': '出生年', 'q3': '居住地區', 'q4': '教育程度',
            'q7': '每日上網時間',
            'q9_1': 'LINE', 'q9_2': 'FB Messenger', 'q9_3': 'WeChat',
            'q9_4': 'WhatsApp', 'q9_5': 'Telegram', 'q9_6': 'Discord',
            'q9_7': 'Skype', 'q9_8': '其他即時通訊',
            'q10_1': 'Facebook', 'q10_2': 'Instagram', 'q10_3': 'Twitter',
            'q10_4': 'Dcard', 'q10_5': 'PTT', 'q10_6': 'TikTok',
            'q10_7': 'LinkedIn', 'q10_8': 'Threads', 'q10_9': '小紅書', 'q10_10': '其他社群',
            'q11_1': 'YouTube', 'q11_2': '愛奇藝', 'q11_3': 'Netflix',
            'q11_4': 'Disney+', 'q11_5': 'HBO GO', 'q11_6': 'LINE TV',
            'q11_7': 'friDay', 'q11_8': '其他影音',
            'q27_1': '社會焦慮',
            'q28_1': '心理健康1', 'q28_2': '心理健康2',
            'q28_3': '心理健康3', 'q28_5': '心理健康5',
            'q29_1': '網路依賴1', 'q29_2': '網路依賴2',
            'q29_3': '網路依賴3', 'q29_4': '網路依賴4'
        }

        # 準備 X
        self.X = self.df[self.feature_cols].copy()

        # 處理缺失值 - 使用中位數填補
        missing_before = self.X.isnull().sum().sum()
        for col in self.X.columns:
            if self.X[col].isnull().any():
                self.X[col].fillna(self.X[col].median(), inplace=True)

        print(f"缺失值處理: {missing_before} → 0")

        # ============================================
        # 建立分類目標變數 (高風險 vs 低風險)
        # ============================================
        # 使用第 75 百分位數作為高風險閾值
        threshold_high = self.df['total_score'].quantile(0.75)
        threshold_low = self.df['total_score'].quantile(0.25)

        print(f"\n風險分群閾值:")
        print(f"  高風險 (>= {threshold_high:.1f}): 前 25%")
        print(f"  低風險 (<= {threshold_low:.1f}): 後 25%")

        # 二分類：高風險 vs 其他
        self.y_binary = (self.df['total_score'] >= threshold_high).astype(int)
        print(f"\n二分類 (高風險=1):")
        print(f"  高風險: {self.y_binary.sum()} ({self.y_binary.mean()*100:.1f}%)")
        print(f"  一般: {len(self.y_binary) - self.y_binary.sum()} ({(1-self.y_binary.mean())*100:.1f}%)")

        # 三分類：低/中/高風險
        self.y_multi = pd.cut(self.df['total_score'],
                             bins=[0, threshold_low, threshold_high, float('inf')],
                             labels=[0, 1, 2]).astype(int)
        print(f"\n三分類 (低=0, 中=1, 高=2):")
        print(self.y_multi.value_counts().sort_index())

        # 連續目標 (回歸用)
        self.y_continuous = self.df['total_score'].copy()

        # 特徵標準化
        self.scaler = StandardScaler()
        self.X_scaled = self.scaler.fit_transform(self.X)

        return self

    def train_classification_models(self):
        """訓練分類模型 - 預測高風險群"""
        print("\n" + "=" * 60)
        print("訓練分類模型 (預測高風險群)")
        print("=" * 60)

        # 分割資料
        X_train, X_test, y_train, y_test = train_test_split(
            self.X_scaled, self.y_binary, test_size=0.2, random_state=42, stratify=self.y_binary
        )

        self.X_train_clf = X_train
        self.X_test_clf = X_test
        self.y_train_clf = y_train
        self.y_test_clf = y_test

        print(f"\n資料分割:")
        print(f"  訓練集: {len(X_train)} 筆 (高風險: {y_train.sum()})")
        print(f"  測試集: {len(X_test)} 筆 (高風險: {y_test.sum()})")

        # 儲存各模型結果
        self.clf_results = {}

        # ============================================
        # 1. Logistic Regression (基準模型)
        # ============================================
        print("\n" + "-" * 40)
        print("【Logistic Regression】")
        print("-" * 40)

        self.lr_model = LogisticRegression(random_state=42, max_iter=1000, class_weight='balanced')
        self.lr_model.fit(X_train, y_train)

        y_pred_lr = self.lr_model.predict(X_test)
        y_prob_lr = self.lr_model.predict_proba(X_test)[:, 1]

        acc_lr = accuracy_score(y_test, y_pred_lr)
        f1_lr = f1_score(y_test, y_pred_lr)
        auc_lr = roc_auc_score(y_test, y_prob_lr)

        print(f"Accuracy: {acc_lr:.4f}")
        print(f"F1 Score: {f1_lr:.4f}")
        print(f"AUC-ROC: {auc_lr:.4f}")

        cv_lr = cross_val_score(self.lr_model, self.X_scaled, self.y_binary, cv=5, scoring='f1')
        print(f"5-fold CV F1: {cv_lr.mean():.4f} (+/- {cv_lr.std()*2:.4f})")

        self.clf_results['Logistic Regression'] = {
            'accuracy': acc_lr, 'f1': f1_lr, 'auc': auc_lr,
            'cv_mean': cv_lr.mean(), 'cv_std': cv_lr.std(),
            'y_pred': y_pred_lr, 'y_prob': y_prob_lr
        }

        # ============================================
        # 2. Random Forest Classifier
        # ============================================
        print("\n" + "-" * 40)
        print("【Random Forest Classifier】")
        print("-" * 40)

        self.rf_clf = RandomForestClassifier(
            n_estimators=100, max_depth=8, min_samples_split=10,
            class_weight='balanced', random_state=42, n_jobs=-1
        )
        self.rf_clf.fit(X_train, y_train)

        y_pred_rf = self.rf_clf.predict(X_test)
        y_prob_rf = self.rf_clf.predict_proba(X_test)[:, 1]

        acc_rf = accuracy_score(y_test, y_pred_rf)
        f1_rf = f1_score(y_test, y_pred_rf)
        auc_rf = roc_auc_score(y_test, y_prob_rf)

        print(f"Accuracy: {acc_rf:.4f}")
        print(f"F1 Score: {f1_rf:.4f}")
        print(f"AUC-ROC: {auc_rf:.4f}")

        cv_rf = cross_val_score(self.rf_clf, self.X_scaled, self.y_binary, cv=5, scoring='f1')
        print(f"5-fold CV F1: {cv_rf.mean():.4f} (+/- {cv_rf.std()*2:.4f})")

        self.clf_results['Random Forest'] = {
            'accuracy': acc_rf, 'f1': f1_rf, 'auc': auc_rf,
            'cv_mean': cv_rf.mean(), 'cv_std': cv_rf.std(),
            'y_pred': y_pred_rf, 'y_prob': y_prob_rf
        }

        # 特徵重要性
        self.rf_clf_importance = pd.DataFrame({
            'feature': self.feature_cols,
            'importance': self.rf_clf.feature_importances_
        }).sort_values('importance', ascending=False)

        print("\n【特徵重要性 Top 10】")
        top_features = self.rf_clf_importance.head(10).copy()
        top_features['feature_name'] = top_features['feature'].map(
            lambda x: self.feature_names.get(x, x)
        )
        print(top_features[['feature_name', 'importance']].to_string(index=False))

        # ============================================
        # 3. Gradient Boosting Classifier
        # ============================================
        print("\n" + "-" * 40)
        print("【Gradient Boosting Classifier】")
        print("-" * 40)

        self.gb_clf = GradientBoostingClassifier(
            n_estimators=100, max_depth=5, learning_rate=0.1,
            random_state=42
        )
        self.gb_clf.fit(X_train, y_train)

        y_pred_gb = self.gb_clf.predict(X_test)
        y_prob_gb = self.gb_clf.predict_proba(X_test)[:, 1]

        acc_gb = accuracy_score(y_test, y_pred_gb)
        f1_gb = f1_score(y_test, y_pred_gb)
        auc_gb = roc_auc_score(y_test, y_prob_gb)

        print(f"Accuracy: {acc_gb:.4f}")
        print(f"F1 Score: {f1_gb:.4f}")
        print(f"AUC-ROC: {auc_gb:.4f}")

        cv_gb = cross_val_score(self.gb_clf, self.X_scaled, self.y_binary, cv=5, scoring='f1')
        print(f"5-fold CV F1: {cv_gb.mean():.4f} (+/- {cv_gb.std()*2:.4f})")

        self.clf_results['Gradient Boosting'] = {
            'accuracy': acc_gb, 'f1': f1_gb, 'auc': auc_gb,
            'cv_mean': cv_gb.mean(), 'cv_std': cv_gb.std(),
            'y_pred': y_pred_gb, 'y_prob': y_prob_gb
        }

        # ============================================
        # 4. XGBoost (如果有安裝)
        # ============================================
        try:
            import xgboost as xgb
            print("\n" + "-" * 40)
            print("【XGBoost Classifier】")
            print("-" * 40)

            self.xgb_clf = xgb.XGBClassifier(
                n_estimators=100, max_depth=5, learning_rate=0.1,
                scale_pos_weight=(len(y_train) - y_train.sum()) / y_train.sum(),
                random_state=42, n_jobs=-1, eval_metric='logloss'
            )
            self.xgb_clf.fit(X_train, y_train)

            y_pred_xgb = self.xgb_clf.predict(X_test)
            y_prob_xgb = self.xgb_clf.predict_proba(X_test)[:, 1]

            acc_xgb = accuracy_score(y_test, y_pred_xgb)
            f1_xgb = f1_score(y_test, y_pred_xgb)
            auc_xgb = roc_auc_score(y_test, y_prob_xgb)

            print(f"Accuracy: {acc_xgb:.4f}")
            print(f"F1 Score: {f1_xgb:.4f}")
            print(f"AUC-ROC: {auc_xgb:.4f}")

            cv_xgb = cross_val_score(self.xgb_clf, self.X_scaled, self.y_binary, cv=5, scoring='f1')
            print(f"5-fold CV F1: {cv_xgb.mean():.4f} (+/- {cv_xgb.std()*2:.4f})")

            self.clf_results['XGBoost'] = {
                'accuracy': acc_xgb, 'f1': f1_xgb, 'auc': auc_xgb,
                'cv_mean': cv_xgb.mean(), 'cv_std': cv_xgb.std(),
                'y_pred': y_pred_xgb, 'y_prob': y_prob_xgb
            }

        except ImportError:
            print("\nXGBoost 未安裝，跳過")

        # ============================================
        # 5. LightGBM (如果有安裝)
        # ============================================
        try:
            import lightgbm as lgb
            print("\n" + "-" * 40)
            print("【LightGBM Classifier】")
            print("-" * 40)

            self.lgb_clf = lgb.LGBMClassifier(
                n_estimators=100, max_depth=5, learning_rate=0.1,
                class_weight='balanced', random_state=42, n_jobs=-1, verbose=-1
            )
            self.lgb_clf.fit(X_train, y_train)

            y_pred_lgb = self.lgb_clf.predict(X_test)
            y_prob_lgb = self.lgb_clf.predict_proba(X_test)[:, 1]

            acc_lgb = accuracy_score(y_test, y_pred_lgb)
            f1_lgb = f1_score(y_test, y_pred_lgb)
            auc_lgb = roc_auc_score(y_test, y_prob_lgb)

            print(f"Accuracy: {acc_lgb:.4f}")
            print(f"F1 Score: {f1_lgb:.4f}")
            print(f"AUC-ROC: {auc_lgb:.4f}")

            cv_lgb = cross_val_score(self.lgb_clf, self.X_scaled, self.y_binary, cv=5, scoring='f1')
            print(f"5-fold CV F1: {cv_lgb.mean():.4f} (+/- {cv_lgb.std()*2:.4f})")

            self.clf_results['LightGBM'] = {
                'accuracy': acc_lgb, 'f1': f1_lgb, 'auc': auc_lgb,
                'cv_mean': cv_lgb.mean(), 'cv_std': cv_lgb.std(),
                'y_pred': y_pred_lgb, 'y_prob': y_prob_lgb
            }

        except ImportError:
            print("\nLightGBM 未安裝，跳過")

        return self

    def train_regression_models(self):
        """訓練回歸模型 - 預測連續分數"""
        print("\n" + "=" * 60)
        print("訓練回歸模型 (預測連續分數)")
        print("=" * 60)

        # 分割資料
        X_train, X_test, y_train, y_test = train_test_split(
            self.X_scaled, self.y_continuous, test_size=0.2, random_state=42
        )

        self.X_train_reg = X_train
        self.X_test_reg = X_test
        self.y_train_reg = y_train
        self.y_test_reg = y_test

        self.reg_results = {}

        # ============================================
        # 1. Ridge Regression
        # ============================================
        print("\n" + "-" * 40)
        print("【Ridge Regression】")
        print("-" * 40)

        self.ridge_model = Ridge(alpha=1.0, random_state=42)
        self.ridge_model.fit(X_train, y_train)

        y_pred_ridge = self.ridge_model.predict(X_test)
        r2_ridge = r2_score(y_test, y_pred_ridge)
        rmse_ridge = np.sqrt(mean_squared_error(y_test, y_pred_ridge))
        mae_ridge = mean_absolute_error(y_test, y_pred_ridge)

        print(f"R²: {r2_ridge:.4f}")
        print(f"RMSE: {rmse_ridge:.4f}")
        print(f"MAE: {mae_ridge:.4f}")

        cv_ridge = cross_val_score(self.ridge_model, self.X_scaled, self.y_continuous, cv=5, scoring='r2')
        print(f"5-fold CV R²: {cv_ridge.mean():.4f} (+/- {cv_ridge.std()*2:.4f})")

        self.reg_results['Ridge'] = {
            'r2': r2_ridge, 'rmse': rmse_ridge, 'mae': mae_ridge,
            'cv_mean': cv_ridge.mean(), 'cv_std': cv_ridge.std(),
            'y_pred': y_pred_ridge
        }

        # ============================================
        # 2. Random Forest Regressor
        # ============================================
        print("\n" + "-" * 40)
        print("【Random Forest Regressor】")
        print("-" * 40)

        self.rf_reg = RandomForestRegressor(
            n_estimators=100, max_depth=8, min_samples_split=10,
            random_state=42, n_jobs=-1
        )
        self.rf_reg.fit(X_train, y_train)

        y_pred_rf = self.rf_reg.predict(X_test)
        r2_rf = r2_score(y_test, y_pred_rf)
        rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))
        mae_rf = mean_absolute_error(y_test, y_pred_rf)

        print(f"R²: {r2_rf:.4f}")
        print(f"RMSE: {rmse_rf:.4f}")
        print(f"MAE: {mae_rf:.4f}")

        cv_rf = cross_val_score(self.rf_reg, self.X_scaled, self.y_continuous, cv=5, scoring='r2')
        print(f"5-fold CV R²: {cv_rf.mean():.4f} (+/- {cv_rf.std()*2:.4f})")

        self.reg_results['Random Forest'] = {
            'r2': r2_rf, 'rmse': rmse_rf, 'mae': mae_rf,
            'cv_mean': cv_rf.mean(), 'cv_std': cv_rf.std(),
            'y_pred': y_pred_rf
        }

        # 特徵重要性
        self.rf_reg_importance = pd.DataFrame({
            'feature': self.feature_cols,
            'importance': self.rf_reg.feature_importances_
        }).sort_values('importance', ascending=False)

        return self

    def kmeans_clustering(self, n_clusters=5):
        """K-Means 聚類分析"""
        print("\n" + "=" * 60)
        print("K-Means 聚類分析")
        print("=" * 60)

        # 使用肘部法則決定最佳群數
        inertias = []
        silhouettes = []
        K_range = range(2, 11)

        from sklearn.metrics import silhouette_score

        for k in K_range:
            kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
            labels = kmeans.fit_predict(self.X_scaled)
            inertias.append(kmeans.inertia_)
            silhouettes.append(silhouette_score(self.X_scaled, labels))

        # 繪製肘部圖和輪廓係數圖
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        ax = axes[0]
        ax.plot(K_range, inertias, 'bo-', linewidth=2, markersize=8)
        ax.set_xlabel('群數 (K)', fontsize=12)
        ax.set_ylabel('Inertia', fontsize=12)
        ax.set_title('肘部法則', fontsize=14)
        ax.grid(True, alpha=0.3)

        ax = axes[1]
        ax.plot(K_range, silhouettes, 'ro-', linewidth=2, markersize=8)
        ax.set_xlabel('群數 (K)', fontsize=12)
        ax.set_ylabel('Silhouette Score', fontsize=12)
        ax.set_title('輪廓係數', fontsize=14)
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig(f'{OUTPUT_DIR}/kmeans_elbow_silhouette.png', dpi=150, bbox_inches='tight')
        plt.close()
        print(f"已儲存: {OUTPUT_DIR}/kmeans_elbow_silhouette.png")

        # 找出最佳 K (輪廓係數最高)
        best_k = K_range[np.argmax(silhouettes)]
        print(f"\n最佳群數 (依輪廓係數): K = {best_k}")
        print(f"使用者指定群數: K = {n_clusters}")

        # 使用指定群數進行聚類
        self.kmeans_model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        self.cluster_labels = self.kmeans_model.fit_predict(self.X_scaled)

        # 將聚類結果加入資料
        cluster_df = self.X.copy()
        cluster_df['cluster'] = self.cluster_labels
        cluster_df['total_score'] = self.y_continuous.values

        # 計算各群描述統計
        print(f"\n【{n_clusters} 群聚類結果】")

        # 性別對照
        gender_map = {1: '男性', 2: '女性'}

        for i in range(n_clusters):
            group = cluster_df[cluster_df['cluster'] == i]
            print(f"\n群 {i} (n={len(group)}, {len(group)/len(cluster_df)*100:.1f}%):")
            print(f"  霸凌傾向: mean={group['total_score'].mean():.2f}, std={group['total_score'].std():.2f}")
            print(f"  平均出生年: {group['q2'].mean():.0f} (約{2024-1911-group['q2'].mean():.0f}歲)")
            print(f"  性別比例: 女性 {(group['q1']==2).mean()*100:.1f}%")
            print(f"  每日上網: {group['q7'].mean():.1f} 小時")

        self.cluster_df = cluster_df
        self.silhouette_scores = silhouettes

        return self

    def plot_classification_results(self):
        """繪製分類結果視覺化"""
        print("\n" + "=" * 60)
        print("繪製分類模型視覺化")
        print("=" * 60)

        from sklearn.metrics import roc_curve, auc, precision_recall_curve

        fig, axes = plt.subplots(2, 2, figsize=(14, 12))

        # ============================================
        # 1. ROC 曲線比較
        # ============================================
        ax = axes[0, 0]
        for model_name, results in self.clf_results.items():
            fpr, tpr, _ = roc_curve(self.y_test_clf, results['y_prob'])
            roc_auc = auc(fpr, tpr)
            ax.plot(fpr, tpr, linewidth=2, label=f'{model_name} (AUC={roc_auc:.3f})')

        ax.plot([0, 1], [0, 1], 'k--', linewidth=1, label='隨機猜測')
        ax.set_xlabel('False Positive Rate', fontsize=12)
        ax.set_ylabel('True Positive Rate', fontsize=12)
        ax.set_title('ROC 曲線比較', fontsize=14)
        ax.legend(loc='lower right')
        ax.grid(True, alpha=0.3)

        # ============================================
        # 2. 模型指標比較
        # ============================================
        ax = axes[0, 1]
        models = list(self.clf_results.keys())
        x = np.arange(len(models))
        width = 0.25

        metrics = ['accuracy', 'f1', 'auc']
        colors = ['steelblue', 'darkorange', 'green']

        for i, (metric, color) in enumerate(zip(metrics, colors)):
            values = [self.clf_results[m][metric] for m in models]
            bars = ax.bar(x + i*width, values, width, label=metric.upper(), color=color, alpha=0.8)

        ax.set_ylabel('分數', fontsize=12)
        ax.set_title('分類模型指標比較', fontsize=14)
        ax.set_xticks(x + width)
        ax.set_xticklabels(models, rotation=15, ha='right')
        ax.legend()
        ax.set_ylim(0, 1)
        ax.grid(True, alpha=0.3, axis='y')

        # ============================================
        # 3. 混淆矩陣 (最佳模型)
        # ============================================
        ax = axes[1, 0]
        best_model = max(self.clf_results.keys(), key=lambda x: self.clf_results[x]['f1'])
        cm = confusion_matrix(self.y_test_clf, self.clf_results[best_model]['y_pred'])

        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
                   xticklabels=['一般', '高風險'], yticklabels=['一般', '高風險'])
        ax.set_xlabel('預測', fontsize=12)
        ax.set_ylabel('實際', fontsize=12)
        ax.set_title(f'混淆矩陣 ({best_model})', fontsize=14)

        # ============================================
        # 4. 特徵重要性
        # ============================================
        ax = axes[1, 1]
        top_n = 12
        top_features = self.rf_clf_importance.head(top_n).copy()
        top_features['feature_name'] = top_features['feature'].map(
            lambda x: self.feature_names.get(x, x)
        )

        colors = plt.cm.Blues(np.linspace(0.4, 0.9, top_n))[::-1]
        bars = ax.barh(range(top_n), top_features['importance'].values, color=colors)
        ax.set_yticks(range(top_n))
        ax.set_yticklabels(top_features['feature_name'].values)
        ax.set_xlabel('重要性分數', fontsize=12)
        ax.set_title('Random Forest 特徵重要性', fontsize=14)
        ax.invert_yaxis()
        ax.grid(True, alpha=0.3, axis='x')

        plt.tight_layout()
        plt.savefig(f'{OUTPUT_DIR}/classification_results.png', dpi=150, bbox_inches='tight')
        plt.close()
        print(f"已儲存: {OUTPUT_DIR}/classification_results.png")

        return self

    def plot_clustering_results(self):
        """繪製聚類結果視覺化"""
        print("\n繪製聚類結果...")

        # PCA 降維到 2D
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(self.X_scaled)

        fig, axes = plt.subplots(2, 2, figsize=(14, 12))

        # ============================================
        # 1. PCA 空間聚類分布
        # ============================================
        ax = axes[0, 0]
        scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1],
                            c=self.cluster_labels, cmap='Set1',
                            alpha=0.6, s=50)
        centers_pca = pca.transform(self.kmeans_model.cluster_centers_)
        ax.scatter(centers_pca[:, 0], centers_pca[:, 1],
                  c='black', marker='X', s=200, edgecolors='white', linewidths=2)
        ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)', fontsize=12)
        ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)', fontsize=12)
        ax.set_title('K-Means 聚類 (PCA 空間)', fontsize=14)
        plt.colorbar(scatter, ax=ax, label='群組')
        ax.grid(True, alpha=0.3)

        # ============================================
        # 2. 各群霸凌傾向箱型圖
        # ============================================
        ax = axes[0, 1]
        cluster_data = [self.cluster_df[self.cluster_df['cluster'] == i]['total_score']
                       for i in range(len(np.unique(self.cluster_labels)))]

        bp = ax.boxplot(cluster_data, patch_artist=True)
        colors = plt.cm.Set1(np.linspace(0, 1, len(cluster_data)))

        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)

        ax.set_xlabel('群組', fontsize=12)
        ax.set_ylabel('霸凌傾向總分', fontsize=12)
        ax.set_title('各群組霸凌傾向分布', fontsize=14)
        ax.grid(True, alpha=0.3, axis='y')

        for i, data in enumerate(cluster_data):
            ax.text(i+1, ax.get_ylim()[1]*0.98, f'n={len(data)}',
                   ha='center', va='top', fontsize=10)

        # ============================================
        # 3. 各群平均特徵雷達圖 (簡化版用棒狀圖)
        # ============================================
        ax = axes[1, 0]

        # 選取重要特徵計算各群平均
        key_features = ['q2', 'q7', 'q27_1']
        feature_labels = ['出生年', '上網時間', '社會焦慮']

        cluster_means = []
        for i in range(len(np.unique(self.cluster_labels))):
            group = self.cluster_df[self.cluster_df['cluster'] == i]
            means = [group[f].mean() for f in key_features]
            cluster_means.append(means)

        cluster_means = np.array(cluster_means)

        # 標準化以便比較
        cluster_means_norm = (cluster_means - cluster_means.mean(axis=0)) / cluster_means.std(axis=0)

        x = np.arange(len(key_features))
        width = 0.15
        colors = plt.cm.Set1(np.linspace(0, 1, len(cluster_means)))

        for i, (means, color) in enumerate(zip(cluster_means_norm, colors)):
            ax.bar(x + i*width, means, width, label=f'群 {i}', color=color, alpha=0.8)

        ax.set_ylabel('標準化平均值', fontsize=12)
        ax.set_title('各群特徵比較', fontsize=14)
        ax.set_xticks(x + width * 2)
        ax.set_xticklabels(feature_labels)
        ax.legend()
        ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        ax.grid(True, alpha=0.3, axis='y')

        # ============================================
        # 4. 群組大小與平均霸凌分數
        # ============================================
        ax = axes[1, 1]

        cluster_sizes = [len(self.cluster_df[self.cluster_df['cluster'] == i])
                        for i in range(len(np.unique(self.cluster_labels)))]
        cluster_scores = [self.cluster_df[self.cluster_df['cluster'] == i]['total_score'].mean()
                         for i in range(len(np.unique(self.cluster_labels)))]

        scatter = ax.scatter(cluster_sizes, cluster_scores, s=300, c=range(len(cluster_sizes)),
                            cmap='Set1', edgecolors='black', linewidths=2)

        for i, (size, score) in enumerate(zip(cluster_sizes, cluster_scores)):
            ax.annotate(f'群 {i}', (size, score), textcoords="offset points",
                       xytext=(0, 10), ha='center', fontsize=12, fontweight='bold')

        ax.set_xlabel('群組大小', fontsize=12)
        ax.set_ylabel('平均霸凌傾向分數', fontsize=12)
        ax.set_title('群組大小 vs 霸凌傾向', fontsize=14)
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig(f'{OUTPUT_DIR}/clustering_visualization.png', dpi=150, bbox_inches='tight')
        plt.close()
        print(f"已儲存: {OUTPUT_DIR}/clustering_visualization.png")

        return self

    def generate_shap_analysis(self):
        """生成 SHAP 分析"""
        print("\n" + "=" * 60)
        print("SHAP 特徵解釋分析")
        print("=" * 60)

        try:
            import shap

            # 使用 Random Forest 分類器
            explainer = shap.TreeExplainer(self.rf_clf)

            # 取樣本
            sample_size = min(200, len(self.X_test_clf))
            X_sample = self.X_test_clf[:sample_size]

            shap_values = explainer.shap_values(X_sample)

            # 取正類的 SHAP 值
            if isinstance(shap_values, list):
                shap_values = shap_values[1]

            display_names = [self.feature_names.get(f, f) for f in self.feature_cols]

            # SHAP Summary Plot
            fig, ax = plt.subplots(figsize=(12, 10))
            shap.summary_plot(shap_values, X_sample,
                            feature_names=display_names,
                            show=False, max_display=15)
            plt.title('SHAP 特徵重要性 (高風險預測)', fontsize=14)
            plt.tight_layout()
            plt.savefig(f'{OUTPUT_DIR}/shap_summary.png', dpi=150, bbox_inches='tight')
            plt.close()
            print(f"已儲存: {OUTPUT_DIR}/shap_summary.png")

            # SHAP Bar Plot
            fig, ax = plt.subplots(figsize=(12, 8))
            shap.summary_plot(shap_values, X_sample,
                            feature_names=display_names,
                            plot_type='bar', show=False, max_display=15)
            plt.title('SHAP 平均絕對值', fontsize=14)
            plt.tight_layout()
            plt.savefig(f'{OUTPUT_DIR}/shap_bar.png', dpi=150, bbox_inches='tight')
            plt.close()
            print(f"已儲存: {OUTPUT_DIR}/shap_bar.png")

            print("SHAP 分析完成!")

        except ImportError:
            print("SHAP 未安裝，跳過此分析")
            print("安裝方式: pip install shap")

        return self

    def save_results(self):
        """儲存分析結果"""
        print("\n" + "=" * 60)
        print("儲存分析結果")
        print("=" * 60)

        # 分類模型比較
        clf_summary = pd.DataFrame([
            {
                'Model': name,
                'Accuracy': results['accuracy'],
                'F1 Score': results['f1'],
                'AUC-ROC': results['auc'],
                'CV F1 Mean': results['cv_mean'],
                'CV F1 Std': results['cv_std']
            }
            for name, results in self.clf_results.items()
        ])
        clf_summary.to_csv(f'{OUTPUT_DIR}/classification_comparison.csv', index=False, encoding='utf-8-sig')
        print(f"已儲存: {OUTPUT_DIR}/classification_comparison.csv")

        # 回歸模型比較
        reg_summary = pd.DataFrame([
            {
                'Model': name,
                'R²': results['r2'],
                'RMSE': results['rmse'],
                'MAE': results['mae'],
                'CV R² Mean': results['cv_mean'],
                'CV R² Std': results['cv_std']
            }
            for name, results in self.reg_results.items()
        ])
        reg_summary.to_csv(f'{OUTPUT_DIR}/regression_comparison.csv', index=False, encoding='utf-8-sig')
        print(f"已儲存: {OUTPUT_DIR}/regression_comparison.csv")

        # 特徵重要性
        self.rf_clf_importance.to_csv(f'{OUTPUT_DIR}/feature_importance.csv', index=False, encoding='utf-8-sig')
        print(f"已儲存: {OUTPUT_DIR}/feature_importance.csv")

        # 聚類結果
        self.cluster_df.to_csv(f'{OUTPUT_DIR}/clustering_results.csv', index=False, encoding='utf-8-sig')
        print(f"已儲存: {OUTPUT_DIR}/clustering_results.csv")

        # 聚類摘要
        cluster_summary = []
        for i in range(len(np.unique(self.cluster_labels))):
            group = self.cluster_df[self.cluster_df['cluster'] == i]
            cluster_summary.append({
                'Cluster': i,
                'Size': len(group),
                'Percentage': f"{len(group)/len(self.cluster_df)*100:.1f}%",
                'Mean Score': group['total_score'].mean(),
                'Std Score': group['total_score'].std(),
                'Mean Age': 2024 - 1911 - group['q2'].mean(),
                'Female Ratio': f"{(group['q1']==2).mean()*100:.1f}%",
                'Mean Internet Hours': group['q7'].mean()
            })

        pd.DataFrame(cluster_summary).to_csv(f'{OUTPUT_DIR}/cluster_summary.csv', index=False, encoding='utf-8-sig')
        print(f"已儲存: {OUTPUT_DIR}/cluster_summary.csv")

        print("\n" + "=" * 60)
        print("所有結果已儲存!")
        print("=" * 60)

        return self


def main():
    """主程式"""
    print("=" * 60)
    print("網路霸凌傾向預測 - 機器學習分析")
    print("資料來源: 台灣傳播調查資料庫 2021 (真實資料)")
    print("=" * 60)

    # 初始化分析器
    data_path = '../data/processed_data_with_score.csv'
    analyzer = CyberbullyingMLAnalyzer(data_path)

    # 執行分析流程
    analyzer.prepare_features()
    analyzer.train_classification_models()
    analyzer.train_regression_models()
    analyzer.kmeans_clustering(n_clusters=5)

    # 視覺化
    analyzer.plot_classification_results()
    analyzer.plot_clustering_results()
    analyzer.generate_shap_analysis()

    # 儲存結果
    analyzer.save_results()

    print("\n" + "=" * 60)
    print("分析完成!")
    print("=" * 60)

    return analyzer


if __name__ == "__main__":
    analyzer = main()
