<template>
  <div class="main">
    <div class="hero" style="justify-content: flex-start">
      <section class="hero is-dark">
        <div class="hero-body">
          <div class="container">
            <h1 class="title">
              Page
              <span class="retarded">not found</span>
            </h1>
            <h2 class="subtitle is-primary">
              return to <a style="color: #D3151B" @click="go">main</a>
            </h2>
          </div>
        </div>
      </section>
      <section class="hero is-large img-block">
        <img src="../assets/notfound.png" width="500" alt="notfound">
      </section>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    go() {
      this.$router.go({ name: 'main' });
    },
  },
};
</script>

<style scoped>
.retarded {
  background: #D3151B;
  padding: 0 0.1rem;
}

.img-block {
  align-items: center;
}
</style>
