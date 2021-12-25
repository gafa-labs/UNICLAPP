<template>
  <v-container class="pa-16">
    <v-row class="display-1 mb-6">Followings</v-row>
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
      :items="followingClubs"
      class="elevation-1"
      item-key="name"
      :search="search"
    >
      <template v-slot:[`item.status`]="{ item }">
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
      header: {
        headers: {
          Authorization:
            "Token " + JSON.parse(localStorage.getItem("user")).token
        }
      },
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
      followingClubs: []
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
          // filter: value => {
          //   var arr = value[0].split(",");
          //   console.log(value);
          //   var check = false;
          //   this.selected.forEach(item => {
          //     if (arr.includes(item)) {
          //       check = true;
          //     }
          //   });
          //   return check;
          // }
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
    unfollow(item) {
      item.status = "unfollowing";
      axios
        .get(
          "http://127.0.0.1:8000/api/clubs/followings/unfollow/" +
            item.id +
            "/",
          this.header
        )
        .then(response => {
          console.log(response.data);
        })
        .catch(e => console.log(e));
      for (var i = 0; i < this.followingClubs.length; i++) {
        if (this.followingClubs[i].status === "unfollowing") {
          this.followingClubs.splice(i, 1);
        }
      }
    }
  },
  created() {
    axios
      .get("http://127.0.0.1:8000/api/clubs/followings/", this.header)
      .then(response => {
        response.data.forEach(club => {
          club.status = "following";
          this.followingClubs.push(club);
        });
        console.log(this.followingClubs);
      })
      .catch(e => console.log(e));
  }
};
</script>
