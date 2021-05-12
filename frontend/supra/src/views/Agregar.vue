<template>
  <div>
    <Encabezado></Encabezado>
    <div class="banner-area">
      <form class="container" action="">
        <h1 class="color">Add an Employee</h1>
        <div class="mb-3">
          <label class="form-label color">Name</label>
          <input
            v-model="integrantes.nombres"
            type="text"
            id="nombre"
            class="form-control"
            aria-describedby="emailHelp"
          />
        </div>
        <div class="mb-3">
          <label class="form-label color">Last Name</label>
          <input v-model="integrantes.apellidos" id="apellido" type="text" class="form-control" />
        </div>

        <div>
          <label class="form-label color">Area</label>
          <select
            v-model="integrantes.areas"
            class="form-select form-select-sm select"
            aria-label="Default select example"
          >
            <option id="area" v-for="lista in todasAreas" :key="lista.id" :value="lista.id">
              {{ lista.nombre }}
            </option>
          </select>
        </div>

        <br />
        <div>
          <label class="form-label color">Sub Area</label>
          <select
            v-model="integrantes.subareas"
            class="form-select form-select-sm select"
            aria-label="Default select example"
          >
            <option id="subarea" v-for="lista in todasSubAreas" :key="lista.id" :value="lista.id">
              {{ lista.nombre }}
            </option>
          </select>
        </div>

        <br />
        <div>
          <label class="form-label color">Document Type</label>
          <select
            v-model="integrantes.documentos"
            class="form-select form-select-sm select"
            aria-label="Default select example"
          >
            <option id="documento" v-for="lista in todosDocumentos" :key="lista.id" :value="lista.id">
              {{ lista.nombre }}
            </option>
          </select>
        </div>
        
        <br />  <div class="mb-3">
          <label class="form-label color">Document Number</label>
          <input v-model="integrantes.numeroDocumentos" id="numerodocumento" type="text" class="form-control" />
        </div>
        <button @click.prevent="guardarIntegrantes()" type="submit" class="btn btn-primary">Submit</button>
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
      integrantes: {id:null, nombres:'', apellidos:'', numeroDocumentos:'', subareas:null, documentos:null, areas:null}
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
        .get("http://localhost:8000/api/Sub_areas/")
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
    guardarIntegrantes(){
      var datos = {
        nombre: this.integrantes.nombres,
        apellido: this.integrantes.apellidos,
        numeroDocumento: this.integrantes.numeroDocumentos,
        subarea: this.integrantes.subareas,
        documento: this.integrantes.documentos,
        area: this.integrantes.areas
      }

      console.log(datos)
      axios.post("http://localhost:8000/api/Empleados/", datos)
      .then((respuesta) => {
        console.log(respuesta.data)
      })

    }
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