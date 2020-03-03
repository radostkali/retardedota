<template>
  <div class="main">
    <div class="section hero achievements-block">
      <div :class="friends ? 'columns' : ''">
        <div :class="friends ? 'column is-9' : ''">
          <h1 class="title" style="text-align: center">Retard's achievements</h1>
          <div class="columns is-mobile is-multiline is-centered">
            <div class="column is-narrow" v-for="(achieve, i) in data" :key="i">
              <achieve-card :achieve="achieve"></achieve-card>
            </div>
          </div>
        </div>
        <div class="column" v-if="friends">
          <h1 class="title" style="text-align: center">Retard's friends</h1>
          <div class="friend-list">
            <div class="friend-block" v-for="(friend, i) in friends" :key="i">
              <div class="friend-info">
                <div class="user-avatar">
                  <a :href="`/${friend.dota_id}`">
                    <figure class="image is-32x32">
                      <img class="is-rounded" :src="friend.avatarfull">
                    </figure>
                  </a>
                </div>
                <div class="user-text">
                  <a :href="`/${friend.dota_id}`">
                    <h1 class="subtitle is-6" style="color: white">
                      {{friend.personaname}}
                    </h1>
                  </a>
                </div>
              </div>
              <a :href="`/${friend.dota_id}`">check</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AchieveCard from './AchieveCard.vue';

export default {
  props: ['data', 'friends'],
  components: {
    'achieve-card': AchieveCard,
  },
};
</script>

<style scoped>
.friend-list {
  display: flex;
  flex-direction: column;
}

.friend-block {
  display: flex;
  margin-bottom: 1rem;
  justify-content: space-between;
}

.friend-info {
  display: flex;
}

.user-avatar {
  margin-right: 0.5rem;
}
</style>
