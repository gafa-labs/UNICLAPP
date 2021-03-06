import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import * as Cookies from "js-cookie";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    isLoggedIn: false
  },
  mutations: {
    initialiseStore(state) {
      state.isLoggedIn = localStorage.getItem("status") == "true";
    }
  }
});
