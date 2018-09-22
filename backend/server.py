from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
app.secret_key = "not a secret"
api = Api(app)
auth = HTTPBasicAuth()
