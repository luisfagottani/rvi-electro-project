<template>
  <div>
    <h2 class="title">Atualize as informações de sua câmera</h2>

    <div class="pklot">
      <div :class="['pklot__info', {'pklot__info--hidden': !showInfoPklot}]">
        <div class="pklot__info-area">
          <img class="icone" :src="HelpIcon" alt="" v-on:mouseover="showHelp = true" v-on:mouseleave="showHelp = false">
          <div :class="['content', {'content--show': this.showHelp}]">
            <p>Ligue 3 pontos sobre uma área da imagem para demarcar uma vaga.</p>
            <img :src="DemarcacaoExemplo" />
          </div>
          <a :class="['pklot__cta pklot__cta--outline']" style="margin: 0 auto; margin-top: auto;" v-on:click="cancelAddSpot()">Cancelar</a>
        </div>
      </div>
      <div class="pklot__canvas">
        <CanvasSpotDraw v-if="showCanvas" @spots="val => (cameraData.spots = val)" :cameraData="cameraData" :videoDimensions="dimensions" @showRemoveCta="val => (deleteSpotStatus = val)" @showAddSpot="val => (showInfoPklot = val)"></CanvasSpotDraw>
        <video id="video-cam" v-if="cameraData.camType === '2'" muted style=""  autoplay :src="cameraData.urlCam"></video>
        <img class="video-img" width="100%" v-if="cameraData.camType === '1' && cameraData.typeIp === 'motion'" style="-webkit-user-select: none;" :src="cameraData.urlCam">
        <canvas id="canvasVideo"  v-if="cameraData.camType === '1' && cameraData.typeIp === 'rstp'"></canvas>
      </div>
      <div class="pklot__menu">
        <div class="pklot__cta-group">
          <a class="pklot__cta pklot__cta--white" v-on:click="addSpot()" >Adicionar Vaga</a>
          <a :class="['pklot__cta pklot__cta--outline', {'pklot__cta--hidden': !deleteSpotStatus}]" v-on:click="removeSpot()">Remover Vaga</a>
        </div>
        <div class="pklot__cta-group">
          <a class="pklot__cta pklot__cta--white" v-on:click="backStep()">Voltar</a>
          <a :class="['pklot__cta pklot__cta--blue', {'hidden': cameraData.spots.length > 0 ? false : true}]" @click="finish()">Atualizar</a>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import CanvasSpotDraw from "@/components/shared/CanvasSpotDraw";
import HelpIcon from "@/assets/icons/help.svg";
import Demarcacao from "@/assets/demarcacao.png";
import { setTimeout } from "timers";
const cv = require("opencv4nodejs");
export default {
  name: "FinalStepEdit",
  beforeDestroy() {
    clearInterval(this.clearInterval);
  },
  mounted() {
    const canvas = document.querySelector(".pklot__canvas");
    const info = document.querySelector(".pklot__info-area");
    const pklot = document.querySelector(".pklot");

    if (this.cameraData.camType === "2") {
      var v = document.getElementById("video-cam");
      v.addEventListener(
        "loadedmetadata",
        e => {
          const canvas = document.querySelector(".pklot__canvas");
          const info = document.querySelector(".pklot__info-area");
          const pklot = document.querySelector(".pklot");
          this.dimensions.widthVideo = canvas.offsetWidth;
          this.dimensions.heightVideo = canvas.offsetHeight;
          this.showCanvas = true;
          canvas.style.height = this.dimensions.heightVideo + "px";
          pklot.style.height = this.dimensions.heightVideo + "px";
          info.style.height = this.dimensions.heightVideo + "px";
          this.$store.dispatch("setLoading", false);
        },
        false
      );
    } else if (this.cameraData.typeIp === "motion") {
      const cameraImg = document.querySelector(".video-img");
      cameraImg.addEventListener("load", e => {
        const canvas = document.querySelector(".pklot__canvas");
        const info = document.querySelector(".pklot__info-area");
        const pklot = document.querySelector(".pklot");
        this.dimensions.widthVideo = canvas.offsetWidth;
        this.dimensions.heightVideo = canvas.offsetHeight;
        this.showCanvas = true;
        canvas.style.height = this.dimensions.heightVideo + "px";
        pklot.style.height = this.dimensions.heightVideo + "px";
        info.style.height = this.dimensions.heightVideo + "px";
        this.$store.dispatch("setLoading", false);
      });
    } else {
      this.vCap = new cv.VideoCapture(this.cameraData.urlCam);
      this.canvasVideo = document.getElementById("canvasVideo");
      this.ctx = this.canvasVideo.getContext("2d");
      this.startInterval();
    }
  },
  components: {
    CanvasSpotDraw
  },
  data: function() {
    return {
      dimensions: {
        widthVideo: this.cameraData.width,
        heightVideo: this.cameraData.height
      },
      vCap: null,
      ctx: null,
      deleteSpotStatus: false,
      showInfoPklot: false,
      HelpIcon: HelpIcon,
      DemarcacaoExemplo: Demarcacao,
      showHelp: false,
      showCanvas: false
    };
  },
  props: ["cameraData"],
  methods: {
    backStep: function() {
      this.$emit("back-step");
    },
    startInterval: function() {
      this.clearInterval = setInterval(() => {
        this.playVideo();
      }, 10);
    },
    finish: function() {
      if (this.cameraData.spots.length > 0) {
        this.cameraData.width = this.dimensions.widthVideo;
        this.cameraData.height = this.dimensions.heightVideo;
        this.$emit("finish", this.cameraData);
      }
    },
    playVideo: function() {
      let frame = this.vCap.read();
      let img = null;
      if (!frame.empty) {
        let width = frame.cols;
        let height = frame.rows;
        let newWidth = document.querySelector(".pklot__canvas").offsetWidth;

        if (width !== newWidth) {
          let scaleMultiplier = newWidth / width;
          let heightVar = height * scaleMultiplier;
          let widthVar = width * scaleMultiplier;
          img = frame.resize(parseInt(heightVar), parseInt(widthVar));
        } else {
          img = frame;
        }
        this.dimensions.widthVideo = img.cols;
        this.dimensions.heightVideo = img.rows;
        this.canvasVideo.width = this.dimensions.widthVideo;
        this.canvasVideo.height = this.dimensions.heightVideo;
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
          this.showCanvas = true;
          this.$store.dispatch("setLoading", false);
        }
      }
    },
    addSpot: function() {
      this.$children[0].addSpot();
    },
    removeSpot: function() {
      this.$children[0].excludeSpot();
    },
    cancelAddSpot: function() {
      this.$children[0].cancelAddSpot();
      this.showInfoPklot = false;
    }
  }
};
</script>

