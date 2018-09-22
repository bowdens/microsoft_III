from flask_restful import Resource
from server import auth, system
from flask import jsonify, request

class Group(Resource):
    #method_decorators = {'get': [auth.login_required]}

    def get(self, group_id):
        group = system.get_group(group_id)
        if group is None:
            return {}, 404
        else:
            return group.to_json()

    def post(self, group_id):
        group = system.get_group(group_id)
        if group is None:
            return {}, 404
        else:
            username = request.form.get("username")
            # because this is a prototype and
            user = system.get_user(username)
            if user is None:
                return {}, 403
            group.add_user(username)
            return group.to_json()

class GroupAll(Resource):
    def get(self):
        groups = system.get_groups()
        group_json = {}
        for group_id in groups.keys():
            group_json[group_id] = groups[group_id].to_dict()
        return jsonify(group_json)
