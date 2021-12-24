<template>
  <div>
    <v-navigation-drawer app>
      <v-list>
        <v-list-item style="justify-content: center;">
          <v-list-item-avatar size="75%">
            <v-img
              src="https://randomuser.me/api/portraits/women/85.jpg"
            ></v-img>
          </v-list-item-avatar>
        </v-list-item>

        <v-list-item>
          <v-list-item-content>
            <v-list-item-title>Name Surname</v-list-item-title>
            <v-list-item-subtitle>PSI: 100</v-list-item-subtitle>
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
            this.userStatus == 'Student' || this.userStatus == 'BoardMember'
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

        <div v-if="this.userStatus == 'BoardMember'">
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
export default {
  data() {
    return {
      userStatus: "BoardMember",
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
        },
        {
          title: "Rank Board Member",
          icon: "mdi-arrow-up-down",
          path: "/rankBoardMember"
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
      ]
    };
  },
  methods: {
    logout() {
      localStorage.removeItem("user");
      this.$router.push("/");
      this.$store.state.isLoggedIn = false;
    }
  }
};
</script>
