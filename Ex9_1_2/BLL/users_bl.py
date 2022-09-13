from DAL.users_address_dal import UsersAddressDAL
from DAL.users_phone_dal import UsersPhoneDAL
from DAL.users_dal import UsersDAL

class UsersBL():
    def __init__(self):
        self.__users_address_dal = UsersAddressDAL()
        self.__users_phone_dal = UsersPhoneDAL()
        self.__users_dal = UsersDAL()
    
    def get_all_users(self):
        all_users = self.__users_dal.get_all_users()
        users = all_users[0:2]
        phones_resp = self.__users_phone_dal.read_file()
        phones = phones_resp["persons"]
        address = self.__users_address_dal.get_all_persons()
        data = []
        for i in range(len(users)):
            phones_in = list(filter(lambda x : x["id"] == users[i]["id"], phones))
            address_in = list(filter(lambda x : int(x["external_id"]) == users[i]["id"], address))
            obj = {"id": users[i]["id"], "name": users[i]["name"], "email": users[i]["email"], "phone": phones_in[0]["phone"], "address": address_in[0]["address"]}
            data.append(obj)
        return data