<template>
  <v-container class="pa-16">
    <v-row class="display-1 mb-6">Upcoming Events</v-row>
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
              <v-col cols="12" md="12">
                <v-row>
                  <v-card
                    elevation="8"
                    class="mx-5 my-5"
                    width="250"
                    v-for="event in allClubsEvents"
                    :key="event"
                    flat
                  >
<<<<<<< HEAD
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
=======
                    <v-card-title>Club: {{ event.club }}</v-card-title>
                    <v-card-text class="text--primary">
                      <div>Event: {{ event.event }}</div>
                      <div>Description: {{ event.description }}</div>
                      <div>Location: {{ event.location }}</div>
                      <div>Date: {{ event.date }}</div>
                    </v-card-text>
                  </v-card>
>>>>>>> parent of 8e4f35b (Merge branch 'unstable-frontendV2' into unstable-backendV2)
                </v-row>
              </v-col>
            </v-row>
          </v-container>
        </v-tab-item>
        <v-tab-item>
          <v-container>
            <v-row>
              <v-col cols="12" md="12">
                <v-row>
                  <v-card
                    outlined
                    raised
                    class="mx-5 my-5"
                    width="250"
                    v-for="event in followingClubsEvents"
                    :key="event"
                  >
<<<<<<< HEAD
                  <v-row class="mt-6 text-h6"
                    >Location: {{ event.location }}</v-row
                  >
                  <v-row class="mt-2 text-h6">Date: {{ event.date }}</v-row>
                  <v-row class="mt-2 text-h6">Time: </v-row>
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
=======
                    <v-card-title>Club: {{ event.club }}</v-card-title>
                    <v-card-text class="text--primary">
                      <div>Event: {{ event.event }}</div>
                      <div>Description: {{ event.description }}</div>
                      <div>Location: {{ event.location }}</div>
                      <div>Date: {{ event.date }}</div>
                    </v-card-text>
                  </v-card>
>>>>>>> parent of 8e4f35b (Merge branch 'unstable-frontendV2' into unstable-backendV2)
                </v-row>
              </v-col>
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
          event: "Event1",
          description: "description",
          location: "location",
          date: "date"
        },
        {
          club: "Science Fiction and Fantasy Society",
          event: "Event1",
          description: "description",
          location: "location",
          date: "date"
        },
        {
          club: "E-Sport Society",
          event: "Event1",
          description: "description",
          location: "location",
          date: "date"
        },
        {
          club: "Astronomy Society",
          event: "Event1",
          description: "description",
          location: "location",
          date: "date"
        },
        {
          club: "Management and Economics Society",
          event: "Event1",
          description: "description",
          location: "location",
          date: "date"
        },
        {
          club: "Science Fiction and Fantasy Society",
          event: "Event1",
          description: "description",
          location: "location",
          date: "date"
        },
        {
          club: "Management and Economics Society",
          event: "Event1",
          description: "description",
          location: "location",
          date: "date"
        }
      ],
      allClubsEvents: [
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        },
        {
          club: "ACM Bilkent Club",
          event: "event2",
          description: "description2",
          location: "location2",
          date: "date2"
        }
      ],
      tab: null,
      sortElements: ["Followers", "Rate", "Events", "Participants"]
    };
<<<<<<< HEAD
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
  },
  created() {
    axios
      .get("http://127.0.0.1:8000/api/events/")
      .then(response => {
        response.data.map(event => {
          if (event.is_online) {
            event.location = "Zoom";
          }
          console.log(event);
          var eventDate = new Date(event.datetime);
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
        });
        this.allClubsEvents = response.data;
      })
      .catch(e => console.log(e));
=======
>>>>>>> parent of 8e4f35b (Merge branch 'unstable-frontendV2' into unstable-backendV2)
  }
};
</script>
