<template>
  <div>
    <h2>Q&A Chat</h2>
    <ul>
      <li v-for="msg in messages" :key="msg.id">
        <strong>{{ msg.user }}:</strong> {{ msg.content }}
      </li>
    </ul>
    <input v-model="newMessage" @keyup.enter="sendMessage" placeholder="Type a message..." />
  </div>
</template>

<script setup>
import { ref } from 'vue'

const messages = ref([])
const newMessage = ref('')

function sendMessage() {
  if (!newMessage.value) return
  messages.value.push({ id: Date.now(), user: 'You', content: newMessage.value })
  newMessage.value = ''
}
</script>
