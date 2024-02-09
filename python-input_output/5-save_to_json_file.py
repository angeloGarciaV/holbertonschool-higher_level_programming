#!/usr/bin/python3
"""save_to_json_file module"""
import json
"""json module"""


def save_to_json_file(my_obj, filename):
    """Write a JSON object to a file

    Args:
        my_obj (any): Python object to write
        filename (str): File to write to
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
