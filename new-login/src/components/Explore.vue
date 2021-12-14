<template>
  <v-container class="pa-16">
    <v-text-field v-model="search" label="Search" class="mx-4"></v-text-field>
    <v-row class="mx-4">
      <v-col cols="12" md="2">
        <v-col cols="12" md="6">
          <v-btn @click="selectAll">Select All</v-btn>
        </v-col>
        <v-col cols="12" md="6">
          <v-btn @click="deselectAll">Deselect All</v-btn>
        </v-col>
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
    </v-data-table>
  </v-container>
</template>
<script>
import Navbar from "../components/Navbar";

export default {
  data() {
    return {
      categories: [
        "Business",
        "Software",
        "Science",
        "Hobbies",
        "Entertainment"
      ],
      selected: ["Business", "Software", "Science", "Hobbies", "Entertainment"],
      search: "",
      clubs: [
        {
          name: "ACM Bilkent Club",
          category: ["Business,Software,Science"],
          followers: "1545",
          rate: "4.5",
          status: "Unfollow"
        },
        {
          name: "Management and Economics Society",
          category: ["Business"],
          followers: "6889",
          rate: "4.6",
          status: "Follow"
        },
        {
          name: "Astronomy Society",
          category: ["Science,Hobbies"],
          followers: "1276",
          rate: "4.7",
          status: "Follow"
        },
        {
          name: "Young Entrepreneur Society",
          category: ["Entertainment,Business"],
          followers: "5642",
          rate: "4.5",
          status: "Unfollow"
        },
        {
          name: "E-Sport Society",
          category: ["Entertainment,Hobbies"],
          followers: "2036",
          rate: "4.2",
          status: "Follow"
        },
        {
          name: "Science Fiction and Fantasy Society",
          category: ["Entertainment,Hobbies"],
          followers: "891",
          rate: "4.3",
          status: "Follow"
        },
        {
          name: "Operational Research Club",
          category: ["Business"],
          followers: "1149",
          rate: "4.0",
          status: "Unfollow"
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
          sortable: false,
          value: "name"
        },
        {
          text: "Category",
          value: "category",
          filter: value => {
            var arr = value[0].split(",");
            var check = false;
            console.log(arr);
            this.selected.forEach(item => {
              if (arr.includes(item)) {
                check = true;
              }
            });
            return check;
          }
        },
        {
          text: "Followers",
          value: "followers"
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
    // selectAll: {
    //   get: function() {
    //     // return this.categories
    //     //   ? this.selected.length == this.categories.length
    //     //   : false;
    //     return true;
    //   },
    //   set: function(value) {
    //     var selected = [];
    //     if (value) {
    //       this.categories.forEach(category => {
    //         selected.push(category);
    //       });
    //     }
    //     this.selected = selected;
    //   }
    // }
  },
  methods: {
    selectAll() {
      this.categories.forEach(category => {
        if (!this.selected.includes(category)) {
          this.selected.push(category);
        }
      });
    },
    deselectAll() {
      this.selected = [];
    }
  },
  components: {
    navBar: Navbar
  }
};
</script>
