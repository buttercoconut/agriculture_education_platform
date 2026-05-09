import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Course from '../views/Course.vue'
import Lesson from '../views/Lesson.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/course/:id', name: 'Course', component: Course, props: true },
  { path: '/lesson/:id', name: 'Lesson', component: Lesson, props: true },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
