<template>
  <v-container class="pa-16">
    <v-row class="display-1 mb-6">Club Profile</v-row>
    <v-row>
      <v-spacer></v-spacer>
      <v-col cols="8">
        <v-row
          style="text-align: center;"
          class="text-h4 font-weight-bold mt-10"
          justify="center"
          >{{ club.name }}</v-row
        >
        <v-row class="mt-6">
          <v-spacer></v-spacer>
          <v-col style="border-right: lightsteelblue solid 1px;" cols="2">
            <v-row class="text-h4 mt-auto" justify="center">
              {{ club.followers }}</v-row
            >
            <v-row class="text-subtitle-1 mt-2" justify="center"
              >Followers</v-row
            >
          </v-col>
          <v-col cols="2">
            <v-row class="text-h4 mt-auto" justify="center">
              {{ club.rate }}</v-row
            >
            <v-row class="text-subtitle-1 mt-2" justify="center">Rate</v-row>
          </v-col>
          <v-spacer></v-spacer>
        </v-row>
        <v-textarea
          label="About"
          v-model="club.about"
          counter="400"
          maxlength="400"
          no-resize
          rows="4"
          outlined
          dense
          rounded
          class="mt-12 px-16"
          background-color="grey lighten-3"
        ></v-textarea>
        <v-row>
          <v-col cols="8"
            ><v-select
              v-model="club.category"
              :items="categories"
              filled
              outlined
              dense
              rounded
              label="Category"
              class="mt-6 px-16"
            ></v-select
          ></v-col>
          <v-col cols="4"
            ><v-btn
              @click="update"
              elevation="2"
              rounded
              color="light-blue accent-2"
              class="mt-6"
              >Update</v-btn
            ></v-col
          >
        </v-row>
        <v-card class="mt-6">
          <v-card-title class="justify-center">Board Members</v-card-title>
          <v-data-table
            :headers="headers"
            :items="club.boardMembers"
            item-key="name"
          >
          </v-data-table>
        </v-card>
      </v-col>
      <v-spacer></v-spacer>
    </v-row>
  </v-container>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      header: {
        headers: {
          Authorization:
            "Token " + JSON.parse(localStorage.getItem("user")).token
        }
      },
      categories: [
        "Business",
        "Software",
        "Science",
        "Hobbies",
        "Entertainment"
      ],
      club: {
        name: "",
        id: "",
        followers: "",
        rate: "",
        about: "",
        category: "",
        boardMembers: []
      }
    };
  },
  methods: {
    update() {
      var newUpdate = {
        about: this.club.about,
        category: this.club.category.toLowerCase()
      };
      var endpoint =
        "http://localhost:8000/api/club/profile/" + this.club.id + "/";
      console.log(endpoint);
      axios.put(endpoint, newUpdate, this.header);
    }
  },
  computed: {
    headers() {
      return [
        {
          text: "Name",
          align: "start",
          value: "name"
        }
      ];
    }
  },
  created() {
    axios
      .get("http://localhost:8000/api/club/profile/", this.header)
      .then(response => {
        console.log(response.data[0]);
        this.club.name = response.data[0].club.name;
        this.club.id = response.data[0].club.id;
        this.club.about = response.data[0].club.about;
        this.club.category =
          response.data[0].club.category.charAt(0).toUpperCase() +
          response.data[0].club.category.slice(1);
        this.club.rate = response.data[0].club.rate;
        this.club.followers = response.data[0].club.number_of_followers;
        response.data.forEach(data => {
          const student = {
            name: data.student.user.full_name
          };
          this.club.boardMembers.push(student);
        });
      });
  }
};
</script>
