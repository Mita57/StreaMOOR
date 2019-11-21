import Vue from 'vue';
import Router from 'vue-router';

import Info from "@/views/Info";
import Hubs from "@/views/Hubs";

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
      component: Info
    },
    {
      path:'/hubs',
      name:'Hubs',
      component:Hubs
    }

  ],
  mode: 'history'
});


export default router;
