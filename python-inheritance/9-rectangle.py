#!/usr/bin/python3
"""Rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""BaseGeometry class"""


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry

    Args:
        BaseGeometry (class): Base class
    """

    def __init__(self, width, height):
        """Rectangle class constructor

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
