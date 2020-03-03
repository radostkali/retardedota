<template>
  <div class="main">
    <div class="hero is-fullheight" style="justify-content: flex-start">
      <section class="hero is-dark">
        <div class="hero-body">
          <div class="container">
            <h1 class="title">
              Check Dota 2 profile's owner
            </h1>
            <h2 class="subtitle is-primary">
              for being <span class="retarded">retarded</span>
            </h2>
          </div>
        </div>
      </section>
      <section class="section is-medium">
        <id-input></id-input>
      </section>
    </div>
  </div>
</template>

<script>
import IdInput from './IdInput.vue';

export default {
  components: { 'id-input': IdInput },
};
</script>

<style scoped>
.retarded {
  background: #D3151B;
  padding: 0 0.1rem;
}
</style>
