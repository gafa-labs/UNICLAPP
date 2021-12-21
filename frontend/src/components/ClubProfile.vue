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
          counter="400"
          maxlength="400"
          :disabled="userStatus === 'ClubAdvisor'"
          no-resize
          rows="4"
          outlined
          dense
          rounded
          class="mt-12 px-16"
          background-color="grey lighten-3"
        ></v-textarea>
        <v-textarea
          label="Category"
          counter="100"
          maxlength="100"
          :disabled="userStatus === 'ClubAdvisor'"
          no-resize
          rows="1"
          outlined
          dense
          rounded
          class="mt-6 px-16"
          background-color="grey lighten-3"
        ></v-textarea>
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
export default {
  data() {
    return {
      userStatus: "ClubAdvisor",
      club: {
        name: "ACM Bilkent Club",
        followers: 1548,
        rate: 4.8,
        about: "This is the field for the description of the club.",
        category: ["Business", "Software", "Science"],
        boardMembers: [
          {
            name: "Ayberk Yasa"
          },
          {
            name: "Fatih Kaplama"
          },
          {
            name: "Gorkem Ayten"
          },
          {
            name: "Mert Atakan Onrat"
          }
        ]
      }
    };
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
  }
};
</script>
