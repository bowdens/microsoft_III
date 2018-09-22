from src.user import User
from server import app, api

api.add_resource(User, "/user/<int:user_id>")

@app.route("/")
def index():
    return "test"
