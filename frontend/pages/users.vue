<template>
  <div class="d-flex flex-column p-4">
    <div class="large-font text-white font-weight-bold text-center mt-4">
      Users
    </div>
    <div class="my-4">
      <b-button id="show-btn" @click="$bvModal.show('bv-modal-create')"
        >create</b-button
      >

      <b-modal id="bv-modal-create" hide-footer>
        <div>Create user</div>
        <b-form-input
          v-model="name"
          class="mb-2"
          placeholder="Enter name"
        ></b-form-input>
        <b-form-input
          v-model="surname"
          class="mb-2"
          placeholder="Enter surname"
        ></b-form-input>
        <b-form-input
          v-model="email"
          class="mb-2"
          placeholder="Enter email"
        ></b-form-input>
        <b-form-input
          v-model="phone"
          class="mb-2"
          placeholder="Enter phone"
        ></b-form-input>
        <b-form-input
          v-model="salary"
          placeholder="Enter salary"
          class="mb-2"
        ></b-form-input>
        <b-form-input
          v-model="cname"
          placeholder="Enter country"
          class="mb-2"
        ></b-form-input>
        <b-button class="mt-3" block @click="create">submit</b-button>
      </b-modal>
      <b-modal id="bv-modal-update" hide-footer>
        <div>Update user</div>
        <b-form-input
          v-model="name"
          class="mb-2"
          placeholder="Enter name"
        ></b-form-input>
        <b-form-input
          v-model="surname"
          class="mb-2"
          placeholder="Enter surname"
        ></b-form-input>
        <b-form-input
          v-model="email"
          class="mb-2"
          placeholder="Enter email"
        ></b-form-input>
        <b-form-input
          v-model="phone"
          class="mb-2"
          placeholder="Enter phone"
        ></b-form-input>
        <b-form-input
          v-model="salary"
          placeholder="Enter salary"
          class="mb-2"
        ></b-form-input>
        <b-form-input
          v-model="cname"
          placeholder="Enter country"
          class="mb-2"
        ></b-form-input>
        <b-button class="mt-3" block @click="update">submit</b-button>
      </b-modal>
    </div>
    <b-table
      class="custom-border"
      table-class="table table-centered w-100"
      thead-tr-class="bg-light"
      tbody-tr-class="hover"
      :items="users.users"
      :fields="fields"
      :bordered="true"
      :fixed="true"
      responsive="sm"
    >
      <template #cell(name)="data">
        {{ data.item.name }}
      </template>
      <template #cell(surname)="data">
        {{ data.item.surname }}
      </template>
      <template #cell(email)="data">
        {{ data.item.email }}
      </template>
      <template #cell(phone)="data">
        {{ data.item.phone }}
      </template>
      <template #cell(salary)="data">
        {{ data.item.salary }}
      </template>
      <template #cell(cname)="data">
        {{ data.item.cname }}
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
  name: "Users",
  async asyncData({ store, params }) {
    await store.dispatch("crud/get_users");
  },
  data() {
    return {
      name: null,
      surname: null,
      email: null,
      phone: null,
      salary: null,
      cname: null,
      fields: [
        { key: "name", label: "Name" },
        { key: "surname", label: "Surname" },
        { key: "email", label: "Email" },
        { key: "phone", label: "Phone" },
        { key: "salary", label: "Salary" },
        { key: "salary", label: "Country" },
        { key: "action1", label: "" },
        { key: "action2", label: "" },
      ],
    };
  },
  computed: {
    ...mapGetters({
      users: "crud/users",
    }),
  },
  methods: {
    async set(data) {
      this.name = data.name;
      this.surname = data.surname;
      this.email = data.email;
      this.phone = data.phone;
      this.salary = +data.salary;
      this.cname = data.cname;
      this.$bvModal.show("bv-modal-update");
    },
    async create() {
      const payload = {};
      payload.name = this.name;
      payload.surname = this.surname;
      payload.email = this.email;
      payload.phone = this.phone;
      payload.salary = +this.salary;
      payload.cname = this.cname;
      await this.$store.dispatch("crud/create_user", payload);
      await this.$store.dispatch("crud/get_users");
      this.$bvModal.hide("bv-modal-create");
      this.name = null;
      this.surname = null;
      this.email = null;
      this.phone = null;
      this.salary = null;
      this.cname = null;
    },
    async update() {
      await this.$store.dispatch("crud/update_user", {
        email: this.email,
        payload: {
          name: this.name,
          surname: this.surname,
          email: this.email,
          phone: this.phone,
          salary: +this.salary,
          cname: this.cname,
        },
      });
      await this.$store.dispatch("crud/get_users");
      this.$bvModal.hide("bv-modal-update");
    },
    async remove(item) {
      const email = item.email;
      await this.$store.dispatch("crud/delete_user", email);
      await this.$store.dispatch("crud/get_users");
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
