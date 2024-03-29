#!/usr/bin/python3
"""class_to_json module"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    """
    return obj.__dict__
