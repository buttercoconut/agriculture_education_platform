<template>
  <div class="course-page">
    <h1>{{ course.title }}</h1>
    <p>{{ course.description }}</p>
    <ul>
      <li v-for="module in course.modules" :key="module.id">
        <strong>{{ module.title }}</strong>
        <ul>
          <li v-for="lesson in module.lessons" :key="lesson.id">
            <router-link :to="{ name: 'Lesson', params: { id: lesson.id } }">
              {{ lesson.title }}
            </router-link>
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCourseStore } from '../store'
import { useRoute } from 'vue-router'

const route = useRoute()
const store = useCourseStore()
const course = store.selectedCourse

onMounted(() => {
  store.fetchCourse(route.params.id)
})
</script>

<style scoped>
.course-page {
  padding: 1rem;
}
</style>
