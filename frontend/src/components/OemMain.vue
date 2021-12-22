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
        <template v-slot:item.description="{ item }">
          {{ truncateString(item.description) }}
        </template>
        <template v-slot:item.date="{ item }">
          {{ formatDate(item) }}
        </template>
        <template v-slot:item.approve="{ item }">
          <v-btn color="green lighten-1" rounded small @click="approve(item)"
            >Approve</v-btn
          >
        </template>
        <template v-slot:item.reject="{ item }">
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
        <template v-slot:item.description="{ item }">
          {{ truncateString(item.description) }}
        </template>
        <template v-slot:item.date="{ item }">
          {{ formatDate(item) }}
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
        <template v-slot:item.description="{ item }">
          {{ truncateString(item.description) }}
        </template>
        <template v-slot:item.date="{ item }">
          {{ formatDate(item) }}
        </template>
      </v-data-table>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      pendingEvents: [
        {
          name: "Introductory Meeting",
          description: "Descriptiiiiiioooooon",
          location: "Mayfest Area",
          date: new Date(2021, 8, 16, 15, 45)
        },
        {
          name: "Introductory Meeting2",
          description: "Descriptiiiiiioooooon",
          location: "Mayfest Area",
          date: new Date(2021, 8, 16, 15, 25)
        },
        {
          name: "Fast & Curious Meeting",
          description:
            "DescriptaaaaaaaaaaiiiiiioooooonDescriptaaaaaaaaaaiiiiiioooooon",
          location: "Cyberpark",
          date: new Date(2022, 3, 6, 21, 45)
        }
      ],
      approvedEvents: [
        {
          name: "approvedIntroductory Meeting",
          description: "Descriptiiiiiioooooon",
          location: "Mayfest Area",
          date: new Date(2021, 8, 16, 15, 45)
        },
        {
          name: "approvedIntroductory Meeting2",
          description: "Descriptiiiiiioooooon",
          location: "Mayfest Area",
          date: new Date(2021, 8, 16, 15, 25)
        },
        {
          name: "approvedFast & Curious Meeting",
          description:
            "DescriptaaaaaaaaaaiiiiiioooooonDescriptaaaaaaaaaaiiiiiioooooon",
          location: "Cyberpark",
          date: new Date(2022, 3, 6, 21, 45)
        }
      ],
      rejectedEvents: [
        {
          name: "rejectedIntroductory Meeting",
          description: "Descriptiiiiiioooooon",
          location: "Mayfest Area",
          date: new Date(2021, 8, 16, 15, 45)
        },
        {
          name: "rejectedIntroductory Meeting2",
          description: "Descriptiiiiiioooooon",
          location: "Mayfest Area",
          date: new Date(2021, 8, 16, 15, 25)
        },
        {
          name: "rejectedFast & Curious Meeting",
          description:
            "DescriptaaaaaaaaaaiiiiiioooooonDescriptaaaaaaaaaaiiiiiioooooon",
          location: "Cyberpark",
          date: new Date(2022, 3, 6, 21, 45)
        }
      ]
    };
  },
  computed: {
    headersPending() {
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
        }
      ];
    },
    headersRejected() {
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
        }
      ];
    }
  },
  methods: {
    logout() {
      this.$router.push("/oemLogin");
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
    },
    approve(item) {
      for (var i = 0; i < this.pendingEvents.length; i++) {
        if (this.pendingEvents[i] === item) {
          this.pendingEvents.splice(i, 1);
          this.approvedEvents.push(item);
        }
      }
    },
    reject(item) {
      for (var i = 0; i < this.pendingEvents.length; i++) {
        if (this.pendingEvents[i] === item) {
          this.pendingEvents.splice(i, 1);
          this.rejectedEvents.push(item);
        }
      }
    }
  }
};
</script>

<style></style>
