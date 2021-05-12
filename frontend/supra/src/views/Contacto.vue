<template>
  <div>
    <Navbar></Navbar>
    <div class="banner-area">
      <div class="container color">
          <div class="text-center">
            <h1>Contact</h1>
          </div>
          <div class="mb-3">
            <label for="exampleFormControlInput1" class="form-label"
              >Name</label
            >
            <input
              type="text"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="name"
            />
            <label for="exampleFormControlInput1" class="form-label"
              >Email</label
            >
            <input
              type="email"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="name@example.com"
            />
          </div>
          <div class="mb-3">
            <label for="exampleFormControlTextarea1" class="form-label"
              >Message</label
            >
            <textarea
              class="form-control"
              id="exampleFormControlTextarea1"
              rows="3"
            ></textarea>
          </div>
          <div class="col-auto">
            <button type="submit" class="btn btn-primary mb-3">Confirm</button>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";

export default {
  name: "Home",
  components: {
    Navbar,
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
.content-area {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.color {
  background-color: #fff;
}
</style>