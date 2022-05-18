<template>
  <div id="app">
    <div id="header">Hello World</div>
    <div id="viewer" ></div>
  </div>
</template>

<script>
import Mirador from 'mirador/dist/es/src/index';
import { miradorImageToolsPlugin } from 'mirador-image-tools';
export default {
  name: 'App',
  mounted(){
    const config = {
      id: 'viewer',
      selectedTheme: 'light',
        allowFullscreen: false,
        language: 'de',
      windows: [{
        imageToolsEnabled: false,
        imageToolsOpen: false,
        manifestId: '',
        sideBarPanel: 'search',
        allowFullscreen: false,
        allowWindowSideBar: true,
        panels: {
        info: true,
              attribution: false,
      canvas: false,
      annotations: true,
      search: false,
      layers: false,
        }
      }],
    };
    Mirador.viewer(config, [
      ...miradorImageToolsPlugin,
    ]);
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
#app {
height: 100%;
}
#header {
height:2em;
}
#viewer {
      display: block;
      height: 500px;
      position: relative;
      }

</style>