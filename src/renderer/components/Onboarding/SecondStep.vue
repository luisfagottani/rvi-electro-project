<template>
  <div class="cont">
    <h2 class="title is-2">Demarque as vagas</h2>
    <div class="park-map">
      <!-- <FabricJs @spots="val => (this.formData.spots = val)"></FabricJs> -->
      <video v-if="this.formData.camType == '2'" width="720" height="576"  autoplay :src="formData.urlCam"></video>
      <img v-else style="-webkit-user-select: none;" :src="formData.urlCam" width="720" height="576">
    </div>
    <div class="field is-grouped">
      <p class="control">
        <a class="button is-pulled-right is-link is-outlined is-medium" v-on:click="backStep()">Voltar</a>
      </p>
      <p class="control">
        <a class="button is-pulled-right is-link is-medium" @click="finish()" :disabled="this.formData.spots.length > 0 ? false : true">Finalizar</a>
      </p>
    </div>
   
  </div>
  
</template>

<script>
  // import FabricJs from '../FabricJs/FabricJs'
  export default {
    name: 'SecondStep',
    // components: {
    //   FabricJs
    // },
    props: ['formData'],
    methods: {
      backStep: function() {
        if(window.confirm("A volta resulta na perda de todos os dados.")){
          this.$emit('back-step')
        }
      },
      finish: function() {
        if(this.formData.spots.length > 0)
          this.$emit('finish', this.formData)
        }
      }
    }
</script>

<style scoped> 
  .title {
    margin-top: 15px;
  }

  .button {
    margin-top: 15px;
  }

  .cont {
    width: 720px;
    height: auto;
    margin: 0 auto;
  }

  .park-map {
    width: 720px;
    height: auto;
    margin-top: 30px;
    position: relative;
  }
</style>
