from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/api/v1/clothes_dataset', methods=['GET'])
def get_clothes_dataset():
    clothes_dataset = pd.read_csv('clothes_dataset.csv')
    return jsonify(clothes_dataset.to_dict(orient='records'))

# Search for a product in the 'productDisplayName' column
@app.route('/search/<string:product>', methods=['GET'])
def get_fuzzy_product(product):
    clothes_dataset = pd.read_csv('clothes_dataset.csv')
    product = clothes_dataset[clothes_dataset['productDisplayName'].str.contains(product, case=False)]
    return jsonify(product.to_dict(orient='records'))  

if __name__ == '__main__':
    app.run(debug=True)
