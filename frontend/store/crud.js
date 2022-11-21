export const state = () => ({
  countries: [],
  discovers: [],
  diseaseTypes: [],
  diseases: [],
  doctors: [],
  publicServants: [],
  records: [],
  specializes: [],
  users: [],
});

export const getters = {
  countries(state) {
    return state.countries;
  },
  discovers(state) {
    return state.discovers;
  },
  diseaseTypes(state) {
    return state.diseaseTypes;
  },
  diseases(state) {
    return state.diseases;
  },
  doctors(state) {
    return state.doctors;
  },
  publicServants(state) {
    return state.publicServants;
  },
  records(state) {
    return state.records;
  },
  specializes(state) {
    return state.specializes;
  },
  users(state) {
    return state.users;
  },
};

export const mutations = {
  SET_COUNTRIES(state, countries) {
    state.countries = countries;
  },
  SET_DISCOVERS(state, discovers) {
    state.discovers = discovers;
  },
  SET_DISEASE_TYPES(state, diseaseTypes) {
    state.diseaseTypes = diseaseTypes;
  },
  SET_DISEASES(state, diseases) {
    state.diseases = diseases;
  },
  SET_DOCTORS(state, doctors) {
    state.doctors = doctors;
  },
  SET_PUBLIC_SERVANTS(state, publicServants) {
    state.publicServants = publicServants;
  },
  SET_RECORDS(state, records) {
    state.records = records;
  },
  SET_SPECIALIZES(state, specializes) {
    state.specializes = specializes;
  },
  SET_USERS(state, users) {
    state.users = users;
  },
};

