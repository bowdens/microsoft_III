from flask_restful import Resource
from server import auth, system

class Group(Resource):
    #method_decorators = {'get': [auth.login_required]}
    
    def get(self, group_id):
        group = system.get_group(group_id)
        if group is None:
            return {}
        else:
            return group.to_json()

    
