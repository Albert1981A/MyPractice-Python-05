from flask import Blueprint, jsonify, request
from BLL.users_bl import UsersBL

users_bl = UsersBL()

users = Blueprint('users', __name__)

@users.route('/', methods=['GET'])
def get_all_users():
    resp = users_bl.get_all_users()
    return jsonify(resp)

@users.route('/<string:id>', methods=['GET'])
def get_user(id):
    resp = users_bl.get_user(id)
    return jsonify(resp)

@users.route('/', methods=['POST'])
def add_user():
    obj = request.json
    resp = users_bl.add_user(obj)
    return jsonify(resp)

@users.route('/<string:id>', methods=['PUT'])
def update_user(id):
    obj = request.json
    resp = users_bl.update_user(id, obj)
    return jsonify(resp)

@users.route('/<string:id>', methods=['DELETE'])
def delete_user(id):
    resp = users_bl.delete_user(id)
    return jsonify(resp)