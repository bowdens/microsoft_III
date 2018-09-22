from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from src.system import System
from src.user_model import UserModel
from src.group_model import GroupModel

app = Flask(__name__)
app.secret_key = "not a secret"
api = Api(app)
auth = HTTPBasicAuth()

system = System()
user = UserModel("first", "last", "tester", "password")
system.add_user(user)

group = GroupModel("1", "name", "location", "description", ["COMP101", "COMP102"], 63643534234, "tester", ["tester"], 5, 1)
system.add_group(group)
