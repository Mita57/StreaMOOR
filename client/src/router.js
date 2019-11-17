import Vue from 'vue';
import Router from 'vue-router';

import Tasks from '@/views/Tasks';
import Login from '@/views/Login';
import SignUp from '@/views/SignUp';
import Account from'@/views/Account';
import CreateTask from "@/views/CreateTask";
import Info from "@/views/Info";

Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: '*',
      redirect: '/login'
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/sign-up',
      name: 'SignUp',
      component: SignUp
    },
      {
          path: '/tasks',
          name: 'Tasks',
          component: Tasks,
      },
    {
      path:'/account',
      name:'Account',
      component: Account,
    },
    {
      path:'/createTask',
      name:'Create task',
      component: CreateTask,
      }
      ,
    {
      path:'/info',
      name:'Info',
      component: Info,

    }

  ],
  mode: 'history'
});


export default router;
