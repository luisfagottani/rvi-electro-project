<template>
  <form>
    <FirstStep
      @next-step="nextStep()" 
      v-if="step == 1"
      :formData="formData"
      @form-data="val => { this.formData = val }">
    </FirstStep>

    <SecondStep
     v-if="step == 2"
     @back-step="backStep()"
     :formData="formData"
     @finish="saveOnboarding">
     </SecondStep>
  </form>
</template>


<script>
const fs = require('fs')
const Store = require('electron-store')
const store = new Store();
var grpc = require('grpc')
var path = require('path')


import FirstStep from './FirstStep'
import SecondStep from './SecondStep'

try {
  var service
  if (process.env.NODE_ENV == 'production'){
    var PROTO_PATH = path.join(__dirname + '/src/project/protos/api.proto');
    service = grpc.load(PROTO_PATH).park;
  }else{
    service = grpc.load('src/core/project/protos/api.proto').park;
  }
} catch (error) {
  alert(error)
}

var client = new service.Parking('localhost:50050',
                                       grpc.credentials.createInsecure());
                                       
export default {
  name: 'OnboardingContainer',
  components: {
      FirstStep,
      SecondStep
  },
  data(){
    return {
      step: 1,
      formData: {},
      responseAddCamera: false
    }
  },
  methods: {
    nextStep: function (event) {
      this.step += 1;
    }, 
    backStep: function(event){
      this.formData = {}
      this.step -= 1;
    },
    saveOnboarding: function(val) {
      const min = 99;
      const max = 999999;
      const random = Math.floor(Math.random() * (max - min + 1)) + min;
      const self = this;

      this.formData = val;
      this.formData.camId = String(new Date().getTime() + random)
      this.formData.path = store.path
      store.set(this.formData.camId, this.formData)

      client.addCamera(this.formData, function(err, response) {
         self.responseAddCamera = response
      });
      setInterval(function(){ 
        if(self.responseAddCamera){
            client.ReturnSpots({value: 1}, function(err, response){
              console.log(response)
            })
        }
      }, 7000);

    }
  }
}
</script>
