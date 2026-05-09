import { defineStore } from 'pinia'
import axios from 'axios'

export const useCourseStore = defineStore('course', {
  state: () => ({
    courses: [],
    selectedCourse: null,
  }),
  actions: {
    async fetchCourses() {
      const res = await axios.get('/api/courses')
      this.courses = res.data
    },
    async fetchCourse(id) {
      const res = await axios.get(`/api/courses/${id}`)
      this.selectedCourse = res.data
    },
  },
})
