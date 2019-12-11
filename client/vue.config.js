module.exports = {
    "transpileDependencies": [
        "vuetify"
    ],
};
    module.rules = {
      test: /\.(html)$/,
      exclude: /(node_modules)/,
      use: {
        loader: "html-loader"
      }
    };
