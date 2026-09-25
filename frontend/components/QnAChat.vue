<template>
  <div>
    <h2>Q&A Chat</h2>
    <div v-for="msg in messages" :key="msg.id">
      {{ msg }}
    </div>
    <input v-model="input" @keyup.enter="send" placeholder="Type a message" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const messages = ref([])
const input = ref('')
let ws

onMounted(() => {
  ws = new WebSocket('ws://localhost:8000/api/qna/ws')
  ws.onmessage = (event) => {
    messages.value.push(event.data)
  }
})

const send = () => {
  if (input.value.trim()) {
    ws.send(input.value)
    input.value = ''
  }
}
</script>
