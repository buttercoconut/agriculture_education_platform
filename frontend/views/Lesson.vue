<template>
  <div class="lesson-page">
    <LessonDetail :lessonId="lessonId" />
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import LessonDetail from '../components/LessonDetail.vue'

const route = useRoute()
const lessonId = Number(route.params.id)
</script>

<style scoped>
.lesson-page {
  padding: 1rem;
}
</style>
