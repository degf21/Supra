<template>
  <div>
    <Navbar></Navbar>
    <div>
      <div class="container text-center">
        <img src="@/assets/supra.jpg" alt="" width="500" height="300" />
        <p class="color">
          Our mission is to be the market leader in transportation and
          logistics, serving customers from around the globe doing business to
          and from Southern California... to and from all points beyond. Since
          our founding in 2009, we have been guided by our core values:
          integrity, service and diversity. We hire and work to retain only the
          most qualified and dedicated individuals who share our values and are
          committed to our company’s vision. Every member of our friendly,
          knowledgeable team is determined to provide the utmost in customer
          service to every one of our customers. Our earned, stellar reputation
          rests on our ability to provide only the highest level of service to
          our customers, to recognize opportunities, and to react to the
          constantly evolving market conditions well ahead of our competition.
          Since we opened our doors, our goal has been to continually affirm and
          expand our reputation as “one of the best” in the market.
        </p>
      </div>
      <div class="container row text-center">
        <h2 class="color">Services</h2>
        <div class="card" style="width: 20rem">
          <img
            src="@/assets/transportation.jpg"
            class="card-img-top"
            alt="..."
            width="1000"
            height="200"
          />
          <div class="card-body">
            <h5 class="card-title">Transportation</h5>
            <p class="card-text">
              Our depth of experience moving cargo to and from Southern
              California ports, businesses and warehouses, make us uniquely
              qualified to move your goods through the complexities of the
              region and beyond. Owning our own assets – our fleet and our
              warehouses – distinguishes us from other transportation companies.
              This ownership gives us control at every stage to ensure the
              reliability you have come to expect from Supra.
            </p>
          </div>
        </div>
        <div class="card" style="width: 20rem">
          <img
            src="@/assets/distribucion.jpg"
            class="card-img-top"
            alt="..."
            width="1000"
            height="200"
          />
          <div class="card-body">
            <h5 class="card-title">Distribution</h5>
            <p class="card-text">
              In 2017 our aggressive growth strategy included broadening our
              service offerings by investing in warehousing facilities.
              Distribution by Supra offers you the perfect no-hassle solution,
              from storing your cargo or freight, to pick and pack and handling
              its delivery. Our facilities are located near transport hubs for
              ease of access and a more cost efficient solution for you. Our
              state-of-the-art warehousing facilities offer both contract
              warehousing with dedicated space and support and public
              warehousing for last minute needs, overflow or seasonal
              inventories. Learn more about our warehousing services and how
              they can meet your needs.
            </p>
          </div>
        </div>
        <div class="card" style="width: 20rem">
          <img
            src="@/assets/logistica.jpg"
            class="card-img-top"
            alt="..."
            width="1000"
            height="200"
          />
          <div class="card-body">
            <h5 class="card-title">Logistics</h5>
            <p class="card-text">
              Deep experience and expertise in transportation, shipping and
              warehousing plus investment in leading logistics software make
              Supra a best-in-class logistics provider. Whether it is navigating
              the complexities of international shipping, North America land
              based transportation or drayage, we will customize a solution to
              meet the needs of your business. At Supra, our goals are aligned
              with those of your business, safe, cost-effective, reliable
              shipping and handling of your goods and freight.
            </p>
          </div>
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
</style>