import Vue from 'vue';
import Vuetify from 'client/src/plugins/vuetify';
import 'vuetify/dist/vuetify.min.css';

Vue.use(Vuetify);

export default new Vuetify({
  icons: {
    iconfont: 'mdi',
  },
  theme:{
    dark:true,
  }
});
