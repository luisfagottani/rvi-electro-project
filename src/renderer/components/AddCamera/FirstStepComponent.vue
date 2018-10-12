<template>
  <div>
    <h2 class="title">Cadastre sua nova câmera.</h2>
    <h3 class="subtitle">Preencha as informações sobre a câmera a ser cadastrada.</h3>

    <div class="container">
      <div class="field">
        <div class="control">
          <input v-bind="showBtn" class="input" type="text" v-model="data.nameCam"
            placeholder="Nome da camera">
        </div>
      </div>

      <div class="field">
        <div class="control">
          <div class="select">
            <select  v-model="data.camType" class="input input--select">
              <option value = "" disabled selected>Selecione o tipo da câmera</option>
              <option value = "1">Camera IP</option>
              <option value = "2">Video Externo</option>
            </select>
          </div>
        </div>
      </div> 

      <div class="field" v-if="data.camType === '2'">
        <input class="file-input" @change="uploadFile()" type="file" name="resume">
        <div class="file-mask">
            <div class="file-mask__cta" @click="selectFile()">
              <img :src="UploadSvg" alt="">
              <span class="file-mask__label">
                Escolha o video...
              </span>
            </div>
            <span class="file-mask__name">
              {{data.urlCam}}
            </span>
        </div>
      </div>

      <div v-if="data.camType === '1' ">
        <div class="field">
          <div class="control">
            <input 
              class="input" 
              type="text" 
              v-model="data.urlCam"
              v-bind="showBtn"
              placeholder="Endereço da Camera IP">
          </div>
        </div>
        <div class="field">
          <div class="control">
            <div class="select">
              <select  v-model="data.typeIp" class="input input--select">
                <option value="motion">Motion JPEG</option>
                <option value="rstp">H.264 (RTSP)</option>
              </select>
            </div>
          </div>
        </div>
      </div>

      <div class="field">
        <a :class="['cta button', {'cta--disabled': disabledBtn}]" v-on:click="nextStep()">Próximo</a>
      </div>
    </div>
    
  </div>
</template>

<script>
import UploadSvg from "@/assets/icons/upload.svg";
export default {
  name: "FirstStep",
  props: ["cameraData"],
  data: function() {
    return {
      data: {
        nameCam: "",
        camType: "",
        urlCam: "",
        typeFile: "",
        typeIp: "motion",
        spots: []
      },
      UploadSvg: UploadSvg,
      disabledBtn: true
    };
  },
  computed: {
    // uma função "getter" computada (computed getter)
    showBtn: function() {
      if (this.data.nameCam && this.data.urlCam) {
        this.disabledBtn = false;
      } else {
        this.disabledBtn = true;
      }
    }
  },
  watch: {
    "data.camType": function() {
      this.data.urlCam = "";
    }
  },
  methods: {
    nextStep: function() {
      if (!this.disabledBtn) {
        if (this.data.camType === "2") {
          this.data.typeIp = "none";
        }
        this.$emit("next-step");
        this.$emit("camera-data", this.data);
      } else {
        alert("Preencha os campos obrigatórios");
      }
    },
    selectFile: function(e) {
      document.querySelector(".file-input").click();
    },
    uploadFile: function() {
      this.data.typeFile = event.currentTarget.files[0].name.split(".").pop();

      if (
        this.data.typeFile !== "mov" &&
        this.data.typeFile !== "avi" &&
        this.data.typeFile !== "mpeg" &&
        this.data.typeFile !== "mp4"
      ) {
        alert("Apenas extensões .mov e .avi");
      } else {
        this.data.urlCam = "file://" + event.currentTarget.files[0].path;
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.file-input {
  // Box Model
  display: none;
}

.file-mask {
  // Box Model
  width: 100%;
  height: 45px;
  border-radius: 9px;
  border: 1px solid;
  border-color: #bbbdc7;
  display: flex;
  align-items: center;

  // Visual
  overflow: hidden;

  // Typography
  font-size: 16px;

  &__cta {
    // Box Model
    display: block;
    height: 100%;
    width: 200px;
    display: flex;
    align-items: center;
    padding: 0px 10px;
    justify-content: space-around;

    // Visual
    background-color: #cccccc;
    color: #000;

    &:hover {
      // Visual
      background-color: #bbbdc7;
      cursor: pointer;
    }

    &:active {
      // Visual
      background-color: darken($color: #bbbdc7, $amount: 10);
    }

    img {
      // Box Model
      width: 22px;
    }
  }

  &__name {
    // Typography
    font-size: 16px;
    color: #ffffff;

    // Box Model
    width: 450px;
    padding: 0px 10px;
  }
}
.field {
  // Box Model
  margin-bottom: 60px;
}
.input {
  // Box Model
  width: 100%;
  height: 45px;
  padding-right: 0;

  // Visual
  background: transparent;
  border: none;
  box-shadow: none;
  border-bottom: 1px solid #bbbdc7;

  // Typography
  font-size: 21px;
  font-weight: 500;
  color: #ffffff;
  border-radius: 0;

  &::-webkit-input-placeholder {
    color: #ffffff;
  }

  &--select {
    // Position
    position: relative;

    // Visual
    -webkit-appearance: none; /* remove the strong OSX influence from Webkit */
  }
}

.select {
  // Position
  position: relative;

  &::after {
    // Box Model
    width: 30px;
    height: 45px;

    // Visual
    content: "";
    background: url("../../assets/icons/arrow-down.svg");
    background-repeat: no-repeat;
    background-position: center;

    // Position
    position: absolute;
    right: 0;
    top: 0;
  }
}

.button {
  // Box Model
  float: right;
}

.container {
  // Box Model
  width: 640px;
  margin: 0 auto;
}
</style>