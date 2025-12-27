<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <nav class="tabbar">
    <RouterLink to="/" class="tab">View incidents</RouterLink>
    <RouterLink to="/submitIncident" class="tab">Submit incident</RouterLink>
  </nav>
</template>

<style scoped>
.tabbar {
  display: flex;
  justify-content: center;
  gap: 3rem;
  background: #2563EB; /* primary */
  padding: 0.5rem 1rem;
}

.tab {
  color: rgba(255,255,255,0.8);
  font-size: 2rem;
  text-decoration: none;
  padding: 0.5rem 0;
  border-bottom: 3px solid transparent;
  transition: all 0.2s ease;
}

.tab:hover {
  color: #fff;
}

.router-link-active {
  color: #fff;
  border-bottom-color: #fff;
  font-weight: 600;
}
</style>