export const actions = {
  async create_doctor(_, payload) {
    try {
      const response = await this.$repositories.crud.create_doctor(payload);
      this._vm.$bvToast.toast("Doctor successfully created!", {
        title: "Doctor",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during doctor creating.", {
        title: "Doctor",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async update_doctor(_, { email, payload }) {
    try {
      const response = await this.$repositories.crud.update_doctor(
        email,
        payload
      );
      this._vm.$bvToast.toast("Doctor successfully updated!", {
        title: "Doctor",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during doctor updating.", {
        title: "Doctor",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async delete_doctor(_, email) {
    try {
      const response = await this.$repositories.crud.delete_doctor(email);
      this._vm.$bvToast.toast("Doctor successfully deleted!", {
        title: "Doctor",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during doctor deleting.", {
        title: "Doctor",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async get_doctors({ commit }, params) {
    try {
      const response = await this.$repositories.crud.get_doctors(params);
      commit("SET_DOCTORS", response.data);
    } catch (error) {}
  },

  async create_country(_, payload) {
    try {
      const response = await this.$repositories.crud.create_country(payload);
      this._vm.$bvToast.toast("Country successfully created!", {
        title: "Country",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during country creating.", {
        title: "Country",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async update_country(_, { cname, payload }) {
    try {
      const response = await this.$repositories.crud.update_country(
        cname,
        payload
      );
      this._vm.$bvToast.toast("Country successfully updated!", {
        title: "Country",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during country updating.", {
        title: "Country",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async delete_country(_, cname) {
    try {
      const response = await this.$repositories.crud.delete_country(cname);
      this._vm.$bvToast.toast("Country successfully deleted!", {
        title: "Country",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during country deleting.", {
        title: "Country",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async get_countries({ commit }, params) {
    try {
      const response = await this.$repositories.crud.get_countries(params);
      commit("SET_COUNTRIES", response.data);
    } catch (error) {}
  },

  async create_discovery(_, payload) {
    try {
      const response = await this.$repositories.crud.create_discovery(payload);
      this._vm.$bvToast.toast("Discover successfully created!", {
        title: "Discover",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during discover creating.", {
        title: "Discover",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async update_discovery(_, { disease_code, cname, payload }) {
    try {
      const response = await this.$repositories.crud.update_discovery(
        disease_code,
        cname,
        payload
      );
      this._vm.$bvToast.toast("Discover successfully updated!", {
        title: "Discover",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during discover updating.", {
        title: "Discover",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async delete_discovery(_, { disease_code, cname }) {
    try {
      const response = await this.$repositories.crud.delete_discovery(
        disease_code,
        cname
      );
      this._vm.$bvToast.toast("Discover successfully deleted!", {
        title: "Discover",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during discover deleting.", {
        title: "Discover",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async get_discoveries({ commit }, params) {
    try {
      const response = await this.$repositories.crud.get_discoveries(params);
      commit("SET_DISCOVERS", response.data);
    } catch (error) {}
  },

  async create_disease_type(_, payload) {
    try {
      const response = await this.$repositories.crud.create_disease_type(
        payload
      );
      this._vm.$bvToast.toast("Disease type successfully created!", {
        title: "Disease type",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during disease type creating.", {
        title: "Disease type",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async update_disease_type(_, { id, payload }) {
    try {
      const response = await this.$repositories.crud.update_disease_type(
        id,
        payload
      );
      this._vm.$bvToast.toast("Disease type successfully updated!", {
        title: "Disease type",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during disease type updating.", {
        title: "Disease type",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async delete_disease_type(_, id) {
    try {
      const response = await this.$repositories.crud.delete_disease_type(id);
      this._vm.$bvToast.toast("Disease type successfully deleted!", {
        title: "Disease type",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during disease type deleting.", {
        title: "Disease type",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async get_disease_types({ commit }, params) {
    try {
      const response = await this.$repositories.crud.get_disease_types(params);
      commit("SET_DISEASE_TYPES", response.data);
    } catch (error) {}
  },

  async create_disease(_, payload) {
    try {
      const response = await this.$repositories.crud.create_disease(payload);
      this._vm.$bvToast.toast("Disease successfully created!", {
        title: "Disease",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during disease creating.", {
        title: "Disease",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async update_disease(_, { disease_code, payload }) {
    try {
      const response = await this.$repositories.crud.update_disease(
        disease_code,
        payload
      );
      this._vm.$bvToast.toast("Disease successfully updated!", {
        title: "Disease",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during disease updating.", {
        title: "Disease",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async delete_disease(_, disease_code) {
    try {
      const response = await this.$repositories.crud.delete_disease(
        disease_code
      );
      this._vm.$bvToast.toast("Disease successfully deleted!", {
        title: "Disease",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during disease deleting.", {
        title: "Disease",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async get_diseases({ commit }, params) {
    try {
      const response = await this.$repositories.crud.get_diseases(params);
      commit("SET_DISEASES", response.data);
    } catch (error) {}
  },

  async create_public_servant(_, payload) {
    try {
      const response = await this.$repositories.crud.create_public_servant(
        payload
      );
      this._vm.$bvToast.toast("Public servant successfully created!", {
        title: "Public servant",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during public servant creating.", {
        title: "Public servant",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async update_public_servant(_, { email, payload }) {
    try {
      const response = await this.$repositories.crud.update_public_servant(
        email,
        payload
      );
      this._vm.$bvToast.toast("Public servant successfully updated!", {
        title: "Public servant",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during public servant updating.", {
        title: "Public servant",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async delete_public_servant(_, email) {
    try {
      const response = await this.$repositories.crud.delete_public_servant(
        email
      );
      this._vm.$bvToast.toast("Public servant successfully deleted!", {
        title: "Public servant",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during public servant deleting.", {
        title: "Public servant",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async get_public_servants({ commit }, params) {
    try {
      const response = await this.$repositories.crud.get_public_servants(
        params
      );
      commit("SET_PUBLIC_SERVANTS", response.data);
    } catch (error) {}
  },

  async create_record(_, payload) {
    try {
      const response = await this.$repositories.crud.create_record(payload);
      this._vm.$bvToast.toast("Record successfully created!", {
        title: "Record",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during record creating.", {
        title: "Record",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async update_record(_, { email, cname, disease_code, payload }) {
    try {
      const response = await this.$repositories.crud.update_record(
        email,
        cname,
        disease_code,
        payload
      );
      this._vm.$bvToast.toast("Record successfully updated!", {
        title: "Record",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during record updating.", {
        title: "Record",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async delete_record(_, { email, cname, disease_code }) {
    try {
      const response = await this.$repositories.crud.delete_record(
        email,
        cname,
        disease_code
      );
      this._vm.$bvToast.toast("DocRecordtor successfully deleted!", {
        title: "Record",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during record deleting.", {
        title: "Record",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async get_records({ commit }, params) {
    try {
      const response = await this.$repositories.crud.get_records(params);
      commit("SET_RECORDS", response.data);
    } catch (error) {}
  },

  async create_specialize(_, payload) {
    try {
      const response = await this.$repositories.crud.create_specialize(payload);
      this._vm.$bvToast.toast("Specialize successfully created!", {
        title: "Specialize",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during specialize creating.", {
        title: "Specialize",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async delete_specialize(_, { email, id }) {
    try {
      const response = await this.$repositories.crud.delete_specialize(
        email,
        id
      );
      this._vm.$bvToast.toast("Specialize successfully deleted!", {
        title: "Specialize",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during specialize deleting.", {
        title: "Specialize",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async get_specializes({ commit }, params) {
    try {
      const response = await this.$repositories.crud.get_specializes(params);
      commit("SET_SPECIALIZES", response.data);
    } catch (error) {}
  },

  async create_user(_, payload) {
    try {
      const response = await this.$repositories.crud.create_user(payload);
      this._vm.$bvToast.toast("User successfully created!", {
        title: "User",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during user creating.", {
        title: "User",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async update_user(_, { email, payload }) {
    try {
      const response = await this.$repositories.crud.update_user(
        email,
        payload
      );
      this._vm.$bvToast.toast("User successfully updated!", {
        title: "User",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during user updating.", {
        title: "User",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async delete_user(_, email) {
    try {
      const response = await this.$repositories.crud.delete_user(email);
      this._vm.$bvToast.toast("User successfully deleted!", {
        title: "User",
        toaster: "b-toaster-bottom-left",
        variant: "success",
        solid: true,
      });
      return response.data;
    } catch (error) {
      this._vm.$bvToast.toast("Error occured during user deleting.", {
        title: "User",
        toaster: "b-toaster-bottom-left",
        variant: "danger",
        solid: true,
      });
    }
  },

  async get_users({ commit }, params) {
    try {
      const response = await this.$repositories.crud.get_users(params);
      commit("SET_USERS", response.data);
    } catch (error) {}
  },
};
