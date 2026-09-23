
<template>
  <div class="course-page">
    <h2>{{ course.title }}</h2>
    <p>{{ course.description }}</p>
    <LessonDetail :lesson="course.lessons[0]" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import LessonDetail from '../components/LessonDetail.vue'

const props = defineProps({ id: String })
const course = ref({ title: '', description: '', lessons: [] })

onMounted(async () => {
  const res = await axios.get(`https://api.example.com/courses/${props.id}`)
  course.value = res.data
})
</script>
