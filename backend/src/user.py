from flask_restful import Resource

class User(Resource):
    def __init__(self):
        pass

    def get(self, user_id):
        return "nothing yet"
