from src.user import User, Subject, Validate
from src.group import Group, GroupAll
from server import app, api, auth

api.add_resource(User, "/user/<user_id>")
api.add_resource(Subject, "/user/<user_id>/subjects")
api.add_resource(Validate, "/validate")
api.add_resource(Group, "/group/<group_id>")
api.add_resource(GroupAll, "/group")

