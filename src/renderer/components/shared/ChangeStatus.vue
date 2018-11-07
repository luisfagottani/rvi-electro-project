<template>
  <div class="modal">
    <div class="modal__content">
      <h2 class="modal__title">Corrigir estado da vaga</h2>
      <button class="modal__cta modal__cta--red" v-on:click="processSpot(1)">Ocupada</button>
      <button class="modal__cta modal__cta--green" v-on:click="processSpot(0)">Disponível</button>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    processSpot: function(val) {
      this.$emit("stateCorrection", val);
    }
  }
};
</script>

<style lang="scss" scoped>
.modal {
  // Box Model
  display: flex;
  width: 100%;
  height: 100%;
  justify-content: center;
  align-items: center;

  // Visual
  background-color: rgba($color: #000000, $alpha: 0.5);

  position: fixed;
  top: 0;
  left: 0;
  z-index: 100;

  &__content {
    // Box Model
    width: 380px;
    height: 250px;
    border-radius: 4px;
    display: flex;

    flex-direction: column;
    align-items: center;

    // Visual
    background-color: #1a1e30;
  }

  &__title {
    font-size: 18px;
    font-weight: bold;
    color: #ffffff;
    margin: 30px 0px;
  }

  &__cta {
    width: 90%;
    height: 50px;
    border-radius: 4px;
    box-shadow: none;
    border: none;
    color: #ffffff;
    font-size: 14px;
    font-weight: bold;
    text-transform: uppercase;
    margin: 10px 0px;
    transition: all 0.2s ease-in-out;

    &:hover {
      cursor: pointer;
      transition: all 0.2s ease-in-out;
    }

    &--red {
      background-color: #a12323;

      &:hover {
        background-color: lighten($color: #a12323, $amount: 10);
      }
    }

    &--green {
      background-color: #176f17;

      &:hover {
        background-color: lighten($color: #176f17, $amount: 10);
      }
    }
  }
}
</style>
