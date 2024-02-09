#!/usr/bin/python3
"""Student module"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance

        Args:
            first_name (string): student's first name
            last_name (string): student's last name
            age (int): student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary description with simple data structure"""
        if (type(attrs) is list and
                all(type(itms) is str for itms in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        with json attributes"""
        for key, value in json.items():
            setattr(self, key, value)
