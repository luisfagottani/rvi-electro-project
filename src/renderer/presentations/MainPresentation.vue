<template>
  <div>
    <div class="menu-area">
      <Menu></Menu>
    </div>
    <div class="stage-area">
      <router-view></router-view>
      <transition name="fade">
        <ConfigureCore v-if="showConfiguration"></ConfigureCore>
      </transition>
    </div>
  </div>
</template>

<script>
import Menu from '../components/Menu/Menu.vue';
import ConfigureCore from '../components/ConfigureCore/ConfigureCore.vue';

const Store = require('electron-store')
const store = new Store();


export default {
  name: 'MainPresentation',
  components: {
      Menu,
      ConfigureCore
  },
  computed: {
    showConfiguration: function() {
      return this.$store.getters.getStatusConfiguration
    }
  }
}
</script>

<style>
  .fade-enter-active, .fade-leave-active {
    transition: opacity .5s;
  }
  .fade-enter, .fade-leave-to /* .fade-leave-active em versões anteriores a 2.1.8 */ {
    opacity: 0;
  }
  .menu-area {
    /* Box Model */
    width: 70px;
    height: 100vh;
    padding-top: 30px;
    float:left;

    /* Visual */
    background-color:#0f1324;
  }
  .stage-area {
    /* Box Model */
    width: calc(100% - 70px);
    height: 100vh;
    float: left;
    padding: 30px;
  }
</style>
