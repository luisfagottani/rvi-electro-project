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
import Menu from '../components/App/Menu.vue';

const Store = require('electron-store')
const store = new Store();


export default {
  name: 'MainPresentation',
  components: {
      Menu
  },
  created () {
      if(this.$store.state.Spots.parkingLot.length < 1){
        let camerasStorage = store.get();
        for (let cameraId in camerasStorage) {
            // skip loop if the property is from prototype
            if (typeof(camerasStorage.cameraId) !== 'undefined') continue;
              let obj = camerasStorage[cameraId];
              this.$store.dispatch('addCamera', obj)
        }
      }
  },
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
    padding-top: 30px;
    float: left;
  }
</style>
