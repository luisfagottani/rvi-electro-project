<template>
  <div>
    <div class="staging">
      <showCamera :getCamera="this.cameraData"></showCamera>
      <div :class="['edit-area', {'edit-area--open': showMenuEdit}]" v-on:click="showMenuEdit = !showMenuEdit">
        <div class="edit-area__icon">
          <span></span>
          <span></span>
          <span></span>
        </div>
        <ul class="edit-area__content">
          <li class="edit">
            <router-link :to="{ name: 'edit-camera', params: {id: this.$route.params.id } }">
              <img :src="EditIcon" alt="">
            </router-link>
          </li>
          <li class="delete">
            <img :src="DeleteIcon" alt="">
          </li>
        </ul>
      </div>
      <!-- <infoSpots cameraId=this.$store.getters.getActualCamera></infoSpots> -->
    </div>
    
  </div>
</template>


<script>
import infoSpots from "./infoSpots";
import showCamera from "./showCamera";
import EditIcon from "@/assets/icons/edit-button.svg";
import DeleteIcon from "@/assets/icons/delete-button.svg";

export default {
  name: "liveContainer",
  components: {
    infoSpots,
    showCamera
  },
  data: function() {
    return {
      EditIcon: EditIcon,
      DeleteIcon: DeleteIcon,
      showMenuEdit: false
    };
  },
  computed: {
    cameraData: function() {
      return this.$store.getters.getCamera(this.$route.params.id);
    }
  }
};
</script>

<style lang="scss" scoped>
.staging {
  /* Box Model */
  display: flex;
  height: auto;
  flex-direction: column;

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
