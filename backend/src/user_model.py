from src.subject import Subject
from passlib.apps import custom_app_context as pwd_context

from flask import jsonify

class UserModel():
    def __init__(self, fname, lname, username, password):
        self.fname = fname
        self.lname = lname
        self.__username = username
        self.password = password
        self.__subjects = []


    def verify_password(self, plaintext_passowrd):
        return pwd_context.ecnrypt(plaintext_password) == self.password

    def to_json(self):
        return jsonify(username=self.username, fname=self.fname, lname=self.lname, subjects=self.subjects)

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self,name):
        self.__fname = name

    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self,name):
        self.__lname = name

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, plaintextPassword):
        self.__password = pwd_context.encrypt(plaintextPassword)

    @property
    def subjects(self):
        return self.__subjects

    def add_subject(self, subject):
        if not instanceof(subject, Subject):
            raise TypeError("Subject must be a Subject")
        self.__subjects.append(subject)
