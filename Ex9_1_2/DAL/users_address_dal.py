from pymongo import MongoClient
from bson import ObjectId

class UsersAddressDAL():
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["userAddressDB"]
        self.__collection = self.__db["persons"]

    # Get all Persons
    def get_all_persons(self):
        return list(self.__collection.find({}))