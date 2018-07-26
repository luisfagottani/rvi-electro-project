<template>
  <div class="modal">
    <div class="modal__content">
      <a @click="closeModal">FECHAR (X)</a>
      <FirstStepComponent
        @next-step="nextStep()" 
        v-if="step == 1"
        :cameraData="cameraData"
        @camera-data="val => { this.cameraData = val }">
      </FirstStepComponent>
    
      <FinalStepComponent
        v-if="step == 2"
        @back-step="backStep()"
        :cameraData="cameraData"
        @finish="saveCamera">
      </FinalStepComponent>
    </div>
  </div>
</template>


<script>
const fs = require('fs')
const Store = require('electron-store')
const store = new Store();


import FirstStepComponent from './FirstStepComponent'
import FinalStepComponent from './FinalStepComponent'

export default {
  name: 'OnboardingContainer',
  components: {
      FirstStepComponent,
      FinalStepComponent
  },
  data(){
    return {
      step: 1,
      cameraData: {},
    }
  },
  methods: {
    nextStep: function (event) {
      this.step += 1;
    }, 
    backStep: function(event){
      this.cameraData = {}
      this.step -= 1;
    },
    saveCamera: function(val) {
      const min = 99;
      const max = 999999;
      const random = Math.floor(Math.random() * (max - min + 1)) + min;
      const self = this;

      this.cameraData = val;
      this.cameraData.camId = String(new Date().getTime() + random)
      this.cameraData.path = store.path
      store.set(this.cameraData.camId, this.cameraData)
      if(this.cameraData.typeFile.length > 0){
        this.cameraData.typeFile = "1"
      }
      debugger;
      this.$store.dispatch('toggleModal', "addCameraModal")
    },
    closeModal: function() {
      this.$store.dispatch('toggleModal', "addCameraModal")
    }
  }
}
</script>

<style lang="scss" scoped> 
  .modal {
    // Box Model
    width: 100%;
    height: 100%;
    display: block;

    /* Position */
    position:  fixed;
    z-index: 10;
    left: 0;
    top: 0;

    // Visual
    background-color: rgba($color: #000000, $alpha: 0.9);

    &__content{
      // Box Model
      width: 900px;
      height: auto;
      max-height: 650px;
      margin: 0 auto;
      margin-top: 70px;
      padding: 30px;
      background-color: #1d233c;
      position: absolute;
      left: 0;
      right: 0;
      bottom: 0;
      top: 0;

      // Visual
      background-color: #1d233c;

      // Position
      position: absolute;
      left: 0;
      right: 0;
      bottom: 0;
      top: 0;
      
      a {
        position: absolute;
        right: 10px;
        top: 10px;
        color: #ffffff;
        font-weight: bold;
      }

    }
  }
</style>

