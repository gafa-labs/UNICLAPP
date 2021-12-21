<template>
  <v-container class="pa-16">
    <v-row class="display-1 mb-6">Profile</v-row>
    <v-row>
      <v-col cols="12" md="4">
        <v-text-field
          :value="information.name"
          label="Name"
          outlined
          disabled
          dense
          rounded
          class="mb-6"
        ></v-text-field>
        <v-text-field
          :value="information.email"
          label="E-mail"
          outlined
          disabled
          dense
          rounded
          class="mb-6"
        ></v-text-field>
        <v-text-field
          value="Change Password"
          filled
          disabled
          dense
          class="mt-4"
        ></v-text-field>
        <v-text-field
          label="Old Password"
          outlined
          dense
          rounded
          class="mt-6"
        ></v-text-field>
        <v-text-field
          label="Create New Password"
          outlined
          dense
          rounded
          class="mt-1"
        ></v-text-field>
        <v-text-field
          label="Confirm New Password"
          outlined
          dense
          rounded
          class="mt-1"
        ></v-text-field>
        <v-row class="mt-1 justify-center">
          <v-btn elevation="2" rounded color="light-blue accent-2"
            >Apply Change</v-btn
          >
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
export default {
  data() {
    return {
      information: {
        name: "Eray Tüzün",
        email: "eray.tuzun@bilkent.edu.tr"
      }
    };
  }
};
</script>
