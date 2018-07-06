<template>
  <div>
    <div class="staging">
      <showCamera></showCamera>
      <infoSpots cameraId=this.$store.getters.getActualCamera></infoSpots>
    </div>
  </div>
</template>


<script>
import infoSpots from './infoSpots';
import showCamera from './showCamera';

export default {
  name: 'liveContainer',
  components: {
    infoSpots,
    showCamera
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
