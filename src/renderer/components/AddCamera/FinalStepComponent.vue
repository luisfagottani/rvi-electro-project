<template>
  <div>
    <h2 class="title">Demarcação das vagas</h2>
    <h3 class="subtitle">Preencha a imagem com as vagas disponíveis do estacionamento.</h3>

    <div class="park-map">
      <video v-if="this.cameraData.camType == '2'" width="720"  autoplay :src="cameraData.urlCam"></video>
      <img v-else style="-webkit-user-select: none;" :src="cameraData.urlCam" width="720" height="576">
    </div>

    <div class="field is-grouped">
      <p class="control">
        <a class="button is-pulled-right is-link is-medium" v-on:click="backStep()">Voltar</a>
      </p>
      <p class="control">
        <a class="button is-pulled-right is-link is-medium" @click="finish()" :disabled="this.cameraData.spots.length > 0 ? false : true">Finalizar</a>
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
    props: ['cameraData'],
    methods: {
      backStep: function() {
        if(window.confirm("A volta resulta na perda de todos os dados.")){
          this.$emit('back-step')
        }
      },
      finish: function() {
        if(this.cameraData.spots.length > 0)
          this.$emit('finish', this.cameraData)
        }
      }
    }
</script>

<style lang="scss" scoped> 
 .title {
    // Typography
    color: #ffffff;
    font-size: 25px;

    // Box Model
    margin: 0;
    margin-bottom: 5px;
    padding-bottom: 10px;
    width: 100%;
    border-bottom: 1px solid #ccc;
  }

  .subtitle {
    // Typography 
    color: #ccc;
    font-size: 16px;

    // Box Model
    margin-top: 0 !important;
    margin-bottom: 20px;
  }

  .field {

    // Box Model
    margin-bottom: 20px;
  }

  .label {
    // Typography
    color: #fff;
    font-weight: 500;
    font-size: 14px;
  }

  .input {
    // Box Model
    height: 45px;
  }

  .container {
    // Box Model
    width: 450px;
    margin: 0 auto;
  }

  .park-map {
    width: auto;
    height: auto;
    margin-top: 30px;
    position: relative;
    margin-bottom: 20px;
  }

  video {
    width: 720px;
    margin: 0 auto;
    display: block;
  }
</style>