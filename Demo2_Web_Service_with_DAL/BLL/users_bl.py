from DAL.users_dal import UsersDAL

class UsersBL():
    def __init__(self):
        self.__usersDAL = UsersDAL()
    
    def get_all_users(self):
        users = self.__usersDAL.get_all_users()
        return users
    
    def get_user(self, id):
        user = self.__usersDAL.get_user(id)
        return user

    def add_user(self, obj):
        resp = self.__usersDAL.add_user(obj)
        return resp

    def update_user(self, id, obj):
        resp = self.__usersDAL.update_user(id, obj)
        return resp

    def delete_user(self, id):
        resp = self.__usersDAL.delete_user(id)
        return resp