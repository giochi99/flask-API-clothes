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

@app.route('/search/top-wear/<string:product>', methods=['GET'])
def get_fuzzy_product(product):
    clothes_dataset = pd.read_csv('clothes_dataset.csv')
    top_wear = clothes_dataset[clothes_dataset['subCategory'].isin(["Topwear", "Loungewear and Nightwear", "Apparel Set", "Saree", "Dress"])]
    product = top_wear[top_wear['productDisplayName'].str.contains(product, case=False)]
    return jsonify(product.to_dict(orient='records'))  

@app.route('/search/bottom-wear/<string:product>', methods=['GET'])
def get_fuzzy_product(product):
    clothes_dataset = pd.read_csv('clothes_dataset.csv')
    bottom_wear = clothes_dataset[clothes_dataset['subCategory'].isin(["Bottomwear", "Innerwear", "Socks"])]
    product = bottom_wear[bottom_wear['productDisplayName'].str.contains(product, case=False)]
    return jsonify(product.to_dict(orient='records'))  

@app.route('/search/foot-wear/<string:product>', methods=['GET'])
def get_fuzzy_product(product):
    clothes_dataset = pd.read_csv('clothes_dataset.csv')
    foot_wear = clothes_dataset[clothes_dataset['masterCategory'].isin(["Footwear"])]
    product = foot_wear[foot_wear['productDisplayName'].str.contains(product, case=False)]
    return jsonify(product.to_dict(orient='records'))  

@app.route('/search/accessories/<string:product>', methods=['GET'])
def get_fuzzy_product(product):
    clothes_dataset = pd.read_csv('clothes_dataset.csv')
    accessories = clothes_dataset[clothes_dataset['masterCategory'].isin(["Accessories", "Personal Care"])]
    product = accessories[accessories['productDisplayName'].str.contains(product, case=False)]
    return jsonify(product.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
