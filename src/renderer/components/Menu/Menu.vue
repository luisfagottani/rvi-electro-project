<template>
    <ul class="menu">
        <li class="menu__item">
          <router-link to="ao-vivo">
            <img :src="MonitorIcon" alt="">
            <span>Ao Vivo</span>
          </router-link>
        </li>
      <li class="menu__item">
        <router-link to="add-camera">
          <img :src="CameraIcon" alt="">
          <span>Cadastrar</br> Camera</span>
        </router-link>
      </li>
      <li class="menu__item">
        <router-link to="backup">
          <img :src="DownloadIcon" alt="">
          <span>Backup</span>
        </router-link>
      </li>
      <li @click="showModalConfigurate" class="menu__item menu__item--end">
        <a href="#">
          <img :src="ConfiguracaoIcon" alt="">
          <span>Ajustes</span>
        </a>
      </li>
    </ul>
</template>


<script>           
import MonitorIcon from '@/assets/icons/monitor.svg'  
import CameraIcon from '@/assets/icons/photo-camera.svg'   
import DownloadIcon from '@/assets/icons/download.svg' 
import ConfiguracaoIcon from '@/assets/icons/settings.svg'   

export default {
  name: 'Menu',
  data: function () {
        return {
            MonitorIcon: MonitorIcon,
            CameraIcon: CameraIcon,
            DownloadIcon: DownloadIcon,
            ConfiguracaoIcon: ConfiguracaoIcon
        }
    },
  methods: {
    showModalConfigurate: function() {
      this.$store.dispatch('handleConfigurationModal')
    }
  }
}
</script>

<style scoped lang="scss">
  .menu {
    /* Box Model */
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
    justify-content: flex-start;
    -webkit-app-region:drag;

    /* Typography */
    text-align: center;
    
    &__item {
       &--end {
        /* Box Model */
        border-bottom: none;
        margin-top: auto;
      }
    }
    &__item a{

      &.router-link-exact-active {
        /* Visual */
        background-color: #2c3049;
      }

      /* Box Model */
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      border-bottom: 1px solid #292d42;
      height: 90px;
      width: 100%;

      img {
        /* Box Model */
        width: 30px;
        margin-bottom: 5px;
      }

      span {
        /* Typography */
        font-size: 11px;
        font-weight: bold;
        color: #fff;
        line-height: 11px;
      }

      &:hover {
        /* Visual */
        cursor: pointer;
        transition: 0.3s all ease-in-out;
        background-color: #2c3049;
      }


    }
  }
</style>

