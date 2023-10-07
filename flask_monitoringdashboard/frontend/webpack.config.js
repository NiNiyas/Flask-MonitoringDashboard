const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    mode: process.env.NODE_ENV === 'production' ? 'production' : 'development',
    entry: ['./js/app.js', './sass/app.scss'],
    output: {
        path: path.resolve(__dirname, '../static'),
        filename: 'js/app.js'
    },
    module: {
        rules: [
            {
                test: /\.scss$/,
                use: [
                    {
                        loader: MiniCssExtractPlugin.loader
                    },
                    {
                        loader: 'css-loader'
                    },
                    {
                        loader: 'sass-loader'
                    }
                ]
            },
            {
                test: /\.(woff(2)?|ttf|eot|svg|otf)(\?v=\d+\.\d+\.\d+)?$/,
                type: 'asset/resource',
                generator: {
                  filename: 'fonts/[name][ext]'
                }
            }
        ]
    },
    plugins: [new MiniCssExtractPlugin({
      filename: 'css/app.css'
    })],
};
