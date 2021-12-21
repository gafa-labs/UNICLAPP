<template>
  <v-container class="pa-16">
    <v-row class="display-1 mb-6">Upcoming Events</v-row>
    <v-card>
      <v-tabs color="deep-blue accent-4" v-model="tab">
        <v-tabs-slider color="blue"></v-tabs-slider>
        <v-tab>All</v-tab>
        <v-tab>Followings</v-tab>
      </v-tabs>

      <v-tabs-items v-model="tab">
        <v-tab-item>
          <v-container fluid>
            <v-row>
              <v-card
                style="display: flex; flex-flow: column wrap;"
                shaped
                elevation="5"
                class="ma-5"
                width="250"
                height="250"
                v-for="event in allClubsEvents"
                :key="event.name"
                flat
              >
                <v-card-title
                  class="mx-2 text-h5"
                  style="word-break: break-word;"
                >
                  <v-row>{{ event.name }}</v-row>
                </v-card-title>
                <v-card-text
                  class="mx-2 text--primary"
                  style="word-break: break-word;"
                >
                  <v-row
                    class="subtitle-1"
                    style="border-bottom: 1px solid lightgray"
                    >by {{ event.club }}</v-row
                  >
                  <v-row class="mt-6 text-h6"
                    >Location: {{ event.location }}</v-row
                  >
                  <v-row class="mt-2 text-h6">Date: {{ event.date }}</v-row>
                </v-card-text>
                <v-row style="position: relative;">
                  <v-col cols="6">
                    <v-btn
                      style="position: absolute; bottom:20px;"
                      color="deep-orange lighten-1"
                      text
                      >Details</v-btn
                    >
                  </v-col>
                  <v-spacer></v-spacer>
                  <v-col cols="6">
                    <v-btn
                      style="position: absolute; bottom:20px;"
                      color="green lighten-1"
                      text
                      >Attend</v-btn
                    >
                  </v-col>
                </v-row>
              </v-card>
            </v-row>
          </v-container>
        </v-tab-item>
        <v-tab-item>
          <v-container fluid>
            <v-row>
              <v-card
                style="display: flex; flex-flow: column wrap;"
                shaped
                elevation="5"
                class="ma-5"
                width="250"
                height="250"
                v-for="event in followingClubsEvents"
                :key="event.name"
                flat
              >
                <v-card-title
                  class="mx-2 text-h5"
                  style="word-break: break-word;"
                >
                  <v-row>{{ event.name }}</v-row>
                </v-card-title>
                <v-card-text
                  class="mx-2 text--primary"
                  style="word-break: break-word;"
                >
                  <v-row
                    class="subtitle-1"
                    style="border-bottom: 1px solid lightgray"
                    >by {{ event.club }}</v-row
                  >
                  <v-row class="mt-6 text-h6"
                    >Location: {{ event.location }}</v-row
                  >
                  <v-row class="mt-2 text-h6">Date: {{ event.date }}</v-row>
                </v-card-text>
                <v-row style="position: relative;">
                  <v-col cols="6">
                    <v-btn
                      style="position: absolute; bottom:20px;"
                      color="deep-orange lighten-1"
                      text
                      >Details</v-btn
                    >
                  </v-col>
                  <v-spacer></v-spacer>
                  <v-col cols="6">
                    <v-btn
                      style="position: absolute; bottom:20px;"
                      color="green lighten-1"
                      text
                      >Attend</v-btn
                    >
                  </v-col>
                </v-row>
              </v-card>
            </v-row>
          </v-container>
        </v-tab-item>
      </v-tabs-items>
    </v-card>
  </v-container>
</template>
<script>
export default {
  data() {
    return {
      followingClubsEvents: [
        {
          club: "Management and Economics Society",
          name: "Event1",
          description: "description",
          location: "location",
          date: "date"
        },
        {
          club: "Science Fiction and Fantasy Society",
          name: "Event2",
          description: "description",
          location: "location",
          date: "date"
        },
        {
          club: "E-Sport Society",
          name: "Event3",
          description: "description",
          location: "location",
          date: "date"
        },
        {
          club: "Astronomy Society",
          name: "Event4",
          description: "description",
          location: "location",
          date: "date"
        },
        {
          club: "Management and Economics Society",
          name: "Event5",
          description: "description",
          location: "location",
          date: "date"
        },
        {
          club: "Science Fiction and Fantasy Society",
          name: "Event6",
          description: "description",
          location: "location",
          date: "date"
        },
        {
          club: "Management and Economics Society",
          name: "Event7",
          description: "description",
          location: "location",
          date: "date"
        }
      ],
      allClubsEvents: [
        {
          club: "ACM Bilkent Club",
          name: "event1",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          name: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          name: "event3",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          name: "event4",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event5",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          name: "event6",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          name: "event7",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          name: "event8",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          name: "event9",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          name: "event10",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          name: "event11",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          name: "event12",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          name: "event13",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          name: "event14",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event15",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          name: "event16",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          name: "event17",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          name: "event18",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          name: "event19",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          name: "event20",
          description: "description2",
          location: "location2",
          date: "date2"
        }
      ],
      tab: null,
      sortElements: ["Followers", "Rate", "Events", "Participants"]
    };
  },
  methods: {}
};
</script>
