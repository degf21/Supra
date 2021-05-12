<template>
  <div>
    <nav
      class="navbar navbar-expand-lg navbar-dark"
      style="background-color: #505160"
    >
      <a class="navbar-brand img-fluid" href="#">
        <img
          src="@/assets/logo.png"
          alt=""
          width="170"
          height="40"
          class="d-inline-block align-text-top"
        />
      </a>

      <div class="container-fluid">
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0 lista">
            <li class="nav-item">
              <a class="nav-link active lista" aria-current="page" href="/"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/nosotros">About Us</a>
            </li>
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="/integrantes"
                >Employeds</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/contacto">Contact</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>
