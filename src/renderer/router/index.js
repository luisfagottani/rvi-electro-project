import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/app',
      name: 'app',
      component: require('@/presentations/mainPresentation').default,
      children: [
        {
          // when /app/ao-vivo is matched
          path: 'ao-vivo',
          name: 'ao-vivo',
          component: require('@/components/Live/liveContainer').default
        }
      ]
    }

  ]
})
