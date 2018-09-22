from src.user import UserModel
from src.group import Group

class System():
    def __init__(self):
        self.__users = {}
        self.__groups = {}

    def get_group(self, id):
        return self.groups.get(id)

    def get_user(self, id):
        return self.users.get(id)

    def add_user(self, user, id):
        if not instanceof(user, UserModel):
            raise TypeError("Invalid type")
        if self.get_user(id) is None:
            self.__users[id] = user
        else:
            raise ValueError("User key is already used")

    def remove_user(self, id):
        if self.get_user(id) is None:
            pass
        else:
            del self.__users[id]
