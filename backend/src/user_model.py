from src.subject import SubjectModel
from passlib.apps import custom_app_context as pwd_context

from json import dumps as jsonify

class UserModel():
    def __init__(self, fname, lname, username, password):
        self.fname = fname
        self.lname = lname
        self.__username = username
        self.password = password
        self.__subjects = []


    def verify_password(self, plaintext_passowrd):
        return pwd_context.ecnrypt(plaintext_password) == self.password

    def get_dict(self):
        subjects = []
        for subject in self.subjects:
            subjects.append(subject.to_dict())

        return {
            "fname": self.fname,
            "lname": self.lname,
            "username": self.username,
            "subjects": subjects
                }

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
        # todo change this back
        self.__password = plaintextPassword
        #self.__password = pwd_context.encrypt(plaintextPassword)

    @property
    def subjects(self):
        return self.__subjects

    def add_subject(self, subject):
        if not isinstance(subject, SubjectModel):
            raise TypeError("Subject must be a Subject")
        self.__subjects.append(subject)
