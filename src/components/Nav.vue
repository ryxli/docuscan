<template>
  <nav>
    <v-app-bar flat app>
      <v-app-bar-nav-icon class="grey--text" @click="drawer = !drawer"></v-app-bar-nav-icon>

      <router-link to="/" style="text-decoration:none;">
        <v-toolbar-title class="grey--text">
          <span class="font-weight-bold blue--text">Docu</span>
          <span>Scan</span>
        </v-toolbar-title>
      </router-link>

      <v-spacer></v-spacer>
      <v-btn depressed class="grey--text">
        <span>Sign Out</span>
        <v-icon right>exit_to_app</v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app class="primary">
      <v-list>
        <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
          <v-list-item-icon>
            <v-icon class="white--text">{{ link.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title class="white--text">{{ link.text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      drawer: false,
      links: [
        { icon: "mdi-view-dashboard", text: "Dashboard", route: "/dashboard" },
        { icon: "mdi-folder", text: "My Files", route: "/files" }
      ]
    };
  }
};
</script>

<style>
li a {
  text-decoration: none;
}
</style>