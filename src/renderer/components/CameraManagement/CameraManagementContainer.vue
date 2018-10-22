<template>
  <div class="cadastro">
    <div class="cadastro__progress" v-bind:style="{width: progress + '%'}"></div>
    <div class="cadastro__content">
      <CameraFormInfo
        v-bind:key="1"
        @next-step="nextStep()" 
        v-if="step == 1 && show == 1"
        :cameraData="cameraData"
        @camera-data="val => { this.cameraData = val }">
      </CameraFormInfo>
    
      <CameraVideo
       v-bind:key="2"
        v-if="step == 2"
        @back-step="backStep()"
        :cameraData="cameraData"
        @finish="saveCamera">
      </CameraVideo>
    </div>
  </div>
</template>

<script>
const fs = require("fs");
const Store = require("electron-store");
const store = new Store();

import CameraFormInfo from "@/components/CameraManagement/CameraFormInfo";
import CameraVideo from "@/components/CameraManagement/CameraVideo";

export default {
  name: "CameraManagement",

  components: {
    CameraFormInfo,
    CameraVideo
  },

  data() {
    return {
      step: 1,
      progress: 50,
      cameraData: {},
      show: false
    };
  },

  mounted() {
    if (this.$route.params.id) {
      this.cameraData = this.$store.getters.getCamera(this.$route.params.id);
      this.show = true;
    } else {
      this.show = true;
    }
  },

  methods: {
    nextStep: function(event) {
      this.step += 1;
      this.progress += 50;
      this.$store.dispatch("setLoading", true);
    },
    backStep: function(event) {
      this.step -= 1;
      this.progress = 50;
    },
    saveCamera: function(val) {
      if (this.$route.params.id) {
        this.updateCamera(val);
      } else {
        this.addCamera(val);
      }
      this.$store.dispatch("showSuccess");
      if (this.$route.params.id) {
        this.$router.push({
          name: "camera",
          params: { id: camera.camId },
          query: { canvasMode: "show" }
        });
      } else {
        this.$router.push({ name: "lista-cameras" });
      }
    },
    updateCamera: function(val) {
      this.cameraData = val;
      this.cameraData.camId = this.$route.params.id;
      this.cameraData.path = store.path;
      store.delete(this.$route.params.id);

      store.set(this.cameraData.camId, this.cameraData);
      if (this.cameraData.typeFile.length > 0) {
        this.cameraData.typeFile = "1";
      }
      this.$store.dispatch("updateCamera", this.cameraData);
    },
    addCamera: function(val) {
      this.cameraData = val;
      this.cameraData.camId = String(
        new Date().getTime() + Math.floor(Math.random() * (999999 - 99 + 1))
      );
      this.cameraData.path = store.path;
      store.set(this.cameraData.camId, this.cameraData);
      if (this.cameraData.typeFile.length > 0) {
        this.cameraData.typeFile = "1";
      }
      this.$store.dispatch("addCamera", this.cameraData);
    }
  }
};
</script>

<style lang="scss" scoped>
.cadastro {
  // Box Model
  width: 100%;
  height: 100%;
  display: block;

  // Visual
  background-color: #3b3d50;

  // Position
  position: relative;

  &__title {
    // Typography
    font-size: 36px;
    font-weight: 600;
    color: #ffffff;
    text-align: center;

    // Box Model
    margin-bottom: 8px;
  }

  &__progress {
    // Position
    position: absolute;
    left: 0;
    top: 0;
    height: 6px;

    // Visual
    background-color: #4a90e2;
    transition: 0.8s all ease-in-out;
  }

  &__content {
    // Box Model
    width: 100%;
    height: 100vh;
    padding: 40px;
  }
}
</style>