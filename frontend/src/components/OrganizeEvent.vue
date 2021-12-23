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
          rows="10"
          row-height="25"
          outlined
          dense
          rounded
          class="mb-6"
        ></v-textarea>
        <v-text-field
          label="Location"
          v-model="newEvent.location"
          clearable
          outlined
          dense
          rounded
          class="mb-6"
        ></v-text-field>
        <v-menu
          ref="menu"
          v-model="picker"
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
              v-model="newEvent.date"
              label="Date"
              prepend-icon="mdi-calendar"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            :min="today"
            v-model="newEvent.date"
            @input="picker = false"
          ></v-date-picker>
        </v-menu>
        <v-menu
          ref="menu"
          v-model="clock"
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
              v-model="newEvent.time"
              label="Time"
              prepend-icon="mdi-clock-time-four-outline"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-time-picker
            v-if="clock"
            scrollable
            :allowed-hours="allowedHours"
            v-model="newEvent.time"
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
          >Your Club's Current Board Members</v-row
        >
        <v-row>
          <v-data-table
            :headers="headers"
            :items="upcomingEvents"
            outlined
            class="elevation-4"
            item-key="name"
          >
            <template v-slot:item.change="{ item }">
              <v-btn
                color="red lighten-1"
                rounded
                small
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
export default {
  data() {
    return {
      error: false,
      newEvent: {
        name: null,
        description: null,
        location: null,
        date: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
          .toISOString()
          .substr(0, 10),
        time: null
      },
      picker: false,
      time: "",
      clock: false,
      today: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
        .toISOString()
        .substr(0, 10),
      date: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
        .toISOString()
        .substr(0, 10),
      upcomingEvents: [
        {
          name: "Event 1",
          description: "Description of event 1",
          location: "Location of event 1",
          date: "01.01.2022",
          time: "17.30"
        },
        {
          name: "Event 2",
          description: "Description of event 2",
          location: "Location of event 2",
          date: "01.02.2022",
          time: "17.30"
        },
        {
          name: "Event 3",
          description: "Description of event 3",
          location: "Location of event 3",
          date: "01.03.2022",
          time: "17.30"
        },
        {
          name: "Event 4",
          description: "Description of event 4",
          location: "Location of event 4",
          date: "01.04.2022",
          time: "17.30"
        }
      ]
    };
  },
  methods: {
    allowedHours(h) {
      let hour = new Date().getHours();
      if (this.newEvent.date == this.today) {
        return h > hour;
      }
      return true;
    },
    removeEvent(event) {
      for (var i = 0; i < this.upcomingEvents.length; i++) {
        if (this.upcomingEvents[i] === event) {
          this.upcomingEvents.splice(i, 1);
        }
      }
    },
    organizeEvent() {
      if (Object.values(this.newEvent).includes(null)) {
        this.error = true;
        return;
      }
      const object = this.newEvent;
      this.upcomingEvents.push(object);
      this.newEvent = {};
      this.newEvent.date = this.today;
      this.error = false;
    }
  },
  computed: {
    headers() {
      return [
        {
          text: "Name",
          align: "center",
          value: "name"
        },
        {
          text: "Description",
          align: "center",
          value: "description"
        },
        {
          text: "Location",
          align: "center",
          value: "location"
        },
        {
          text: "Date",
          align: "center",
          value: "date"
        },
        {
          text: "Time",
          align: "center",
          value: "time"
        },
        {
          text: "",
          align: "center",
          value: "change"
        }
      ];
    }
  }
};
</script>
