<template>
    <ul class="menu">
      <li class="menu__item">
        <img :src="MonitorIcon" alt="">
        <span>Ao Vivo</span>
      </li>
      <li class="menu__item">
        <img :src="CameraIcon" alt="">
        <span>Cadastrar</br> Camera</span>
      </li>
      <li class="menu__item">
        <img :src="DownloadIcon" alt="">
        <span>Backup</span>
      </li>
      <li class="menu__item menu__item--settings">
        <img :src="ConfiguracaoIcon" alt="">
        <span>Ajustes</span>
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
    }
}
</script>

<style scoped lang="scss">
  .menu {
    /* Box Model */
    display: flex;
    flex-direction: column;
    width: 100%;

    /* Typography */
    text-align: center;

    &__item {
      /* Box Model */
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      border-bottom: 1px solid #292d42;
      height: 90px;

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

      &--settings {
        /* Box Model */
        border-bottom: none;
      }

      &:hover {
        cursor: pointer;
        transition: 0.3s all ease-in-out;
        background-color: #2c3049;
      }
    }
  }
</style>

