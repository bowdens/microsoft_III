from flask import jsonify

class GroupModel():
    def __init__(self, id, name, location, description, course_code, time, convenor, max_capacity, privacy_level):
        self.__id = id
        self.__name = name
        self.location = location
        self.description = description
        self.course_code = course_code
        self.time = time
        self.convenor = convenor
        self.attendees = [convenor]
        self.__max_capacity = max_capacity
        self.privacy_level = privacy_level


    def to_json(self):
        return jsonify(name=self.name, location=self.location, description=self.description, course_code=self.course_code, max_capacity=self.max_capacity, time=self.time, attendees=self.attendees, id=self.id, convenor=self.convenor, privacy_level=self.privacy_level)

    def to_dict(self):
        return {"name": self.name, "location": self.location, "description": self.description, "course_code": self.course_code, "max_capacity": self.max_capacity, "num_attending": self.num_attending(), "id": self.id, "privacy_level":self.privacy_level, "convenor":self.convenor}

    def add_user(self, user):
        if user in self.attendees:
            return
        elif len(self.attendees) >= self.max_capacity:
            return
        else:
            self.attendees.append(user)

    def num_attending(self):
      return len(self.attendees)


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

    @property
    def max_capacity(self):
        return self.__max_capacity

    @max_capacity.setter
    def max_capacity(self, max_capacity):
        if max_capacity > 0 and max_capacity < 1000:
            self.__max_capacity = max_capacity
        else:
            raise ValueError("max_capacity must be valid {}".format(max_capacity))
