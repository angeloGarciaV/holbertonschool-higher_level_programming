#!/usr/bin/python3
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
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
