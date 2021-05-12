<template>
  <div class="container">
    <div>
      <label class="form-label color ">Area</label>
      <select
        class="form-select form-select-sm select"
        aria-label="Default select example"
      >
        <option selected>Choose a option</option>
        <option v-for="lista in todasAreas" :key="lista.id">
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
        <option v-for="lista in todasSubAreas" :key="lista.id">
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
        <option v-for="lista in todosDocumentos" :key="lista.id">
          {{ lista.nombre }}
        </option>
      </select>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
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

<style scoped>
.select {
  padding: 8px 12px;
  color: #333333;
  background-color: #eeeeee;
  border: 1px solid#dddddd;
  cursor: pointer;
  border-radius: 5px;
}
.color{
  color : #fff
}
</style>