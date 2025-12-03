import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/HomeView.vue'),
    meta: { title: '首頁' }
  },
  {
    path: '/overview',
    name: 'Overview',
    component: () => import('../views/OverviewView.vue'),
    meta: { title: '資料概覽' }
  },
  {
    path: '/models',
    name: 'Models',
    component: () => import('../views/ModelsView.vue'),
    meta: { title: 'ML 模型比較' }
  },
  {
    path: '/clusters',
    name: 'Clusters',
    component: () => import('../views/ClustersView.vue'),
    meta: { title: '聚類分析' }
  },
  {
    path: '/features',
    name: 'Features',
    component: () => import('../views/FeaturesView.vue'),
    meta: { title: '特徵重要性' }
  },
  {
    path: '/findings',
    name: 'Findings',
    component: () => import('../views/FindingsView.vue'),
    meta: { title: '研究發現' }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0, behavior: 'smooth' }
    }
  }
})

router.beforeEach((to, from, next) => {
  document.title = `${to.meta.title || '首頁'} | 網路霸凌傾向分析`
  next()
})

export default router
