<template>
  <div class="dashboard">
    <v-subheader class="grey--text">Dashboard</v-subheader>

    <label>
      File
      <input type="file" id="file" ref="file" v-on:change="handleFileUpload()" />
      <v-btn v-on:click="submitFile()">Submit</v-btn>
    </label>

    <v-container class="my-5">
      <v-data-table
        v-model="selected"
        :headers="headers"
        :items="documents"
        item-key="name"
        select-all
        show-select
      >
        <template slot="items" slot-scope="props">
          <td>
            <v-checkbox v-model="props.selected" primary hide-details></v-checkbox>
          </td>
          <td>{{ props.item.name }}</td>
          <td class="text-xs-left">{{ props.item.scannedYet }}</td>
          <td class="text-xs-left">{{ props.item.safeBy }}</td>
        </template>
      </v-data-table>
      <v-btn color="primary" @click="deleteItem">Delete</v-btn>
    </v-container>

    <p>{{ message }}</p>
    <input v-model="message" />
  </div>
</template>


<script>
export default {
  data() {
    return {
      message:
        "Type whatever you want in the bottom and you can access it like this in the html template portion: {{ message }} filler",
      file: "",
      selected: [],
      dialog: false,
      headers: [
        {
          text: "Document",
          align: "left",
          sortable: true,
          value: "name"
        },
        { text: "Scanned?", value: "scanned" },
        { text: "Safe", value: "safe" }
      ],
      documents: [
        {
          name: "Frozen",
          scanned: "yes",
          safe: "no"
        },
        {
          name: "Frozen Yogurt",
          scanned: "yes",
          safe: "yes"
        }
      ]
    };
  },
  methods: {
    handleFileUpload() {
      this.file = this.$refs.file.files[0];
    },
    submitFile() {
      let formData = new FormData();
      formData.append("file", this.file);
      axios
        .post("/single-file", formData, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        })
        .then(function() {
          console.log("SUCCESS!!");
        })
        .catch(function() {
          console.log("FAILURE!!");
        });
    },
    deleteItem() {
      for (var i = 0; i < this.selected.length; i++) {
        const index = this.documents.indexOf(this.selected[i]);
        this.documents.splice(index, 1);
      }
      this.dialog = false;
    }
  }
};
</script>
