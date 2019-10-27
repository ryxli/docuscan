<template>
  <div class="dashboard">
    <v-subheader class="grey--text">Dashboard</v-subheader>

    <!-- <upload-button title="Browse" @uploaded="updateParent"></upload-button> -->
    <v-textarea
      filled
      id="textarea"
      v-model="message"
      placeholder="Please copy and paste your contract here..."
      rows="10"
      max-rows="15"
    ></v-textarea>
    <v-btn color="primary" @click="find_phrases">Scan</v-btn>

    <p>{{output}}</p>
  </div>
</template>



<script>
import axios from "axios";
import UploadButton from "@/components/UploadButton";
export default {
  data() {
    return {
      message: "",
      output: ""
    };
  },
  methods: {
    find_phrases() {
      var new_message = this.message.replace(" ", "%20");
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
