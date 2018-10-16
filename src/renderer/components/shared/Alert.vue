<template>
  <div class="alert">
    <div class="alert__content">
      <p>{{this.getMessage}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Alert",
  computed: {
    getMessage() {
      return this.$store.getters.getMessageAlert;
    }
  }
};
</script>

<style lang="scss" scoped>
.alert {
  // Position
  position: absolute;
  top: 10px;
  right: 20px;

  // Box Model
  min-width: 200px;
  max-width: 400px;
  min-height: 70px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  padding: 0px 20px;

  //Visual
  border-radius: 4px;
  background-color: #ff5252;

  // Typography
  color: #fff;

  p {
    text-align: right;
  }
}
</style>
