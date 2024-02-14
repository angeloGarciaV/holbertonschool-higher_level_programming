#!/usr/bin/python3
"""Module for Base class
    """
import json


class Base:
    """Base class for all other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new instance of Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            str: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
