export default {
  // Disable server-side rendering: https://go.nuxtjs.dev/ssr-mode
  mode: "spa",
  // ssr: true,
  target: "server",
  server: {
    host: "0.0.0.0",
  },
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: "db-front",
    htmlAttrs: {
      lang: "en",
    },
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: "" },
      { name: "format-detection", content: "telephone=no" },
    ],
    link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" }],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    { src: "~/plugins/vuelidate" },
    { src: "~/plugins/repository" },
    { src: "~/plugins/toast" },
    { src: "~/plugins/vue-particles", mode: "client" },
  ],
  axios: {
    proxy: true,
  },
  proxy: {
    "/api": {
      target:
        process.env.NODE_ENV === "production" ? "" : "http://localhost:8000",
      pathRewrite: { "^/api": "/api" },
    },
  },

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    "bootstrap-vue/nuxt",
    "@nuxtjs/axios",
  ],

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},
};
