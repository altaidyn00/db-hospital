<template>
  <div class="d-flex flex-column p-4">
    <div class="large-font text-white font-weight-bold text-center mt-4">Diseases</div>
    <div class="my-4">
      <b-button id="show-btn" @click="$bvModal.show('bv-modal-create')"
        >create</b-button
      >

      <b-modal id="bv-modal-create" hide-footer>
        <div>Create disease</div>
        <b-form-input
          v-model="disease_code"
          class="mb-2 mt-2"
          placeholder="Enter disease_code"
        ></b-form-input>
        <b-form-input
          v-model="description"
          class="mb-2"
          placeholder="Enter description"
        ></b-form-input>
        <b-form-input
          v-model="id"
          class="mb-2"
          placeholder="Enter id"
        ></b-form-input>
        <b-form-input
          v-model="pathogen"
          placeholder="Enter pathogen"
        ></b-form-input>
        <b-button class="mt-3" block @click="create">submit</b-button>
      </b-modal>
      <b-modal id="bv-modal-update" hide-footer>
        <div>Update disease</div>
        <b-form-input
          v-model="disease_code"
          class="mb-2 mt-2"
          placeholder="Enter disease code"
        ></b-form-input>
        <b-form-input
          v-model="description"
          class="mb-2"
          placeholder="Enter description"
        ></b-form-input>
        <b-form-input
          v-model="id"
          class="mb-2"
          placeholder="Enter id"
        ></b-form-input>
        <b-form-input
          v-model="pathogen"
          placeholder="Enter pathogen"
        ></b-form-input>
        <b-button class="mt-3" block @click="update">submit</b-button>
      </b-modal>
    </div>
    <b-table
      class="custom-border"
      table-class="table table-centered w-100"
      thead-tr-class="bg-light"
      tbody-tr-class="bg-light"
      :items="diseases.diseases"
      :fields="fields"
      :bordered="true"
      :fixed="true"
      responsive="sm"
    >
      <template #cell(disease_code)="data">
        {{ data.item.disease_code }}
      </template>
      <template #cell(description)="data">
        {{ data.item.description }}
      </template>
      <template #cell(pathogen)="data">
        {{ data.item.pathogen }}
      </template>
      <template #cell(id)="data">
        {{ data.item.id }}
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
  name: "Disease",
  async asyncData({ store }) {
    await store.dispatch("crud/get_diseases");
  },
  data() {
    return {
      disease_code: null,
      description: null,
      pathogen: null,
      id: null,
      fields: [
        { key: "disease_code", label: "Disease code" },
        { key: "description", label: "Description" },
        { key: "pathogen", label: "Pathogen" },
        { key: "id", label: "ID" },
        { key: "action1", label: "" },
        { key: "action2", label: "" },
      ],
    };
  },
  computed: {
    ...mapGetters({
      diseases: "crud/diseases",
    }),
  },
  methods: {
    async set(data) {
      this.disease_code = data.disease_code;
      this.description = data.description;
      this.pathogen = data.pathogen;
      this.id = +data.id;
      this.$bvModal.show("bv-modal-update");
    },
    async create() {
      const payload = {};
      payload.disease_code = this.disease_code;
      payload.description = this.description;
      payload.pathogen = this.pathogen;
      payload.id = +this.id;
      await this.$store.dispatch("crud/create_disease", payload);
      await this.$store.dispatch("crud/get_diseases");
      this.$bvModal.hide("bv-modal-create");
      this.disease_code = null;
      this.description = null;
      this.pathogen = null;
      this.id = null;
    },
    async update() {
      await this.$store.dispatch("crud/update_disease", {
        disease_code: this.disease_code,
        payload: {
          disease_code: this.disease_code,
          description: this.description,
          pathogen: this.pathogen,
          id: this.id,
        },
      });
      await this.$store.dispatch("crud/get_diseases");
      this.$bvModal.hide("bv-modal-update");
    },
    async remove(data) {
      const disease_code = data.disease_code;
      await this.$store.dispatch("crud/delete_disease", disease_code);
      await this.$store.dispatch("crud/get_diseases");
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
