<template>
  <div class="container">
    <div class="large-12 medium-12 small-12 cell">
      <input type="file" ref="file" style="display: none" />
      <v-btn @click="$refs.file.click()">Upload</v-btn>
      <v-btn @click="onClickButton()">Submit</v-btn>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "upload-button",
  data() {
    return {
      file: ""
    };
  },
  methods: {
    onClickButton(event) {
      this.file = this.$refs.file.files[0];
      this.$emit("uploaded", this.file);
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