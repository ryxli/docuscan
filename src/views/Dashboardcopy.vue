<template>
  <div class="dashboard">
    <v-subheader class="grey--text">Dashboard</v-subheader>

    <upload-button title="Browse" @uploaded="updateParent"></upload-button>
    <v-container class="my-5">
      <v-data-table v-model="selected" :headers="headers" :items="documents" item-key="name">
        <template slot="items" slot-scope="props">
          <td>
            <v-checkbox v-model="props.selected" primary hide-details></v-checkbox>
          </td>
          <td>{{ props.item.name }}</td>
          <td class="text-xs-left">{{ props.item.scannedYet }}</td>
          <td class="text-xs-left">{{ props.item.safeBy }}</td>
        </template>
      </v-data-table>
    </v-container>

    <v-container>
      <v-textarea
        filled
        id="textarea"
        v-model="message"
        placeholder="Please upload your contract above and paste the contents of it in here..."
        rows="10"
        max-rows="15"
      ></v-textarea>
      <v-btn color="primary" @click="find_phrases">Scan</v-btn>
    </v-container>

    <p>{{output}}</p>
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
      message: "",
      output: "",
      temp64: "",
      selected: [],
      dialog: false,
      headers: [
        {
          text: "Document",
          align: "left",
          sortable: true,
          value: "name"
        },
        { text: "Size", value: "size" }
      ],
      documents: [],
      addDocForm: {
        name: "",
        size: "",
        base64: ""
      }
    };
  },
  methods: {
    getBase64(file) {
      var reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = function() {
        this.temp64 = reader.result;
        console.log(reader.result);
      };
      reader.onerror = function(error) {
        console.log("Error: ", error);
      };
    },
    updateParent(value) {
      var update = true;
      for (var i = 0; i < this.documents.length; i++) {
        if (this.documents[0]["name"] == value.name) {
          update = false;
        }
      }
      if (update) {
        console.log(update);
        console.log(this.documents);
        this.src = value; // someValue
        this.addDocForm.name = value.name;
        this.addDocForm.size = value.size;
        this.getBase64(value);
        this.addDocForm.base64 = this.temp64;
        this.find_phrases();
        const payload = {
          name: this.addDocForm.name,
          size: this.addDocForm.size,
          base64: this.addDocForm.base64
        };
        this.addDoc(payload);
        this.getDocs();
        this.initForm();
      }
    },
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
    },
    getDocs() {
      const path = "http://localhost:5000/documents";
      axios
        .get(path)
        .then(res => {
          this.documents = res.data.documents;
        })
        .catch(error => {
          console.error(error);
        });
    },
    addDoc(payload) {
      const path = "http://localhost:5000/documents";
      axios
        .post(path, payload)
        .then(() => {
          this.getDocs();
        })
        .catch(error => {
          console.log(error);
          this.getDocs();
        });
    },
    initForm() {
      this.addDocForm.name = "";
      this.addDocForm.size = "";
    }
  },
  created() {
    this.getDocs();
  }
};
</script>
