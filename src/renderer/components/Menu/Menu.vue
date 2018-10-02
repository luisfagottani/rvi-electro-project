<template>
    <ul class="menu">
        <li class="menu__item menu__item--title">
          <span>Câmeras</span>
        </li>
        <li class="menu__item">
          <router-link to="ao-vivo">
            <img :src="GaleraIcon" alt="">
            <span>Galeria</span>
          </router-link>
        </li>
        <li class="menu__item">
          <router-link to="add-camera">
            <img :src="NewCameraIcon" alt="">
            <span>Nova Camera</span>
          </router-link>
        </li>
        <li class="menu__item">
          <router-link to="teste">
            <img :src="BackupIcon" alt="">
            <span>Backup</span>
          </router-link>
        </li>
        <li class="menu__item menu__item--title">
          <span>Configurações</span>
        </li>
        <li class="menu__item">
          <router-link to="teta">
            <img :src="SuperviserSystemIcon" alt="">
            <span>Treinar sistema</span>
          </router-link>
        </li>
        <li class="menu__item">
          <router-link to="teste">
            <img :src="SettingsIcon" alt="">
            <span>Personalizar</span>
          </router-link>
        </li>
      <!-- <li @click="showModalAddCamera" class="menu__item">
        <a href="#">
          <img :src="CameraIcon" alt="">
          <span>Cadastrar</br> Camera</span>
        </a>
      </li> -->
      <!-- <li class="menu__item">
        <router-link to="backup">
          <img :src="DownloadIcon" alt="">
          <span>Backup</span>
        </router-link>
      </li> -->
      <!-- <li @click="showModalConfigurate" class="menu__item menu__item--end">
        <a href="#">
          <img :src="ConfiguracaoIcon" alt="">
          <span>Ajustes</span>
        </a>
      </li> -->
    </ul>
</template>


<script>           
import GaleraIcon from '@/assets/icons/galerias.svg'  
import NewCameraIcon from '@/assets/icons/new-camera.svg'   
import BackupIcon from '@/assets/icons/backup.svg' 
import SuperviserSystemIcon from '@/assets/icons/treinar-sistema.svg' 
import SettingsIcon from '@/assets/icons/personalizar.svg'   

export default {
  name: 'Menu',
  data: function () {
        return {
            GaleraIcon: GaleraIcon,
            NewCameraIcon: NewCameraIcon,
            BackupIcon: BackupIcon,
            SettingsIcon: SettingsIcon,
            SuperviserSystemIcon: SuperviserSystemIcon
        }
    },
  methods: {
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

      &--title {
        // Typography
        text-align: center;

        // Box Model
        margin-bottom: 8px;
        margin-top: 25px;

        span {
          // Box Model
          width: 232px;
          display: inline-block;
          // Visual
          border-bottom: 1px solid #BBBDC7;

          // Typography
          text-align: left;
          font-size: 20px;
          font-weight: bold;
          color: #BBBDC7;
          line-height: 34px;
        }
      }
    }
    &__item a{
      position: relative;

      &.router-link-exact-active {
        &:after {
          // Visual
          content: '';

          // Position
          position: absolute;
          left: 0;
          top: 0;

          // Box Model
          display: block;
          height: 100%;
          width: 4px;
          background-color: #4A90E2;
        }
      }

      /* Box Model */
      display: flex;
      justify-content: flex-start;
      align-items: center;
      height: 50px;
      width: 100%;

      img {
        /* Box Model */
        height: 18px;
        margin-bottom: 5px;
        margin-right: 18px;
        margin-left: 20px;
      }

      span {
        /* Typography */
        font-size: 16px;
        font-weight: normal;
        color: #fff;
        line-height: 17px;
      }

      &:hover {
        /* Visual */
        cursor: pointer;
        
        &:after {
          // Visual
          content: '';

          // Position
          position: absolute;
          left: 0;
          top: 0;

          // Box Model
          display: block;
          height: 100%;
          width: 4px;
          background-color: #4A90E2;
        }
      }


    }
  }
</style>

