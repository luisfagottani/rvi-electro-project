
<template>
  <div class="columns">
    <div class="column is-one-fifth ">
      <section class="hero background is-fullheight">
        <div class="hero-body">
          <div class="container">
            <h1 class="title has-text-centered font-white	">
              RVI
            </h1>
            <h2 class="subtitle has-text-centered	font-white">
              Processo de configuração
            </h2>
          </div>
        </div>
      </section>
    </div>

    <div class="column">
      <OnboardingContainer></OnboardingContainer>
    </div>
  </div>
</template>
 

<script>
import OnboardingContainer from '../components/Onboarding/OnboardingContainer';
export default {
  name: 'WelcomePresentation',
  components: {
      OnboardingContainer
  }   
}
</script> 

<style scoped>

  .background {
    background-color: #4286f4;
    padding: 0;
    margin: 0;
  } 

  .title {
    font-size:80px;
  }

  .subtitle {
    font-size: 30px;
  }

  .font-white {
    color: #ffffff;
  }
</style>

