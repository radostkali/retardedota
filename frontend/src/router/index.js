import Vue from 'vue';
import VueRouter from 'vue-router';
import Main from '../components/Main.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'main',
    component: Main,
  },
  {
    path: '/:dota_id',
    name: 'user-page',
    props: true,
    component: () => import(/* webpackChunkName: "about" */ '../components/UserPage.vue'),
  },
  {
    path: '*',
    name: 'not-found',
    component: () => import(/* webpackChunkName: "about" */ '../components/NotFound.vue'),
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
