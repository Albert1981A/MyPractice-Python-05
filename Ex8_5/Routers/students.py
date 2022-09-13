from flask import Blueprint, jsonify, request
from BLL.students_bl import StudentBl

students = Blueprint('students', __name__)
student_bl = StudentBl()

# Get all students
@students.route('/', methods=['GET'])
def get_all_students():
    # => get me first-name if their is a parameter first-name => "http://127.0.0.1:5000/students?first-name=Avi"
    first_name = request.args.get('first-name') 
    print(first_name)
    return jsonify(student_bl.get_all_students(first_name))

# Get student
@students.route('/<string:id>', methods=['GET'])
def get_student(id):
    return jsonify(student_bl.get_student(id))

# Add student
@students.route('/', methods=['POST'])
def add_student():
    obj = request.json
    return jsonify(student_bl.add_student(obj))

# Update student
@students.route('/<string:id>', methods=['PUT'])
def update_student(id):
    obj = request.json
    return jsonify(student_bl.update_student(id,obj))

# Delete student
@students.route('/<string:id>', methods=['DELETE'])
def delete_student(id):
    return jsonify(student_bl.delete_student(id))