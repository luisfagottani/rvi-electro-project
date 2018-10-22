<template>
  <div :class="['mask', {'mask--show': showLoading}]">
    <div class="logo">
      <span class="logo__big-circle">
        <span class="left"></span>
        <span class="right"></span>
        <span class="top"></span>
        <span class="bottom"></span>
      </span>
      <span class="logo__small-circle"></span>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    showLoading: function() {
      return this.$store.getters.getLoadingState;
    }
  }
};
</script>

<style lang="scss" scoped>
.mask {
  // Position
  position: fixed;
  z-index: 15;
  top: 0;
  left: 0;

  // Visual
  background-color: rgba($color: #000000, $alpha: 1);
  opacity: 0;
  visibility: hidden;
  transition: 0.4s ease-in-out 0.4s all;

  // Box Model
  width: 100vw;
  height: 100vh;

  &--show {
    transition: 0.4s ease-in-out all;
    opacity: 1;
    visibility: visible;
  }
}
.logo {
  // Box Model
  width: 80px;
  height: 80px;
  margin: auto;

  // Position
  position: absolute;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;

  // Visual
  transition: 0.4s ease-in-out transform;
  transform: scale(0);

  .mask--show & {
    transition: 0.4s ease-in-out 0.3s transform;
    transform: scale(1.5);
  }

  &__big-circle {
    // Box Model
    width: 80px;
    height: 80px;
    display: block;
    border-radius: 50%;

    // Visual
    border: 6px solid #fff;
    background-color: transparent;
    animation: rotateCircle 0.7s ease-in-out infinite;

    // Position
    position: relative;

    .left,
    .right,
    .top,
    .bottom {
      // Box Model
      width: 8px;
      height: 16px;
      display: block;

      // Visual
      background-color: #000;

      // Position
      position: absolute;
    }

    .top {
      // Position
      top: -10px;
      left: 31px;
    }

    .bottom {
      // Position
      bottom: -10px;
      left: 31px;
    }

    .left {
      // Box Model
      width: 16px;
      height: 8px;

      // Position
      top: 30px;
      left: -10px;
    }

    .right {
      // Box Molde
      width: 16px;
      height: 8px;

      // Position
      top: 30px;
      right: -10px;
    }
  }
  &__small-circle {
    // Position
    position: absolute;
    top: 15px;
    left: 15px;

    // Box Model
    width: 50px;
    height: 50px;
    border: 6px solid #0183c2;
    display: block;

    // Visual
    background-color: transparent;
    border-radius: 50%;
    animation: scaleCircle 0.7s ease-in-out infinite;
  }
}

@keyframes rotateCircle {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(180deg);
  }
}

@keyframes scaleCircle {
  0% {
    transform: scale(0.5);
  }
  50% {
    transform: scale(1);
  }
  100% {
    transform: scale(0.5);
  }
}
</style>

