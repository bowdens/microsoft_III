from src.user import User
from src.group import Group
from server import app, api, auth

api.add_resource(User, "/user/<user_id>")
api.add_resource(Group, "/group/<group_id>")


@app.route("/")
def index():
    return "test"

@auth.verify_password
def verify_password(username, password):
    if username == "test" and password == "test":
        return True
    return False
