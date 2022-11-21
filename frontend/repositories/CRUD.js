export default ($axios) => ({
  create_doctor(payload) {
    return $axios.post("/api/v1/doctors", payload);
  },

  update_doctor(email, payload) {
    return $axios.put(`/api/v1/doctors/${email}`, payload);
  },

  delete_doctor(email) {
    return $axios.delete(`/api/v1/doctors/${email}`);
  },

  get_doctors() {
    return $axios.get("/api/v1/doctors");
  },

  create_country(payload) {
    return $axios.post("/api/v1/countries", payload);
  },

  update_country(cname, payload) {
    return $axios.put(`/api/v1/countries/${cname}`, payload);
  },

  delete_country(cname) {
    return $axios.delete(`/api/v1/countries/${cname}`);
  },

  get_countries() {
    return $axios.get("/api/v1/countries");
  },

  create_discovery(payload) {
    return $axios.post("/api/v1/discoveries", payload);
  },

  update_discovery(disease_code, cname, payload) {
    return $axios.put(`/api/v1/discoveries/${disease_code}/${cname}`, payload);
  },

  delete_discovery(disease_code, cname) {
    return $axios.delete(`/api/v1/discoveries/${disease_code}/${cname}`);
  },

  get_discoveries() {
    return $axios.get("/api/v1/discoveries");
  },

  create_disease_type(payload) {
    return $axios.post("/api/v1/disease_types", payload);
  },

  update_disease_type(id, payload) {
    return $axios.put(`/api/v1/disease_types/${id}`, payload);
  },

  delete_disease_type(id) {
    return $axios.delete(`/api/v1/disease_types/${id}`);
  },

  get_disease_types() {
    return $axios.get("/api/v1/disease_types");
  },

  create_disease(payload) {
    return $axios.post("/api/v1/diseases", payload);
  },

  update_disease(disease_code, payload) {
    return $axios.put(`/api/v1/diseases/${disease_code}`, payload);
  },

  delete_disease(disease_code) {
    return $axios.delete(`/api/v1/diseases/${disease_code}`);
  },

  get_diseases() {
    return $axios.get("/api/v1/diseases");
  },

  create_public_servant(payload) {
    return $axios.post("/api/v1/public_servants", payload);
  },

  update_public_servant(email, payload) {
    return $axios.put(`/api/v1/public_servants/${email}`, payload);
  },

  delete_public_servant(email) {
    return $axios.delete(`/api/v1/public_servants/${email}`);
  },

  get_public_servants() {
    return $axios.get("/api/v1/public_servants");
  },

  create_record(payload) {
    return $axios.post("/api/v1/records", payload);
  },

  update_record(email, cname, disease_code, payload) {
    return $axios.put(
      `/api/v1/records/${email}/${cname}/${disease_code}`,
      payload
    );
  },

  delete_record(email, cname, disease_code) {
    return $axios.delete(`/api/v1/records/${email}/${cname}/${disease_code}`);
  },

  get_records() {
    return $axios.get("/api/v1/records");
  },

  create_specialize(payload) {
    return $axios.post("/api/v1/specializes", payload);
  },

  delete_specialize(email, id) {
    return $axios.delete(`/api/v1/specializes/${email}/${id}`);
  },

  get_specializes() {
    return $axios.get("/api/v1/specializes");
  },

  create_user(payload) {
    return $axios.post("/api/v1/users", payload);
  },

  update_user(email, payload) {
    return $axios.put(`/api/v1/users/${email}`, payload);
  },

  delete_user(email) {
    return $axios.delete(`/api/v1/users/${email}`);
  },

  get_users() {
    return $axios.get("/api/v1/users");
  },
});
