<template>
  <div>
    <v-navigation-drawer app>
      <v-list>
        <v-list-item two-line style="justify-content: center;">
          <v-icon x-large style="font-size: 150px">mdi-account</v-icon>
        </v-list-item>

        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="text-center" style="font-size: 28px">{{
              information.name
            }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-divider></v-divider>

        <div v-if="this.userStatus == 'ClubAdvisor'">
          <router-link
            v-for="item in clubAdvisorListItems"
            :key="item.title"
            tag="v-list-item"
            :to="item.path"
            link
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </router-link>
        </div>

        <div
          v-if="
            this.userStatus == 'Student' ||
              this.userStatus == 'BoardMember' ||
              this.userStatus == 'BoardChairman'
          "
        >
          <router-link
            v-for="item in studentListItems"
            :key="item.title"
            tag="v-list-item"
            :to="item.path"
            link
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </router-link>
        </div>

        <v-divider></v-divider>

        <div
          v-if="
            this.userStatus == 'BoardMember' ||
              this.userStatus == 'BoardChairman'
          "
        >
          <router-link
            v-for="item in boardMemberListItems"
            :key="item.title"
            tag="v-list-item"
            :to="item.path"
            link
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </router-link>
          <div v-if="this.userStatus == 'BoardChairman'">
            <router-link
              v-for="item in boardChairmenListItems"
              :key="item.title"
              tag="v-list-item"
              :to="item.path"
              link
            >
              <v-list-item-icon>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-item-icon>

              <v-list-item-content>
                <v-list-item-title>{{ item.title }}</v-list-item-title>
              </v-list-item-content></router-link
            >
          </div>
        </div>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar flat app>
      <v-spacer></v-spacer>
      <v-app-bar-title>
        <span class="font-weight-light display-2">UNI</span
        ><span class="display-2">CLAPP</span>
      </v-app-bar-title>
      <v-spacer></v-spacer>
      <v-btn class="mr-2" text color="green" to="/main">
        Tutorial
        <v-icon class="ml-1">mdi-comment-question</v-icon>
      </v-btn>
      <v-btn text color="red" @click="logout">
        LOGOUT
        <v-icon class="ml-1">mdi-exit-to-app</v-icon>
      </v-btn>
    </v-app-bar>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      information: {
        name: "",
        psi: 98
      },
      userStatus: "",
      studentListItems: [
        { title: "Profile", icon: "mdi-account", path: "/profile" },
        { title: "Explore", icon: "mdi-magnify", path: "/explore" },
        { title: "Followings", icon: "mdi-account-plus", path: "/followings" },
        {
          title: "Upcoming Events",
          icon: "mdi-calendar-clock",
          path: "/upcomingEvents"
        },
        { title: "Event History", icon: "mdi-history", path: "/eventHistory" },
        {
          title: "Event Tracker",
          icon: "mdi-calendar-range",
          path: "/eventTracker"
        },
        { title: "Campus Map", icon: "mdi-map", path: "/campusMap" },
        { title: "Leaderboard", icon: "mdi-trophy", path: "/leaderboard" }
      ],
      boardMemberListItems: [
        {
          title: "Club Profile",
          icon: "mdi-account-group",
          path: "/clubProfile"
        },
        {
          title: "Organize Event",
          icon: "mdi-pencil",
          path: "/organizeEvent"
        },
        {
          title: "Event Result",
          icon: "mdi-calendar-check",
          path: "/eventResult"
        }
      ],
      clubAdvisorListItems: [
        {
          title: "Profile",
          icon: "mdi-account",
          path: "/advisorProfile"
        },
        {
          title: "Club Profile",
          icon: "mdi-account-group",
          path: "/clubProfile"
        },
        {
          title: "Event Result",
          icon: "mdi-calendar-check",
          path: "/eventResult"
        }
      ],
      boardChairmenListItems: [
        {
          title: "Rank Board Member",
          icon: "mdi-arrow-up-down",
          path: "/rankBoardMember"
        }
      ]
    };
  },
  methods: {
    logout() {
      localStorage.removeItem("user");
      this.$router.push("/");
      this.$store.state.isLoggedIn = false;
    }
  },
  created() {
    if (localStorage.getItem("status") === "true") {
      var token = "Token " + JSON.parse(localStorage.getItem("user")).token;
      axios
        .get("http://localhost:8000/api/profiles/student/", {
          headers: { Authorization: token }
        })
        .then(response => {
          this.information = response.data;
        })
        .catch(e => console.log(e));
    }
    var status = JSON.parse(localStorage.getItem("user")).type;
    if (status === "boardchairman") {
      status = "BoardChairman";
    } else if (status == "boardmember") {
      status = "BoardMember";
    } else if (status == "student") {
      status = "Student";
    }

    this.userStatus = status;
  }
};
</script>
