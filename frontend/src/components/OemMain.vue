<template>
  <v-container class="pa-16">
    <v-row>
      <v-spacer></v-spacer>
      <v-btn text color="red" @click="logout">
        LOGOUT
        <v-icon class="ml-1">mdi-exit-to-app</v-icon>
      </v-btn>
    </v-row>
    <v-row class="display-1 mb-4 font-weight-bold">Pending Events</v-row>
    <v-row>
      <v-data-table
        :headers="headersPending"
        :items="pendingEvents"
        outlined
        class="elevation-4"
        item-key="name"
        sort-by="date"
      >
        <template v-slot:[`item.description`]="{ item }">
          {{ truncateString(item.description) }}
        </template>
        <template v-slot:[`item.date`]="{ item }">
          {{ item }}
        </template>
        <template v-slot:[`item.approve`]="{ item }">
          <v-btn color="green lighten-1" rounded small @click="approve(item)"
            >Approve</v-btn
          >
        </template>
        <template v-slot:[`item.reject`]="{ item }">
          <v-btn color="red lighten-1" rounded small @click="reject(item)"
            >Reject</v-btn
          >
        </template>
      </v-data-table>
    </v-row>
    <v-row class="display-1 mt-10 mb-4 font-weight-bold">Approved Events</v-row>
    <v-row>
      <v-data-table
        :headers="headersApproved"
        :items="approvedEvents"
        outlined
        class="elevation-4"
        item-key="name"
        sort-by="date"
      >
        <template v-slot:[`item.description`]="{ item }">
          {{ truncateString(item.description) }}
        </template>
        <template v-slot:[`item.date`]="{ item }">
          {{ item }}
        </template>
      </v-data-table>
    </v-row>
    <v-row class="display-1 mt-10 mb-4 font-weight-bold">Rejected Events</v-row>
    <v-row>
      <v-data-table
        :headers="headersRejected"
        :items="rejectedEvents"
        outlined
        class="elevation-4"
        item-key="name"
        sort-by="date"
      >
        <template v-slot:[`item.description`]="{ item }">
          {{ truncateString(item.description) }}
        </template>
        <template v-slot:[`item.date`]="{ item }">
          {{ item }}
        </template>
      </v-data-table>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      pendingEvents: [],
      approvedEvents: [],
      rejectedEvents: []
    };
  },
  computed: {
    headersPending() {
      return [
        {
          text: "Event Name",
          align: "left",
          value: "name",
          sortable: false
        },
        {
          text: "Club Name",
          align: "left",
          value: "clubName",
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
          text: "Start Date",
          align: "center",
          value: "start_datetime",
          sortable: false
        },
        {
          text: "End Date",
          align: "center",
          value: "end_datetime",
          sortable: false
        },
        {
          text: "Approve",
          align: "center",
          value: "approve",
          sortable: false
        },
        {
          text: "Reject",
          align: "center",
          value: "reject",
          sortable: false
        }
      ];
    },
    headersApproved() {
      return [
        {
          text: "Event Name",
          align: "left",
          value: "name",
          sortable: false
        },
        {
          text: "Club Name",
          align: "left",
          value: "clubName",
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
          text: "Start Date",
          align: "center",
          value: "start_datetime",
          sortable: false
        },
        {
          text: "End Date",
          align: "center",
          value: "end_datetime",
          sortable: false
        }
      ];
    },
    headersRejected() {
      return [
        {
          text: "Event Name",
          align: "left",
          value: "name",
          sortable: false
        },
        {
          text: "Club Name",
          align: "left",
          value: "clubName",
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
          text: "Start Date",
          align: "center",
          value: "start_datetime",
          sortable: false
        },
        {
          text: "End Date",
          align: "center",
          value: "end_datetime",
          sortable: false
        }
      ];
    }
  },
  methods: {
    logout() {
      this.$router.push("/oemLogin");
    },
    formatDate(item) {
      if (item) {
        return new Date(item).toLocaleString();
      }
      return "";
    },
    truncateString(str) {
      if (str.length > 30) {
        return str.slice(0, 30) + "...";
      } else {
        return str;
      }
    },
    approve(item) {
      for (var i = 0; i < this.pendingEvents.length; i++) {
        if (this.pendingEvents[i] === item) {
          this.pendingEvents.splice(i, 1);
          this.approvedEvents.push(item);
          const endpoint =
            "http://localhost:8000/api/events/oem/" + item.id + "/";
          axios.put(endpoint, { event_status: "upcoming" });
        }
      }
    },
    reject(item) {
      for (var i = 0; i < this.pendingEvents.length; i++) {
        if (this.pendingEvents[i] === item) {
          this.pendingEvents.splice(i, 1);
          this.rejectedEvents.push(item);
          const endpoint =
            "http://localhost:8000/api/events/oem/" + item.id + "/";
          axios.put(endpoint, { event_status: "rejected" });
        }
      }
    }
  },
  created() {
    axios
      .get("http://localhost:8000/api/events/oem/")
      .then(response => {
        response.data.forEach(event => {
          var parsedEvent = {
            id: event.id,
            name: event.name,
            clubName: event.club.name,
            description: event.description,
            location: event.location,
            start_datetime: this.formatDate(event.start_datetime),
            end_datetime: this.formatDate(event.end_datetime),
            status: event.event_status
          };
          if (parsedEvent.status === "pending") {
            this.pendingEvents.push(parsedEvent);
          } else if (parsedEvent.status === "upcoming") {
            this.approvedEvents.push(parsedEvent);
          } else if (parsedEvent.status === "rejected") {
            this.rejectedEvents.push(parsedEvent);
          }
        });
      })
      .catch(e => {
        console.log(e);
      });
  }
};
</script>

<style></style>
