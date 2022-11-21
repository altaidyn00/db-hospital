<template>
  <div>
    <Header />
    <div class="particles-background d-flex flex-column">
      <Nuxt class="nuxt-page" />
      <vue-particles
        color="#44EE77"
        :particleOpacity="0.7"
        linesColor="#44EE77"
        :particlesNumber="50"
        shapeType="circle"
        :particleSize="7"
        :linesWidth="3"
        :lineLinked="true"
        :lineOpacity="0.4"
        :linesDistance="250"
        :moveSpeed="4"
        :clickEffect="false"
        id="particles-js"
      >
      </vue-particles>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped lang="scss">
.nuxt-page {
  min-height: 100vh !important;
  align-items: center;
  z-index: 1;
}

.particles-background {
  justify-content: center;
}

.particles-background #particles-js {
  height: 100%;
  width: 100%;
  background-color: #ca8167 !important;
  position: absolute;
}
</style>
