<template>
  <div>
    <div class="menu-area">
      <Menu></Menu>
    </div>
    <AppContainer></AppContainer>
  </div>
</template>

<script>
import AppContainer from '../components/App/appContainer.vue';
import Menu from '../components/App/Menu.vue';

const Store = require('electron-store')
const store = new Store();


export default {
  name: 'MainPresentation',
  components: {
      AppContainer,
      Menu,
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

    /* Visual */
    background-color:#0f1324;
  }
</style>
