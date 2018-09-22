import flask
import flask_login
from src.login import check_password, User
from server import app

@app.route("/")
def index():
    return "test"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return flask.render_template('login.html')
    return flask.redirect(flask.url_for('homepage'))


@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    groups = []
    if flask.request.method == 'POST':
      groups = flask.request.get("http://localhost:5000/group").json()


    #else display all groups in the system -- maybe sort by date
    #just have a list of group names, date-time, course
    return flask.render_template('homepage.html', groups=groups)

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'
