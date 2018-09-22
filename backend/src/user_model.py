from src.subject import Subject

def UserModel():
    def __init__(self, fname, lname, username, password):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password
        self.__subjects = []


    def verify_password(self, plaintext_passowrd):
        return pwd_context.ecnrypt(plaintext_password) == self.password

    def add_subject(self, subject):
        if not instanceof(subject, Subject):
            raise TypeError("subject must be a Subject")
        self.__subjects.append(subject)

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

