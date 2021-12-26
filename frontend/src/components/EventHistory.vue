<template>
  <v-container class="pa-16">
    <v-row class="display-1 mb-6">Event History</v-row>
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
        <v-tab disabled>Followings</v-tab>
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
                    >Average Rate: {{ event.avgRate }}</v-row
                  >
                  <v-row class="mt-2 text-h6"
                    >Your Rate:
                    {{ event.isRated ? event.rate : "Not Rated" }}</v-row
                  >
                </v-card-text>
                <v-row style="position: relative;"
                  ><v-rating
                    style="position: absolute; bottom:20px; left:25px;"
                    :readonly="event.isRated"
                    @input="rated(event)"
                    clearable
                    hover
                    length="5"
                    v-model="event.rate"
                  ></v-rating
                ></v-row>
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
                    >Average Rate: {{ event.avgRate }}</v-row
                  >
                  <v-row class="mt-2 text-h6"
                    >Your Rate:
                    {{ event.isRated ? event.rate : "Not Rated" }}</v-row
                  >
                </v-card-text>
                <v-row style="position: relative;"
                  ><v-rating
                    style="position: absolute; bottom:20px; left:25px;"
                    :readonly="event.isRated"
                    @input="rated(event)"
                    clearable
                    hover
                    length="5"
                    v-model="event.rate"
                  ></v-rating
                ></v-row>
              </v-card>
            </v-row>
          </v-container>
        </v-tab-item>
      </v-tabs-items>
    </v-card>
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
      search: "",
      isClicked: false,
      followingClubsEvents: [
        {
          club: "Management and Economics Society",
          name: "Event1",
          rate: 0,
          avgRate: 0,
          isRated: false
        },
        {
          club: "Science Fiction and Fantasy Society",
          name: "Event2",
          rate: 0,
          avgRate: 0,
          isRated: false
        },
        {
          club: "E-Sport Society",
          name: "Event3",
          rate: 0,
          avgRate: 0,
          isRated: false
        },
        {
          club: "Astronomy Society",
          name: "Event4",
          rate: 0,
          avgRate: 0,
          isRated: false
        },
        {
          club: "Management and Economics Society",
          name: "Event5",
          rate: 0,
          avgRate: 0,
          isRated: false
        },
        {
          club: "Science Fiction and Fantasy Society",
          name: "Event6",
          rate: 0,
          avgRate: 0,
          isRated: false
        }
      ],
      allClubsEvents: [],
      tab: null
    };
  },
  methods: {
    rated(event) {
      this.$set(event, "isRated", true);
      var rateJson = { rate: event.rate };
      axios
        .put(
          "http://127.0.0.1:8000/api/events/" + event.eventId + "/rate-event/",
          rateJson,
          this.header
        )
        .then(response => {})
        .catch(e => console.log(e));
    },
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
      .get("http://localhost:8000/api/events/event-history/", this.header)
      .then(response => {
        var studentRate = 0;
        var avgRate = 0;
        var eventId = 0;
        response.data.forEach(item => {
          studentRate = item.rate;
          avgRate = item.event.rate;
          eventId = item.id;
          const tmp = JSON.parse(JSON.stringify(item.event));
          this.$set(tmp, "avgRate", avgRate);
          this.$set(tmp, "eventId", eventId);
          this.$set(tmp, "studentRate", studentRate);
          this.$set(tmp, "isRated", studentRate != 0);
          this.allClubsEvents.push(tmp);
        });
        this.allClubsEvents.forEach(item => {
          axios
            .get("http://127.0.0.1:8000/api/clubs/" + item.club + "/")
            .then(club => {
              item.club = club.data.name;
            })
            .catch(er => console.log(er));
        });
      })
      .catch(e => console.log(e));
  }
};
</script>
