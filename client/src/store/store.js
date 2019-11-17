import Vue from 'vue'
import Vuex from 'vuex'
import VuexEasyFirestore from 'vuex-easy-firestore'
Vue.use(Vuex)

// import from step 1
import { Firebase, initFirebase } from '../firebase.js'
// import from step 3 (below)
import worksModule from './modules/worksModule.js'
import usersModule from './modules/usersModule.js'

// do the magic 🧙🏻‍♂️
const easyFirestore = VuexEasyFirestore(
  [usersModule, worksModule],
  {logging: true, FirebaseDependency: Firebase}
)

// include as PLUGIN in your vuex store
// please note that "myModule" should ONLY be passed via the plugin
const storeData = {
  plugins: [easyFirestore],
  // ... your other store data
}

// initialise Vuex
export const store = new Vuex.Store(storeData)

// initFirebase
initFirebase()
  .catch(error => {
    // take user to a page stating an error occurred
    // (might be a connection error, or the app is open in another tab)
  })

export default store