<style lang="scss" scoped>
.title {
  // Box Model
  margin-top: 0px;
  margin-bottom: 34px !important;
}

.subtitle {
  // Box Model
  margin-bottom: 24px;
}

.container {
  // Box Model
  width: auto;
  margin: 0 auto;
}

.pklot {
  // Box Model
  display: flex;

  &__info {
    // Position
    position: fixed;
    left: 0;
    top: 0;
    z-index: 0;

    // Box Model
    width: 100%;
    height: 100%;

    // Visual
    background-color: rgba(#000000, 1);
    visibility: visible;
    transition: 0.3s all ease-in-out;

    &-area {
      // Box Model
      width: 300px;
      display: flex;
      flex-direction: column;

      // Position
      position: absolute;
      top: 133px;
      right: 0;

      .icone {
        // Box Model
        width: 50px;
        margin-left: 110px;

        // Visual
        opacity: 0.6;

        &:hover {
          cursor: pointer;
          opacity: 1;
        }
      }

      .content {
        width: 270px;
        background-color: transparent;
        margin-top: 0px;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;

        transition: 0.3s all ease-in-out;
        visibility: hidden;
        opacity: 0;

        &--show {
          // Visual
          transition: 0.3s all ease-in-out;
          visibility: visible;
          opacity: 1;
        }
        p {
          // Typography
          font-size: 16px;
          text-align: center;
          font-weight: bold;
          margin-bottom: 30px;
          margin-top: 15px;
          color: #fff;
          line-height: 22px;
          padding: 0px 20px;
        }

        img {
          // Box Model
          width: 120px;
        }
      }
    }

    &--hidden {
      // Box Model
      visibility: hidden;
      opacity: 0;

      // Visual
      transition: 0.3s all ease-in-out;
    }
  }

  &__canvas {
    // Box Model
    width: calc(100% - 280px);
    position: relative;

    video {
      // Box Model
      width: 100%;
      display: block;
    }
  }
  &__menu {
    // Box Model
    width: 280px;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  &__cta-group {
    // Box Model
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
  }

  &__cta {
    // Box Miodel
    display: flex;
    align-items: center;
    justify-content: center;
    width: 200px;
    height: 44px;
    margin-bottom: 10px;

    // Visual
    border-radius: 6px;
    box-shadow: 0px 0px 3px 0px #77b3f9;
    border: 1px solid;
    transition: 0.3s all ease-in-out;
    visibility: visible;
    opacity: 1;

    // Typography
    text-align: center;
    font-weight: bold;
    font-size: 16px;
    text-transform: uppercase;

    &.hidden {
      pointer-events: none;
      background-color: #ccc;
      border: 1px solid #ccc;
    }

    .pklot__info--hidden & {
      // Box Model
      display: none;
    }
    &--hidden {
      // Box Model
      visibility: hidden;
      opacity: 0;

      // Visual
      transition: 0.2s all ease-in-out;
    }

    &--white {
      // Visual
      background-color: #ffffff;
      border-color: #ffffff;

      // Typography
      color: #74b0f6;

      &:hover {
        // Visual
        background-color: darken($color: #ffffff, $amount: 10);
        border-color: darken($color: #ffffff, $amount: 10);
      }
    }

    &--blue {
      // Visual
      background-color: #74b0f6;
      color: #ffffff;
      border-color: #74b0f6;

      &:hover {
        // Visual
        background-color: darken($color: #74b0f6, $amount: 10);
        border-color: darken($color: #74b0f6, $amount: 10);
      }
    }

    &--outline {
      // Visual
      background-color: transparent;
      border-color: #ffffff;

      // Typography
      color: #ffffff;

      &:hover {
        background-color: #ffffff;
        color: #74b0f6;
      }
    }

    &:hover {
      // Visual
      cursor: pointer;
      transition: 0.3s all ease-in-out;
    }
  }
}
</style>