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
                    <figure v-if="patreon" class="image is-32x32 img-link"
                      :title="(patreon === 'premium') ?
                      'Premium non-retard supporter' :
                      'Project supporter'">
                      <img :src="(patreon === 'premium') ?
                      'https://gamepedia.cursecdn.com/dota2_gamepedia/d/d2/Emoticon_dac15_cool.gif?version=55cbf725ab03cb27a5cf58c091c02189' :
                      'https://gamepedia.cursecdn.com/dota2_gamepedia/b/bd/Emoticon_dealwithit.gif?version=7ba89329d74fdb19bea42cf64411912d'">
                    </figure>
                  </h1>
                  <h2 class="subtitle is-primary">
                    ID {{$route.params.dota_id}}
                    <a :href="`https://www.dotabuff.com/players/${$route.params.dota_id}`" title="Dotabuff">
                      <figure class="image is-16x16 img-link">
                        <img src="../assets/dotabuff.png">
                      </figure>
                    </a>
                    <b-button type="is-primary is-small btn" outlined
                      v-if="update" @click="updateData">
                      Update Data
                    </b-button>
                  </h2>
                </div>
              </div>
              <div class="column">
                <div class="rate-block">
                  <span class="rank">{{rank}}</span>
                  <div class="rate">
                    <figure class="image is-16x16 rate-one" v-for="(j, i) in rate" :key="i">
                      <img src="../assets/rate.png" alt="rate" >
                    </figure>
                    <figure class="image is-16x16 rate-one" v-for="(j, i) in (5 - rate)" :key="i">
                      <img src="../assets/rate-bnw.png" alt="rate" >
                    </figure>
                  </div>
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
import axios from 'axios';
import IdInput from './IdInput.vue';

const urlUpdate = '/api/update';

export default {
  props: ['username', 'avatar', 'update', 'dota_id', 'rate', 'patreon'],
  components: { 'id-input': IdInput },
  methods: {
    updateData() {
      axios.post(urlUpdate, { dota_id: this.dota_id })
        .then((response) => {
          const { data } = response;
          if (data.status === 'success') {
            this.$router.go();
          }
        });
    },
  },
  computed: {
    rank() {
      if (this.rate === 0) {
        return 'Holy doter';
      }
      if (this.rate === 1) {
        return 'Almost retard';
      }
      if (this.rate === 2) {
        return 'Default retard';
      }
      if (this.rate === 3) {
        return 'Piece of retard';
      }
      if (this.rate === 4) {
        return 'Retarded retard';
      }
      if (this.rate === 5) {
        return 'Absolute retard';
      }
      return 'Hmmm';
    },
  },
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

.btn {
  margin-left: 1rem;
}

.rate-block {
  display: flex;
  height: 100%;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: fit-content;
  background-color: #161616;
  padding: 0.7rem 1rem;
}

@media screen and (max-width: 600px) {
  .rate-block {
    width: auto;
  }

  .search-block {
    justify-content: center;
  }
}

.rank {
  color: #D3151B;
  font-size: 1.1rem;
}

.rate {
  display: flex;
  justify-content: center;
}

.rate-one:not(:last-child) {
  margin-right: 0.3rem;
}
</style>
