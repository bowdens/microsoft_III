from flask_restful import Resource
from server import auth, system
from json import dumps

class User(Resource):
    #method_decorators = {'get': [auth.login_required]}

    def get(self, user_id):
        user = system.get_user(user_id)
        if user is None:
            return {}
        else:
            print("dict = {}".format(user.get_dict()))
            return user.get_dict()

