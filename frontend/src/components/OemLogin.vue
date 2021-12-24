<template>
  <v-container class="fill-height light-blue lighten-5" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="8">
        <v-card class="elevation-12">
          <v-row>
            <v-col cols="12">
              <v-card-text class="mt-5 text-center">
                <span class="display-2 light-blue--text text--darken-3">
                  Hi OEM! </span
                ><span class=" display-1 light-blue--text text--darken-3">
                  Sign in to UNICLAPP
                </span>

                <v-form>
                  <v-text-field
                    label="Username"
                    name="username"
                    prepend-icon="mdi-account"
                    type="text"
                    color="light-blue darken-3"
                  />
                  <v-text-field
                    label="Password"
                    name="password"
                    prepend-icon="mdi-lock"
                    :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                    :type="showPassword ? 'text' : 'password'"
                    color="light-blue darken-3"
                    @click:append="showPassword = !showPassword"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <div class="text-center mb-10">
                <v-btn
                  @click="goToMainPage"
                  color="light-blue darken-3"
                  dark
                  rounded
                  >SIGN IN</v-btn
                >
              </div>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
export default {
  data() {
    return {
      step: 1,
      showPassword: false
    };
  },
  methods: {
    goToMainPage() {
      this.$router.push("/oemMain");
    }
  }
};
</script>
