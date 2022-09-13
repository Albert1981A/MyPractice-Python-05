from flask import Blueprint, jsonify, request
from BLL.products_bl import ProductsBL

products_bl = ProductsBL()

products = Blueprint('products', __name__)

@products.route('/', methods=['GET'])
def get_all_products():
    resp = products_bl.get_all_products()
    return jsonify(resp)

@products.route('/<string:id>', methods=['GET'])
def get_product(id):
    resp = products_bl.get_product(id)
    return jsonify(resp)

@products.route('/', methods=['POST'])
def add_product():
    obj = request.json
    resp = products_bl.add_product(obj)
    return jsonify(resp)

@products.route('/<string:id>', methods=['PUT'])
def update_product(id):
    obj = request.json
    resp = products_bl.update_product(id, obj)
    return jsonify(resp)

@products.route('/<string:id>', methods=['DELETE'])
def delete_product(id):
    resp = products_bl.delete_product(id)
    return jsonify(resp)