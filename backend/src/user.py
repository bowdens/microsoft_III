from flask_restful import Resource
from flask import request
from server import auth, system
from src.user_model import UserModel
from src.subject import SubjectModel

class User(Resource):
    #method_decorators = {'get': [auth.login_required]}

    def get(self, user_id):
        user = system.get_user(user_id)
        if user is None:
            return {}, 404
        else:
            return user.get_dict()

    def post(self, user_id):
        user = system.get_user(user_id)
        if not user is None:
            # user is not none - we don't want to overwrite it
            return {}, 412

        username = request.form.get("username")
        password = request.form.get("password")
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        if username is None:
            raise ValueError("Username cannot be none")
        if password is None:
            raise ValueError("Password cannot be none")
        if fname is None:
            raise ValueError("Fname cannot be none")
        if lname is None:
            raise ValueError("Lname cannot be none")
        user = UserModel(fname, lname, username, password)
        system.add_user(user)
        return user.get_dict(), 201

class Subject(Resource):
    def get(self, user_id):
        user = system.get_user(user_id)
        if user is None:
            return {}, 404
        else:
            subjects = []
            for subject in user.subjects:
                subjects.append(subject.to_dict())
            return subjects

    def post(self, user_id):
        user = system.get_user(user_id)
        if user is None:
            return {}, 404
        else:
            courseCode = request.form.get("courseCode")
            mark = request.form.get("mark")
            if courseCode is None:
                raise ValueError("courseCode cannot be none")
            if mark is None:
                raise ValueError("mark cannot be none")
            subject = SubjectModel(courseCode, mark)
            user.add_subject(subject)

            return self.get(user_id)


class Validate(Resource):
    def post(self):
        username = request.form.get("username")
        password = request.form.get("password")
        if system.validate_user(username, password):
            return "true"
        else:
            return "false"
