<template>
  <v-container class="pa-16">
    <v-row class="display-1 mb-14">Profile</v-row>
    <v-row>
      <v-col
        cols="12"
        md="4"
        class="pr-16"
        style="border-right: 2px solid lightsteelblue"
      >
        <v-text-field
          :value="information.name"
          label="Name"
          outlined
          disabled
          dense
          rounded
          class="mb-6"
        ></v-text-field>
        <v-text-field
          :value="information.student_id"
          label="ID"
          outlined
          disabled
          dense
          rounded
          class="mb-6"
        ></v-text-field>
        <v-text-field
          :value="information.email"
          label="E-mail"
          outlined
          disabled
          dense
          rounded
          class="mb-6"
        ></v-text-field>
        <v-text-field
          :value="information.department"
          label="Department"
          outlined
          disabled
          dense
          rounded
          class="mb-6"
        ></v-text-field>
        <v-row>
          <v-col
            cols="6"
            align-self="center"
            class="pl-4 title font-weight-bold"
          >
            PSI Score
          </v-col>
          <v-col cols="6">
            <v-btn color="grey lighten-2" elevation="1" fab x-large>
              <span class="grey--text text--darken-2 display-1 font-weight-bold"
                >98</span
              >
            </v-btn>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="12" md="4" class="pl-16">
        <v-row>
          <v-col cols="12" md="8">
            <v-text-field
              :value="information.hes_code"
              v-model="information.hes_code"
              label="HES Code"
              outlined
              dense
              rounded
              class="mb-6"
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <v-btn
              @click="submitHES"
              elevation="2"
              rounded
              color="green lighten-1"
              >Submit</v-btn
            ><v-snackbar :color="color" timeout="2000" v-model="snackbar">
              {{ text }}

              <template v-slot:action="{ attrs }">
                <v-btn
                  color="white"
                  text
                  v-bind="attrs"
                  @click="snackbar = false"
                >
                  Close
                </v-btn>
              </template>
            </v-snackbar>
          </v-col>
        </v-row>
        <v-text-field
          value="Change Password"
          filled
          disabled
          dense
          class="mt-4"
        ></v-text-field>
        <v-text-field
          label="Old Password"
          v-model="oldPassword"
          type="password"
          outlined
          dense
          rounded
          class="mt-6"
        ></v-text-field>
        <v-text-field
          label="Create New Password"
          v-model="newPassword"
          type="password"
          outlined
          dense
          rounded
          class="mt-1"
        ></v-text-field>
        <v-text-field
          label="Confirm New Password"
          v-model="confirmPassword"
          type="password"
          outlined
          dense
          rounded
          class="mt-1"
        ></v-text-field>
        <v-row class="mt-1 justify-center">
          <v-btn
            @click="changePass"
            elevation="2"
            rounded
            color="light-blue accent-2"
            >Apply Change</v-btn
          >
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      color: "",
      text: "",
      snackbar: false,
      header: {
        headers: {
          Authorization:
            "Token " + JSON.parse(localStorage.getItem("user")).token
        }
      },
      oldPassword: "",
      newPassword: "",
      confirmPassword: "",
      information: {
        name: "",
        student_id: "",
        email: "",
        department: "",
        psi: 98,
        hes_code: ""
      }
    };
  },
  methods: {
    submitHES() {
      axios
        .put(
          "http://localhost:8000/api/profiles/student/" +
            this.information.id +
            "/update-hes/",
          { hes_code: this.information.hes_code },
          this.header
        )
        .then(response => {
          this.color = "green darken-1";
          this.text = "HES code was updated";
        })
        .catch(e => {
          this.color = "red darken-1";
          this.text = "HES code is not valid";
        })
        .finally(f => {
          this.snackbar = true;
        });
    },
    changePass() {
      // if (
      //   (this.newPassword == "") |
      //   (this.confirmPassword == "") |
      //   (this.oldPassword == "")
      // ) {
      //   alert("FILL ALL THE BLANKS");
      // }
      var id = JSON.parse(localStorage.getItem("user")).id;
      var info = {
        password: this.newPassword,
        password2: this.confirmPassword,
        old_password: this.oldPassword
      };
      axios
        .put(
          "http://localhost:8000/api/change-password/" + id + "/",
          info,
          this.header
        )
        .then(response => {
          this.color = "green darken-1";
          this.text = "Password was changed";
          this.oldPassword = "";
          this.newPassword = "";
          this.confirmPassword = "";
        })
        .catch(e => {
          console.log(e.response.data);
          var mes;
          if (e.response.data.old_password) {
            mes = e.response.data.old_password.old_password;
          } else if (e.response.data.password) {
            mes = e.response.data.password[0];
          }

          this.color = "red darken-1";
          this.text = mes;
        })
        .finally(f => {
          this.snackbar = true;
        });
    }
  },
  created() {
    var token = "Token " + JSON.parse(localStorage.getItem("user")).token;

    axios
      .get("http://localhost:8000/api/profiles/student/", {
        headers: { Authorization: token }
      })
      .then(response => {
        this.information = response.data;
      })
      .catch(e => console.log(e));
  }
};
</script>
