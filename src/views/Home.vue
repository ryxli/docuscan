<template>
  <div class="home">
    <v-container class="my-12 .display-3">
      <v-row wrap>
        <v-col cols="12">
          <h1>Sign with Confidence</h1>
        </v-col>
        <v-col cols="12">
          <h3 class="font-weight-light">And never fall for a shady contract again.</h3>
        </v-col>
        <v-col cols="2">
          <router-link to="/dashboard" tag="v-btn">
            <v-btn depressed outline block dark class="blue">Import Contracts</v-btn>
          </router-link>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {};
</script>

<style>
h1 {
  font-size: 44px;
}
</style>
