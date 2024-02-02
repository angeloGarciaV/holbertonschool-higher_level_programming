#!/usr/bin/python3
"""Class Square with size attribute"""


class Square:
    """Class Square with size attribute"""

    def __init__(self, size=0):
        """Initializes size as private attribute for Square class"""
        try:
            self.__size = size
        except ValueError:
            print("size must be >= 0")
