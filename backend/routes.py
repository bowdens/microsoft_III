from src.user import User, Subject
from src.group import Group, GroupAll
from server import app, api, auth

api.add_resource(User, "/user/<user_id>")
api.add_resource(Subject, "/user/<user_id>/subjects")
api.add_resource(Group, "/group/<group_id>")
api.add_resource(GroupAll, "/group")


@app.route("/")
def index():
    return "test"

@auth.verify_password
def verify_password(username, password):
    if username == "test" and password == "test":
        return True
    return False
