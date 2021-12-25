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
                  <v-row class="mt-2 text-h6">Time: {{ event.time }}</v-row>
                </v-card-text>
                <v-row style="position: relative;">
                  <v-col cols="6">
                    <v-btn
                      style="position: absolute; bottom:20px;"
                      color="deep-orange lighten-1"
                      text
                      @click="showDetail(event)"
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
                      @click="cancelEnrollment(event)"
                      >Cancel</v-btn
                    >
                    <v-btn
                      style="position: absolute; bottom:20px;"
                      color="green lighten-1"
                      text
                      v-if="event.status === 'not attending'"
                      @click="enrollEvent(event)"
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
                  <v-row class="mt-2 text-h6"
                    >Date: {{ formatDate(event.date) }}</v-row
                  >
                  <v-row class="mt-2 text-h6">Time: </v-row>
                </v-card-text>
                <v-row style="position: relative;">
                  <v-col cols="6">
                    <v-btn
                      style="position: absolute; bottom:20px;"
                      color="deep-orange lighten-1"
                      text
                      @click="showDetail(event)"
                      @click.stop="detailDialog = true"
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
                      @click="event.status = 'not attending'"
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
    <v-dialog v-model="detailDialog" max-width="500">
      <v-card>
        <v-card-title class="text-h5 mb-3">
          Event Result
        </v-card-title>

        <v-card-text class="pl-9">
          <v-row class="text-subtitle-1"> Name: {{ showedEvent.name }} </v-row>
          <v-row class="text-subtitle-1">
            Description: {{ showedEvent.description }}
          </v-row>
          <v-row class="text-subtitle-1">
            Location: {{ showedEvent.location }}
          </v-row>
          <v-row class="text-subtitle-1">
            Date: {{ formatDate(showedEvent) }}
          </v-row>
          <v-row class="text-subtitle-1"> Rate: {{ showedEvent.rate }} </v-row>
          <v-row class="text-subtitle-1">
            Number of Participants: {{ showedEvent.participants }}
          </v-row>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" text @click="detailDialog = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
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
      detailDialog: false,
      showedEvent: {},
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
      allClubsEvents: [],
      tab: null,
      sortElements: ["Followers", "Rate", "Events", "Participants"]
    };
  },
  methods: {
    enrollEvent(event) {
      event.status = "attending";
      console.log(event);
      axios
        .get(
          "http://127.0.0.1:8000/api/events/" + event.id + "/enroll/",
          this.header
        )
        .then(response => {});
    },
    cancelEnrollment(event) {
      event.status = "not attending";
      axios
        .get(
          "http://127.0.0.1:8000/api/events/" +
            event.id +
            "/cancel-enrollment/",
          this.header
        )
        .then(response => {});
    },
    showDetail(item) {
      this.detailDialog = true;
      this.showedEvent = item;
    },
    formatDate(item) {
      if (item.date) {
        return item.date.toLocaleString();
      }
      return "";
    },
    searched(events) {
      if (this.search === "") {
        return events;
      }
      return events.filter(event => {
        return event.name.toLowerCase().includes(this.search.toLowerCase());
      });
    },
    displayEvents(response) {
      response.map(event => {
        if (event.is_online) {
          event.location = "Zoom";
        }
        var eventDate = new Date(event.start_datetime);
        var eventHour = eventDate.getHours().toString();
        var eventMinutes = eventDate.getMinutes().toString();
        if (eventMinutes.length == 1) {
          eventMinutes = "0" + eventMinutes;
        } else if (eventHour.length == 1) {
          eventHour = "0" + eventHour;
        }
        var eventTime = eventHour + "." + eventMinutes;
        var eventDay = eventDate.toLocaleDateString();
        event.date = eventDay;
        event.time = eventTime;
        axios
          .get("http://127.0.0.1:8000/api/clubs/" + event.club + "/")
          .then(club => {
            event.club = club.data.name;
          })
          .catch(er => console.log(er));
        console.log(event);
        const newEvent = JSON.parse(JSON.stringify(event));
        this.allClubsEvents.push(newEvent);
      });
    }
  },
  created() {
    axios
      .get("http://127.0.0.1:8000/api/events/all-upcoming-events/", this.header)
      .then(response => {
        console.log(response.data);
        this.displayEvents(response.data.all_upcoming_events);
        var enrolled = response.data.enrolled_events;
        this.allClubsEvents.forEach(event => {
          if (enrolled.includes(event.id)) {
            event.status = "attending";
          } else {
            event.status = "not attending";
          }
        });
      })
      .catch(e => console.log(e));
    //   axios
    //     .get("http://127.0.0.1:8000/api/events/")
    //     .then(response => {
    //       response.data.map(event => {
    //         if (event.is_online) {
    //           event.location = "Zoom";
    //         }
    //         var eventDate = new Date(event.start_datetime);
    //         var eventHour = eventDate.getHours().toString();
    //         var eventMinutes = eventDate.getMinutes().toString();
    //         if (eventMinutes.length == 1) {
    //           eventMinutes = "0" + eventMinutes;
    //         } else if (eventHour.length == 1) {
    //           eventHour = "0" + eventHour;
    //         }
    //         var eventTime = eventHour + "." + eventMinutes;
    //         var eventDay = eventDate.toLocaleDateString();
    //         event.date = eventDay;
    //         event.time = eventTime;
    //         axios
    //           .get("http://127.0.0.1:8000/api/clubs/" + event.club + "/")
    //           .then(club => {
    //             event.club = club.data.name;
    //           })
    //           .catch(er => console.log(er));
    //         console.log(event);
    //       });
    //       this.allClubsEvents = response.data;
    //     })
    //     .catch(e => console.log(e));
  }
};
</script>
