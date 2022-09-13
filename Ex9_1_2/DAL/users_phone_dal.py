import os
import sys
import json

class UsersPhoneDAL():
    def __init__(self):
        self.__path = os.path.join(sys.path[0], 'Data/persons.json')
    
    def read_file(self):
        with open(self.__path, 'r') as file:
            return json.load(file)
    
    def write_file(self, obj):
        with open(self.__path, 'w') as file:
            json.dump(obj, file)
            return "Updated !"