from flask_restful import Resource
from server import auth, system
from flask import jsonify

class Group(Resource):
    #method_decorators = {'get': [auth.login_required]}

    def get(self, group_id):
        group = system.get_group(group_id)
        if group is None:
            return {}
        else:
            return group.to_json()

class GroupAll(Resource):
    def get(self):
        groups = system.get_groups()
        group_json = {}
        for group_id in groups.keys():
            group_json[group_id] = groups[group_id].to_dict()
        return jsonify(group_json)