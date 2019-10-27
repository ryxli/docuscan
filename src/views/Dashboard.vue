<template>
  <div class="dashboard">
    <v-subheader class="grey--text">Dashboard</v-subheader>

    <upload-button title="Browse" :selectedCallback="fileSelectedFunc"></upload-button>
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
      <v-btn color="primary" @click="find_phrases">Scan</v-btn>
      <v-btn color="primary" @click="deleteItem">Delete</v-btn>
    </v-container>

    <p>{{ output }}</p>
    <input v-model="message" />
  </div>
</template>


<script>
import axios from "axios";
import UploadButton from "@/components/UploadButton";
export default {
  components: {
    UploadButton
  },
  data() {
    return {
      src: "",
      message:
        "Type whatever you want in the bottom and you can access it like this in the html template portion",
      output: "dummy",
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
        .then(function(response) {
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
      console.log("Got here");
    },
    find_phrases() {
      var s = " ";
      console.log(this.message.replace(/ /g, "%20"));
      var new_message = this.message.replace(" ", "%20");
      console.log("Got here");
      this.output = "Loading...";
      axios.get("http://localhost:5000/calc/".concat(new_message)).then(
        function(response) {
          console.log("Success");

          this.output = response.data;
          console.log(this.output);
        }.bind(this)
      );
    }
  }
};
</script>
