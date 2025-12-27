<script setup>
import { ref, onMounted } from 'vue'
import { getIncidents } from '/src/apihelper.js'
import Incident from '../components/Incident.vue'

const incidents = ref([])
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    incidents.value = await getIncidents()
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="incident-list">
    <h1>Incidents</h1>

    <p v-if="loading">Loading...</p>
    <p v-else-if="error" style="color:red">{{ error }}</p>

    <Incident
      v-for="incident in incidents"
      :key="incident.id"
      :incident="incident"
    />
  </div>
</template>

<style scoped>
.incident-list {
  max-width: 900px;
  margin: 2rem auto;
}
h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
}
</style>
