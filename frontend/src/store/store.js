import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import * as Cookies from "js-cookie";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    isLoggedIn: false
  },
<<<<<<< HEAD
  mutations: {
    initialiseStore(state) {
      console.log(localStorage.getItem("status"));
      state.isLoggedIn = localStorage.getItem("status");
    }
  }
=======
  plugins: [createPersistedState({})]
>>>>>>> parent of 8e4f35b (Merge branch 'unstable-frontendV2' into unstable-backendV2)
});
