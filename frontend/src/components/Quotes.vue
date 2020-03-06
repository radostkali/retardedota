<template>
  <div class="main">
    <div class="container">
      <div class="quote-container">
        <h1 class="subtitle is-5 quote">
          «{{quote.quote}}»
        </h1>
        <h2 class="subtitle is-6 author">
          {{quote.author}}
        </h2>
      </div>
    </div>
  </div>
</template>

<script>
import randQuote from '../data/quotes';

export default {
  data() {
    return {
      quote: null,
      timer: null,
    };
  },
  methods: {
    quoteTimer() {
      this.timer = setInterval(() => {
        this.quote = randQuote();
      }, 10000);
    },
  },
  beforeDestroy() {
    clearInterval(this.timer);
  },
  created() {
    this.quote = randQuote();
    this.quoteTimer();
  },
};
</script>

<style scoped>
.quote-container {
  height: 33rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.quote {
  width: 44rem;
  text-align: center;
  color: #969696;
}

.author {
  padding-bottom: 5rem;
}

@media screen and (max-width: 600px) {
  .quote {
    width: 95%;
  }
}
</style>
