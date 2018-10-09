<template>
  <ul class="camera-menu" >
    <li class="camera-menu__item" v-on:click="changeCamera(camera.camId)"  :key="camera.camId" v-for="camera in menuCams">
      <img src="" alt="">
      <span>{{camera.nameCam}}</span>
    </li>
  </ul>
</template>

<script>
export default {
  name: "menuCameras",
  computed: {
    menuCams: function() {
      return this.$store.getters.getAllCameras;
    }
  },
  methods: {
    changeCamera: function(id) {
      this.$store.dispatch("setCamera", id);
    }
  }
};
</script>

<style lang="scss" scoped>
.camera-menu {
  height: 100%;
  padding: 0;
  display: flex;
  flex-direction: column;
  width: 219px;
  background-color: #3b3d50;
  margin-right: 4px;

  &__item {
    height: 150px;
    width: 219px;
    background-color: #2a2d3f;
    margin-bottom: 4px;

    &--add {
      background-color: #2a2d3f;
    }
  }
}
</style>

