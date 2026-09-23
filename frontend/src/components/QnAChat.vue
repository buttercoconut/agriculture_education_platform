
<template>
  <div class="qna-chat">
    <ul>
      <li v-for="msg in messages" :key="msg.id">
        <strong>{{ msg.user }}:</strong> {{ msg.text }}
      </li>
    </ul>
    <input v-model="newMessage" @keyup.enter="sendMessage" placeholder="질문 입력" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import io from 'socket.io-client'

const messages = ref([])
const newMessage = ref('')
const socket = io('https://api.example.com')

onMounted(() => {
  socket.on('message', (msg) => {
    messages.value.push(msg)
  })
})

function sendMessage() {
  if (newMessage.value.trim() === '') return
  const msg = { user: 'me', text: newMessage.value }
  socket.emit('message', msg)
  messages.value.push(msg)
  newMessage.value = ''
}
</script>
