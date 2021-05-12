<template>
  <div>
    <Encabezado></Encabezado>
    <div class="banner-area">
      <form class="container" action="">
        <h1 class="color">Add an Employee</h1>
        <div class="mb-3">
          <label class="form-label color">Name</label>
          <input
            type="text"
            id="nombre"
            class="form-control"
            aria-describedby="emailHelp"
          />
        </div>
        <div class="mb-3">
          <label class="form-label color">Last Name</label>
          <input id="apellido" type="text" class="form-control" />
        </div>

        <div>
          <label class="form-label color">Area</label>
          <select
            class="form-select form-select-sm select"
            aria-label="Default select example"
          >
            <option selected>Choose a option</option>
            <option id="area" v-for="lista in todasAreas" :key="lista.id">
              {{ lista.nombre }}
            </option>
          </select>
        </div>

        <br />
        <div>
          <label class="form-label color">Sub Area</label>
          <select
            class="form-select form-select-sm select"
            aria-label="Default select example"
          >
            <option selected>Choose a option</option>
            <option id="subarea" v-for="lista in todasSubAreas" :key="lista.id">
              {{ lista.nombre }}
            </option>
          </select>
        </div>

        <br />
        <div>
          <label class="form-label color">Document Type</label>
          <select
            class="form-select form-select-sm select"
            aria-label="Default select example"
          >
            <option selected>Choose a option</option>
            <option id="documento" v-for="lista in todosDocumentos" :key="lista.id">
              {{ lista.nombre }}
            </option>
          </select>
        </div>
        
        <br />
        <div class="mb-3">
          <label class="form-label color">Document Number</label>
          <input id="numerodocumento" type="text" class="form-control" />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
        <a href="/integrantes" class="btn btn-primary">Cancel</a>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
// @ is an alias to /src
import Encabezado from "@/components/Encabezado.vue";

export default {
  components: {
    Encabezado,
  },

  data() {
    return {
      todasAreas: null,
      todasSubAreas: null,
      todosDocumentos: null,
    };
  },
  mounted() {
    this.getTodasAreas();
    this.getTodasSubAreas();
    this.getTodosDocumentos();
  },

  methods: {
    getTodasAreas() {
      axios
        .get("http://localhost:8000/api/Areas/")
        .then((response) => {
          this.todasAreas = response.data;
        })
        .catch((e) => console.log(e));
    },
    getTodasSubAreas() {
      axios
        .get("http://localhost:8000/api/Sub_Areas/")
        .then((response) => {
          this.todasSubAreas = response.data;
        })
        .catch((e) => console.log(e));
    },
    getTodosDocumentos() {
      axios
        .get("http://localhost:8000/api/Documentos/")
        .then((response) => {
          this.todosDocumentos = response.data;
        })
        .catch((e) => console.log(e));
    },
  },
};
</script>

<style>
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
.banner-area {
  width: 100%;
  height: 100vh;
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("../assets/supra.png");
  background-size: cover;
}
.color {
  color: #fff;
}
</style>