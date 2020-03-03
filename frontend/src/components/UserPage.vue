<template>
  <div class="hello">
    <no-user v-if="status === 'not_found'"></no-user>
    <no-games v-if="status === 'no_games'"></no-games>
    <pending v-if="status === 'pending'" :username="username" :dota_id="dota_id"></pending>
    <complete v-if="status === 'complete'" :username="username" :avatar="avatar"></complete>
    <quotes v-if="status == 'pending' && !data"></quotes>
    <user-data v-if="data" :data="data" :friends="friends"></user-data>
    <b-loading :active.sync="loading"></b-loading>
  </div>
</template>

<script>
import axios from 'axios';
import NoUser from './NoUser.vue';
import NoGames from './NoGames.vue';
import Pending from './Pending.vue';
import Complete from './Complete.vue';
import UserData from './UserData.vue';
import Quotes from './Quotes.vue';

export default {
  name: 'UserPage',
  props: ['dota_id'],
  components: {
    'no-user': NoUser,
    'no-games': NoGames,
    'user-data': UserData,
    pending: Pending,
    complete: Complete,
    quotes: Quotes,
  },
  data() {
    return {
      loading: false,
      status: null,
      username: null,
      avatar: null,
      friends: null,
      data: null,
    };
  },
  methods: {
    check_status() {
      this.loading = true;
      const urlCheckStatus = `/api/check_status/${this.dota_id}`;
      axios.get(urlCheckStatus)
        .then((response) => {
          const { data } = response;
          this.loading = false;
          this.status = data.status;
          this.username = data.personaname;
          this.avatar = data.avatar;
          this.friends = data.friends;
          if (data.data) {
            this.data = data.data;
          }
          console.log(data);
        });
    },
  },
  created() {
    this.check_status();
  },
  watch: {
    dota_id() {
      this.data = null;
      this.check_status();
    },
  },
};
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
