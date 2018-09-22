from flask import jsonify

class Subject():
    marks = ["HD", "DN", "CR", "PS", "FL", "ON"]
    def __init__(self, courseCode, mark):
        self.courseCode = courseCode
        self.mark = mark

    def to_dict(self):
        return {
                "courseCode": self.courseCode,
                "mark": self.mark
                }

    @property
    def courseCode(self):
        return self.__courseCode

    @courseCode.setter
    def courseCode(self, courseCode):
        self.__courseCode = courseCode

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        if mark in self.marks:
            self.__mark = mark
        else:
            raise ValueError("Mark must be one of {}".format(marks))

