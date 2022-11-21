<template>
  <div class="d-flex flex-column p-4">
    <div class="large-font text-white font-weight-bold text-center mt-4">
      Public servants
    </div>
    <div class="my-4">
      <b-button id="show-btn" @click="$bvModal.show('bv-modal-create')"
        >create</b-button
      >

      <b-modal id="bv-modal-create" hide-footer>
        <div>Create public servant</div>
        <b-form-input v-model="email" class="mb-2 mt-2" placeholder="Enter email"></b-form-input>
        <b-form-input
          v-model="department"
          placeholder="Enter department"
        ></b-form-input>
        <b-button class="mt-3" block @click="create">submit</b-button>
      </b-modal>
      <b-modal id="bv-modal-update" hide-footer>
        <div>Update public servant</div>
        <b-form-input v-model="email" class="mb-2 mt-2" placeholder="Enter email"></b-form-input>
        <b-form-input
          v-model="department"
          placeholder="Enter department"
        ></b-form-input>
        <b-button class="mt-3" block @click="update">submit</b-button>
      </b-modal>
    </div>
    <b-table
      class="custom-border"
      table-class="table table-centered w-100"
      thead-tr-class="bg-light"
      tbody-tr-class="hover"
      :items="publicServants.public_servants"
      :fields="fields"
      :bordered="true"
      :fixed="true"
      responsive="sm"
    >
      <template #cell(email)="data">
        {{ data.item.email }}
      </template>
      <template #cell(department)="data">
        {{ data.item.department }}
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
import { mapGetters } from "vuex";
export default {
  name: "Public servant",
  async asyncData({ store }) {
    await store.dispatch("crud/get_public_servants");
  },
  data() {
    return {
      email: null,
      department: null,
      fields: [
        { key: "email", label: "Email" },
        { key: "department", label: "Department" },
        { key: "action1", label: "" },
        { key: "action2", label: "" },
      ],
    };
  },
  computed: {
    ...mapGetters({
      publicServants: "crud/publicServants",
    }),
  },
  methods: {
    async set(data) {
      this.email = data.email;
      this.department = data.department;
      this.$bvModal.show("bv-modal-update");
    },
    async create() {
      const payload = {};
      payload.email = this.email;
      payload.department = this.department;
      await this.$store.dispatch("crud/create_public_servant", payload);
      await this.$store.dispatch("crud/get_public_servants");
      this.$bvModal.hide("bv-modal-create");
      this.email = null;
      this.department = null;
    },
    async update() {
      await this.$store.dispatch("crud/update_public_servant", {
        email: this.email,
        payload: { email: this.email, department: this.department },
      });
      await this.$store.dispatch("crud/get_public_servants");
      this.$bvModal.hide("bv-modal-update");
    },
    async remove(data) {
      const email = data.email;
      await this.$store.dispatch("crud/delete_public_servant", email);
      await this.$store.dispatch("crud/get_public_servants");
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
