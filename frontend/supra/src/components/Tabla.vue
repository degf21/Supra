<template>
  <div>
    <div id="app" class="container">
      <div class="row">
        <table class="table table-striped table-hover table-bordered color">
          <thead>
            <tr class="table-dark">
              <th scope="col">#</th>
              <th scope="col">Document Tipe</th>
              <th scope="col">Document Number</th>
              <th scope="col">Name</th>
              <th scope="col">Last Name</th>
              <th scope="col">Area</th>
              <th scope="col">Sub Area</th>
              <th scope="col">Edit</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in datosPaginados" :key="item.id">
              <td>{{ item.id }}</td>
              <td>{{ item.NombreDocumento }}</td>
              <td>{{ item.numeroDocumento }}</td>
              <td>{{ item.nombre }}</td>
              <td>{{ item.apellido }}</td>
              <td>{{ item.NombreArea}}</td>
              <td>{{ item.NombreSub_Area}}</td>
              <td><a href="#!"><img src="@/assets/edit.png"></a></td>

            </tr>
          </tbody>
        </table>
        <nav aria-label="Page navigation example">
          <ul class="pagination">
            <li v-on:click="getPreviousPage()" class="page-item">
              <a class="page-link" href="#">Previous</a>
            </li>
            <li v-for="pagina in totalPaginas()" :key="pagina" v-on:click="getDataPagina(pagina)" class="page-item" v-bind:class="isActive(pagina)"><a class="page-link" href="#">{{pagina}}</a></li>
            <li v-on:click="getNextPage()" class="page-item"><a class="page-link" href="#">Next</a></li>
          </ul>
        </nav>
        <div>
          <a href="/integrantes/agregar" class="boton btn btn-primary">Add</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      tareas: [], // articulos
      elementosPorPagina: 10,
      datosPaginados: [],
      paginaActual: 1
    };
  },
  mounted() {
    this.getEmpleados();
    this.getDataPagina(1);
  },
  methods: {
    async getEmpleados() {
      await axios
        .get("http://localhost:8000/api/Empleados/")
        .then((response) => {
          this.tareas = response.data;
          console.log(response.data)
        })
        .catch((e) => console.log(e));
    },
    totalPaginas() {
      return Math.ceil(this.tareas.length / this.elementosPorPagina);
    },
    getDataPagina(noPagina){
      this.paginaActual = noPagina;
      this.datosPaginados = [];
      let ini = (noPagina * this.elementosPorPagina) - this.elementosPorPagina;
      let fin = (noPagina * this.elementosPorPagina);
      this.datosPaginados = this.tareas.slice(ini, fin);
    },
    getPreviousPage(){
      if (this.paginaActual > 1) {
        this.paginaActual--;
      }
      this.getDataPagina(this.paginaActual);
    },
    getNextPage(){
      if (this.paginaActual < this.totalPaginas()) {
        this.paginaActual++;
      }
      this.getDataPagina(this.paginaActual);
    },
    isActive(noPagina){
      if (noPagina == this.paginaActual) {
        return 'active';
      } else {
        return '';
      }
    },
  },
};
</script>

<style>
.color {
  background-color: #fff;
}
</style>