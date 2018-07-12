<template>
  <div class="modal">
    <div class="modal__content">
      <a @click="closeModal">FECHAR MODAL</a>
    </div>
  </div>
</template>


<script>

export default {
  name: 'ConfigureCore',
  methods: {
    closeModal: function() {
      this.$store.dispatch('handleConfigurationModal')
    }
  }
}
</script>

<style lang="scss" scoped> 
  .modal {
    // Box Model
    width: 100%;
    height: 100%;
    display: block;

    /* Position */
    position:  fixed;
    z-index: 10;
    left: 0;
    top: 0;

    // Visual
    background-color: rgba($color: #000000, $alpha: 0.9);

    &__content{
      // Box Model
      width: 900px;
      height: 500px;
      margin:  100px auto;

      // Visual
      background-color: #1d233c;

      // Position
      position: absolute;
      left: 0;
      right: 0;
      bottom: 0;
      top: 0;

    }
  }
</style>
