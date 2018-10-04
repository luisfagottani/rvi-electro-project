<template>
  <div class="cadastro">
    <div class="cadastro__progress" v-bind:style="{width: progress + '%'}"></div>
    <div class="cadastro__content">
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
      progress: 50,
      cameraData: {},
    }
  },
  methods: {
    nextStep: function (event) {
      this.step += 1;
      this.progress += 50;
    }, 
    backStep: function(event){
      this.cameraData = {}
      this.step -= 1;
      this.progress = 50;
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
    }
  }
}
</script>

<style lang="scss" scoped> 
  .cadastro {
    // Box Model
    width: 100%;
    height: 100%;
    display: block;

    // Visual
    background-color: #3B3D50;

    // Position
    position: relative;

    &__title {
      // Typography
      font-size: 36px;
      font-weight: 600;
      color: #FFFFFF;
      text-align: center;

      // Box Model
      margin-bottom: 8px
    }

    &__progress {
      // Position
      position: absolute;
      left: 0;
      top: 0;
      height: 6px;

      // Visual
      background-color: #4A90E2;
      transition: 0.8s all ease-in-out ;
      
    }

    &__content{
      // Box Model
      width: 100%;
      height: 100vh;
      padding: 40px;
      

    }
  }
</style>

