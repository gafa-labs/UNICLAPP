<template>
  <div>
    <!-- Sizes your content based upon application components -->
    <!-- Provides the application the proper gutter -->
    <v-container fluid>
      <h1>This is a main page</h1>
      <!-- If using vue-router -->
      <router-view></router-view>
    </v-container>

    <v-footer app>
      <!-- -->
    </v-footer>
  </div>
</template>

<script>
import Navbar from "../components/Navbar";
export default {
  components: {
    navBar: Navbar
  }
};
</script>
