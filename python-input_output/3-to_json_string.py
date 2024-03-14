#!/usr/bin/python3
"""to_json_string module"""


def to_json_string(my_obj):
    """Converts a python object to a JSON string

    Args:
        my_obj (any): Python object to convert

    Returns:
        str: JSON string
    """
    import json
    return json.dumps(my_obj)
