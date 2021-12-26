import Vue from "vue";
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";
import colors from "vuetify/lib/util/colors";

Vue.use(Vuetify);

const opts = {
  theme: {
    themes: {
      dark: {
        darkColor: "#277BD"
      }
    },
    dark: false
  }
};

export default new Vuetify(opts);
