#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class

    Args:
        obj: object to check
        a_class (class): class to check against

    Returns:
        bool: True if the object is an instance of a class
        that inherited (directly or indirectly) from the specified class.
        False otherwise
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
