from flask_restful import Resource
from server import auth, system

class User(Resource):
    #method_decorators = {'get': [auth.login_required]}

    def get(self, user_id):
        user = system.get_user(user_id)
        if user is None:
            return {}
        else:
            return user.to_json()

