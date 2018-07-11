<template>
  <div>
    <div class="cont">
      <h2 class="title is-2">{{this.formData.nameCam}}</h2>
      <div class="park-map">
        <!-- <video v-if="this.formData.camType == '2' " width="720" height="576"  autoplay :src="formData.urlCam"></video>
        <img v-else style="-webkit-user-select: none;" :src="formData.urlCam" width="720" height="576"> -->
      </div>
    </div>
  </div>
</template>


<script>

                                       
export default {
  name: 'appContainer',
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
