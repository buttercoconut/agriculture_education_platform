<template>
  <div class="lesson-detail">
    <h2>{{ lesson.title }}</h2>
    <p>{{ lesson.content }}</p>
    <div v-if="lesson.videoUrl">
      <video :src="lesson.videoUrl" controls width="100%"></video>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const props = defineProps({
  lessonId: { type: Number, required: true },
})

const lesson = ref({})

onMounted(async () => {
  const res = await axios.get(`/api/lessons/${props.lessonId}`)
  lesson.value = res.data
})
</script>

<style scoped>
.lesson-detail {
  padding: 1rem;
}
</style>
