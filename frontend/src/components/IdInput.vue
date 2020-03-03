<template>
  <div class="main">
    <div class="container">
      <div class="field has-addons input-container">
        <div :class="['control input-wrapper', small ? 'small' : '']">
          <input class="input is-primary" type="text"
            :placeholder="small ? 'Search user' : 'Example: 120150156'"
            v-model="input" @keypress.enter="check_id">
          <p :class="[error_message ? 'is-primary' : 'is-light', 'help']">
            {{error_message ?
              error_message : 'Paste DotaID, SteamID, Steam url or Dotabuff url'}}
          </p>
        </div>
        <div class="control">
          <a class="button is-primary" @click="check_id">
            Check It
          </a>
        </div>
      </div>
    </div>
    <b-loading :active.sync="loading"></b-loading>
  </div>
</template>

<script>
import axios from 'axios';

const urlCheckId = '/api/check_user';

export default {
  props: ['small'],
  data() {
    return {
      input: null,
      error_message: null,
      loading: false,
    };
  },
  methods: {
    check_id() {
      this.loading = true;
      axios.post(urlCheckId, { input: this.input })
        .then((response) => {
          const { data } = response;
          this.loading = false;
          if (data.status === 'error') {
            this.error_message = data.message;
          } else if (data.status === 'success') {
            this.error_message = null;
            if (data.dota_id !== this.$route.params.dota_id) {
              this.$router.push({ name: 'user-page', params: { dota_id: data.dota_id } });
            } else {
              this.$router.go();
            }
          }
        });
    },
  },
};
</script>

<style scoped>
div.input-container {
  justify-content: center;
}

div.input-wrapper {
  width: 30rem;
}

div.input-wrapper.small {
  width: 20rem;
}

@media screen and (max-width: 600px) {
  div.input-wrapper, div.input-wrapper.small {
    width: auto;
  }
}
</style>
