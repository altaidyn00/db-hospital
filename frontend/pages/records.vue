<template>
  <div class="d-flex flex-column p-4">
    <div class="large-font text-white font-weight-bold text-center mt-4">
      Records
    </div>
    <div class="my-4">
      <b-button id="show-btn" @click="$bvModal.show('bv-modal-create')"
        >create</b-button
      >

      <b-modal id="bv-modal-create" hide-footer>
        <div>Create record</div>
        <b-form-input
          v-model="email"
          class="mb-2 mt-2"
          placeholder="Enter email"
        ></b-form-input>
        <b-form-input
          v-model="disease_code"
          class="mb-2"
          placeholder="Enter disease code"
        ></b-form-input>
        <b-form-input
          v-model="cname"
          class="mb-2"
          placeholder="Enter country"
        ></b-form-input>
        <b-form-input
          v-model="total_deaths"
          class="mb-2"
          placeholder="Enter total deaths"
        ></b-form-input>
        <b-form-input
          v-model="total_patients"
          placeholder="Enter total patients"
        ></b-form-input>
        <b-button class="mt-3" block @click="create">submit</b-button>
      </b-modal>
      <b-modal id="bv-modal-update" hide-footer>
        <div>Update record</div>
        <b-form-input
          v-model="total_deaths"
          class="mb-2"
          placeholder="Enter total deaths"
        ></b-form-input>
        <b-form-input
          v-model="total_patients"
          placeholder="Enter total patients"
        ></b-form-input>
        <b-button class="mt-3" block @click="update">submit</b-button>
      </b-modal>
    </div>
    <b-table
      class="custom-border"
      table-class="table table-centered w-100"
      thead-tr-class="bg-light"
      tbody-tr-class="bg-light"
      :items="records.records"
      :fields="fields"
      :bordered="true"
      :fixed="true"
      responsive="sm"
    >
      <template #cell(email)="data">
        {{ data.item.email }}
      </template>
      <template #cell(disease_code)="data">
        {{ data.item.disease_code }}
      </template>
      <template #cell(cname)="data">
        {{ data.item.cname }}
      </template>
      <template #cell(total_deaths)="data">
        {{ data.item.total_deaths }}
      </template>
      <template #cell(total_patients)="data">
        {{ data.item.total_patients }}
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
  name: "Records",
  async asyncData({ store }) {
    await store.dispatch("crud/get_records");
  },
  data() {
    return {
      email: null,
      disease_code: null,
      cname: null,
      total_deaths: null,
      total_patients: null,
      fields: [
        { key: "email", label: "Email" },
        { key: "disease_code", label: "Disease code" },
        { key: "cname", label: "Country" },
        { key: "total_deaths", label: "Total deaths" },
        { key: "total_patients", label: "Total patients" },
        { key: "action1", label: "" },
        { key: "action2", label: "" },
      ],
    };
  },
  computed: {
    ...mapGetters({
      records: "crud/records",
    }),
  },
  methods: {
    async set(data) {
      this.email = data.email;
      this.cname = data.cname;
      this.disease_code = data.disease_code;
      this.total_deaths = +data.total_deaths;
      this.total_patients = +data.total_patients;
      this.$bvModal.show("bv-modal-update");
    },
    async create() {
      const payload = {};
      payload.email = this.email;
      payload.cname = this.cname;
      payload.disease_code = this.disease_code;
      payload.total_deaths = +this.total_deaths;
      payload.total_patients = +this.total_patients;
      await this.$store.dispatch("crud/create_record", payload);
      await this.$store.dispatch("crud/get_records");
      this.$bvModal.hide("bv-modal-create");
      this.email = null;
      this.cname = null;
      this.disease_code = null;
      this.total_deaths = null;
      this.total_patients = null;
    },
    async update() {
      await this.$store.dispatch("crud/update_record", {
        email: this.email,
        cname: this.cname,
        disease_code: this.disease_code,
        payload: {
          email: this.email,
          cname: this.cname,
          disease_code: this.disease_code,
          total_deaths: +this.total_deaths,
          total_patients: +this.total_patients,
        },
      });
      await this.$store.dispatch("crud/get_records");
      this.$bvModal.hide("bv-modal-update");
    },
    async remove(data) {
      const email = data.email;
      const cname = data.cname;
      const disease_code = data.disease_code;
      await this.$store.dispatch("crud/delete_record", {
        email,
        cname,
        disease_code,
      });
      await this.$store.dispatch("crud/get_records");
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