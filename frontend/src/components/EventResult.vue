<template>
  <v-container class="pa-16">
    <v-row class="display-1 mb-6">Event Result</v-row>
    <v-row class="text-h5 mt-16 mb-6 font-weight-bold"
      >Your Club's Past Events</v-row
    >
    <v-row>
      <v-data-table
        :headers="headers"
        :items="pastEvents"
        outlined
        class="elevation-4"
        item-key="name"
        sort-by="date"
      >
        <template v-slot:item.description="{ item }">
          {{ truncateString(item.description) }}
        </template>
        <template v-slot:item.date="{ item }">
          {{ formatDate(item) }}
        </template>
        <template v-slot:item.result="{ item }">
          <v-btn
            color="red lighten-1"
            rounded
            small
            @click="showResult(item)"
            @click.stop="resultDialog = true"
            >Show</v-btn
          >
        </template>
      </v-data-table>
    </v-row>
    <v-dialog v-model="resultDialog" max-width="500">
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
          <v-btn color="green darken-1" text @click="resultDialog = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>
<script>
export default {
  data() {
    return {
      resultDialog: false,
      showedEvent: {},
      pastEvents: [
        {
          name: "Introductory Meeting",
          description: "Descriptiiiiiioooooon",
          location: "Mayfest Area",
          date: new Date(2021, 8, 16, 15, 45),
          rate: 4.3,
          participants: 1200
        },
        {
          name: "Introductory Meeting2",
          description: "Descriptiiiiiioooooon",
          location: "Mayfest Area",
          date: new Date(2021, 8, 16, 15, 25),
          rate: 2.3,
          participants: 2344
        },
        {
          name: "Fast & Curious Meeting",
          description:
            "DescriptaaaaaaaaaaiiiiiioooooonDescriptaaaaaaaaaaiiiiiioooooon",
          location: "Cyberpark",
          date: new Date(2022, 3, 6, 21, 45),
          rate: 1.8,
          participants: 19
        }
      ]
    };
  },
  computed: {
    headers() {
      return [
        {
          text: "Name",
          align: "left",
          value: "name",
          sortable: false
        },
        {
          text: "Description",
          align: "left",
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
          value: "date",
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
  }
};
</script>
