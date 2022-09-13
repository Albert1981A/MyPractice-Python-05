from pymongo import MongoClient
from bson import ObjectId

class StudentBl():
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["studentsdb"]
        self.__collection = self.__db["students"]

    # Get all students
    def get_all_students(self, first_name):
        if first_name != None:
            return list(self.__collection.find({ "first_name": first_name })) # will search by first_name
        else:
            return list(self.__collection.find({}))

    # Get student
    def get_student(self, id):
        return self.__collection.find_one({ "_id": ObjectId(id) })

    # Add student
    def add_student(self, obj):
        self.__collection.insert_one(obj)
        return "Created with ID: " + str(obj["_id"]) # => after the creation obj receives the id automatically

    # Update student
    def update_student(self,id, obj):
        self.__collection.update_one({"_id": ObjectId(id)}, {"$set": obj})
        return "Updated !"

    # Delete student
    def delete_student(self,id):
        self.__collection.delete_one({"_id": ObjectId(id)})
        return "Deleted !"