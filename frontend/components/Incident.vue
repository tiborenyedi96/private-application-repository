<!-- src/components/Incident.vue -->
<template>
  <article class="incident">
    <header class="incident-header">
      <h3 class="title">{{ incident.title || 'Untitled incident' }}</h3>
      <div class="badges">
        <span class="badge" :class="severityClass">{{ incident.severity || 'N/A' }}</span>
        <span class="badge" :class="statusClass">{{ incident.status || 'N/A' }}</span>
      </div>
    </header>

    <p class="description">{{ incident.description || '—' }}</p>

    <footer class="incident-footer">
      <span class="meta">Created at: {{ formattedDate }}</span>
    </footer>
  </article>
</template>

<script setup>
const props = defineProps({
  incident: { type: Object, required: true }
})

const formattedDate = new Date(props.incident.created_at).toLocaleString()

const severityClass = ({
  HIGH: 'error',
  MEDIUM: 'warning',
  LOW: 'success'
}[props.incident.severity]) || 'info'

const statusClass = ({
  RESOLVED: 'success',
  IN_PROGRESS: 'info',
  OPEN: 'error'
}[props.incident.status]) || 'info'
</script>

<style scoped>
.incident {
  background: #fff;
  border-radius: 14px;
  padding: 2rem;
  margin: 1.5rem auto;
  box-shadow: 0 2px 4px rgba(0,0,0,0.06),
              0 4px 6px rgba(0,0,0,0.1);
  max-width: 900px;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.incident-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.title {
  font-size: 1.8rem;
  font-weight: 700;
  margin: 0;
}

.description {
  font-size: 1.25rem;
  margin: 0;
  color: #374151;
  line-height: 1.6;
}

.incident-footer { margin-top: 0.75rem; }
.meta { font-size: 1rem; color: #6B7280; }

.badges { display: flex; gap: 0.75rem; }

.badge {
  display: inline-block;
  padding: 0.4rem 0.8rem;
  border-radius: 999px;
  font-size: 1rem;
  font-weight: 600;
}

.badge.success { background: #DCFCE7; color: #166534; }
.badge.warning { background: #FEF3C7; color: #92400E; }
.badge.error   { background: #FEE2E2; color: #B91C1C; }
.badge.info    { background: #DBEAFE; color: #1E40AF; }
</style>
