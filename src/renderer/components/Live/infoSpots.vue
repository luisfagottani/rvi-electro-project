<template>
  <div class="dash">
    <ul class="dash__infos">
      <li class="dash__item">
        00
        <span>Número </br>de Vagas</span>
      </li>

      <li class="dash__item dash__item--empty">
        --
        <span>Disponíveis</span>
      </li>

      <li class="dash__item dash__item--occupied">
        --
        <span>Ocupadas</span>
      </li>
    </ul>
  </div>
</template>


<script>
                                       
export default {
  name: 'infoSpots',
  data(){
    return {
     formData: {}
    }
  },
}
</script>

<style lang="scss" scoped> 
  .dash {
    /* Box Model */
    display: flex;
    height: 80%;
    width: 276px;
    align-self: center;
    justify-content: center;
    padding: 10px;


    /* Visual */
    background-color: #060810;
    box-shadow: 0px 0px 29px -3px rgba(0,0,0,0.27);

    &__infos {
      /* Box Model */
      display: flex;
      flex-direction: column;
      justify-content: space-around;
    }

    &__item {
      /* Box Model */
      display: flex;
      flex-direction: column;
      align-items: center;

      /* Typography */
      color: #fff;
      font-size: 70px;
      font-weight: 800;
      line-height: 70px;

      span {
        /* Typography */
        font-size: 14px;
        font-weight: bold;
        line-height: 14px;
        text-transform: uppercase;
        color: #ada7a7;
        text-align: center;
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
