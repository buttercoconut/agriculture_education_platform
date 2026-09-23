<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script setup>
import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'
import Course from './views/Course.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/course/:id', component: Course, props: true }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

const app = createApp({})
app.use(router)
app.mount('#app')
</script>

<style>
/* global styles */
</style>
