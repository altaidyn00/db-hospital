<template>
  <div class="d-flex flex-column p-4">
    <div class="large-font text-white font-weight-bold text-center mt-4">
      Specializes
    </div>
    <div class="my-4">
      <b-button id="show-btn" @click="$bvModal.show('bv-modal-create')"
        >create</b-button
      >

      <b-modal id="bv-modal-create" hide-footer>
        <div>Create specialize</div>
        <b-form-input
          v-model="email"
          class="mb-2 mt-2"
          placeholder="Enter email"
        ></b-form-input>
        <b-form-input
          v-model="id"
          placeholder="Enter disease type id"
        ></b-form-input>
        <b-button class="mt-3" block @click="create">submit</b-button>
      </b-modal>
      <b-modal id="bv-modal-update" hide-footer>
        <div>Update doctor</div>
        <b-form-input
          v-model="email"
          class="mb-2 mt-2"
          placeholder="Enter email"
        ></b-form-input>
        <b-form-input
          v-model="id"
          placeholder="Enter disease type id"
        ></b-form-input>
        <b-button class="mt-3" block @click="update">submit</b-button>
      </b-modal>
    </div>
    <b-table
      class="custom-border"
      table-class="table table-centered w-100"
      thead-tr-class="bg-light"
      tbody-tr-class="hover"
      :items="specializes.specializes"
      :fields="fields"
      :bordered="true"
      :fixed="true"
      responsive="sm"
    >
      <template #cell(email)="data">
        {{ data.item.email }}
      </template>
      <template #cell(id)="data">
        {{ data.item.id }}
      </template>
      <template #cell(action1)="data">
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
  name: "Specialize",
  async asyncData({ store }) {
    await store.dispatch("crud/get_specializes");
  },
  data() {
    return {
      email: null,
      id: null,
      fields: [
        { key: "email", label: "Email" },
        { key: "id", label: "Disease type id" },
        { key: "action1", label: "" },
      ],
    };
  },
  computed: {
    ...mapGetters({
      specializes: "crud/specializes",
    }),
  },
  methods: {
    async set(data) {
      this.email = data.email;
      this.id = data.id;
      this.$bvModal.show("bv-modal-update");
    },
    async create() {
      const payload = {};
      payload.email = this.email;
      payload.id = this.id;
      await this.$store.dispatch("crud/create_specialize", payload);
      await this.$store.dispatch("crud/get_specializes");
      this.$bvModal.hide("bv-modal-create");
      this.email = null;
      this.id = null;
    },
    async remove(data) {
      const email = data.email;
      const id = data.id;
      await this.$store.dispatch("crud/delete_specialize", { email, id });
      await this.$store.dispatch("crud/get_specializes");
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
