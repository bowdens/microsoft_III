from flask import jsonify

class GroupModel():
    def __init__(self, id, name, location, description, course_code, time, convenor, atendees, max_capacity, privacy_level):
        self.__id = id
        self.__name = name
        self.location = location
        self.description = description
        self.course_code = course_code
        self.time = time
        self.convenor = convenor
        self.atendees = atendees
        self.max_capacity = max_capacity
        self.privacy_level = privacy_level


    def to_json(self):
        return jsonify(name=self.name, location=self.location, description=self.description, course_code=self.course_code)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name