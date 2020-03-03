<template>
  <div class="main">
    <div class="hero" style="justify-content: flex-start">
      <section class="hero is-dark">
        <div class="hero-body">
          <div class="container">
            <div class="columns">
              <div class="user-block column">
                <div class="user-avatar" v-if="avatar">
                  <figure class="image is-64x64">
                    <img :src="avatar">
                  </figure>
                </div>
                <div class="user-text">
                  <h1 class="title">
                    {{username ? username : 'User'}}
                  </h1>
                  <h2 class="subtitle is-primary with-links">
                    ID {{$route.params.dota_id}}
                    <a :href="`https://www.dotabuff.com/players/${$route.params.dota_id}`" title="Dotabuff">
                      <figure class="image is-16x16 img-link">
                        <img src="../assets/dotabuff.png">
                      </figure>
                    </a>
                  </h2>
                </div>
              </div>
              <div class="column search-block">
                <id-input :small="true"></id-input>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import IdInput from './IdInput.vue';

export default {
  props: ['username', 'avatar'],
  components: { 'id-input': IdInput },
};
</script>

<style scoped>
.retarded {
  background: #D3151B;
  padding: 0 0.1rem;
}

.search-block {
  display: flex;
  justify-content: flex-end;
}

.user-block {
  display: flex;
  align-items: center;
}

.user-avatar {
  margin-right: 1rem;
}

.img-link {
  display: inline-block;
  padding-top: 0.1rem;
  margin-left: 0.3rem;
}
</style>
