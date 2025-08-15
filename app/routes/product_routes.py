from flask import Blueprint, jsonify
from app.services.product_service import ProductService

product_blueprint = Blueprint('product_blueprint', __name__)
product_service = ProductService()

@product_blueprint.route('/products', methods=['GET'])
def get_products():
    products = product_service.get_products()
    return jsonify(products), 200

@product_blueprint.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = product_service.get_product_by_id(product_id)
    if product:
        return jsonify(product), 200
    else:
        return jsonify({"message": "Product not found"}), 404
