import CRUD from "~/repositories/CRUD";

export default $axios => ({
    crud: CRUD($axios),
});