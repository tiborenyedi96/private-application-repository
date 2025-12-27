<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { createIncident } from '/src/apihelper.js'

const router = useRouter()

const title = ref('')
const description = ref('')
const severity = ref('LOW')
const loading = ref(false)
const error = ref('')
const titleMax = 64
const descMax = 2000

async function submit() {
  error.value = ''
  const t = title.value.trim()
  const d = description.value.trim()
  if (!t || !d) {
    error.value = 'Title and description are required.'
    return
  }
  if (t.length > titleMax) {
    error.value = `Title must be ≤ ${titleMax} characters.`
    return
  }
  if (d.length > descMax) {
    error.value = `Description must be ≤ ${descMax} characters.`
    return
  }

  loading.value = true
  try {
    await createIncident({ title: t, description: d, severity: severity.value })
    router.push('/')
  } catch (e) {
    error.value = String(e?.message || e)
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="page">
    <h1>Submit incident</h1>

    <form class="form" @submit.prevent="submit" novalidate>
      <label class="field">
        <span class="label">Title <span class="req">*</span></span>
        <input v-model="title" :maxlength="titleMax" required placeholder="Short summary"/>
        <span class="hint">{{ title.length }}/{{ titleMax }}</span>
      </label>

      <label class="field">
        <span class="label">Description <span class="req">*</span></span>
        <textarea v-model="description" :maxlength="descMax" rows="6" required
                  placeholder="What happened, impact, workaround…"/>
        <span class="hint">{{ description.length }}/{{ descMax }}</span>
      </label>

      <label class="field">
        <span class="label">Severity</span>
        <select v-model="severity">
          <option value="LOW">LOW</option>
          <option value="MEDIUM">MEDIUM</option>
          <option value="HIGH">HIGH</option>
        </select>
      </label>

      <div class="actions">
        <button class="btn secondary" type="button" @click="router.push('/')">Cancel</button>
        <button class="btn primary" type="submit" :disabled="loading">
          {{ loading ? 'Submitting…' : 'Create incident' }}
        </button>
      </div>

      <p v-if="error" class="error">{{ error }}</p>
    </form>
  </div>
</template>

<style scoped>
.page {
  max-width: 820px;
  margin: 0 auto;
  padding: 0 auto;
  color: #111827;
}
h1 {
  font-size: 2rem;
  margin: 0 0 1rem;
}
.form {
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 1px 2px rgba(0,0,0,.06), 0 1px 4px rgba(0,0,0,.08);
  padding: 5rem;
  display: grid;
  gap: 1rem;
}
.field { display: grid; gap: .5rem; }
.label { font-weight: 600; }
.req { color:#DC2626; }

input, textarea, select {
  width: 100%;
  font-size: 1.05rem;
  padding: .75rem .9rem;
  border: 1px solid #E5E7EB;
  border-radius: 10px;
  background: #fff;
  color: #111827;
  outline: none;
}
input:focus, textarea:focus, select:focus {
  border-color: #2563EB;
  box-shadow: 0 0 0 3px rgba(37,99,235,.15);
}
.hint { color: #6B7280; font-size: .85rem; }

.actions {
  display: flex;
  justify-content: flex-end;
  gap: .75rem;
  margin-top: .25rem;
}
.btn {
  font-size: 1rem;
  padding: .6rem 1rem;
  border-radius: 10px;
  border: 1px solid transparent;
  cursor: pointer;
}
.btn.primary {
  background: #2563EB;
  color: #fff;
}
.btn.primary:disabled {
  opacity: .7;
  cursor: not-allowed;
}
.btn.primary:not(:disabled):hover {
  background: #1D4ED8;
}
.btn.secondary {
  background: #fff;
  border-color: #E5E7EB;
  color: #111827;
}
.btn.secondary:hover {
  background: #F3F4F6;
}
.error {
  color:#B91C1C;
  font-weight:600;
  margin:.25rem 0 0;
}
</style>
