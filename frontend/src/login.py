import flask
import flask_login
from server import app

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
users = {'test': {'password': '123456'}}

class User(flask_login.UserMixin):
    pass

def check_password(username, password):
  return password == users[username]['password']

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'