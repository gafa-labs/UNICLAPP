<template>
  <v-container class="pa-16">
    <v-row class="display-1 mb-6">Leaderboard</v-row>
    <v-text-field v-model="search" label="Search" filled rounded dense>
    </v-text-field>
    <v-row class="align-center mb-2">
      <v-col cols="12" sm="1" class="pl-5">
        Sort by:
      </v-col>
      <v-col cols="12" sm="11">
        <v-chip-group mandatory active-class="primary--text">
          <v-chip v-for="el in sortElements" :key="el.key" @click="sort(el)">{{
            el.value
          }}</v-chip>
        </v-chip-group>
      </v-col>
    </v-row>
    <v-data-table
      :headers="headers"
      :items="clubs"
      class="elevation-1"
      item-key="name"
      :search="search"
      :sort-desc="true"
      :sort-by="sortBy"
    >
    </v-data-table>
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
      sortBy: "followers",
      search: "",
      sortElements: [
        {
          key: "number_of_followers",
          value: "Followers"
        },
        {
          key: "rate",
          value: "Rate"
        },
        {
          key: "number_of_events",
          value: "Events"
        },
        {
          key: "number_of_total_participants",
          value: "Participants"
        }
      ],
      //sortElements: ["Followers", "Rate", "Events", "Participants"],
      clubs: []
    };
  },
  computed: {
    headers() {
      return [
        {
          text: "Name",
          align: "start",
          value: "name",
          sortable: false
        },
        {
          text: "Category",
          value: "category",
          sortable: false
        },
        {
          text: "Followers",
          value: "number_of_followers",
          sortable: false
        },
        {
          text: "Average Rate",
          sortable: false,
          value: "rate"
        },
        {
          text: "Total Events",
          sortable: false,
          value: "number_of_events"
        },
        {
          text: "Total Participants",
          sortable: false,
          value: "number_of_total_participants"
        }
      ];
    }
  },
  methods: {
    follow(item) {
      item.status = "following";
    },
    unfollow(item) {
      item.status = "unfollowing";
    },
    sort(value) {
      this.sortBy = value.key;
    }
  },
  created() {
    axios
      .get("http://127.0.0.1:8000/api/clubs/leaderboard/", this.header)
      .then(response => {
        this.clubs = response.data;
      })
      .catch(e => console.log(e));
  }
};
</script>
