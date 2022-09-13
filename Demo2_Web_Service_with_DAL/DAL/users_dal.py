import requests

class UsersDAL():
    def __init__(self):
        self.__url = "https://jsonplaceholder.typicode.com/users"
    
    def get_all_users(self):
        resp = requests.get(self.__url)
        return resp.json()
    
    def get_user(self, id):
        resp = requests.get(self.__url + "/" + id )
        return resp.json()

    def add_user(self, obj):
        resp = requests.post(self.__url, json=obj)
        return resp.json()

    def update_user(self, id, obj):
        resp = requests.put(self.__url + "/" + id, json=obj)
        return resp.json()

    def delete_user(self, id):
        resp = requests.delete(self.__url + "/" + id)
        return resp.json()