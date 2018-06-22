<template>
  
<section class="hero cont is-fullheight">
  <div class="hero-body">
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
        <a class="button is-pulled-right is-link is-outlined is-medium" :disabled="disabledBtn == true" v-on:click="nextStep()">Próximo Passo</a>
      </div>
    </div>
  </div>
</section>

</template>

<script>
  export default {
    name: 'FirstStep',
    props: ['formData'],
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
          this.$emit('form-data', this.data);
        }else{
          alert("Preencha os campos obrigatórios");
        }
      },
      uploadFile: function() {
        this.data.typeFile = event.currentTarget.files[0].name.split('.').pop();

        if(this.data.typeFile !== "mov" && this.data.typeFile !== "avi" && this.data.typeFile !== "mpeg"  ){
          alert("Apenas extensões .mov e .avi")
        }else{
          this.data.urlCam = 'file://' + event.currentTarget.files[0].path;
        }
      }
    }
    
  }
</script>

<style scoped>
  .cont {
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
  }
</style>


