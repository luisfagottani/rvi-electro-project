<template>
  <div class="camera-show">
    <div class="camera-show__palco">
      <CanvasSpotDraw v-if="showCanvas" :cameraData="this.getCamera" @idSpot="val => showModalSpotCorrection(val)"  :videoDimensions="dimensions" ></CanvasSpotDraw>
      <img id="videoImg" class="video-img" width="100%" v-show="this.getCamera.camType === '1' && this.getCamera.typeIp === 'motion'" style="-webkit-user-select: none;" :src="this.getCamera.urlCam + '?time=1'">
      <canvas id="canvasVideo"  v-show="(this.getCamera.camType === '1' || this.getCamera.camType === '2') && this.getCamera.typeIp !== 'motion'"></canvas>
    </div>
    <div class="camera" v-if="this.videoNotDisplay">
      <h2 class="title">Câmera não disponível... :(</h2>
      <p class="subtitle">Não foi possivel conectar a câmera, verifique sua internet e endereço cadastrado.</p>
    </div>
    <ChangeStatus v-show="showModal" @closeModal="showModal = false & $children[1].selectCanvasClear()"  @stateCorrection="val => stateCorrection(val)" />
  </div>
</template>


<script>
import CanvasSpotDraw from "@/components/shared/CanvasSpotDraw";
import ChangeStatus from "@/components/shared/ChangeStatus";
import { setTimeout, clearTimeout } from "timers";
const cv = require("opencv4nodejs");
export default {
  name: "ShowCamera",
  components: {
    CanvasSpotDraw,
    ChangeStatus
  },
  data() {
    return {
      canvas: "",
      client: this.$store.getters.getClientApi,
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
      showCanvas: false,
      repeat: 0,
      correctState: "",
      showModal: false,
      theSpot: ""
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
      this.$store.dispatch("setLoading", {
        status: true,
        message: "Carregando a câmera",
        showMessage: true
      });
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
          this.vCap = new cv.VideoCapture(this.getCamera.urlCam);
          this.canvasVideo = document.getElementById("canvasVideo");
          this.canvasVideo.height = this.dimensions.heightVideo;
          this.canvasVideo.width = this.dimensions.widthVideo;
          this.ctx = this.canvasVideo.getContext("2d");
          this.startInterval();
        } catch (error) {
          this.$store.dispatch("setLoading", {
            status: true,
            message: "",
            showMessage: false
          });
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
      }, 50);
    },
    changeStatusSpot: function(spot) {
      this.$store.getters.getCanvas.getObjects().forEach(function(o) {
        if (o.id === spot.id) {
          if (spot.statusSpot === 1) {
            o.set("fill", "rgba(255, 0, 0, 0.3)");
            o.set("stroke", "rgba(255, 0, 0, 0.3)");
          } else {
            o.set("fill", "rgba(0,255,0, 0.4)");
            o.set("stroke", "rgba(0,255,0, 0.4)");
          }
        }
      });

      this.getCamera.spots.forEach(spots => {
        if (spot.id === spots.id) {
          if (spot.statusSpot === 1) {
            this.$set(spots, "status", 1);
          } else {
            this.$set(spots, "status", 0);
          }
        }
      });

      this.$store.getters.getCanvas.renderAll();
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

        if (this.repeat === 30) {
          this.processVagas(img);
          this.repeat = 0;
        }

        // create new ImageData from raw mat data
        const imgData = new ImageData(
          new Uint8ClampedArray(matRGBA.getData()),
          img.cols,
          img.rows
        );
        this.ctx.putImageData(imgData, 0, 0);
        if (this.$store.getters.getLoadingState) {
          this.$store.dispatch("setLoading", {
            status: true,
            message: "Processando as vagas",
            showMessage: true
          });
        }
        this.repeat++;
      }
    },
    getBase64Image: function(img) {
      const canvas = document.createElement("canvas");
      canvas.width = img.naturalWidth;
      canvas.height = img.naturalHeight;
      const ctx = canvas.getContext("2d");
      ctx.drawImage(img, 0, 0);
      const dataURL = canvas.toDataURL("image/png");
      return dataURL.replace(/^data:image\/(png|jpg);base64,/, "");
    },
    processVagas: function(img) {
      let frame = "";
      if (
        (this.getCamera.camType === "1" || this.getCamera.camType === "2") &&
        this.getCamera.typeIp !== "motion"
      ) {
        frame = img;
      } else {
        img = img
          .replace("data:image/jpeg;base64", "")
          .replace("data:image/png;base64", ""); //Strip image type prefix
        const buffer = Buffer.from(img, "base64");
        frame = cv.imdecode(buffer);
      }
      this.getCamera.image = cv
        .imencode(
          ".jpg",
          frame.resize(this.getCamera.height, this.getCamera.width)
        )
        .toString("base64");
      this.getCamera.image = Buffer.from(this.getCamera.image);
      if (this.$store.getters.getLoadingState) {
        this.getCamera.newCamera = 1;
      } else {
        this.getCamera.newCamera = 0;
      }
      this.client.processImage(this.getCamera, (err, response) => {
        if (!err) {
          response.spots.forEach(element => {
            this.changeStatusSpot(element);
          });
          if (this.$store.getters.getLoadingState) {
            this.$store.dispatch("setLoading", {
              status: false,
              message: "",
              showMessage: false
            });
          }
        }
        if (err) {
          console.log(err);
        }
      });
    },
    playMotion: function(e) {
      if (this.$store.getters.getLoadingState) {
        this.$store.dispatch("setLoading", {
          status: true,
          message: "Processando as vagas!",
          showMessage: true
        });
      }
      const base64 = this.getBase64Image(e.srcElement);
      this.processVagas(base64);
      this.motionVideo.src =
        this.motionVideo.src.replace(/\?[^\n]*$/, "?") + new Date().getTime(); // 'this' refers to the image
      this.repeat++;
    },
    errorPlayMotion: function() {
      this.motionVideo.style.display = "none";
      this.$store.dispatch("setLoading", {
        status: false,
        message: "",
        showMessage: false
      });
      this.$store.dispatch(
        "setMessageAlert",
        "Não foi possivel conectar a câmera"
      );
      this.videoNotDisplay = true;
    },
    showModalSpotCorrection: function(val) {
      this.showModal = true;
      this.theSpot = val;
    },

    stateCorrection: function(val) {
      this.showModal = false;
      let aux = Object.assign({}, this.getCamera);
      let objectSpot = Object.assign(
        {},
        aux.spots.find(x => x.id === this.theSpot)
      );
      objectSpot.status = val;
      aux.spots = objectSpot;
      this.client.stateCorrection(aux, (err, response) => {
        if (!err) {
          console.log(response);
        }
        if (err) {
          console.log(err);
        }
      });

      this.$store.getters.getCanvas.getObjects().forEach(function(o) {
        if (o.id === objectSpot.id) {
          if (objectSpot.status === 1) {
            o.set("fill", "rgba(255, 0, 0, 0.3)");
            o.set("stroke", "rgba(255, 0, 0, 0.3)");
          } else {
            o.set("fill", "rgba(0,255,0, 0.4)");
            o.set("stroke", "rgba(0,255,0, 0.4)");
          }
        }
      });

      this.getCamera.spots.forEach(spots => {
        if (objectSpot.id === spots.id) {
          if (objectSpot.status === 1) {
            this.$set(spots, "status", 1);
          } else {
            this.$set(spots, "status", 0);
          }
        }
      });
      this.$store.getters.getCanvas.renderAll();
      this.$children[1].selectCanvasClear();
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
