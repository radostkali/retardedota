<template>
  <div class="main">
    <div :class="['card', `card-size-${achieve.rank}`]">
      <div class="card-content">
        <div class="media">
          <div class="media-left">
            <figure class="image is-48x48">
              <img :src="achieve.detail_img" alt="Detail image">
            </figure>
          </div>
          <div class="media-content">
            <p class="title is-4">{{achieve.name}}</p>
            <p class="subtitle is-6 is-grey">{{achieve.detail}}</p>
          </div>
        </div>

        <div class="content" v-html="achieve.description"></div>
      </div>
      <footer class="card-footer">
        <div class="card-footer-item is-grey">
          Retard rank:
          <div class="rate-block">
            <figure class="image is-16x16 rate-one" v-for="(j, i) in achieve.rank" :key="i">
              <img src="../assets/rate.png" alt="rate" >
            </figure>
            <span v-if="achieve.rank === 0">oh shit</span>
          </div>
        </div>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  props: ['achieve'],
};
</script>

<style scoped>
.is-grey {
  color: #838383;
}

.rate-block {
  display: inline-flex;
  margin-left: 0.1rem;
}

.bnw {
  filter: grayscale(100%);
}

.rate-one {
  margin-left: 0.2rem;
}

.card-size-0 {
  max-width: 15rem;
}

.card-size-1 {
  max-width: 15rem;
}

.card-size-2 {
  max-width: 17rem;
}

.card-size-3 {
  max-width: 19rem;
}

.card-size-4 {
  max-width: 21rem;
}

.card-size-5 {
  max-width: 22rem;
}


</style>
