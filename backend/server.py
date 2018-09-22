from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from src.system import System
from src.user_model import UserModel
from src.subject import Subject

app = Flask(__name__)
app.secret_key = "not a secret"
api = Api(app)
auth = HTTPBasicAuth()

system = System()
user = UserModel("first", "last", "tester", "password")
user.add_subject(Subject("COMP1511", "DN"))
user.add_subject(Subject("COMP1521", "CR"))
system.add_user(user)
