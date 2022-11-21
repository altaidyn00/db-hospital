<template>
  <div>
    <b-navbar toggleable="lg" class="header-custom">
      <b-navbar-brand @click="$router.push('/')" :style="{ color: 'white' }"
        >Assignment 2</b-navbar-brand
      >

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item-dropdown class="CRUD-dropdown" text="CRUD" right>
            <b-dropdown-item @click="$router.push('/disease-types')">Disease types</b-dropdown-item>
            <b-dropdown-item @click="$router.push('/countries')">Countries</b-dropdown-item>
            <b-dropdown-item @click="$router.push('/diseases')">Diseases</b-dropdown-item>
            <b-dropdown-item @click="$router.push('/discovers')">Discovers</b-dropdown-item>
            <b-dropdown-item @click="$router.push('/users')">Users</b-dropdown-item>
            <b-dropdown-item @click="$router.push('/public-servants')"
              >Public servants</b-dropdown-item
            >
            <b-dropdown-item @click="$router.push('/doctors')">Doctors</b-dropdown-item>
            <b-dropdown-item @click="$router.push('/specializes')">Specializes</b-dropdown-item>
            <b-dropdown-item @click="$router.push('/records')">Records</b-dropdown-item>
          </b-nav-item-dropdown></b-navbar-nav
        >
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: "Header",
};
</script>

<style scoped lang="scss">
.header {
  width: 100%;
  position: absolute;
  z-index: 1;
}

.header-custom {
  background-color: #ca8167;
  background: #ca8167;
}

.CRUD-dropdown > .nav-link {
  color: white !important;
}
</style>
