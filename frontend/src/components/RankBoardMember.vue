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
          v-model="promotingCandidate.student_name"
          label="Student Name"
          outlined
          dense
          rounded
          class="mt-10 mb-2"
        ></v-text-field>
        <v-text-field
          v-model="promotingCandidate.student_id"
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

        <v-data-table
          :headers="headers"
          :items="boardMembers"
          outlined
          class="elevation-4"
          item-key="name"
        >
          <template v-slot:[`item.status`]="{ item }">
            <v-btn
              color="red lighten-1"
              rounded
              small
              v-if="item.student_id != chairmanId"
              @click="demote(item)"
              >Demote</v-btn
            >
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      chairmanId: "",
      header: {
        headers: {
          Authorization:
            "Token " + JSON.parse(localStorage.getItem("user")).token
        }
      },
      promotingCandidate: {
        student_name: "",
        student_id: "",
        email: ""
      },
      boardMembers: []
    };
  },
  computed: {
    headers() {
      return [
        {
          text: "Name",
          align: "center",
          value: "student_name"
        },
        {
          text: "ID",
          align: "center",
          value: "student_id"
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
      axios
        .post(
          "http://localhost:8000/api/accounts/rank/promote-student/",
          object,
          this.header
        )
        .then(response => {
          object.objectId = response.data;
          this.boardMembers.push(object);
          this.promotingCandidate = {};
        })
        .catch(e => {
          alert("There is no such a student!");
          this.promotingCandidate = {};
        });
    },
    demote(item) {
      for (var i = 0; i < this.boardMembers.length; i++) {
        if (this.boardMembers[i] === item) {
          this.boardMembers.splice(i, 1);
          const endpoint =
            "http://localhost:8000/api/accounts/rank/demote-boardmember/" +
            item.objectId +
            "/";
          axios.delete(endpoint).catch(e => {
            console.log(e);
          });
        }
      }
    }
  },
  created() {
    axios
      .get("http://localhost:8000/api/profiles/student/", this.header)
      .then(response => {
        this.chairmanId = response.data.student_id;
      });
    axios
      .get("http://localhost:8000/api/club/boardmembers/", this.header)
      .then(response => {
        response.data.forEach(object => {
          const boardMember = {
            student_name: object.student.user.full_name,
            student_id: object.student.student_id,
            email: object.student.user.email,
            objectId: object.id
          };
          this.boardMembers.push(boardMember);
        });
      })
      .catch(e => {
        console.log(e);
      });
  }
};
</script>
