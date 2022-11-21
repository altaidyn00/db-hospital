<template>
  <div class="d-flex flex-column p-4">
    <div class="large-font text-white font-weight-bold text-center mt-4">Countries</div>
    <div class="my-4">
      <b-button id="show-btn" @click="$bvModal.show('bv-modal-create')"
        >create</b-button
      >

      <b-modal id="bv-modal-create" hide-footer>
        <div>Create country</div>
        <b-form-input
          v-model="cname"
          class="mb-2 mt-2"
          placeholder="Enter name"
        ></b-form-input>
        <b-form-input
          v-model="population"
          placeholder="Enter population"
        ></b-form-input>
        <b-button class="mt-3" block @click="create">submit</b-button>
      </b-modal>
      <b-modal id="bv-modal-update" hide-footer>
        <div>Update country</div>
        <b-form-input
          v-model="cname"
          class="mb-2 mt-2"
          placeholder="Enter name"
        ></b-form-input>
        <b-form-input
          v-model="population"
          placeholder="Enter population"
        ></b-form-input>
        <b-button class="mt-3" block @click="update">submit</b-button>
      </b-modal>
    </div>
    <b-table
      class="custom-border"
      table-class="table table-centered w-100"
      thead-tr-class="bg-light"
      tbody-tr-class="bg-light"
      :items="countries.countries"
      :fields="fields"
      :bordered="true"
      :fixed="true"
      responsive="sm"
    >
      <template #cell(cname)="data">
        {{ data.item.cname }}
      </template>
      <template #cell(population)="data">
        {{ data.item.population }}
      </template>
      <template #cell(action1)="data">
        <div class="font-weight-bold action-button" @click="set(data.item)">
          update
        </div>
      </template>
      <template #cell(action2)="data">
        <div class="font-weight-bold action-button" @click="remove(data.item)">
          delete
        </div>
      </template>
    </b-table>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "Countries",
  async asyncData({ store }) {
    await store.dispatch("crud/get_countries");
  },
  data() {
    return {
      cname: null,
      population: null,
      fields: [
        { key: "cname", label: "Name" },
        { key: "population", label: "Population" },
        { key: "action1", label: "" },
        { key: "action2", label: "" },
      ],
    };
  },
  computed: {
    ...mapGetters({
      countries: "crud/countries",
    }),
  },
  methods: {
    async set(data) {
      this.cname = data.cname;
      this.population = +data.population;
      this.$bvModal.show("bv-modal-update");
    },
    async create() {
      const payload = {};
      payload.cname = this.cname;
      payload.population = +this.population;
      await this.$store.dispatch("crud/create_country", payload);
      await this.$store.dispatch("crud/get_countries");
      this.$bvModal.hide("bv-modal-create");
      this.cname = null;
      this.population = null;
    },
    async update() {
      await this.$store.dispatch("crud/update_country", {
        cname: this.cname,
        payload: { cname: this.cname, population: this.population },
      });
      await this.$store.dispatch("crud/get_countries");
      this.$bvModal.hide("bv-modal-update");
    },
    async remove(item) {
      const cname = item.cname;
      await this.$store.dispatch("crud/delete_country", cname);
      await this.$store.dispatch("crud/get_countries");
    },
  },
};
</script>

<style lang="scss">
.large-font {
  font-size: 50px;
}

.action-button:hover {
  cursor: pointer;
  color: #35ca62;
}

.btn {
  background-color: black;
  border-color: black;
}

.btn:hover {
  background-color: #35ca62;
  border-color: #35ca62;
}

.custom-border .table .rowgroup .hover {
  background-color: white !important;
  background: white !important;
}
</style>
