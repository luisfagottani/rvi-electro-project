<template>
  <AppContainer></AppContainer>
</template>

<script>
import AppContainer from '../components/App/appContainer.vue';
var PythonShell = require('python-shell');

var options = {
  mode: 'text',
  pythonPath: '/Users/luis.agottani/anaconda2/envs/tcc/bin/python3',
  pythonOptions: ['-u']
};

const Store = require('electron-store')
const store = new Store();


export default {
  name: 'OnboardingContainer',
  components: {
      AppContainer 
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

<style>

</style>
