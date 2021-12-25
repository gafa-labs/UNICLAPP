<template>
  <v-container class="pa-16">
    <v-row class="display-1 mb-6">Organize Event</v-row>
    <v-row>
      <v-col
        cols="12"
        md="4"
        class="pr-16"
        style="border-right: 2px solid lightsteelblue"
      >
        <v-text-field
          label="Name"
          v-model="newEvent.name"
          clearable
          outlined
          dense
          hide-details="auto"
          rounded
          class="mb-6"
        ></v-text-field>
        <v-textarea
          label="Description"
          v-model="newEvent.description"
          counter="400"
          maxlength="400"
          no-resize
          rows="5"
          row-height="15"
          outlined
          dense
          rounded
          class="mb-6"
        ></v-textarea>
        <v-switch
          :label="isOnline ? 'Online' : 'Face to Face'"
          v-model="isOnline"
        ></v-switch>
        <v-switch
          :label="
            hasGE
              ? 'GE points will be awarded'
              : 'GE points will not be awarded'
          "
          v-model="hasGE"
        ></v-switch>
        <v-text-field
          :label="isOnline ? 'Online' : 'Location'"
          v-model="newEvent.location"
          clearable
          :disabled="isOnline"
          outlined
          dense
          rounded
          class="mb-6"
        ></v-text-field>
        <v-menu
          ref="menu"
          v-model="picker1"
          :close-on-content-click="false"
          :nudge-right="40"
          :return-value.sync="time"
          transition="scale-transition"
          offset-y
          max-width="290px"
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="startDateFormatted"
              label="Start Date"
              prepend-icon="mdi-calendar"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            :min="today"
            v-model="newEvent.startDate"
            @input="picker1 = false"
          ></v-date-picker>
        </v-menu>
        <v-menu
          ref="menu"
          v-model="picker2"
          :close-on-content-click="false"
          :nudge-right="40"
          :return-value.sync="time"
          transition="scale-transition"
          offset-y
          max-width="290px"
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="endDateFormatted"
              label="End Date"
              prepend-icon="mdi-calendar"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            :min="today"
            v-model="newEvent.endDate"
            @input="picker2 = false"
          ></v-date-picker>
        </v-menu>
        <v-menu
          ref="menu"
          v-model="clock1"
          :close-on-content-click="false"
          :nudge-right="40"
          :return-value.sync="time"
          transition="scale-transition"
          offset-y
          max-width="290px"
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="newEvent.startTime"
              label="Start Time"
              prepend-icon="mdi-clock-time-four-outline"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-time-picker
            v-if="clock1"
            scrollable
            :allowed-hours="allowedHours"
            v-model="newEvent.startTime"
            format="24hr"
            full-width
            @click:minute="$refs.menu.save(time)"
          ></v-time-picker>
        </v-menu>
        <v-menu
          ref="menu"
          v-model="clock2"
          :close-on-content-click="false"
          :nudge-right="40"
          :return-value.sync="time"
          transition="scale-transition"
          offset-y
          max-width="290px"
          min-width="290px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="newEvent.endTime"
              label="End Time"
              prepend-icon="mdi-clock-time-four-outline"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-time-picker
            v-if="clock2"
            scrollable
            :allowed-hours="allowedSecondHours"
            v-model="newEvent.endTime"
            format="24hr"
            full-width
            @click:minute="$refs.menu.save(time)"
          ></v-time-picker>
        </v-menu>
        <v-row class="mt-6 justify-center">
          <v-btn
            elevation="2"
            rounded
            color="green lighten-1"
            @click="organizeEvent"
            >Organize</v-btn
          >
        </v-row>
        <v-row v-if="error" class="red--text mt-6"
          >ALL FIELDS MUST BE FILLED</v-row
        >
      </v-col>
      <v-col cols="12" md="8" class="pl-16">
        <v-row class="text-h5 mb-6 font-weight-bold"
          >Your Club's Current Events</v-row
        >
        <v-row>
          <v-data-table
            :headers="headers"
            :items="upcomingEvents"
            outlined
            class="elevation-4"
            item-key="name"
          >
            <template v-slot:[`item.change`]="{ item }">
              <v-btn
                color="red lighten-1"
                rounded
                small
                v-if="item.event_status != 'Past'"
                @click="removeEvent(item)"
                >Remove
                <v-icon right>mdi-close-outline</v-icon>
              </v-btn>
            </template>
          </v-data-table>
        </v-row>
      </v-col>
    </v-row>
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
      isOnline: true,
      hasGE: true,
      error: false,
      newEvent: {
        name: null,
        description: null,
        location: null,
        startDate: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
          .toISOString()
          .substr(0, 10),
        endDate: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
          .toISOString()
          .substr(0, 10),
        startTime: null,
        endTime: null
      },
      picker1: false,
      picker2: false,
      time: "",
      clock1: false,
      clock2: false,
      today: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
        .toISOString()
        .substr(0, 10),
      date: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
        .toISOString()
        .substr(0, 10),
      upcomingEvents: []
    };
  },
  methods: {
    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      return `${day}/${month}/${year}`;
    },
    eventType() {
      if (this.isOnline) {
        return "Online";
      } else {
        return "Face to Face";
      }
    },
    allowedHours(h) {
      let hour = new Date().getHours();
      if (this.newEvent.startDate == this.today) {
        return h > hour;
      }
      return true;
    },
    allowedSecondHours(h) {
      if (
        this.newEvent.endDate == this.newEvent.startDate &&
        this.newEvent.startTime
      ) {
        var timeArr = this.newEvent.startTime.split(":");
        var hourInt = parseInt(timeArr[0]);
        var start = new Date();
        start.setHours(hourInt);
        return h > start.getHours();
      }
      return true;
    },
    removeEvent(event) {
      console.log(event.id);
      axios
        .delete("http://localhost:8000/api/events/" + event.id + "/delete/")
        .then(response => {
          console.log(response.data);
        })
        .catch(e => console.log(e));
      for (var i = 0; i < this.upcomingEvents.length; i++) {
        if (this.upcomingEvents[i] === event) {
          this.upcomingEvents.splice(i, 1);
        }
      }
    },
    organizeEvent() {
      if (this.isOnline) {
        this.newEvent.location = "Online";
      }
      if (Object.values(this.newEvent).includes(null)) {
        this.error = true;
        return;
      }
      var start_datetime =
        this.newEvent.startDate + "T" + this.newEvent.startTime + ":00+03:00";
      var end_datetime =
        this.newEvent.endDate + "T" + this.newEvent.endTime + ":00+03:00";
      var event = {
        name: this.newEvent.name,
        description: this.newEvent.description,
        ge_status: this.hasGE,
        is_online: this.isOnline,
        start_datetime: start_datetime,
        end_datetime: end_datetime,
        location: this.newEvent.location
      };
      var organizedEvent = {};
      axios
        .post("http://localhost:8000/api/events/create/", event, this.header)
        .then(response => {
          console.log(response.data);
          organizedEvent = response.data;
          organizedEvent.start_datetime = this.formattedDate(
            organizedEvent.start_datetime
          );
          organizedEvent.end_datetime = this.formattedDate(
            organizedEvent.end_datetime
          );
          organizedEvent.ge_status = organizedEvent.ge_status
            ? "Awarded"
            : "Not Awarded";
          console.log(organizedEvent);
          this.upcomingEvents.push(organizedEvent);
          this.newEvent = {};
          this.newEvent.date = this.today;
          this.error = false;
        })
        .catch(e => console.log(e));
    },
    formattedDate(datetime) {
      var date = new Date(datetime);
      var hh = date.getHours().toLocaleString();
      var min = date.getMinutes().toLocaleString();
      if (min.length == 1) {
        min = "0" + min;
      }
      var time = hh + ":" + min;
      var dd = String(date.getDate()).padStart(2, "0");
      var mm = String(date.getMonth() + 1).padStart(2, "0");
      var yyyy = date.getFullYear();
      date = dd + "/" + mm + "/" + yyyy;
      date = date + "\n" + time;
      return date;
    }
  },
  computed: {
    startDateFormatted() {
      return this.formatDate(this.newEvent.startDate);
    },
    endDateFormatted() {
      return this.formatDate(this.newEvent.endDate);
    },
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
          text: "Start Date Time",
          align: "center",
          value: "start_datetime",
          sortable: false
        },
        {
          text: "End Date Time",
          align: "center",
          value: "end_datetime",
          sortable: false
        },
        {
          text: "GE Status",
          align: "center",
          value: "ge_status",
          sortable: false
        },
        {
          text: "GE Points",
          align: "center",
          value: "ge_point",
          sortable: false
        },
        {
          text: "Status",
          align: "center",
          value: "event_status",
          sortable: false
        },
        {
          text: "",
          align: "center",
          value: "change",
          sortable: false
        }
      ];
    }
  },
  created() {
    axios
      .get("http://localhost:8000/api/events/club-events/", this.header)
      .then(response => {
        response.data.forEach(event => {
          event.event_status =
            event.event_status.charAt(0).toUpperCase() +
            event.event_status.slice(1);
        });
        this.upcomingEvents = response.data;
        console.log(response.data);
        this.upcomingEvents.map(event => {
          event.start_datetime = this.formattedDate(event.start_datetime);
          event.end_datetime = this.formattedDate(event.end_datetime);
          event.ge_status = event.ge_status ? "Awarded" : "Not Awarded";
        });
      })
      .catch(e => console.log(e));
  }
};
</script>
