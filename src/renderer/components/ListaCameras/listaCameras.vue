<template>
  <div>
    <ul class="camera-menu" v-if="menuCams.length > 0">
      <li class="camera-menu__item" v-on:click="changeCamera(camera.camId)"  :key="camera.camId" v-for="camera in menuCams">
        <router-link :to="{ name: 'camera', params: {id: camera.camId}, query: {canvasMode: 'show'}}">
          <img :src="path + camera.camId + '.png'" alt="">
          <span>{{camera.nameCam}}</span>
        </router-link>
      </li>
    </ul>
    <div v-else class="camera-menu__item camera-menu__item--add" v-on:click="addCamera()" >
          <img :src="PlusCamera" alt="">
          <span>Nova Câmera</span>
      </div>
  </div>
</template>

<script>
import ExampleImage from "@/assets/imagem01.png";
import PlusCamera from "@/assets/icons/new-camera.svg";
export default {
  name: "menuCameras",
  data() {
    return {
      ExampleImage: ExampleImage,
      PlusCamera: PlusCamera,
      path: "static/thumbs/"
    };
  },
  beforeRouteLeave(to, from, next) {
    if (to.name === "camera") {
      this.$store.dispatch("setLoading", {
        status: true,
        message: "",
        showMessage: false
      });
      this.sleep(2000).then(() => {
        next();
      });
    } else {
      next();
    }
  },
  computed: {
    menuCams: function() {
      return this.$store.getters.getAllCameras;
    }
  },
  created() {
    this.$store.dispatch("setLoading", {
      status: false,
      message: "",
      showMessage: false
    });
  },
  methods: {
    changeCamera: function(id) {
      this.$store.dispatch("setCamera", id);
    },
    sleep(time) {
      return new Promise(resolve => setTimeout(resolve, time));
    },
    addCamera: function() {
      this.$router.push({ name: "add-camera", query: { canvasMode: "add" } });
    }
  }
};
</script>

<style lang="scss" scoped>
.camera-menu {
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  margin-top: 30px;
  justify-content: flex-start;

  &__item {
    height: 230px;
    width: 280px;
    background-color: #2a2d3f;
    margin-bottom: 30px;
    box-shadow: 0px 4px 7px 0px rgba($color: #000000, $alpha: 0.3);
    border-radius: 4px;
    overflow: hidden;
    position: relative;
    transition: 0.3s ease-in-out all;
    margin-right: 15px;
    margin-left: 15px;

    &:hover {
      transition: 0.3s ease-in-out all;
      box-shadow: 0px 4px 7px 0px rgba($color: #000000, $alpha: 0.6);

      span {
        transition: 0.3s ease-in-out all;
        background-color: rgba($color: #1a1e30, $alpha: 0.8);
        color: #fff;
      }
    }

    img {
      height: 100%;
      display: block;
    }

    span {
      display: block;
      position: absolute;
      bottom: 0;
      background-color: rgba($color: #000000, $alpha: 0.5);
      color: #ffffff;
      padding: 10px;
      transition: 0.3s ease-in-out all;
      border-top-right-radius: 4px;
    }

    &:hover {
      // Visual
      cursor: pointer;
    }

    &--add {
      // Box Model
      margin: 20px;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;

      // isual
      background-color: #2a2d3f;
      img {
        width: 54px;
        margin: 0 auto;
        height: auto;
        margin-bottom: 20px;
      }
      span {
        // Position
        position: static;

        // Visual
        background-color: transparent;

        // Typography
        color: #bbbdc7;
        text-align: center;
        font-size: 16px;
      }

      &:hover {
        span {
          background-color: transparent;
        }
      }
    }
  }
}
</style>

