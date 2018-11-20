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
      component: require('@/presentations/MainPresentation').default,
      children: [{
          path: 'lista-cameras',
          name: 'lista-cameras',
          component: require('@/components/ListaCameras/ListaCameras').default
        },
        {
          path: 'select-camera',
          name: 'select-camera',
          component: require('@/components/TreinarSistema/selectCamera').default
        },
        {
          // when /home/camera/:id is matched
          path: 'camera/:id',
          name: 'camera',
          component: require('@/components/Live/LiveContainer').default
        },
        {
          // when /home/camera/:id is matched
          path: 'camera/:id',
          name: 'camera-training',
          component: require('@/components/TreinarSistema/LiveContainer').default
        },
        {
          // when /home/camera/:id is matched
          path: 'camera/edit/:id',
          name: 'edit-camera',
          component: require('@/components/CameraManagement/CameraManagementContainer').default
        },
        {
          // when /home/camera/add is matched
          path: 'camera/add/',
          name: 'add-camera',
          component: require('@/components/CameraManagement/CameraManagementContainer').default
        }
      ]
    }

  ]
})

export default router
