<template>
  <div>
    <div class="staging">
      <ShowCamera :getCamera="this.cameraData"></ShowCamera>
    </div>
  </div>
</template>


<script>
const Store = require("electron-store");
const store = new Store();

import ShowCamera from "./ShowCamera";

export default {
  name: "liveContainerTraining",
  components: {
    ShowCamera
  },
  data: function() {
    return {
      showMenuEdit: false
    };
  },
  computed: {
    cameraData: function() {
      return this.$store.getters.getCamera(this.$route.params.id);
    }
  },
  methods: {}
};
</script>

<style lang="scss" scoped>
.staging {
  /* Box Model */
  display: flex;
  height: 100vh;
  flex-direction: column;
  justify-content: space-around;

  // Position
  position: relative;
}

.edit-area {
  // Box Model
  // Position
  position: fixed;
  right: 30px;
  bottom: 60px;
  z-index: 10;

  &__icon {
    // Box Model
    width: 60px;
    height: 60px;
    border-radius: 50%;
    transform: rotate(0deg);
    cursor: pointer;

    // Visual
    background-color: #7c99cc;
    box-shadow: 0px 4px 7px 0px rgba($color: #000000, $alpha: 0.3);

    // Position
    position: relative;

    span {
      // Box Model
      display: block;
      height: 4px;
      width: 35px;
      transform: rotate(0deg);
      border-radius: 5px;

      // Position
      left: 13px;
      position: absolute;

      // Visual
      opacity: 1;
      transition: 0.25s ease-in-out;
      background-color: #ffffff;

      &:nth-child(1) {
        top: 18px;
      }

      &:nth-child(2) {
        top: 28px;
      }

      &:nth-child(3) {
        top: 38px;
      }
    }

    .edit-area--open & {
      span {
        &:nth-child(1) {
          top: 28px;
          transform: rotate(135deg);
        }

        &:nth-child(2) {
          opacity: 0;
          left: -60px;
        }

        &:nth-child(3) {
          top: 28px;
          transform: rotate(-135deg);
        }
      }
    }
  }

  &__content {
    // Position
    position: absolute;
    left: -60px;
    top: 0;

    li {
      width: 50px;
      height: 50px;
      border-radius: 50%;

      // Position
      position: absolute;
      left: 20px;
      top: 0;

      // Visual
      box-shadow: 0px 4px 7px 0px rgba($color: #000000, $alpha: 0.3);
      cursor: pointer;
      opacity: 0;
      visibility: hidden;
      transition: 0.3s ease-in-out all;

      &.delete {
        background-color: #7c99cc;
        border: 1px solid #2e4369;
        text-align: center;
        img {
          display: inline-block;
          width: 30px;
          margin-top: 9px;
        }
      }
      .edit-area--open & {
        transition: 0.3s ease-in-out all;
        opacity: 1;
        visibility: visible;

        &.delete {
          // Visual
          transition: 0.3s ease-in-out all;

          // Position
          top: -60px;
          left: 45px;
        }

        &.edit {
          // Visual
          left: 0px;
          transition: 0.3s ease-in-out all;
        }
      }
    }
  }
}
</style>
