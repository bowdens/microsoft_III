from flask_restful import Resource
from server import auth, system
from passlib.apps import custom_app_context as pwd_context

class User(Resource):
    method_decorators = {'get': [auth.login_required]}

    def get(self, user_id):
        return system.get_user(user_id)

