import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

const router = new Router({
  routes: [{
      path: '/app',
      name: 'app',
      component: require('@/App').default,
    },
    {
      path: '/home',
      name: 'home',
      component: require('@/presentations/mainPresentation').default,
      children: [{
          path: 'lista-cameras',
          name: 'lista-cameras',
          component: require('@/components/ListaCameras/listaCameras').default
        },
        {
          // when /home/camera/:id is matched
          path: 'camera/:id',
          name: 'camera',
          component: require('@/components/Live/liveContainer').default
        },
        {
          // when /home/camera/:id is matched
          path: 'camera/edit/:id',
          name: 'edit-camera',
          component: require('@/components/EditCamera/editCameraContainer').default
        },
        {
          // when /home/add-camera is matched
          path: 'add-camera',
          name: 'add-camera',
          component: require('@/components/AddCamera/AddCameraContainer').default
        }
      ]
    }

  ]
})

export default router
