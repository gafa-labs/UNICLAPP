<template>
  <v-container class="pa-16">
    <v-row class="display-1 mb-6">Explore</v-row>
    <v-text-field
      v-model="search"
      label="Search"
      filled
      rounded
      dense
    ></v-text-field>
    <v-row class="align-center mb-2">
      <v-col cols="12" md="2" v-if="!selectedAll">
        <v-btn @click="selectAll">Select All</v-btn>
      </v-col>
      <v-col cols="12" md="2" v-if="selectedAll">
        <v-btn @click="unselectAll">Unselect All</v-btn>
      </v-col>
      <v-col cols="12" md="2">
        <v-checkbox
          v-model="selected"
          label="Business"
          value="Business"
        ></v-checkbox>
      </v-col>
      <v-col cols="12" md="2">
        <v-checkbox
          v-model="selected"
          label="Software"
          value="Software"
        ></v-checkbox>
      </v-col>
      <v-col cols="12" md="2">
        <v-checkbox
          v-model="selected"
          label="Science"
          value="Science"
        ></v-checkbox>
      </v-col>
      <v-col cols="12" md="2">
        <v-checkbox
          v-model="selected"
          label="Hobbies"
          value="Hobbies"
        ></v-checkbox>
      </v-col>
      <v-col cols="12" md="2">
        <v-checkbox
          v-model="selected"
          label="Entertainment"
          value="Entertainment"
        ></v-checkbox>
      </v-col>
    </v-row>
    <v-data-table
      :headers="headers"
      :items="clubs"
      class="elevation-1"
      item-key="name"
      :search="search"
    >
      <template v-slot:[`item.status`]="{ item }">
        <v-btn
          color="green lighten-1"
          rounded
          small
          v-if="item.status === 'unfollowing'"
          @click="follow(item)"
          >Follow</v-btn
        >
        <v-btn
          color="red lighten-1"
          rounded
          small
          v-if="item.status === 'following'"
          @click="unfollow(item)"
          >Unfollow</v-btn
        >
      </template>
    </v-data-table>
  </v-container>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      selectedAll: true,
      categories: [
        "Business",
        "Software",
        "Science",
        "Hobbies",
        "Entertainment"
      ],
      selected: ["Business", "Software", "Science", "Hobbies", "Entertainment"],
      search: "",
      clubs: []
    };
  },
  computed: {
    headers() {
      return [
        {
          text: "Name",
          align: "start",
          value: "name"
        },
        {
          text: "Category",
          value: "category"
        },
        {
          text: "Followers",
          value: "number_of_followers"
        },
        {
          text: "Rate",
          value: "rate"
        },
        {
          text: "Following",
          sortable: false,
          align: "center",
          value: "status"
        }
      ];
    }
  },
  methods: {
    selectAll() {
      this.selectedAll = true;
      this.categories.forEach(category => {
        if (!this.selected.includes(category)) {
          this.selected.push(category);
        }
      });
    },
    unselectAll() {
      this.selectedAll = false;
      this.selected = [];
    },
    follow(item) {
      item.status = "following";
    },
    unfollow(item) {
      item.status = "unfollowing";
    }
  },
  created() {
    axios
      .get("http://127.0.0.1:8000/api/clubs/")
      .then(response => {
        response.data.map(club => {
          if (!club.number_of_followers) {
            club.number_of_followers = 0;
          }
        });
        this.clubs = response.data;
      })
      .catch(e => console.log(e));
  }
};
</script>
