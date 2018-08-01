<template>
  <div>
    <h2 class="title">Nova câmera</h2>
    <h3 class="subtitle">Preencha as informações</h3>

    <div class="container">
      <div class="field">
        <label class="label">Nome da camera</label>
        <div class="control">
          <input v-bind="showBtn" class="input" type="text" v-model="data.nameCam"
            placeholder="Nome da camera">
        </div>
      </div>

      <div class="field">
        <label class="label">Tipo de Camera</label>
        <div class="control">
          <div class="select">
            <select  v-model="data.camType">
              <option disabled selected>Selecione o tipo</option>
              <option value="1">Camera IP</option>
              <option value="2">Video Externo</option>
            </select>
          </div>
        </div>
      </div> 

      <div class="field" v-if="data.camType == 2">
        <label class="label">Selecione o arquivo</label>
        <div class="file has-name is-fullwidth">
          <label class="file-label">
            <input class="file-input" @change="uploadFile()" type="file" name="resume">
            <span class="file-cta">
              <span class="file-icon">
                <i class="fas fa-upload"></i>
              </span>
              <span class="file-label">
                Choose a file…
              </span>
            </span>
            <span class="file-name">
              {{data.urlCam}}
            </span>
          </label>
        </div>
      </div>

      <div class="field" v-if="data.camType == 1 ">
        <label class="label">Link da camêra IP</label>
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
        <a class="button is-pulled-right is-link is-medium" :disabled="disabledBtn == true" v-on:click="nextStep()">Próximo Passo</a>
      </div>
    </div>
    
  </div>
</template>

<script>
  export default {
    name: 'FirstStep',
    props: ['cameraData'],
    data() {
      return {
        data: {
          nameCam: '',
          camType: 1,
          urlCam: '',
          typeFile: '',
          spots: []
        },
        disabledBtn: true
      }
    },
    computed: {
      // uma função "getter" computada (computed getter)
      showBtn: function () {
        if(this.data.nameCam && this.data.urlCam){
          this.disabledBtn = false
        }else{
          this.disabledBtn = true
        }
      }
    },
    watch: {
      'data.camType': function() {
        this.data.urlCam = ''
      }
    },
    methods: {
      nextStep: function() {
        if(!this.disabledBtn){
          this.$emit('next-step');
          this.$emit('camera-data', this.data);
        }else{
          alert("Preencha os campos obrigatórios");
        }
      },
      uploadFile: function() {
        this.data.typeFile = event.currentTarget.files[0].name.split('.').pop();

        if(this.data.typeFile !== "mov" && this.data.typeFile !== "avi" && this.data.typeFile !== "mpeg" && this.data.typeFile !== "mp4"   ){
          alert("Apenas extensões .mov e .avi")
        }else{
          this.data.urlCam = 'file://' + event.currentTarget.files[0].path;
        }
      }
    }
    
  }
</script>

<style lang="scss" scoped>

  .title {
    // Typography
    color: #ffffff;
    font-size: 25px;

    // Box Model
    margin: 0;
    margin-bottom: 5px;
    padding-bottom: 10px;
    width: 100%;
    border-bottom: 1px solid #ccc;
  }

  .subtitle {
    // Typography 
    color: #ccc;
    font-size: 16px;

    // Box Model
    margin-top: 0 !important;
    margin-bottom: 20px;
  }

  .field {

    // Box Model
    margin-bottom: 20px;
  }

  .label {
    // Typography
    color: #fff;
    font-weight: 500;
    font-size: 14px;
  }

  .input {
    // Box Model
    height: 45px;
  }

  .container {
    // Box Model
    width: 450px;
    margin: 0 auto;
  }
</style>