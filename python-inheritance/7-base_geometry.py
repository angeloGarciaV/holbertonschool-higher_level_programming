#!/usr/bin/python3
""" BaseGeometry module"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Area method

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator method

        Args:
            name (string): name
            value (int): integer to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
