<template>
  <v-container class="pa-16">
    <v-row class="display-1 mb-6">Leaderboard</v-row>
    <v-text-field v-model="search" label="Search" filled rounded dense>
    </v-text-field>
    <v-row class="align-center mb-2">
      <v-col cols="12" md="2">
        Sort by:
      </v-col>
      <v-col cols="12" md="10">
        <v-chip-group mandatory active-class="primary--text">
          <v-chip v-for="el in sortElements" :key="el" @click="sort(el)">{{
            el
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
export default {
  data() {
    return {
      sortBy: "followers",
      search: "",
      sortElements: ["Followers", "Rate", "Events", "Participants"],
      clubs: [
        {
          name: "ACM Bilkent Club",
          category: ["Business,Software,Science"],
          followers: "1545",
          rate: "4.5",
          events: 10,
          participants: 123
        },
        {
          name: "Management and Economics Society",
          category: ["Business"],
          followers: "6889",
          rate: "4.6",
          events: 11,
          participants: 125
        },
        {
          name: "Astronomy Society",
          category: ["Science,Hobbies"],
          followers: "1276",
          rate: "4.7",
          events: 12,
          participants: 143
        },
        {
          name: "Young Entrepreneur Society",
          category: ["Entertainment,Business"],
          followers: "5642",
          rate: "4.5",
          events: 9,
          participants: 183
        },
        {
          name: "E-Sport Society",
          category: ["Entertainment,Hobbies"],
          followers: "2036",
          rate: "4.2",
          events: 21,
          participants: 223
        },
        {
          name: "Science Fiction and Fantasy Society",
          category: ["Entertainment,Hobbies"],
          followers: "891",
          rate: "4.3",
          events: 15,
          participants: 23
        },
        {
          name: "Operational Research Club",
          category: ["Business"],
          followers: "1149",
          rate: "4.0",
          events: 17,
          participants: 423
        }
      ]
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
          value: "followers",
          sortable: false
        },
        {
          text: "Total Rate",
          sortable: false,
          value: "rate"
        },
        {
          text: "Total Events",
          sortable: false,
          value: "events"
        },
        {
          text: "Total Participants",
          sortable: false,
          value: "participants"
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
      value = value.toLowerCase();
      this.sortBy = value;
    }
  }
};
</script>
