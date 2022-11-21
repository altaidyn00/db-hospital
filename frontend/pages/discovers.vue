<template>
  <div class="d-flex flex-column p-4">
    <div class="large-font text-white font-weight-bold text-center mt-4">
      Discover
    </div>
    <div class="my-4">
      <b-button id="show-btn" @click="$bvModal.show('bv-modal-create')"
        >create</b-button
      >

      <b-modal id="bv-modal-create" hide-footer>
        <div>Create discover</div>
        <b-form-input
          class="mb-2 mt-2"
          v-model="disease_code"
          placeholder="Enter disease code"
        ></b-form-input>
        <b-form-input
          v-model="cname"
          class="mb-2"
          placeholder="Enter country name"
        ></b-form-input>
        <b-form-input
          v-model="first_enc_date"
          placeholder="Enter first encription date"
        ></b-form-input>
        <b-button class="mt-3" block @click="create">submit</b-button>
      </b-modal>
      <b-modal id="bv-modal-update" hide-footer>
        <div>Update discover</div>
        <b-form-input
          v-model="disease_code"
          class="mb-2 mt-2"
          placeholder="Enter disease code"
        ></b-form-input>
        <b-form-input
          v-model="cname"
          class="mb-2 mt-2"
          placeholder="Enter country name"
        ></b-form-input>
        <b-form-input
          v-model="first_enc_date"
          placeholder="Enter first encription date"
        ></b-form-input>
        <b-button class="mt-3" block @click="update">submit</b-button>
      </b-modal>
    </div>
    <b-table
      class="custom-border"
      table-class="table table-centered w-100"
      thead-tr-class="bg-light"
      tbody-tr-class="hover"
      :items="discovers.discoveries"
      :fields="fields"
      :bordered="true"
      :fixed="true"
      responsive="sm"
    >
      <template #cell(disease_code)="data">
        {{ data.item.disease_code }}
      </template>
      <template #cell(cname)="data">
        {{ data.item.cname }}
      </template>
      <template #cell(first_enc_date)="data">
        {{ data.item.first_enc_date }}
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
  name: "Discovers",
  async asyncData({ store }) {
    await store.dispatch("crud/get_discoveries");
  },
  data() {
    return {
      disease_code: null,
      cname: null,
      first_enc_date: null,
      fields: [
        { key: "disease_code", label: "Disease code" },
        { key: "cname", label: "Country" },
        { key: "first_enc_date", label: "First encription date" },
        { key: "action1", label: "" },
        { key: "action2", label: "" },
      ],
    };
  },
  computed: {
    ...mapGetters({
      discovers: "crud/discovers",
    }),
  },
  methods: {
    async set(data) {
      this.disease_code = data.disease_code;
      this.cname = data.cname;
      this.first_enc_date = data.first_enc_date;
      this.$bvModal.show("bv-modal-update");
    },
    async create() {
      const payload = {};
      payload.disease_code = this.disease_code;
      payload.cname = this.cname;
      payload.first_enc_date = this.first_enc_date;
      await this.$store.dispatch("crud/create_discovery", payload);
      await this.$store.dispatch("crud/get_discoveries");
      this.$bvModal.hide("bv-modal-create");
      this.disease_code = null;
      this.cname = null;
      this.first_enc_date = null;
    },
    async update() {
      await this.$store.dispatch("crud/update_discovery", {
        disease_code: this.disease_code,
        cname: this.cname,
        payload: this.payload,
      });
      await this.$store.dispatch("crud/get_discoveries");
      this.$bvModal.hide("bv-modal-update");
    },
    async remove(item) {
      await this.$store.dispatch("crud/delete_discovery", {
        disease_code: item.disease_code,
        cname: item.cname,
      });
      await this.$store.dispatch("crud/get_discoveries");
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
