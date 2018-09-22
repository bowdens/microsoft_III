from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from src.system import System
from src.user_model import UserModel
from src.subject import SubjectModel
from src.group_model import GroupModel

app = Flask(__name__)
app.secret_key = "not a secret"
api = Api(app)
auth = HTTPBasicAuth()

system = System()
user = UserModel("first", "last", "tester", "password")
user.add_subject(SubjectModel("COMP1511", "DN"))
user.add_subject(SubjectModel("COMP1521", "CR"))
system.add_user(user)

group = GroupModel("1", "name", "location", "description", ["COMP1511", "COMP1521"], 63643534234, "tester", ["tester"], 5, 1)
system.add_group(group)
