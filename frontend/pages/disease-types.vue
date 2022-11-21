<template>
  <div class="d-flex flex-column p-4">
    <div class="large-font text-white font-weight-bold text-center mt-4">
      Disease types
    </div>
    <div class="my-4">
      <b-button id="show-btn" @click="$bvModal.show('bv-modal-create')"
        >create</b-button
      >

      <b-modal id="bv-modal-create" hide-footer>
        <div>Create disease type</div>
        <b-form-input
          v-model="description"
          class="mt-2"
          placeholder="Enter description"
        ></b-form-input>
        <b-button class="mt-3" block @click="create">submit</b-button>
      </b-modal>
      <b-modal id="bv-modal-update" hide-footer>
        <div>Update disease type</div>
        <b-form-input
          v-model="description"
          class="mt-2"
          placeholder="Enter description"
        ></b-form-input>
        <b-button class="mt-3" block @click="update">submit</b-button>
      </b-modal>
    </div>
    <b-table
      class="custom-border"
      table-class="table table-centered w-100"
      thead-tr-class="bg-light"
      tbody-tr-class="hover"
      :items="diseaseTypes.disease_types"
      :fields="fields"
      :bordered="true"
      :fixed="true"
      responsive="sm"
    >
      <template #cell(id)="data">
        {{ data.item.id }}
      </template>
      <template #cell(description)="data">
        {{ data.item.description }}
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
  name: "Disease types",
  async asyncData({ store }) {
    await store.dispatch("crud/get_disease_types");
  },
  data() {
    return {
      id: null,
      description: null,
      fields: [
        { key: "id", label: "ID" },
        { key: "description", label: "Description" },
        { key: "action1", label: "" },
        { key: "action2", label: "" },
      ],
    };
  },
  computed: {
    ...mapGetters({
      diseaseTypes: "crud/diseaseTypes",
    }),
  },
  methods: {
    async set(data) {
      this.id = data.id;
      this.description = data.description;
      this.$bvModal.show("bv-modal-update");
    },
    async create() {
      const payload = {};
      payload.id = +this.id;
      payload.description = this.description;
      await this.$store.dispatch("crud/create_disease_type", payload);
      await this.$store.dispatch("crud/get_disease_types");
      this.$bvModal.hide("bv-modal-create");
      this.id = null;
      this.description = null;
    },
    async update() {
      await this.$store.dispatch("crud/update_disease_type", {
        id: this.id,
        payload: { description: this.description },
      });
      await this.$store.dispatch("crud/get_disease_types");
      this.$bvModal.hide("bv-modal-update");
    },
    async remove(item) {
      const id = item.id;
      await this.$store.dispatch("crud/delete_disease_type", id);
      await this.$store.dispatch("crud/get_disease_types");
    },
  },
};
</script>

<style scoped lang="scss">
.large-font {
  font-size: 50px;
}

.action-button {
  color: white;
}

.action-button:hover {
  cursor: pointer;
  color: blue;
}
</style>
