import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/welcolme',
      name: 'welcomeConfiguration',
      component: require('@/presentations/WelcomePresentation').default
    },
    {
      path: '/app',
      name: 'app',
      component: require('@/presentations/mainPresentation').default
    }

  ]
})
