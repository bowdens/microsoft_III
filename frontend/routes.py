import flask
import flask_login
from src.login import check_password, User
from server import app
import requests

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
    #if flask.request.method == 'POST':
    groups = requests.get("http://localhost:5000/group").json()

    #else display all groups in the system -- maybe sort by date
    #just have a list of group names, date-time, course
    return flask.render_template('homepage.html', groups=groups)

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@app.route('/group/<id>', methods=['GET', 'POST'])
def show_group(id):
    if flask.request.method == 'GET':
        try:
            group = requests.get("http://localhost:5000/group/{}".format(id)).json()
            return flask.render_template('group.html', group=group)
        except Exception as e:
            return flask.render_template('error.html', error="Could not reach api server\n{}".format(e))
    else:
        try:
            username = flask.request.form['username']
            group = requests.post("http://localhost:5000/group/{}".format(id), data={"username":username}).json()
            print(group)
            if group.get('attendees') is None:
                return flask.render_template('error.html', error="could not register under that name")

            return flask.render_template('group.html', group=group)
        except Exception as e:
            print(e)
            return flask.render_template('error.html', error="There was an error registering for this event\n{}".format(e))
