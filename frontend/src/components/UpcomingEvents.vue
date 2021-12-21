<template>
  <v-container class="pa-16">
    <v-row class="display-1 mb-6">Upcoming Events</v-row>
    <v-text-field
      v-model="search"
      label="Search"
      filled
      rounded
      dense
    ></v-text-field>
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
                v-model="search"
                v-for="event in searched(allClubsEvents)"
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
                      color="red lighten-1"
                      text
                      v-if="event.status === 'attending'"
                      @click="event.status = 'not attending'"
                      >Cancel</v-btn
                    >
                    <v-btn
                      style="position: absolute; bottom:20px;"
                      color="green lighten-1"
                      text
                      v-if="event.status === 'not attending'"
                      @click="event.status = 'attending'"
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
                v-model="search"
                v-for="event in searched(followingClubsEvents)"
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
                      color="red lighten-1"
                      text
                      v-if="event.status === 'attending'"
                      @click="event.status = 'not attending'"
                      >Cancel</v-btn
                    >
                    <v-btn
                      style="position: absolute; bottom:20px;"
                      color="green lighten-1"
                      text
                      v-if="event.status === 'not attending'"
                      @click="event.status = 'attending'"
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
      search: "",
      followingClubsEvents: [
        {
          club: "Management and Economics Society",
          name: "Event1",
          description: "description",
          location: "location",
          date: "date",
          status: "not attending"
        },
        {
          club: "Science Fiction and Fantasy Society",
          name: "Event2",
          description: "description",
          location: "location",
          date: "date",
          status: "not attending"
        },
        {
          club: "E-Sport Society",
          name: "Event3",
          description: "description",
          location: "location",
          date: "date",
          status: "not attending"
        },
        {
          club: "Astronomy Society",
          name: "Event4",
          description: "description",
          location: "location",
          date: "date",
          status: "not attending"
        },
        {
          club: "Management and Economics Society",
          name: "Event5",
          description: "description",
          location: "location",
          date: "date",
          status: "not attending"
        },
        {
          club: "Science Fiction and Fantasy Society",
          name: "Event6",
          description: "description",
          location: "location",
          date: "date",
          status: "attending"
        },
        {
          club: "Management and Economics Society",
          name: "Event7",
          description: "description",
          location: "location",
          date: "date",
          status: "attending"
        }
      ],
      allClubsEvents: [
        {
          club: "ACM Bilkent Club",
          name: "event1",
          description: "description2",
          location: "location2",
          date: "date2",
          status: "attending"
        },
        {
          club: "ACM Bilkent Club",
          name: "event2",
          description: "description2",
          location: "location2",
          date: "date2",
          status: "not attending"
        },
        {
          club: "ACM Bilkent Club",
          name: "event3",
          description: "description2",
          location: "location2",
          date: "date2",
          status: "attending"
        },
        {
          club: "ACM Bilkent Club",
          name: "event4",
          description: "description2",
          location: "location2",
          date: "date2",
          status: "not attending"
        },
        {
          club: "ACM Bilkent Club",
          name: "event5",
          description: "description2",
          location: "location2",
          date: "date2",
          status: "not attending"
        },
        {
          club: "ACM Bilkent Club",
          name: "event6",
          description: "description2",
          location: "location2",
          date: "date2",
          status: "not attending"
        },
        {
          club: "ACM Bilkent Club",
          name: "event7",
          description: "description2",
          location: "location2",
          date: "date2",
          status: "not attending"
        },
        {
          club: "ACM Bilkent Club",
          name: "event8",
          description: "description2",
          location: "location2",
          date: "date2",
          status: "not attending"
        },
        {
          club: "ACM Bilkent Club",
          name: "event9",
          description: "description2",
          location: "location2",
          date: "date2",
          status: "not attending"
        },
        {
          club: "ACM Bilkent Club",
          name: "event10",
          description: "description2",
          location: "location2",
          date: "date2",
          status: "not attending"
        }
      ],
      tab: null,
      sortElements: ["Followers", "Rate", "Events", "Participants"]
    };
  },
  methods: {
    searched(events) {
      if (this.search === "") {
        return events;
      }
      return events.filter(event => {
        return event.name.toLowerCase().includes(this.search.toLowerCase());
      });
    }
  }
};
</script>
