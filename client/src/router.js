import Vue from 'vue';
import Router from 'vue-router';

import Info from "@/views/Info";

Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: '*',
      redirect: '/info'
    },
    {
      path:'/info',
      name:'Info',
      component: Info,

    }

  ],
  mode: 'history'
});


export default router;
