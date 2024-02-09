#!/usr/bin/python3
"""Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Square class constructor

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """String representation of the square

        Returns:
            string: representation of the square
        """
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
