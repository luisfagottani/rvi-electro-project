<template>
  <div>
    <div class="staging">
      <showCamera></showCamera>
      <infoSpots cameraId=this.$store.getters.getActualCamera></infoSpots>
    </div>
    <!-- <menuCameras></menuCameras> -->
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
    margin-top: 30px;
  }
</style>
