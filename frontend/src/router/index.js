import { createRouter, createWebHistory } from 'vue-router'
import incidentListView from '../../views/incidentListView.vue'
import incidentSubmitView from '../../views/incidentSubmitView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: incidentListView
    },
    {
      path: '/submitIncident',
      component: incidentSubmitView
    }
  ],
})

export default router
