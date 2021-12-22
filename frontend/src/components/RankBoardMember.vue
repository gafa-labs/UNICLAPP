<template>
  <v-container class="pa-16">
    <v-row class="display-1 mb-6">Rank Board Member</v-row>
    <v-row>
      <v-col
        cols="12"
        md="4"
        class="pr-16"
        style="border-right: 2px solid lightsteelblue"
      >
        <v-text-field
          v-model="promotingCandidate.name"
          label="Student Name"
          outlined
          dense
          rounded
          class="mt-10 mb-2"
        ></v-text-field>
        <v-text-field
          v-model="promotingCandidate.id"
          label="Student ID"
          outlined
          dense
          rounded
          class="mb-2"
        ></v-text-field>
        <v-text-field
          v-model="promotingCandidate.email"
          label="Student E-mail"
          outlined
          dense
          rounded
          class="mb-2"
        ></v-text-field>
        <v-row class="justify-center"
          ><v-btn elevation="2" rounded color="blue lighten-1" @click="promote"
            >Promote</v-btn
          ></v-row
        >
      </v-col>
      <v-col cols="12" md="8" class="pl-16">
        <v-row class="text-h5 mb-6 font-weight-bold"
          >Your Club's Current Board Members</v-row
        >
        <v-row>
          <v-data-table
            :headers="headers"
            :items="boardMembers"
            outlined
            class="elevation-4"
            item-key="name"
          >
            <template v-slot:item.status="{ item }">
              <v-btn
                color="red lighten-1"
                rounded
                small
                v-if="true"
                @click="demote(item)"
                >Demote</v-btn
              >
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
      promotingCandidate: {
        name: "",
        id: "",
        email: ""
      },
      boardMembers: [
        {
          name: "Ayberk Yasa",
          id: 21802180,
          email: "ayberk.yasa@ug.bilkent.edu.tr"
        },
        {
          name: "Fatih Kaplama",
          id: 21902190,
          email: "fatih.kaplama@ug.bilkent.edu.tr"
        },
        {
          name: "Gorkem Ayten",
          id: 21202120,
          email: "gorkem.ayten@gmail.com"
        },
        {
          name: "Mert Atakan Onrat",
          id: 21212121,
          email: "atakan.onrat@gmail.com"
        }
      ]
    };
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
          text: "ID",
          align: "center",
          value: "id"
        },
        {
          text: "E-mail",
          align: "center",
          value: "email"
        },
        {
          text: "Demote",
          align: "center",
          value: "status"
        }
      ];
    }
  },
  methods: {
    promote() {
      const object = this.promotingCandidate;
      this.boardMembers.push(object);
      this.promotingCandidate = {};
    },
    demote(item) {
      for (var i = 0; i < this.boardMembers.length; i++) {
        if (this.boardMembers[i] === item) {
          this.boardMembers.splice(i, 1);
        }
      }
    }
  }
};
</script>
