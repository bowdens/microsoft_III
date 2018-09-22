from flask_restful import Resource


class Group(Resource):
    def get(self, group_id):
        return "todo"

