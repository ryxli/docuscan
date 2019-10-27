<template>
  <div class="dashboard">
    <v-subheader class="grey--text">Dashboard</v-subheader>

    <upload-button title="Browse" @uploaded="updateParent"></upload-button>
    <v-container class="my-5">
      <v-data-table
        v-model="selected"
        :headers="headers"
        :items="documents"
        item-key="name"
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
        this.addDocForm.base64 = this.getBase64(value);
        this.src = value;
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
    deleteItem() {
      for (var i = 0; i < this.selected.length; i++) {
        this.onDeleteDoc(this.selected[0]);
      }
    },
    removeDoc(docID) {
      const path = `http://localhost:5000/documents/${docID}`;
      axios
        .delete(path)
        .then(() => {
          this.getDocs();
          this.message = "Doc removed!";
          this.showMessage = true;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
          this.getDocs();
        });
    },
    onDeleteDoc(doc) {
      this.removeDoc(doc.id);
    },
    decode64(payload) {
      var pdfData = atob(payload["base64"]);
      var pdfjsLib = window["pdfjs-dist/build/pdf"];
      pdfjsLib.GlobalWorkerOptions.workerSrc =
        "//mozilla.github.io/pdf.js/build/pdf.worker.js";
      var loadingTask = pdfjsLib.getDocument({ data: pdfData });

      loadingTask.promise.then(
        function(pdf) {
          var pdfDocument = pdf;
          var pagesPromises = [];

          for (var i = 0; i < pdf.numPages; i++) {
            // Required to prevent that i is always the total of pages
            (function(pageNumber) {
              pagesPromises.push(getPageText(pageNumber, pdfDocument));
            })(i + 1);
          }

          Promise.all(pagesPromises).then(function(pagesText) {
            // Display text of all the pages in the console
            console.log(pagesText);
          });
          return pagesText;
        },
        function(reason) {
          // PDF loading error
          console.error(reason);
        }
      );
    },
    find_phrases() {
      var s = this.decode64(this.selected[0]["base64"]);
      console.log(s.replace(/ /g, "%20"));
      var new_message = s.replace(" ", "%20");
      console.log("Got here");
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
  getPageText(pageNum, PDFDocumentInstance) {
    // Return a Promise that is solved once the text of the page is retrieven
    return new Promise(function(resolve, reject) {
      PDFDocumentInstance.getPage(pageNum).then(function(pdfPage) {
        // The main trick to obtain the text of the PDF page, use the getTextContent method
        pdfPage.getTextContent().then(function(textContent) {
          var textItems = textContent.items;
          var finalString = "";

          // Concatenate the string of the item to the final string
          for (var i = 0; i < textItems.length; i++) {
            var item = textItems[i];

            finalString += item.str + " ";
          }

          // Solve promise with the text retrieven from the page
          resolve(finalString);
        });
      });
    });
    return finalString;
  },

  created() {
    this.getDocs();
  }
};
</script>
