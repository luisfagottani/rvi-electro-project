<template>
  <div>
    <Menu></Menu>
    <div class="cont">
      <h2 class="title is-2">{{this.formData.nameCam}}</h2>
      <div class="park-map">
        <FabricJs :spotsData="this.formData.spots"></FabricJs>
        <video width="720" height="576"  autoplay :src="formData.urlCam"></video>
      </div>
    </div>
  </div>
</template>


<script>

import Menu from './Menu'
import FabricJs from '../FabricJs/FabricJs'

const fs = require('fs')
var grpc = require('grpc')
var path = require('path')


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

var client = new service.Parking('localhost:50060',
                                       grpc.credentials.createInsecure());

                                       
export default {
  name: 'OnboardingContainer',
  components: {
      Menu,
      FabricJs
  },
  data(){
    return {
     formData: {}
    }
  },
  created() {
    this.formData = this.$store.state.Spots.parkingLot[0];
    client.addCamera(this.formData, function(err, response) {
        self.responseAddCamera = response
    });
    this.verifiySpots();

  },  
  methods: {
     verifiySpots: function(){
      var vm = this;
       var SelectObject = function (spot) {
          vm.$store.state.Spots.canvas.getObjects().forEach(function(o) {
              if(o.id === spot.id) {
                  if(spot.statusSpot === 1){
                    o.set("fill", "rgba(255, 0, 0, 0.3)");
                    o.set("stroke", "rgba(255, 0, 0, 0.3)");
                  }else{
                    o.set("fill", "rgba(0,255,0, 0.4)");
                    o.set("stroke", "rgba(0,255,0, 0.4)");
                  }
                  
              }
          })

           vm.$store.state.Spots.canvas.renderAll();
      }
     
      setInterval(function(){ 
        if(self.responseAddCamera){
            client.ReturnSpots({value: 1}, function(err, response){
              response.spots.forEach(element => {
                SelectObject(element)
              });
            })
        }
      }, 3000);
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
    width: auto;
    height: auto;
    margin-top: 30px;
    position: relative;
  }
</style>
