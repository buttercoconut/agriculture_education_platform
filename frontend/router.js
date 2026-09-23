import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Course from '@/views/Course.vue'
import QA from '@/views/QA.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/course/:id', name: 'Course', component: Course, props: true },
  { path: '/qa', name: 'QA', component: QA },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
