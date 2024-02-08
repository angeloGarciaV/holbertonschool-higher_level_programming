#!/usr/bin/python3
"""is_same_class module"""


def is_same_class(obj, a_class):
    """Checks if obj is exactly an instance of a_class;

    Args:
        obj (class): object to be checked
        a_class (class): class to check against

    Returns:
        bool: True if the object is exactly an instance of the specified class;
    """
    return type(obj) is a_class
