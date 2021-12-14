import Vue from "vue";
import App from "./App.vue";
import VueRouter from "vue-router";
import { routes } from "./routes";
import vuetify from "./plugins/vuetify";
import { store } from "./store/store";

Vue.config.productionTip = false;

Vue.directive("color", {
  bind(el, binding, vnode) {
    if (binding.arg == "background") {
      el.style.backgroundColor = binding.value;
    } else {
      el.style.color = binding.value;
    }
  }
});

Vue.use(VueRouter);

const router = new VueRouter({
  routes: routes,
  mode: "history"
});

new Vue({
  router: router,
  vuetify: vuetify,
  store: store,
  render: h => h(App)
}).$mount("#app");
