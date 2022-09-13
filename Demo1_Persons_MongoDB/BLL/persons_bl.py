from pymongo import MongoClient
from bson import ObjectId

class PersonBl():
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["personsdb"]
        self.__collection = self.__db["persons"]

    # Get all Persons
    def get_all_persons(self):
        return list(self.__collection.find({}))

    # Get Person
    def get_person(self, id):
        return self.__collection.find_one({ "_id": ObjectId(id) })

    # Add Person
    def add_person(self, obj):
        self.__collection.insert_one(obj)
        return "Created with ID: " + str(obj["_id"]) # => after the creation obj receives the id automatically

    # Update Person
    def update_person(self,id, obj):
        self.__collection.update_one({"_id": ObjectId(id)}, {"$set": obj})
        return "Updated !"

    # Delete Person
    def delete_person(self,id):
        self.__collection.delete_one({"_id": ObjectId(id)})
        return "Deleted !"