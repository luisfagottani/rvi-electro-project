<template>
  <div class="camera-show">
    <h1 class="camera-show__title">{{getCamera.nameCam}}</h1>
    <div class="camera-show__palco">
      <div :class="['lds-ripple', {remove: !isLoading}]"><div></div><div></div> <span class="loading">Aguarde, análisando as vagas...</span>
      <span :class="['error-conection', {show: !errorConection}]">Falha na conexão com o servidor...</span></div>
      <CanvasPark></CanvasPark>
      <canvas id="myCanvas" width="720px" height="420px"></canvas>
      <!-- <img v-else style="-webkit-user-select: none;" :src="camera.urlCam" width="720" height="576"> -->
      
    </div>
  </div>
</template>


<script>
import CanvasPark from '../CanvasPark/CanvasParkContainer'
import { setTimeout } from 'timers';
const cv = require('opencv4nodejs')
export default {
  name: 'showCamera',
  components: {
      CanvasPark
  },
  data(){
    return {
     canvas: this.$store.getters.getCanvas,
     client: this.$store.getters.getClientApi,
     errorConection: false
    }
  },
  computed: {
    getCamera: function() {
      return this.$store.getters.getCamera
    },
    isLoading: function() {
      return this.$store.getters.getIsLoading
    },
  },
  mounted(){
    this.verifiySpots();
  },
  methods: {
    verifiySpots: function(){
      var vm = this;
      // set canvas dimensions
      let vCap =  new cv.VideoCapture(this.getCamera.urlCam);
      const canvasVideo = document.getElementById('myCanvas');
      canvasVideo.height = 405
      canvasVideo.width = 720
      const ctx = canvasVideo.getContext('2d');

      var SelectObject = function (spot) {
          vm.$store.getters.getCanvas.getObjects().forEach(function(o) {
              if(o.id === spot.id) {
                  debugger;
                  if(spot.statusSpot === 1){
                    o.set("fill", "rgba(255, 0, 0, 0.3)");
                    o.set("stroke", "rgba(255, 0, 0, 0.3)");
                  }else{
                    o.set("fill", "rgba(0,255,0, 0.4)");
                    o.set("stroke", "rgba(0,255,0, 0.4)");
                  }
                  
              }
          })
    
          vm.getCamera.spots.forEach(function(spots) {
            if(spot.id === spots.id) {
              if(spot.statusSpot === 1){
                vm.$set(spots, 'status', 1)
              }else{
                vm.$set(spots, 'status', 0)
              }
            }
          })

          vm.$store.getters.getCanvas.renderAll();
        }

      let i = 0
    
      function playVideo () {
        
        let frame = vCap.read();
        if(!frame) {
          vCap.set(cv.CAP_PROP_POS_FRAMES, 0)
        }
        let img = frame.resize(405, 720);

        const matRGBA = img.channels === 1
        ? img.cvtColor(cv.COLOR_GRAY2RGBA)
        : img.cvtColor(cv.COLOR_BGR2RGBA);

        // create new ImageData from raw mat data
        const imgData = new ImageData(
          new Uint8ClampedArray(matRGBA.getData()),
          img.cols,
          img.rows
        );

        ctx.putImageData(imgData, 0, 0);

        if(i == 80){
           vm.getCamera.image = cv.imencode('.jpg', frame.resize(405, 720)).toString("base64");
           vm.getCamera.image = Buffer.from(vm.getCamera.image)
           vm.getCamera.width = 720
           vm.getCamera.height = 405
           vm.client.processImage(vm.getCamera, function(err, response) {
             if(!err){
                vm.errorConection = false;
                if(vm.isLoading !== false)
                  vm.$store.dispatch('setIsLoading')
                response.spots.forEach(element => { 
                  SelectObject(element)
                });
             }else{
               if(vm.isLoading === false)
                  vm.$store.dispatch('setIsLoading')
                 vm.errorConection = true;
             }
           });
          i = 0;
        }
        i++;
      }

    setInterval(playVideo, 50)

    }
  }
}
</script>

<style lang="scss" scoped> 
  .camera-show {
    .lds-ripple {
      display: inline-block;
      position: absolute;
      width: 100%;
      height: 102%;
      background-color: rgba($color: #000000, $alpha: 0.8);
      z-index: 10;
      display: flex;
      align-items: center;
      flex-direction: column;
      justify-content: center;

      &.remove {
        transition: 0.5s all ease-in-out;
        opacity: 0;
        visibility: hidden;
        z-index: 3;
      }


    }
    .error-conection {
      color: red;
      font-size: 13px;
      font-weight: bold;
      &.show {
        opacity: 0;
        visibility: hidden;
      }
    }
    .lds-ripple .loading {
      text-align: center;
      color: #ffffff;
      font-weight: bold;
      margin: 0 auto;
      padding-top: 120px;
      font-size: 13px;
    }
    .lds-ripple div {
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      margin:  auto;
      position: absolute;
      border: 4px solid #fff;
      opacity: 1;
      border-radius: 50%;
      animation: lds-ripple 1.5s cubic-bezier(0, 0.2, 0.8, 1) infinite;
    }
    .lds-ripple div:nth-child(2) {
      animation-delay: -0.5s;
    }
    @keyframes lds-ripple {
      0% {
        top: 28px;
        left: 28px;
        width: 0;
        height: 0;
        opacity: 1;
      }
      100% {
        top: -1px;
        left: -1px;
        width: 58px;
        height: 58px;
        opacity: 0;
      }
    }
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
