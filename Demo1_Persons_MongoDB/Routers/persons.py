from flask import Blueprint, jsonify, request
from BLL.persons_bl import PersonBl

persons = Blueprint('persons', __name__)
person_bl = PersonBl()

# Get all Persons
@persons.route('/', methods=['GET'])
def get_all_persons():
    return jsonify(person_bl.get_all_persons())

# Get Person
@persons.route('/<string:id>', methods=['GET'])
def get_person(id):
    return jsonify(person_bl.get_person(id))

# Add Person
@persons.route('/', methods=['POST'])
def add_person():
    obj = request.json
    return jsonify(person_bl.add_person(obj))

# Update Person
@persons.route('/<string:id>', methods=['PUT'])
def update_person(id):
    obj = request.json
    return jsonify(person_bl.update_person(id,obj))

# Delete Person
@persons.route('/<string:id>', methods=['DELETE'])
def delete_person(id):
    return jsonify(person_bl.delete_person(id))