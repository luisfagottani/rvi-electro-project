<template>
  <div>
    <div class="staging">
      <showCamera></showCamera>
      <infoSpots></infoSpots>
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
  },
  data(){
    return {
     formData: {}
    }
  },
}
</script>

<style lang="scss" scoped> 
  .staging {
    /* Box Model */
    display: flex;
    height: 80vh;
    margin-top: 30px;
  }
</style>
