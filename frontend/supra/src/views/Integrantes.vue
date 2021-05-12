<template>
  <div>
    <div class="banner-area">
      <Navbar></Navbar>
      <Cabecera></Cabecera>
      <Search></Search>
      <Tabla></Tabla>
    </div>
  </div>
</template>

<script>
import Cabecera from "@/components/Cabecera.vue";
import Tabla from "@/components/Tabla.vue";
import Search from "@/components/Search.vue";
import Navbar from "@/components/Navbar.vue";

export default {
  name: "App",
  components: {
    Cabecera,
    Tabla,
    Search,
    Navbar,
  },
};
</script>

<style>
  *{
    padding: 0;
    margin: 0;
    box-sizing: border-box;
  }
  .banner-area{
    width: 100%;
    height: 100vh;
    background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url("../assets/supra.png");
    background-size: cover;
  }
</style>