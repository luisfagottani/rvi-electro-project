<template>
  <div id="app">
    <LoadingState></LoadingState>
    <router-view></router-view>
  </div>
</template>

<script>
const Store = require("electron-store");
const store = new Store();

const fs = require("fs");
const grpc = require("grpc");
const path = require("path");
require("fabric");

try {
  var service;
  if (process.env.NODE_ENV == "production") {
    const PROTO_PATH = path.join(__dirname + "/src/project/protos/api.proto");
    service = grpc.load(PROTO_PATH).park;
  } else {
    service = grpc.load("src/core/sample/protos/api.proto").park;
  }
} catch (error) {
  alert(error);
}

let client = new service.Parking(
  "localhost:50060",
  grpc.credentials.createInsecure()
);
import LoadingState from "@/components/shared/LoadingState.vue";
import { setTimeout, setInterval } from "timers";
export default {
  name: "rviapp",
  beforeMount() {
    this.$store.dispatch("setLoading", true);
    this.initSystem();
  },
  methods: {
    initSystem: function() {
      this.$store.dispatch("setPythonApi", client);
      if (Object.keys(store.get()).length < 1) {
        this.$router.push({ name: "lista-cameras" });
      } else {
        let camerasStorage = store.get();
        let cont = 0;
        for (let cameraId in camerasStorage) {
          // skip loop if the property is from prototype
          if (typeof camerasStorage.cameraId !== "undefined") continue;
          if (cont == 0) {
            this.$store.dispatch("setCamera", cameraId);
          }
          let obj = camerasStorage[cameraId];
          this.$store.dispatch("addCamera", obj);
          cont++;
        }
        this.$router.push({ name: "lista-cameras" });
      }
    }
  },
  components: {
    LoadingState
  }
};
</script>

<style lang="scss">
html,
body,
div,
span,
applet,
object,
iframe,
h1,
h2,
h3,
h4,
h5,
h6,
p,
blockquote,
pre,
a,
abbr,
acronym,
address,
big,
cite,
code,
del,
dfn,
em,
img,
ins,
kbd,
q,
s,
samp,
small,
strike,
strong,
sub,
sup,
tt,
var,
b,
u,
i,
center,
dl,
dt,
dd,
ol,
ul,
li,
fieldset,
form,
label,
legend,
table,
caption,
tbody,
tfoot,
thead,
tr,
th,
td,
article,
aside,
canvas,
details,
embed,
figure,
figcaption,
footer,
header,
hgroup,
menu,
nav,
output,
ruby,
section,
summary,
time,
mark,
audio,
video {
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  vertical-align: baseline;
}

body {
  overflow: hidden;
  background-color: #1d233c;
  height: 100vh;
  -ms-overflow-style: scrollbar;
  font-family: "Open Sans", sans-serif;
}

/* HTML5 display-role reset for older browsers */
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
menu,
nav,
section {
  display: block;
}
body {
  line-height: 1;
}
ol,
ul {
  list-style: none;
}
blockquote,
q {
  quotes: none;
}
blockquote:before,
blockquote:after,
q:before,
q:after {
  content: "";
  content: none;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}

* {
  -webkit-user-select: none;
  outline: none;
  box-sizing: border-box;
}

a {
  text-decoration: none;
}

.cta {
  // Box Model
  padding: 14px 80px;

  // Visual
  background-color: #74b0f6;
  box-shadow: 0px 0px 3px 0 rgba($color: #77b3f9, $alpha: 0.7);
  border-radius: 3px;
  transition: 0.5s all ease-in-out;

  // Typography
  font-size: 17px;
  font-weight: 700;
  color: #ffffff;
  text-align: center;
  text-transform: uppercase;

  &--disabled {
    // Visual
    background-color: #ccc;
    color: #000;
    pointer-events: none;
    cursor: not-allowed;
  }

  &:hover {
    // Visual
    transition: 0.3s all ease-in-out;
    background-color: darken($color: #74b0f6, $amount: 20);
    cursor: pointer;
  }
}

.title {
  // Typography
  font-size: 36px;
  font-weight: 600;
  color: #ffffff;
  text-align: center;

  // Box Model
  margin-bottom: 8px;
  margin-top: 90px;
}

.subtitle {
  // Typography
  color: #ffffff;
  font-size: 16px;
  text-align: center;

  // Box Model
  margin-top: 0;
  margin-bottom: 80px;
}
</style>
