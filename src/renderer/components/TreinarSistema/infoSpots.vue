<template>
  <div class="panel-info">
    <ul class="panel-info__spots">
      <li class="panel-info__item">
        {{allSpots}}
        <span>{{allSpots > 1 ? 'vagas' : 'vaga'}}</span>
      </li>

      <li class="panel-info__item panel-info__item--empty">
        {{emptySpots}}
        <span>{{emptySpots > 1 ? 'disponíveis' : 'disponivel'}}</span>
      </li>

      <li class="panel-info__item panel-info__item--occupied">
        {{occupiedSpots}}
        <span>{{occupiedSpots > 1 ? 'ocupadas' : 'ocupada'}}</span>
      </li>
    </ul>
  </div>
</template>


<script>
export default {
  name: "infoSpots",
  computed: {
    getCamera: function() {
      return this.$store.getters.getCamera(this.$route.params.id);
    },
    allSpots: function() {
      return this.getCamera.spots.length;
    },
    emptySpots: function() {
      const spots = this.getCamera.spots;
      var total = 0;
      spots.forEach(spot => {
        if (spot.status == "0") total += 1;
      });
      return total;
    },
    occupiedSpots: function() {
      const spots = this.getCamera.spots;
      var total = 0;
      spots.forEach(spot => {
        if (spot.status == "1") total += 1;
      });
      return total;
    }
  }
};
</script>

<style lang="scss" scoped>
.panel-info {
  /* Box Model */
  height: 100px;
  width: 100%;
  padding: 25px 16px;

  /* Position */
  position: absolute;
  top: 0;
  left: 0;
  z-index: 5;

  /* Visual */
  background-color: rgba($color: #000000, $alpha: 0.9);

  &__spots {
    /* Box Model */
    display: flex;
    padding-left: 40px;
  }

  &__item {
    /* Box Model */
    display: flex;
    align-items: flex-end;
    margin-right: 45px;

    /* Typography */
    color: #fff;
    font-size: 40px;
    font-weight: 800;
    line-height: 39px;

    span {
      /* Typography */
      font-size: 20px;
      font-weight: bold;
      line-height: 24px;
      color: #ffffff;
      margin-left: 10px;
    }

    &--occupied {
      color: #b30421;
    }

    &--empty {
      color: #1e8625;
    }
  }
}
</style>
