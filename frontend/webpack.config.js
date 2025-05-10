const path = require('path');

module.exports = {
  entry: './src/index.js',  // Entry point for our React app
  output: {
    path: path.resolve(__dirname, '../static/frontend'),  // Output to Django's static directory
    filename: 'main.js',  // The bundled JavaScript file
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react']
          }
        }
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      }
    ]
  }
};