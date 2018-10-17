<template>
  <div class="camera-show">
    <div class="camera-show__palco">
      <CanvasSpotDraw v-if="showCanvas" :cameraData="this.getCamera" :videoDimensions="dimensions" ></CanvasSpotDraw>
      <img id="videoImg" class="video-img" width="100%" v-show="this.getCamera.camType === '1' && this.getCamera.typeIp === 'motion'" style="-webkit-user-select: none;" :src="this.getCamera.urlCam + '?time=1'">
      <canvas id="canvasVideo"  v-show="(this.getCamera.camType === '1' || this.getCamera.camType === '2') && this.getCamera.typeIp !== 'motion'"></canvas>
    </div>
    <div class="camera" v-if="this.videoNotDisplay">
      <h2 class="title">Câmera não disponível... :(</h2>
      <p class="subtitle">Não foi possivel conectar a câmera, verifique sua internet e endereço cadastrado.</p>
    </div>
  </div>
</template>


<script>
import CanvasSpotDraw from "@/components/shared/CanvasSpotDraw";
import { setTimeout, clearTimeout } from "timers";
const cv = require("opencv4nodejs");
export default {
  name: "showCamera",
  components: {
    CanvasSpotDraw
  },
  data() {
    return {
      canvas: "",
      // client: this.$store.getters.getClientApi,
      errorConection: false,
      vCap: "",
      canvasVideo: "",
      ctx: "",
      dimensions: {
        widthVideo: this.getCamera.width,
        heightVideo: this.getCamera.height
      },
      clearInterval: "",
      motionVideo: "",
      videoNotDisplay: false,
      showCanvas: false
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
    if (this.motionVideo !== "") {
      this.motionVideo.removeEventListener("load", this.playMotion);
      this.motionVideo.removeEventListener("error", this.errorPlayMotion);
    }
  },
  methods: {
    init: function() {
      // this.verifiySpots();
      const stage = document.querySelector(".camera-show");
      this.dimensions.widthVideo = stage.offsetWidth;
      const scaleMultiplier = this.dimensions.widthVideo / this.getCamera.width;
      this.dimensions.heightVideo = parseInt(
        this.getCamera.height * scaleMultiplier
      );
      this.showCanvas = true;
      if (
        (this.getCamera.camType === "1" || this.getCamera.camType === "2") &&
        this.getCamera.typeIp !== "motion"
      ) {
        try {
          debugger;
          this.vCap = new cv.VideoCapture(this.getCamera.urlCam);
          this.canvasVideo = document.getElementById("canvasVideo");
          this.canvasVideo.height = this.dimensions.heightVideo;
          this.canvasVideo.width = this.dimensions.widthVideo;
          this.ctx = this.canvasVideo.getContext("2d");
          this.startInterval();
        } catch (error) {
          this.$store.dispatch("setLoading", false);
          this.$store.dispatch(
            "setMessageAlert",
            "Não foi possivel conectar a câmera"
          );
          this.videoNotDisplay = true;
        }
      } else {
        this.$nextTick(function() {
          this.motionVideo = document.getElementById("videoImg");
          this.motionVideo.addEventListener("load", this.playMotion, false);
          this.motionVideo.addEventListener(
            "error",
            this.errorPlayMotion,
            false
          );
        });
      }
    },
    startInterval: function() {
      this.clearInterval = setInterval(() => {
        this.playVideo();
      }, 100);
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
        img = frame.resize(
          this.dimensions.heightVideo,
          this.dimensions.widthVideo
        );
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
    },
    playMotion: function() {
      if (this.$store.getters.getLoadingState) {
        this.$store.dispatch("setLoading", false);
      }
      this.motionVideo.src =
        this.motionVideo.src.replace(/\?[^\n]*$/, "?") + new Date().getTime(); // 'this' refers to the image
    },
    errorPlayMotion: function() {
      this.motionVideo.style.display = "none";
      this.$store.dispatch("setLoading", false);
      this.$store.dispatch(
        "setMessageAlert",
        "Não foi possivel conectar a câmera"
      );
      this.videoNotDisplay = true;
    }
  }
};
</script>

<style lang="scss" scoped>
.title {
  margin-bottom: 20px;
}
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
