
<template>
  <div class="lesson-detail">
    <h4>{{ lesson.title }}</h4>
    <p v-html="lesson.content" />
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({ lesson: Object })
</script>
