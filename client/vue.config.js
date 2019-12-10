module.exports = {
    "transpileDependencies": [
        "vuetify"
    ],
    devServer:{
        proxy:'http://127.0.0.1:5000'
    }
};
    module.rules = {
      test: /\.(html)$/,
      exclude: /(node_modules)/,
      use: {
        loader: "html-loader"
      }
    };
