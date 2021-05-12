<template>
  <div class="home">
    <Encabezado></Encabezado>
    <div class="banner-area">
      <div class="content-area">
        <div class="content">
          <h1>Supra National Express</h1>
          <p>Moving Ahead Of The Rest</p>
          <a href="/integrantes" class="boton btn btn-primary">Click Here</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Encabezado from "@/components/Encabezado.vue";

export default {
  name: "Home",
  components: {
    Encabezado,
  },
};
</script>

<style scoped>

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
  .content-area{
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .content{
    text-align: center;
  }
  .content h1{
    font-size: 80px;
    color: #fff;
  }
  .content p{
    font-size: 40px;
    color: #ddd;
  }
  .content .boton {
    border: none;
    outline: none;
    padding: 15px;
    margin-top: 25px;
    border-radius: 25px;
    color: #eee;
    font-size: 18px;
    cursor: pointer;
  }
</style>
