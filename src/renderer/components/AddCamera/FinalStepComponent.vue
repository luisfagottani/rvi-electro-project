<template>
  <div>
    <h2 class="title">Cadastre sua nova câmera.</h2>
    <h3 class="subtitle">Preencha as informações sobre a câmera a ser cadastrada.</h3>

    <div class="pklot">
      <div class="pklot__canvas">
        <CanvasPark @spots="val => (cameraData.spots = val)" :videoDimensions="dimensions" ></CanvasPark>
        <video id="video-cam" v-if="cameraData.camType === '2'" muted style=""  autoplay :src="cameraData.urlCam"></video>
        <img v-else style="-webkit-user-select: none;" :src="cameraData.urlCam">
      </div>
      <div class="pklot__menu">
        <div class="pklot__cta-group">
          <a class="pklot__cta pklot__cta--white" v-on:click="addSpot()" >Adicionar Vaga</a>
          <a class="pklot__cta pklot__cta--outline" @click="removeSpot()">Remover Vaga</a>
        </div>
        <div class="pklot__cta-group">
          <!-- <a class="pklot__cta pklot__cta--white" v-on:click="backStep()">Voltar</a> -->
          <a class="pklot__cta pklot__cta--blue" @click="finish()" :disabled="cameraData.spots.length > 0 ? false : true">Finalizar</a>
        </div>
      </div>
      
    </div>

  </div>
</template>

<script>
import CanvasPark from "./CanvasPaint";
export default {
  name: "SecondStep",
  mounted() {
    if (this.cameraData.camType === "2") {
      var v = document.getElementById("video-cam");
      v.addEventListener(
        "loadedmetadata",
        e => {
          const canvas = document.querySelector(".pklot__canvas");
          const pklot = document.querySelector(".pklot");
          this.dimensions.widthVideo = canvas.offsetWidth;
          this.dimensions.heightVideo = canvas.offsetHeight;
          canvas.style.height = this.dimensions.heightVideo + "px";
          pklot.style.height = this.dimensions.heightVideo + "px";
        },
        false
      );
    }
  },
  components: {
    CanvasPark
  },
  data: function() {
    return {
      dimensions: {
        widthVideo: 0,
        heightVideo: 0
      }
    };
  },
  props: ["cameraData"],
  methods: {
    backStep: function() {
      if (window.confirm("Suas informações serão perdidas :(")) {
        this.$emit("back-step");
      }
    },
    finish: function() {
      if (this.cameraData.spots.length > 0)
        this.$emit("finish", this.cameraData);
    },
    addSpot: function() {
      this.$children[0].addSpot();
    }
  }
};
</script>

<style lang="scss" scoped>
.title {
  // Box Model
  margin-top: 0px;
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

    // Typography
    text-align: center;
    font-weight: bold;
    font-size: 16px;

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