#!/usr/bin/python3
"""Class Square with size attribute"""


class Square:
    """Class Square with size attribute"""

    def __init__(self, size=0):
        """Initializes size as private attribute for Square class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size

    def area(self):
        """calculates the area of a square

        Returns:
            int: the area of the square
        """
        return self._size**2
