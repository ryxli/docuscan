<template>
  <div class="btn btn-primary jbtn-file">
    <v-container>
      <input type="file" ref="files" multiple v-on:change="fileUpload()" />
      <v-btn v-on:click="submitFile()">Upload</v-btn>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "upload-button",
  data() {
    return {
      files: []
    };
  },
  methods: {
    filesUpload() {
      this.files = this.$refs.files.files;
    },
    submitFile() {
      let formData = new FormData();
      for (var i = 0; i < this.files.length; i++) {
        let file = this.files[i];

        formData.append("files[" + i + "]", file);
      }

      axios
        .post("/multiple-files", formData, {
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
    }
  }
};
</script>

<style scoped>
.jbtn-file {
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.jbtn-file input[type="file"] {
  position: absolute;
  top: 0;
  right: 0;
  min-width: 100%;
  min-height: 100%;
  text-align: right;
  filter: alpha(opacity=0);
  opacity: 0;
  outline: none;
  cursor: inherit;
  display: block;
}
</style>