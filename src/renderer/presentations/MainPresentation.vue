<template>
  <div>
    <div class="menu-area">
      <Menu></Menu>
    </div>
    <div class="stage-area">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Menu from '../components/Menu/Menu.vue';

const Store = require('electron-store')
const store = new Store();


export default {
  name: 'MainPresentation',
  components: {
      Menu
  }
}
</script>

<style scoped>
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
