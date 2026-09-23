
<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const courses = ref([])

onMounted(async () => {
  const res = await axios.get('https://api.example.com/courses')
  courses.value = res.data
})
</script>

<template>
  <div>
    <h1>코스 목록</h1>
    <ul>
      <li v-for="course in courses" :key="course.id">
        <router-link :to="`/course/${course.id}`">{{ course.title }}</router-link>
      </li>
    </ul>
  </div>
</template>
