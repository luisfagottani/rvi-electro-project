<template>
  <div>
    <div class="menu-area">
      <img :src="RviIcon" class="menu-area__logo" alt="">
      <Menu></Menu>
    </div>
    <div class="stage-area">
      <router-view></router-view>
      <transition name="fade" :duration="200">
        <ConfigureCore v-if="showConfiguration"></ConfigureCore>
      </transition>

      <transition name="fade" :duration="200">
        <AddCameraContainer v-if="showAddCamera"></AddCameraContainer>
      </transition>
    </div>
  </div>
</template>

<script>
import Menu from '../components/Menu/Menu.vue';
import ConfigureCore from '../components/ConfigureCore/ConfigureCore.vue';
import AddCameraContainer from '../components/AddCamera/addCameraContainer.vue';
import RviIcon from '@/assets/icons/rvi.svg'  

const Store = require('electron-store')
const store = new Store();


export default {
  name: 'MainPresentation',
  data: function () {
        return {
            RviIcon: RviIcon
        }
  },
  components: {
      Menu,
      ConfigureCore,  
      AddCameraContainer
  },
  computed: {
    showConfiguration: function() {
      return this.$store.getters.getStatusModal("settingsModal")
    },
    showAddCamera: function() {
      return this.$store.getters.getStatusModal("addCameraModal")
    }
  }
}
</script>

<style scoped lang="scss">
  .fade-enter-active, .fade-leave-active {
    transition: opacity .5s;
  }
  .fade-enter, .fade-leave-to /* .teste-leave-active em versões anteriores a 2.1.8 */ {
    opacity: 0;
  }
  .menu-area {
    /* Box Model */
    width: 280px;
    height: 100vh;
    padding-top: 30px;
    float:left;

    /* Visual */
    background-color:#1A1E30;

    &__logo {
      // Box Model
      margin: 0px 10px 5px 25px;
    }
  }
  .stage-area {
    /* Box Model */
    width: calc(100% - 280px);
    height: 100vh;
    float: left;
    background-color: #3B3D50;
  }
</style>
