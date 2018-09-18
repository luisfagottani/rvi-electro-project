<template>
  <ul class="camera-menu" >
    <li class="camera-menu__item" v-on:click="changeCamera(camera.camId)"  :key="camera.camId" v-for="camera in menuCams">
      <img src="" alt="">
      <span>{{camera.nameCam}}</span>
    </li>
    <li class="camera-menu__item camera-menu__item--add" v-on:click="changeCamera(camera.camId)">
      <img src="" alt="">
      <span>Nova Câmera</span>
    </li>
  </ul>
</template>

<script>
export default {
  name: 'menuCameras',
   computed: {
    menuCams: function() {
      return this.$store.getters.getAllCameras
    },
  },
  methods: {
    changeCamera: function(id){
      this.$store.dispatch('setCamera', id)
    }
  }
}
</script>

<style lang="scss" scoped>
  .camera-menu {
    height: 100%;
    padding: 0;
    display: flex;
    flex-direction: column;
    width: 219px;
    background-color: #3B3D50;
    margin-right: 4px;

    &__item {
      height: 150px;
      width: 219px;
      background-color: #2A2D3F;
      margin-bottom: 4px;
      
      &--add{
        background-color: #2A2D3F;
      }
    }
   
  }
</style>

