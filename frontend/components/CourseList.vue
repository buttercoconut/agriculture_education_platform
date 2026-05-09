<template>
  <div class="course-list">
    <h2>교육 콘텐츠 목록</h2>
    <ul>
      <li v-for="course in courses" :key="course.id">
        <router-link :to="{ name: 'Course', params: { id: course.id } }">
          {{ course.title }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCourseStore } from '../store'

const store = useCourseStore()
const courses = store.courses

onMounted(() => {
  store.fetchCourses()
})
</script>

<style scoped>
.course-list ul {
  list-style: none;
  padding: 0;
}
.course-list li {
  margin: 0.5rem 0;
}
</style>
