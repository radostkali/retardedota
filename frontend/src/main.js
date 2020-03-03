import Vue from 'vue';
import './registerServiceWorker';
import Buefy from 'buefy';
import router from './router';
import App from './App.vue';

Vue.use(Buefy);

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
