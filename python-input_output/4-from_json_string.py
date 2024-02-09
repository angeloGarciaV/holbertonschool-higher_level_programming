#!/usr/bin/python3
"""from_json_string module"""
import json
"""json module"""


def from_json_string(my_str):
    """Converts a JSON string to a python object

    Args:
        my_str (string): JSON string to convert

    Returns:
        Object : Python object
    """
    return json.loads(my_str)
