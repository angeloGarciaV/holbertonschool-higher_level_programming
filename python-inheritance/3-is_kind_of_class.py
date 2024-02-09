#!/usr/bin/python3
"""is_kind_of_class module."""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of,
    or if obj is an instance of a class that inherited from, a_class.

    Args:
        obj (class 'int'): object to be checked
        a_class (class): class to be checked against

    Returns:
        bool: True if obj is an instance of a class
        or one that inherited from, a_class.
    """
    return isinstance(obj, a_class)
