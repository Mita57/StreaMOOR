import Vue from 'vue';
import Router from 'vue-router';

import Info from "@/views/Info";
import Hubs from "@/views/Hubs";
import Register from "@/views/Register";
import Channels from "@/views/Channels";
import Channel from "@/views/Channel";
import Search from "@/views/Search";

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
    },
    {
      path:'/register',
      name:'Register',
      component:Register
    },
    {
      path: '/hubs/:id',
      name:'Channels',
      component:Channels
    }
      ,
    {
      path: '/hubs/:id/:user',
      name: 'Channel',
      component: Channel
    },
    {
      path: '/search:/input',
      name: 'Search',
      component: Search
    }

  ],
  mode: 'history'
});


export default router;
