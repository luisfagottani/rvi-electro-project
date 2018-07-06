<template>
  <div class="camera-show">
    <h1 class="camera-show__title">Camera 01</h1>
    <div class="camera-show__palco">
      
    </div>
  </div>
</template>


<script>
                                       
export default {
  name: 'showCamera',
  data(){
    return {
     formData: {}
    }
  },
}
</script>

<style lang="scss" scoped> 
  .camera-show {
    /* Box Model */
    width:770px;
    padding: 20px;

    /* Visual */
    background-color: #0f1324;
    box-shadow: 0px 0px 29px -3px rgba(0,0,0,0.27);

    &__title {
      /* Box Model */
      margin: 0;
      margin-bottom: 10px;

      /* Typography */
      font-size: 16px;
      font-weight: bold;
      color: #ffffff;
    }

    &__palco {
      width: 100%;
      height: 90%;
      background-color: #ffffff;
    }
  }
</style>
