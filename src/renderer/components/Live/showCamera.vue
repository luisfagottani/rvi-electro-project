<template>
  <div class="camera-show">
    <h1 class="camera-show__title">{{camera.nameCam}}</h1>
    <div class="camera-show__palco">
      <CanvasPark></CanvasPark>
      <video v-if="camera.camType == '2' " width="100%"  autoplay :src="camera.urlCam"></video>
      <img v-else style="-webkit-user-select: none;" :src="camera.urlCam" width="720" height="576">
    </div>
  </div>
</template>


<script>
import CanvasPark from '../CanvasPark/CanvasParkContainer'

export default {
  name: 'showCamera',
  components: {
      CanvasPark
  },
  data(){
    return {
     camera: this.$store.getters.getCamera,
     canvas: this.$store.getters.getCanvas,
     client: this.$store.getters.getClientApi
    }
  },
  mounted(){
    this.client.addCamera(this.camera, function(err, response) {
        self.responseAddCamera = response
    });
    this.verifiySpots();
  },
  methods: {
    verifiySpots: function(){
      var vm = this;
       var SelectObject = function (spot) {
          canvas.getObjects().forEach(function(o) {
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
    
          vm.camera.spots.forEach(function(spots) {
            if(spot.id === spots.id) {
              if(spot.statusSpot === 1){
                vm.$set(spots, 'status', 1)
              }else{
                vm.$set(spots, 'status', 0)
              }
            }
          })

            canvas.renderAll();
      }
     
      setInterval(function(){ 
        if(self.responseAddCamera){
            vm.client.ReturnSpots({value: 1}, function(err, response){
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
      position: relative;
    }
  }
</style>
