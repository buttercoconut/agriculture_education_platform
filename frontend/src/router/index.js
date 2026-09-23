
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Course from '../views/Course.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/course/:id', component: Course, props: true }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
