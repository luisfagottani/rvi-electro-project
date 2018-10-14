<template>
  <div class="camera-show">
    <div class="camera-show__palco">
      <CanvasPark :getCamera="this.getSpots"></CanvasPark>
      <img class="video-img" width="100%" v-show="this.getCamera.camType === '1' && this.getCamera.typeIp === 'motion'" style="-webkit-user-select: none;" :src="this.getCamera.urlCam">
      <canvas id="canvasVideo"  v-show="(this.getCamera.camType === '1' || this.getCamera.camType === '2') && this.getCamera.typeIp !== 'motion'"></canvas>
    </div>
  </div>
</template>


<script>
import CanvasPark from "../CanvasPark/CanvasParkContainer";
import { setTimeout } from "timers";
const cv = require("opencv4nodejs");
export default {
  name: "showCamera",
  components: {
    CanvasPark
  },
  data() {
    return {
      canvas: this.$store.getters.getCanvas,
      // client: this.$store.getters.getClientApi,
      errorConection: false,
      vCap: "",
      canvasVideo: "",
      ctx: "",
      width: "",
      height: "",
      clearInterval: ""
    };
  },
  props: ["getCamera"],
  computed: {
    getSpots: function() {
      return this.getCamera;
    }
  },
  mounted() {
    this.init();
  },
  beforeDestroy() {
    clearInterval(this.clearInterval);
  },
  methods: {
    init: function() {
      // this.verifiySpots();
      const stage = document.querySelector(".camera-show");
      this.width = stage.offsetWidth;
      const scaleMultiplier = this.width / this.getCamera.width;
      this.height = parseInt(this.getCamera.height * scaleMultiplier);
      if (
        (this.getCamera.camType === "1" || this.getCamera.camType === "2") &&
        this.getCamera.typeIp !== "motion"
      ) {
        this.vCap = new cv.VideoCapture(this.getCamera.urlCam);
        this.canvasVideo = document.getElementById("canvasVideo");
        this.canvasVideo.height = this.height;
        this.canvasVideo.width = this.width;
        this.ctx = this.canvasVideo.getContext("2d");
        this.startInterval();
      }
      this.$nextTick(function() {
        this.GetCanvasAtResoution(this.width);
      });
    },
    startInterval: function() {
      this.clearInterval = setInterval(() => {
        this.playVideo();
      }, 100);
    },
    GetCanvasAtResoution: function(newWidth) {
      let canvas = this.$store.getters.getCanvas;
      if (canvas.width != newWidth) {
        var scaleMultiplier = newWidth / canvas.width;
        const heightVar = canvas.getHeight() * scaleMultiplier;
        const widthVar = canvas.getWidth() * scaleMultiplier;
        var objects = canvas.getObjects();
        for (var i in objects) {
          objects[i].scaleX = objects[i].scaleX * scaleMultiplier;
          objects[i].scaleY = objects[i].scaleY * scaleMultiplier;
          objects[i].left = objects[i].left * scaleMultiplier;
          objects[i].top = objects[i].top * scaleMultiplier;
          objects[i].setCoords();
        }
        var obj = canvas.backgroundImage;
        if (obj) {
          obj.scaleX = obj.scaleX * scaleMultiplier;
          obj.scaleY = obj.scaleY * scaleMultiplier;
        }

        canvas.discardActiveObject();
        canvas.setWidth(parseInt(widthVar));
        canvas.setHeight(parseInt(heightVar));
        canvas.renderAll();
        canvas.calcOffset();
      }
    },
    verifiySpots: function() {
      var vm = this;
      this.canvasVideo.height = vm.height;
      this.canvasVideo.width = vm.width;

      // const SelectObject = function(spot) {
      //   vm.$store.getters.getCanvas.getObjects().forEach(function(o) {
      //     if (o.id === spot.id) {
      //       if (spot.statusSpot === 1) {
      //         o.set("fill", "rgba(255, 0, 0, 0.3)");
      //         o.set("stroke", "rgba(255, 0, 0, 0.3)");
      //       } else {
      //         o.set("fill", "rgba(0,255,0, 0.4)");
      //         o.set("stroke", "rgba(0,255,0, 0.4)");
      //       }
      //     }
      //   });

      //   vm.getCamera.spots.forEach(function(spots) {
      //     if (spot.id === spots.id) {
      //       if (spot.statusSpot === 1) {
      //         vm.$set(spots, "status", 1);
      //       } else {
      //         vm.$set(spots, "status", 0);
      //       }
      //     }
      //   });

      //   vm.$store.getters.getCanvas.renderAll();
      // };
    },
    playVideo: function() {
      let frame = this.vCap.read();
      let img = null;
      if (!frame.empty) {
        img = frame.resize(this.height, this.width);
        const matRGBA =
          img.channels === 1
            ? img.cvtColor(cv.COLOR_GRAY2RGBA)
            : img.cvtColor(cv.COLOR_BGR2RGBA);

        // create new ImageData from raw mat data
        const imgData = new ImageData(
          new Uint8ClampedArray(matRGBA.getData()),
          img.cols,
          img.rows
        );
        this.ctx.putImageData(imgData, 0, 0);
        if (this.$store.getters.getLoadingState) {
          this.$store.dispatch("setLoading", false);
        }
      }

      // let frame = this.vCap.read();
      // if (!frame) {
      //   this.vCap.set(cv.CAP_PROP_POS_FRAMES, 0);
      // }

      // let img = frame.resize(this.getCamera.height, this.getCamera.width);
      // const matRGBA =
      //   img.channels === 1
      //     ? img.cvtColor(cv.COLOR_GRAY2RGBA)
      //     : img.cvtColor(cv.COLOR_BGR2RGBA);

      // // create new ImageData from raw mat data
      // const imgData = new ImageData(
      //   new Uint8ClampedArray(matRGBA.getData()),
      //   img.cols,
      //   img.rows
      // );

      // this.vCap.read(src);
      // cv.imshow("canvasVideo", this.vCap.read());

      // if (i == 80) {
      //   vm.getCamera.image = cv
      //     .imencode(".jpg", frame.resize(vm.height, vm.width))
      //     .toString("base64");
      //   vm.getCamera.image = Buffer.from(vm.getCamera.image);
      //   vm.getCamera.width = vm.width;
      //   vm.getCamera.height = vm.height;
      //   vm.client.processImage(vm.getCamera, function(err, response) {
      //     if (!err) {
      //       vm.errorConection = false;
      //       if (vm.isLoading !== false) vm.$store.dispatch("setIsLoading");
      //       response.spots.forEach(element => {
      //         SelectObject(element);
      //       });
      //     } else {
      //       if (vm.isLoading === false) vm.$store.dispatch("setIsLoading");
      //       vm.errorConection = true;
      //     }
      //   });
      //   i = 0;
      // }
    }
  }
};
</script>

<style lang="scss" scoped>
.camera-show {
  height: auto;
  /* Box Model */
  width: 100%;

  &__title {
    /* Box Model */
    margin: 0;

    /* Typography */
    font-size: 16px;
    font-weight: bold;
    color: #ffffff;
  }

  &__palco {
    width: 100%;
    position: relative;
  }
}
</style>
