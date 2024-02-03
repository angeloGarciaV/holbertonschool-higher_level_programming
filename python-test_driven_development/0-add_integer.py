#!/usr/bin/python3
"""Module for add_integer function"""


def add_integer(a, b=98):
    """Add two integers

    Args:
        a int: first integer
        b (int, optional): seocnd integer. Defaults to 98.

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        int: sum of a and b
    """
    return int(a) + int(b)
