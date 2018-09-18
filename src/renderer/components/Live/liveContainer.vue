<template>
  <div>
    <div class="staging">
      <menuCameras></menuCameras>
      <showCamera></showCamera>
      <!-- <infoSpots cameraId=this.$store.getters.getActualCamera></infoSpots> -->
    </div>
    
  </div>
</template>


<script>
import infoSpots from './infoSpots';
import showCamera from './showCamera';
import menuCameras from './menuCameras';

export default {
  name: 'liveContainer',
  components: {
    infoSpots,
    showCamera,
    menuCameras
  }
}
</script>

<style lang="scss" scoped> 
  .staging {
    /* Box Model */
    display: flex;
    height: auto;
  }
</style>
