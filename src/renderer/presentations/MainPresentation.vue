<template>
  <div>
    <div class="menu-area">
      <img :src="RviIcon" class="menu-area__logo" alt="">
      <Menu></Menu>
    </div>
    <div class="stage-area">
      <router-view></router-view>
      <transition name="fade" :duration="200">
        <ConfirmeAction v-if="showSuccess"></ConfirmeAction>
      </transition>
    </div>
    <transition name="fade" :duration="200">
      <Alert v-if="showAlert"></Alert>
    </transition>
  </div>
</template>

<script>
import Menu from "../components/Menu/Menu.vue";
import ConfirmeAction from "../components/shared/ConfirmeAction.vue";
import Alert from "../components/shared/Alert.vue";
import RviIcon from "@/assets/icons/rvi.svg";

const Store = require("electron-store");
const store = new Store();

export default {
  name: "MainPresentation",
  data: function() {
    return {
      RviIcon: RviIcon
    };
  },
  components: {
    Menu,
    ConfirmeAction,
    Alert
  },
  computed: {
    showSuccess: function() {
      return this.$store.getters.getStatusSuccess;
    },
    showAlert: function() {
      return this.$store.getters.getShowAlert;
    }
  }
};
</script>

<style scoped lang="scss">
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
  opacity: 1;
}
.fade-enter, .fade-leave-to /* .teste-leave-active em versões anteriores a 2.1.8 */ {
  transition: opacity 0.5s;
  opacity: 0;
}
.menu-area {
  /* Box Model */
  width: 280px;
  height: 100vh;
  padding-top: 30px;
  float: left;

  /* Visual */
  background-color: #1a1e30;

  &__logo {
    // Box Model
    margin: 0px 10px 5px 25px;
  }
}
.stage-area {
  /* Box Model */
  width: calc(100% - 280px);
  height: 100vh;
  float: left;
  background-color: #3b3d50;
}
</style>
