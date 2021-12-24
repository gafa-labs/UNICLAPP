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
              <span
                class="grey--text text--darken-2 display-1 font-weight-bold"
                >{{ information.psi }}</span
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
              label="HES Code"
              outlined
              dense
              rounded
              class="mb-6"
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <v-btn elevation="2" rounded color="green lighten-1">Submit</v-btn>
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
          outlined
          dense
          rounded
          class="mt-6"
        ></v-text-field>
        <v-text-field
          label="Create New Password"
          outlined
          dense
          rounded
          class="mt-1"
        ></v-text-field>
        <v-text-field
          label="Confirm New Password"
          outlined
          dense
          rounded
          class="mt-1"
        ></v-text-field>
        <v-row class="mt-1 justify-center">
          <v-btn elevation="2" rounded color="light-blue accent-2"
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
