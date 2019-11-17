import Vue from 'vue';
import firebase from 'firebase';
import App from './App.vue';
import router from './router';
import Vuex from 'vuex';
import vuetify from './plugins/vuetify';
import '@babel/polyfill'
import {store} from './store/store'
//import VueFire from 'vuefire';
Vue.config.productionTip = false;

let app = '';
//firebase.initializeApp(config);
Vue.use(vuetify);
Vue.use(Vuex);
//Vue.use(VueFire);


firebase.auth().onAuthStateChanged(() => {
  if (!app) {
    /* eslint-disable no-new */
    app = new Vue({
      router,
      vuetify,
      store,
      render: h => h(App)
    }).$mount('#app');
  }
});
