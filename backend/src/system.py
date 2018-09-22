from src.user_model import UserModel
from src.group_model import GroupModel

class System():
    def __init__(self):
        self.__users = {}
        self.__groups = {}

    def get_groups(self):
        return self.__groups
        
    def get_group(self, id):
        return self.__groups.get(id)
        
    def add_group(self, group):
        if not isinstance(group, GroupModel):
            raise TypeError("Invalid type")
        id = group.id
        if self.get_group(id) is None:
            self.__groups[id] = group
        else:
            raise ValueError("Group key is already used")

    def get_user(self, id):
        print("getting {} in {}".format(id, self.__users))
        return self.__users.get(id)

    def add_user(self, user):
        if not isinstance(user, UserModel):
            raise TypeError("Invalid type")
        id = user.username
        if self.get_user(id) is None:
            self.__users[id] = user
        else:
            raise ValueError("User key is already used")

    def remove_user(self, id):
        if self.get_user(id) is None:
            pass
        else:
            del self.__users[id]
