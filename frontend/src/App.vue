<script setup>
import { RouterView, RouterLink, routeLocationKey } from 'vue-router';
import Menu from '../components/Menu.vue';
import Incident from '../components/Incident.vue';
</script>

<template>
  <Menu/>
  <main>
    <RouterView/>
  </main>
</template>