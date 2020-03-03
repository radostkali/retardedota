<template>
  <div class="main">
    <div class="hero" style="justify-content: flex-start">
      <section class="hero is-dark">
        <div class="hero-body">
          <div class="container">
            <h1 class="title">
              {{username ? `User ${username}` : 'User'}} data are
                <span class="retarded">in processing</span>
                <img class="loading" alt="Loading" @mouseenter="newEmoticon"
                  :src="emoticon"
                  decoding="async" width="32" height="32">
            </h1>
            <h2 class="subtitle is-primary">
              it can take some time
            </h2>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import randEmoticon from '../data/emoticons';

export default {
  props: ['username', 'dota_id'],
  data() {
    return {
      emoticon: 'https://gamepedia.cursecdn.com/dota2_gamepedia/e/ea/Emoticon_haste.gif?version=1ab09768368705b24f481f0f644c4807',
      polling: null,
    };
  },
  methods: {
    newEmoticon() {
      this.emoticon = randEmoticon();
    },
    pollStatus() {
      this.polling = setInterval(() => {
        const urlCheckStatus = `/api/check_status/${this.dota_id}`;
        axios.get(urlCheckStatus)
          .then((response) => {
            const { data } = response;
            if (data.status === 'complete' || data.status === 'no_games') {
              this.$router.go();
            }
          });
      }, 1500);
    },
  },
  beforeDestroy() {
    clearInterval(this.polling);
  },
  created() {
    this.pollStatus();
  },
};
</script>

<style scoped>
.retarded {
  background: #D3151B;
  padding: 0 0.1rem;
}

.loading {
  margin-left: 0.9rem;
}
</style>
