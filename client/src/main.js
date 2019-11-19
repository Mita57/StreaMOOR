import Vue from 'vue';
import App from './App.vue';
import router from './router';
import Vuex from 'vuex';
import vuetify from './plugins/vuetify';
import '@babel/polyfill'
import {store} from './store/store'
Vue.config.productionTip = false;

let app = '';
Vue.use(vuetify);
Vue.use(Vuex);


    app = new Vue({
      router,
      vuetify,
      store,
      render: h => h(App)
    }).$mount('#app');
