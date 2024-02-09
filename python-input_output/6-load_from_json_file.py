#!/usr/bin/python3
"""load_from_json_file module"""
import json
"""json module"""


def load_from_json_file(filename):
    """Load a JSON object from a file

    Args:
        filename (str): File to load from

    Returns:
        any: Python object
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
