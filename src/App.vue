<template>
  <v-app style="
    background: #F0F0F0;
  ">
    <Nav />
    <v-content class="mx-4 mb-4">
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import Nav from "@/components/Nav";
export default {
  name: "App",
  components: { Nav },
  data: () => ({
    //
  })
};
</script>
