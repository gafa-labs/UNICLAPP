<template>
  <v-container class="fill-height light-blue lighten-5" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="8">
        <v-card class="elevation-12">
          <v-window v-model="step">
            <v-window-item :value="1">
              <v-row>
                <v-col cols="12" md="8">
                  <v-card-text class="mt-5">
                    <h1
                      class="text-center display-2 light-blue--text text--darken-3"
                    >
                      Sign in to UNICLAPP
                    </h1>
                    <v-form>
                      <v-text-field
                        label="Email"
                        name="Email"
                        prepend-icon="mdi-email"
                        v-model="information.email"
                        type="text"
                        color="light-blue accent-2"
                      />
                      <v-text-field
                        id="password"
                        label="Password"
                        name="password"
                        v-model="information.password"
                        prepend-icon="mdi-lock"
                        :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                        :type="showPassword ? 'text' : 'password'"
                        color="light-blue darken-3"
                        @click:append="showPassword = !showPassword"
                      ></v-text-field>
                    </v-form>
                    <v-row justify="end">
                      <v-btn text color="light-blue darken-3"
                        >Forgot your password?</v-btn
                      >
                    </v-row>
                  </v-card-text>
                  <div class="text-center mb-10">
                    <v-btn
                      @click="goToMainPage"
                      color="light-blue darken-3"
                      dark
                      >SIGN IN</v-btn
                    >
                  </div>
                </v-col>
                <v-col cols="12" md="4" class="light-blue darken-3">
                  <v-card-text class="white--text mt-12">
                    <h1 class="text-center display-1">Hello,</h1>
                    <h3 class="text-center">
                      Click Sign Up button to register the system
                    </h3>
                  </v-card-text>
                  <v-card-actions class="justify-center white--text">
                    <v-btn
                      class="light-blue lighten-5"
                      elevation="10"
                      outlined
                      rounded
                      text
                      @click="step++"
                      x-large
                    >
                      Sign Up
                    </v-btn>
                  </v-card-actions>
                </v-col>
              </v-row>
            </v-window-item>
            <v-window-item :value="2">
              <v-row>
                <v-col cols="12" md="8">
                  <h1
                    v-color="this.$vuetify.theme.themes.dark.darkColor"
                    class="text-center display-2 mt-5"
                  >
                    Sign up to UNICLAPP
                  </h1>
                  <v-row>
                    <v-col cols="12" md="6">
                      <v-card-text class="">
                        <v-form>
                          <v-text-field
                            id="name"
                            label="Name"
                            v-model="register.full_name"
                            prepend-icon="mdi-account"
                            type="text"
                            color="light-blue accent-2"
                          />
                          <v-text-field
                            id="id"
                            label="ID"
                            v-model="register.studentid"
                            prepend-icon="mdi-id-card"
                            type="text"
                            color="light-blue accent-2"
                          />
                          <v-text-field
                            id="department"
                            label="Department"
                            v-model="register.department"
                            prepend-icon="mdi-school"
                            type="text"
                            color="light-blue accent-2"
                          ></v-text-field>
                        </v-form>
                      </v-card-text>
                    </v-col>
                    <v-divider class="mt-8 mb-8" vertical inset></v-divider>
                    <v-col cols="12" md="6">
                      <v-card-text class="">
                        <v-form>
                          <v-text-field
                            id="email"
                            label="Email"
                            v-model="register.email"
                            prepend-icon="mdi-email"
                            type="text"
                            color="light-blue accent-2"
                          />
                          <v-text-field
                            id="password"
                            label="Password"
                            name="password"
                            v-model="register.password"
                            prepend-icon="mdi-lock"
                            :append-icon="
                              showPassword ? 'mdi-eye' : 'mdi-eye-off'
                            "
                            :type="showPassword ? 'text' : 'password'"
                            color="light-blue accent-2"
                            @click:append="showPassword = !showPassword"
                          ></v-text-field>
                        </v-form>
                      </v-card-text>
                    </v-col>
                  </v-row>
                  <div class="text-center mb-10">
<<<<<<< HEAD
                    <v-btn
                      @click="registerStudent"
                      color="light-blue darken-3"
                      dark
=======
                    <v-btn rounded color="light-blue accent-2" dark v-color:
>>>>>>> parent of 8e4f35b (Merge branch 'unstable-frontendV2' into unstable-backendV2)
                      >SIGN UP</v-btn
                    >
                  </div>
                </v-col>
                <v-col cols="12" md="4" :class="darkColor">
                  <v-card-text class="white--text mt-12">
                    <h1 class="text-center display-1">Hello,</h1>
                    <h3 class="text-center">
                      Click Sign In button to login the system
                    </h3>
                  </v-card-text>
                  <v-card-actions class="justify-center white--text">
                    <v-btn
                      class="light-blue lighten-5"
                      elevation="10"
                      outlined
                      rounded
                      text
                      @click="step--"
                      x-large
                    >
                      Sign In
                    </v-btn>
                  </v-card-actions>
                </v-col>
              </v-row>
            </v-window-item>
          </v-window>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      information: { email: "", password: "" },
      register: {
        email: "",
        password: "",
        full_name: "",
        studentid: "",
        department: ""
      },
      darkColor: "light-blue darken-3",
      step: 1,
      showPassword: false
    };
  },
  props: {
    source: String
  },
  created() {
    this.$store.state.isLoggedIn = false;
    localStorage.setItem("status", false);
  },
  methods: {
    goToMainPage() {
      axios
        .post("http://localhost:8000/api/login/", this.information)
        .then(response => {
          console.log(response);
          localStorage.setItem("user", JSON.stringify(response.data));
          this.$store.state.isLoggedIn = true;
          localStorage.setItem("status", true);
          this.$router.push("/main");
        })
        .catch(e => {
          console.log(e.response);
          if (e.response.status == 400) {
            alert("Email or password is incorrect. Please try again!");
            return;
          }
        });
    },
    registerStudent() {
      console.log("girdi");
      axios
        .post("http://localhost:8000/api/register/", this.register)
        .then(response => {
          console.log(response.data);
          this.step--;
        })
        .catch(e => console.log(e.response));
    }
  }
};
</script>
