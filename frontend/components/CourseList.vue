<template>
  <div>
    <h2>Course List</h2>
    <ul>
      <li v-for="course in courses" :key="course.id">
        {{ course.title }} - {{ course.description }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const courses = ref([])

onMounted(async () => {
  const res = await axios.get('http://localhost:8000/api/course/')
  courses.value = res.data
})
</script>
