<template>
  <v-container class="pa-16">
    <v-row class="display-1 mb-6">Event History</v-row>
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
                    outlined
                    raised
                    class="mx-5 my-5"
                    width="250"
                    v-for="event in allClubsEvents"
                    :key="event.name"
                  >
                    <v-row class="mx-auto my-auto"
                      ><v-card-title
                        >Club: {{ event.club }}</v-card-title
                      ></v-row
                    >
                    <v-row class="mx-auto my-auto"
                      ><v-card-text class="text--primary">
                        <div>Event: {{ event.name }}</div>
                        <div>Average Rate: {{ event.avgRate }}</div>
                        <div style="hidden">
                          Your Rate:
                          {{ event.isRated ? event.rate : "Not Rated" }}
                        </div>
                      </v-card-text></v-row
                    >
                    <v-row class="mx-auto my-auto" @click.prevent
                      ><v-rating
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
                    :key="event.name"
                  >
                    <v-row class="mx-auto my-auto"
                      ><v-card-title
                        >Club: {{ event.club }}</v-card-title
                      ></v-row
                    >
                    <v-row class="mx-auto my-auto"
                      ><v-card-text class="text--primary">
                        <div>Event: {{ event.name }}</div>
                        <div>Average Rate: {{ event.avgRate }}</div>
                        <div style="hidden">
                          Your Rate:
                          {{ event.isRated ? event.rate : "Not Rated" }}
                        </div>
                      </v-card-text></v-row
                    >
                    <v-row class="mx-auto my-auto" @click.prevent
                      ><v-rating
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
      isClicked: false,
      rating: 0,
      followingClubsEvents: [
        {
          club: "Management and Economics Society",
          name: "Event1",
          rate: 4.3,
          avgRate: 0,
          isRated: false
        },
        {
          club: "Science Fiction and Fantasy Society",
          name: "Event2",
          rate: 4.3,
          avgRate: 0,
          isRated: false
        },
        {
          club: "E-Sport Society",
          name: "Event3",
          rate: 4.3,
          avgRate: 0,
          isRated: false
        },
        {
          club: "Astronomy Society",
          name: "Event4",
          rate: 4.3,
          avgRate: 0,
          isRated: false
        },
        {
          club: "Management and Economics Society",
          name: "Event5",
          rate: 4.3,
          avgRate: 0,
          isRated: false
        },
        {
          club: "Science Fiction and Fantasy Society",
          name: "Event6",
          rate: 4.3,
          avgRate: 0,
          isRated: false
        }
      ],
      allClubsEvents: [
        {
          club: "ACM Bilkent Club",
          name: "event7",
          rate: 4.3,
          avgRate: 0,
          isRated: false
        },
        {
          club: "ACM Bilkent Club",
          name: "event8",
          rate: 4.3,
          avgRate: 0,
          isRated: false
        },
        {
          club: "ACM Bilkent Club",
          name: "event9",
          rate: 4.3,
          avgRate: 0,
          isRated: false
        },
        {
          club: "ACM Bilkent Club",
          name: "event10",
          rate: 4.3,
          isRated: false
        },
        {
          club: "ACM Bilkent Club",
          name: "event11",
          rate: 4.3,
          avgRate: 0,
          isRated: false
        }
      ],
      tab: null
    };
  },
  methods: {
    rated(event) {
      event.isRated = true;
    }
  }
};
</script>
