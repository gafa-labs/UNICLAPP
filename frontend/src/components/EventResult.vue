<template>
  <v-container class="pa-16">
    <v-row class="display-1 mb-6">Event Result</v-row>
    <v-row class="text-h5 mt-16 mb-6 font-weight-bold"
      >Your Club's Past Events</v-row
    >
    <v-data-table
      :headers="headers"
      :items="pastEvents"
      class="elevation-1"
      item-key="name"
      sort-by="date"
    >
      <template v-slot:[`item.description`]="{ item }">
        {{ truncateString(item.description) }}
      </template>
      <template v-slot:[`item.result`]="{ item }">
        <v-btn
          color="green lighten-1"
          rounded
          small
          @click="showResult(item)"
          @click.stop="resultDialog = true"
          >Show</v-btn
        >
      </template>
    </v-data-table>

    <v-dialog v-model="resultDialog" max-width="500">
      <v-card>
        <v-card-title class="text-h5 mb-3">
          Event Result
        </v-card-title>

        <v-card-text class="pl-9">
          <v-row class="text-subtitle-1">
            <strong>Name: </strong> {{ showedEvent.name }}
          </v-row>
          <v-row class="text-subtitle-1 ">
            <strong>Description: </strong> {{ showedEvent.description }}
          </v-row>
          <v-row class="text-subtitle-1">
            <strong>Location: </strong> {{ showedEvent.location }}
          </v-row>
          <v-row class="text-subtitle-1">
            <strong>Date: </strong> {{ showedEvent.start_datetime }}
          </v-row>
          <v-row class="text-subtitle-1">
            <strong>Rate: </strong> {{ showedEvent.rate }}
          </v-row>
          <v-row class="text-subtitle-1">
            <strong>Number of Participants: </strong>
            {{ showedEvent.number_of_participants }}
          </v-row>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" text @click="resultDialog = false">
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
      resultDialog: false,
      showedEvent: {},
      pastEvents: []
    };
  },
  computed: {
    headers() {
      return [
        {
          text: "Name",
          align: "center",
          value: "name",
          sortable: false
        },
        {
          text: "Description",
          align: "center",
          value: "description",
          sortable: false
        },
        {
          text: "Location",
          align: "center",
          value: "location",
          sortable: false
        },
        {
          text: "Date",
          align: "center",
          value: "start_datetime",
          sortable: false
        },
        {
          text: "Result",
          align: "center",
          value: "result",
          sortable: false
        }
      ];
    }
  },
  methods: {
    showResult(item) {
      this.showedEvent = item;
    },
    formatDate(item) {
      if (item.date) {
        return item.date.toLocaleString();
      }
      return "";
    },
    truncateString(str) {
      if (str.length > 50) {
        return str.slice(0, 50) + "...";
      } else {
        return str;
      }
    }
  },
  created() {
    axios
      .get("http://127.0.0.1:8000/api/events/results/", this.header)
      .then(response => {
        response.data.forEach(event => {
          event.start_datetime = new Date(
            event.start_datetime
          ).toLocaleString();
          this.pastEvents.push(event);
        });
      })
      .catch(e => console.log(e));
  }
};
</script>
