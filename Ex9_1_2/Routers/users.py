from flask import Blueprint, jsonify, request
from BLL.users_bl import UsersBL
users_bl = UsersBL()

users = Blueprint('users', __name__)

@users.route('/', methods=['GET'])
def get_all_users():
    resp = users_bl.get_all_users()
    return jsonify(resp)